import traceback as tb
from flask import Blueprint, request, flash, render_template, redirect, url_for
from werkzeug.datastructures import MultiDict
from views.forms import ItemForm, ProductFetchForm
from sql.db import DB
from roles.permissions import admin_permission
from flask_login import login_required, current_user
from utils.lazy import DictToObject
from utils.AsosAPI import AsosAPI

admin = Blueprint('admin', __name__, url_prefix='/',template_folder='templates')

@admin.route("/admin/item", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def item():
    # UCID: dg574
    # Date: 12/11/2023
    # Method to add/edit item as admin
    form = ItemForm()
    id = request.args.get("id", form.id.data or None)
    type = "Edit" if id else "Create"
    if id and not form.name.data:
        try:
            result = DB.selectOne("SELECT id, name, description, stock, unit_price, image FROM IS601_S_Items WHERE id = %s", id)
            if result.status and result.row:
                form.process(MultiDict(result.row))
        except Exception as e:
            print("Error fetching item", e)
            flash("Item not found", "danger")
        return render_template("item.html", form=form, type=type)

    if form.validate_on_submit():
        visibility = True if int(form.stock.data) > 0 else False
        if form.id.data: # it's an update
            try:
                result = DB.update("UPDATE IS601_S_Items set name = %s, description = %s, stock = %s, unit_price = %s, image=%s, visibility=%s WHERE id = %s",
                form.name.data, form.description.data, form.stock.data, form.unit_price.data, form.image.data, visibility, form.id.data)
                if result.status:
                    flash(f"Updated {form.name.data}", "success")
            except Exception as e:
                print("Error updating item", e)
                flash(f"Error updating item {form.name.data}", "danger")
        else: # it's a create
            try:
                result = DB.update("""INSERT INTO IS601_S_Items (name, description, stock, unit_price, image, visibility) 
                VALUES (%s,%s,%s,%s,%s,%s)""",
                form.name.data, form.description.data, form.stock.data, form.unit_price.data, form.image.data, visibility)
                if result.status:
                    flash(f"Created {form.name.data}", "success")
                    form = ItemForm() # clear form
            except Exception as e:
                print("Error creating item", e)
                flash(f"Error creating item {form.name.data}", "danger")

        try:
            result = DB.selectOne("SELECT id, name, description, stock, unit_price, image FROM IS601_S_Items WHERE id = %s", id)
            if result.status and result.row:
                form.process(MultiDict(result.row))
        except Exception as e:
            print("Error fetching item", e)
            flash("Item not found", "danger")
    return render_template("item.html", form=form, type=type)
    
@admin.route("/admin/view_item", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def view_item():
    # UCID: dg574
    # Date: 12/11/2023
    # Method to view item as admin
    try:
        id = request.args.get("id", None)
        result = DB.selectOne("SELECT id, name, description, stock, unit_price, product_url, image FROM IS601_S_Items WHERE id = %s", id)
        if result.status and result.row:
            rows = result.row
    except Exception as e:
        print("Error fetching item", e)
        flash("Item not found", "danger")
        rows = []
    return render_template("view_item.html", rows=rows if rows else {})

@admin.route("/admin/items/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    # UCID: dg574
    # Date: 12/11/2023
    # Method to delete item as admin
    id = request.args.get("id")
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_S_Items WHERE id = %s", id)
            if result.status:
                flash("Deleted item", "success")
        except Exception as e:
            print("Error deleting item",e)
            flash("Error deleting item", "danger")
    return redirect(url_for("admin.items"))


@admin.route("/admin/items", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def items():
    # UCID: dg574
    # Date: 12/11/2023
    # Method to view item as admin user
    rows = {}
    query = """SELECT id, name, description, stock, unit_price, image, visibility
               FROM IS601_S_Items LIMIT 25"""
    try:
        result = DB.selectAll(query)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(tb.format_exc())
        flash("There was a problem loading items", "danger")
    return render_template("admin_items.html", rows=rows)

@admin.route("/admin/orders", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def orders():
    # UCID: dg574
    # Date: 12/11/2023
    # Method to list all orders
    rows = []
    try:
        result = DB.selectAll("""
        SELECT o.id, u.username, total_price, number_of_items, o.created 
        FROM IS601_S_Orders o
        JOIN IS601_Users u on o.user_id = u.id 
        """)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting orders", e)
        flash("Error fetching orders", "danger")
    return render_template("orders.html", rows=rows)

@admin.route("/admin/order", methods=["GET"])
@admin_permission.require(http_exception=403)
def order():
    # UCID: dg574
    # Date: 12/11/2023
    # Method to view a particular order details
    rows = []
    total = 0
    id = request.args.get("id")
    if not id:
        flash("Invalid order", "danger")
        return redirect(url_for("shop.orders"))
    try:
        # locking query to order_id and user_id so the user can see only their orders
        result = DB.selectAll("""
        SELECT name, oi.unit_price, oi.quantity, (oi.unit_price*oi.quantity) as subtotal 
        FROM IS601_S_OrderItems oi 
        JOIN IS601_S_Items i on oi.item_id = i.id 
        WHERE order_id = %s
        """, id)
        if result.status and result.rows:
            rows = result.rows
            total = sum(int(row["subtotal"]) for row in rows)
        result = DB.selectAll("""
        SELECT first_name, last_name, address, payment_method
        FROM IS601_S_Orders where id=%s
        """, id)
        if result.status and result.rows:
            order_info = result.rows
    except Exception as e:
        print("Error getting order", e)
        flash("Error fetching order", "danger")
        rows = []
        total = None
        order_info = []
    print(rows)
    print(order_info)
    return render_template("order.html", rows=rows, total=total, order_info=order_info )

insert_query = """INSERT INTO IS601_S_Items
                (name, description, category, stock, unit_price, visibility, image, product_url, source)
                VALUES (%(name)s, %(description)s, %(category)s, %(stock)s, %(unit_price)s, %(visibility)s, %(image)s, %(product_url)s, %(source)s)
                ON DUPLICATE KEY UPDATE name = VALUES(name), description = VALUES(description), category = VALUES(category), stock = VALUES(stock), unit_price = VALUES(unit_price), visibility = VALUES(visibility), image = VALUES(image), product_url = VALUES(product_url), source = VALUES(source)"""

@admin.route("/admin/items/fetch", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def fetch():
    form = ProductFetchForm()
    if form.validate_on_submit():
        limit = form.limit.data
        print(limit)
        if limit >= 1:
            api_results = AsosAPI.get_products(limit)
            if api_results:
                try:
                    print(api_results)
                    result = DB.insertMany(insert_query, api_results)
                    if result.status:
                        flash("Loaded in records", "success")
                except Exception as e:
                    print(f"Error inserting into cards table {e}")
                    flash("There was an error inserting the data", "danger")
                
    return render_template("product_fetch.html", form=form)