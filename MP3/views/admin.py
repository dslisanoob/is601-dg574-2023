import csv
import io
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from sql.db import DB
import traceback

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/import", methods=["GET", "POST"])
def importCSV():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', "warning")
            return redirect(request.url)
        
        # TODO importcsv-1: Check that it's a .csv file, return a proper flash message if it's not
        #dg574-12/05/23
        if file and secure_filename(file.filename):
            file_name = secure_filename(file.filename)
            if file_name.endswith('.csv'):
                organizations = []
                donations = []

                organization_query = """
                INSERT INTO IS601_MP3_Organizations (name, address, city, country, state, zip, website, description)
                VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s, %(description)s)
                ON DUPLICATE KEY UPDATE 
                    address=values(address),
                    city=values(city),
                    country=values(country),
                    state=values(state),
                    zip=values(zip),
                    website=values(website),
                    description=values(description)
                """

                donation_query = """
                INSERT INTO IS601_MP3_Donations (donor_firstname, donor_lastname, donor_email, item_name, item_description, item_quantity, organization_id, donation_date, comments)
                VALUES (%(donor_firstname)s, %(donor_lastname)s, %(donor_email)s, %(item_name)s, %(item_description)s, %(quantity)s, 
                        (SELECT id FROM IS601_MP3_Organizations WHERE name = %(organization_name)s LIMIT 1), 
                        %(donation_date)s, %(comments)s)
                ON DUPLICATE KEY UPDATE 
                    donor_firstname=%(donor_firstname)s,
                    donor_lastname=%(donor_lastname)s,
                    donor_email=%(donor_email)s,
                    item_name=%(item_name)s, 
                    item_quantity = %(quantity)s,
                    item_description= %(item_description)s,
                    comments=%(comments)s, 
                    organization_id = (SELECT id FROM IS601_MP3_Organizations WHERE name=%(organization_name)s LIMIT 1),
                    donation_date = %(donation_date)s,
                    comments=%(comments)s
                """

                try:
                    # Read the file as a stream
                    stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)
                    
                    # TODO importcsv-2: Read the csv file stream as a dictionary
                    #dg574-12/05/23
                    csv_reader = csv.DictReader(stream)
                    for row in csv_reader:
                        # TODO importcsv-3: Extract organization data and append to the organization list
                        # as a dictionary only with organization data if all organization fields are present
                        #dg574-12/05/23
                        # print('organization_name' in row)
                        # print(all(key in row for key in ['organization_name', 'organization_address', 'organization_city', 'organization_country', 'organization_state', 'organization_zip,', 'organization_website', 'organization_description']))
                        try:
                            organizations.append({
                            'name': row['organization_name'],
                            'address': row['organization_address'],
                            'city': row['organization_city'],
                            'country': row['organization_country'],
                            'state': row['organization_state'],
                            'zip': row['organization_zip'],
                            'website': row['organization_website'],
                            'description': row['organization_description'],
                            })
                        except Exception as e:
                            traceback.print_exc()
                            print(row)
                            flash("There was an error loading in the CSV data for organizations", "danger")

                        # TODO importcsv-4: Extract donation data and append to the donation list
                        # as a dictionary only with donation data if all donation fields are present
                        #dg574-12/05/23
                        if any(key in row for key in ['donor_firstname', 'donor_lastname', 'donor_email', 'item_name', 'item_description', 'quantity', 'organization_name', 'donation_date', 'comments']):
                            donations.append({
                                'donor_firstname': row['donor_name'].split()[0] if row["donor_name"] else '',
                                'donor_lastname': row['donor_name'].split()[1] if len(row["donor_name"].split())>1 else '',
                                'donor_email': row['donor_email'],
                                'item_name': row['item_name'],
                                'item_description': row['item_description'],
                                'quantity': row['quantity'],
                                'organization_name': row['organization_name'],
                                'donation_date': row['donation_date'],
                                'comments': row['comments'],
                            })
                        
                    if len(organizations) > 0:
                        print(f"Inserting or updating {len(organizations)} organizations")
                        try:
                            result = DB.insertMany(organization_query, organizations)
                            # TODO importcsv-5: Display a flash message about the number of organizations inserted
                             #dg574-12/05/23
                            flash(f"{len(organizations)} organizations inserted or updated", "success")
                        except Exception as e:
                            traceback.print_exc()
                            flash("There was an error loading in the CSV data for organizations", "danger")
                    else:
                        # TODO importcsv-6: Display a flash message (info) that no organizations were loaded
                         #dg574-12/05/23
                        flash("No organizations to import", "info")

                    if len(donations) > 0:
                        print(f"Inserting or updating {len(donations)} donations")
                        try:
                            result = DB.insertMany(donation_query, donations)
                            # TODO importcsv-7: Display a flash message about the number of donations loaded
                             #dg574-12/05/23
                            flash(f"{len(donations)} donations inserted or updated", "success")
                        except Exception as e:
                            traceback.print_exc()
                            flash("There was an error loading in the CSV data for donations", "danger")
                    else:
                        # TODO importcsv-8: Display a flash message (info) that no donations were loaded
                         #dg574-12/05/23
                        flash("No donations to import", "info")

                    try:
                        result = DB.selectOne("SHOW SESSION STATUS LIKE 'questions'")
                        print(f"Result {result}")
                    except Exception as e:
                        traceback.print_exc()
                        flash("There was an error counting session queries", "danger")
                        
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error processing the CSV file", "danger")
            else:
                flash("Select only csv files")

    return render_template("upload.html")
