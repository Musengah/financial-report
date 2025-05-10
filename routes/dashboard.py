from flask import render_template
from flask_login import login_required
from . import routes_bp

@routes_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
