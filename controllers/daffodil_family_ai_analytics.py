from odoo import http
import pandas as pd
from odoo.http import request
import requests
from queue import Queue
from threading import Thread
import threading
import time

class Analytics(http.Controller):
    @http.route('/ai/analytics', website=True, auth='public', methods=['POST', 'GET'], csrf=False)
    def analytics(self, **kwargs):

        return request.render("daffodil_central_management_dashboard.ai_analytics")


