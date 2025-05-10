from flask import render_template
from flask_login import login_required
from . import routes_bp

@routes_bp.route('/reports')
@login_required
def reports():
    return render_template('reports.html')
