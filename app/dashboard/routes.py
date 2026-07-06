from flask import current_app
from flask import render_template

from . import dashboard_bp


@dashboard_bp.route("/")
def index():

    current_app.logger.info("Dashboard loaded")

    return render_template("dashboard/index.html")
