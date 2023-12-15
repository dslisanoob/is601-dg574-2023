from flask import Blueprint, request, render_template
hello = Blueprint('hello', __name__, url_prefix='/',template_folder='templates')


@hello.route('/')
def index():
    # UCID: dg574
    # Date: 12/11/2023
    # Welcome page template
    name = request.args.get('name', 'Grader')
    return render_template("welcome.html", name=name)