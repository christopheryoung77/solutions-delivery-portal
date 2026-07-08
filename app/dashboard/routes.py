from flask import current_app
from flask import render_template

from . import dashboard_bp
from app.services.dashboard_service import DashboardService


@dashboard_bp.route("/")
def index():

    current_app.logger.info("Dashboard loaded")

    dashboard = DashboardService()

    summary = dashboard.get_summary()

    return render_template(
        "dashboard/index.html",
        summary=summary,
    )
