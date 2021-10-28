from odoo import http
import pandas as pd
from odoo.http import request
import requests
from queue import Queue
from threading import Thread
import threading
import time

class CentralManagement(http.Controller):
    @http.route('/', website=True, auth='user', methods=['POST', 'GET'], csrf=False)
    def central_management_dashboard(self, **kwargs):

        desired_group_name = request.env['res.groups'].search([('name', '=', 'Daffodil Family Central Management System')])
        is_desired_group = request.env.user.id in desired_group_name.users.ids

        if is_desired_group:

            #API call from thread
            def thread_api_call(concern_data):

                dashboard_data = requests.get(url=concern_data['api_url'])
                if dashboard_data.status_code == 200:
                    try:
                        jason_dashboard_data = dashboard_data.json()
                        return {
                            'concern_url':concern_data['base_url'],
                            'name':concern_data['name'],
                            'email': concern_data['email'] if concern_data['email'] else "No",
                            'password': concern_data['password'] if concern_data['password'] else "No",
                            'logo': concern_data['logo'] if concern_data['logo'] else "https://mct.daffodilvarsity.edu.bd/images/diuIcon.png",
                            'data': jason_dashboard_data
                        }
                    except Exception as e:
                        return {
                            'concern_url': concern_data['base_url'],
                            'name': concern_data['name'],
                            'email': concern_data['email'] if concern_data['email'] else "No",
                            'password': concern_data['password'] if concern_data['password'] else "No",
                            'data': {}
                        }

                else:
                    return {
                        'concern_url': concern_data['base_url'],
                        'name': concern_data['name'],
                        'email': concern_data['email'] if concern_data['email'] else "No",
                        'password': concern_data['password'] if concern_data['password'] else "No",
                        'data': {}
                    }



            #Getting data from daffodil.family.concerns
            daffodil_family_concerns = request.env['daffodil.family.concerns'].sudo().search([])

            #Declare a que for storing information
            que = Queue()
            threads_list = list()

            #Creating multiple thread for multiple concerns
            for daffodil_family_concern in daffodil_family_concerns:
                URL = daffodil_family_concern.domain+"/api/central/management/dashboard/"
                #URL = "http://192.168.10.155:8070/api/central/management/dashboard/"
                t = Thread(target=lambda q, arg1: q.put(thread_api_call(arg1)), args=(que, {
                    'name':daffodil_family_concern.name.upper(),
                    'api_url':URL,
                    'base_url':daffodil_family_concern.domain,
                    'logo': daffodil_family_concern.logo,
                    'email':daffodil_family_concern.admin_user_email,
                    'password':daffodil_family_concern.admin_user_password
                }))
                print(threading.active_count())
                while threading.active_count() > 10:
                    time.sleep(1)
                t.start()
                threads_list.append(t)

            #Join all thread together for getting data al together so that we can return data together
            for t in threads_list:
                t.join()

            # Getting data from thread function
            central_management_sections = list()
            while not que.empty():
                result = que.get()
                if result['data']:
                    central_management_sections.append(result)

            return request.render("daffodil_central_management_dashboard.central_management_dashboard",
                                  {'central_management_sections': central_management_sections})
        else:
            return "You Don't have permission"

    @http.route('/<string:concern_name>', website=True, auth='user', methods=['POST', 'GET'], csrf=False)
    def central_management_concerns(self, concern_name = False, **kwargs):
        desired_group_name = request.env['res.groups'].search(
            [('name', '=', 'Daffodil Family Central Management System')])
        is_desired_group = request.env.user.id in desired_group_name.users.ids

        if is_desired_group:
            if concern_name:
                daffodil_family_concern = request.env['daffodil.family.concerns'].sudo().search([('name','=',concern_name.lower())])[-1]
                URL = daffodil_family_concern.domain+"/api/central/management/concern/dashboard/"
                #URL = "http://192.168.10.155:8070/api/central/management/concern/dashboard/"
                concern_dashboard_data = requests.get(url=URL)
                return request.render("daffodil_central_management_dashboard.central_management_concern",
                                      {'central_management_sections': concern_dashboard_data.json(),'concern_name':concern_name})
        else:
            return "You Don't have permission"

    @http.route('/<string:concern_name>/<string:module_name>', website=True, auth='user', methods=['POST', 'GET'],
                csrf=False)
    def central_management_module(self, concern_name=False,module_name=False, **kwargs):

        desired_group_name = request.env['res.groups'].search(
            [('name', '=', 'Daffodil Family Central Management System')])
        is_desired_group = request.env.user.id in desired_group_name.users.ids

        if is_desired_group:
            if module_name == "Support Ticket":
                daffodil_family_concern = request.env['daffodil.family.concerns'].sudo().search([('name', '=', concern_name.lower())])[-1]
                URL = daffodil_family_concern.domain + "/api/central/management/concern/dashboard/support/ticket"
                #URL = "http://192.168.10.155:8070/api/central/management/concern/dashboard/support/ticket"
                concern_dashboard_data = requests.get(url=URL)
                concern_dashboard_data_json = concern_dashboard_data.json()
                return request.render("daffodil_central_management_dashboard.central_management_module_support_ticket",
                                      {
                                          'central_management_module_card': concern_dashboard_data_json['card_information'],
                                          'central_management_module_table':concern_dashboard_data_json['table_information'],
                                          'concern_name': concern_name,
                                          'module_name':module_name
                                      })



            elif module_name == "Project":
                daffodil_family_concern = request.env['daffodil.family.concerns'].sudo().search([('name', '=', concern_name.lower())])[-1]
                URL = daffodil_family_concern.domain + "/api/central/management/concern/dashboard/project"
                #URL = "http://192.168.10.155:8070/api/central/management/concern/dashboard/project"
                concern_dashboard_data = requests.get(url=URL)
                concern_dashboard_data_json = concern_dashboard_data.json()
                return request.render("daffodil_central_management_dashboard.central_management_concern_project",
                                      {
                                          'central_management_module_card': concern_dashboard_data_json,
                                          'concern_name': concern_name,
                                          'module_name': module_name
                                      })


            elif module_name == "Event":

                daffodil_family_concern = request.env['daffodil.family.concerns'].sudo().search([('name', '=', concern_name.lower())])[-1]
                URL = daffodil_family_concern.domain + "/api/central/management/concern/dashboard/event"
                #URL = "http://192.168.10.155:8070/api/central/management/concern/dashboard/event"
                concern_dashboard_data = requests.get(url=URL)
                concern_dashboard_data_json = concern_dashboard_data.json()
                print(concern_dashboard_data_json)
                return request.render("daffodil_central_management_dashboard.central_management_module_event",
                                      {
                                          'central_management_module_card': concern_dashboard_data_json['card_information'],
                                          'central_management_module_table':concern_dashboard_data_json['table_information'],
                                          'concern_name': concern_name,
                                          'module_name':module_name
                                      })


            elif module_name == "Opportunity":

                daffodil_family_concern = request.env['daffodil.family.concerns'].sudo().search([('name', '=', concern_name.lower())])[-1]
                URL = daffodil_family_concern.domain + "/api/central/management/concern/dashboard/opportunity"
                #URL = "http://192.168.10.155:8070/api/central/management/concern/dashboard/opportunity"
                concern_dashboard_data = requests.get(url=URL)
                concern_dashboard_data_json = concern_dashboard_data.json()
                return request.render("daffodil_central_management_dashboard.central_management_module_opportunity",
                                      {
                                          'central_management_module_card': concern_dashboard_data_json['card_information'],
                                          'central_management_module_table':concern_dashboard_data_json['table_information'],
                                          'central_management_module_lead_table': concern_dashboard_data_json[
                                              'table_information_lead'],
                                          'concern_name': concern_name,
                                          'module_name':module_name
                                      })

            elif module_name == "Employee":

                daffodil_family_concern = request.env['daffodil.family.concerns'].sudo().search([('name', '=', concern_name.lower())])[-1]
                URL = daffodil_family_concern.domain + "/api/central/management/concern/dashboard/employee"
                #URL = "http://192.168.10.155:8070/api/central/management/concern/dashboard/employee"
                concern_dashboard_data = requests.get(url=URL)
                concern_dashboard_data_json = concern_dashboard_data.json()
                print(concern_dashboard_data_json)
                return request.render("daffodil_central_management_dashboard.central_management_module_employee",
                                      {
                                          'central_management_module_card': concern_dashboard_data_json['card_information'],
                                          'central_management_module_table': concern_dashboard_data_json[
                                              'table_information'],
                                          'concern_name': concern_name,
                                          'module_name': module_name
                                      })


            elif module_name == "Accounts":
                daffodil_family_concern = \
                request.env['daffodil.family.concerns'].sudo().search([('name', '=', concern_name.lower())])[-1]
                URL = daffodil_family_concern.domain + "/api/central/management/concern/dashboard/accounts"
                #URL = "http://192.168.10.155:8070/api/central/management/concern/dashboard/accounts"
                concern_dashboard_data = requests.get(url=URL)
                concern_dashboard_data_json = concern_dashboard_data.json()
                return request.render("daffodil_central_management_dashboard.central_management_module_accounts",
                                      {
                                          'central_management_module_card': concern_dashboard_data_json['card_information'],
                                          'central_management_module_table': concern_dashboard_data_json[
                                              'table_information'],
                                          'concern_name': concern_name,
                                          'module_name': module_name
                                      })
            else:
                return "Work in under process"
        else:
            return "You Don't have permission"



    @http.route('/<string:concern_name>/<string:module_name>/<string:project_id>', website=True, auth='user',
                methods=['POST', 'GET'],
                csrf=False)
    def central_management_module_task(self, concern_name=False, module_name=False,project_id=False, **kwargs):

        desired_group_name = request.env['res.groups'].search(
            [('name', '=', 'Daffodil Family Central Management System')])
        is_desired_group = request.env.user.id in desired_group_name.users.ids

        if is_desired_group:
            daffodil_family_concern = \
            request.env['daffodil.family.concerns'].sudo().search([('name', '=', concern_name.lower())])[-1]
            URL = daffodil_family_concern.domain + "/api/central/management/concern/dashboard/project/task?project_id="+str(project_id)
            #URL = "http://192.168.10.155:8070/api/central/management/concern/dashboard/project/task?project_id="+str(project_id)
            concern_dashboard_data = requests.get(url=URL)
            concern_dashboard_data_json = concern_dashboard_data.json()
            return request.render("daffodil_central_management_dashboard.central_management_module_project_task",
                                  {
                                      'central_management_module_card': concern_dashboard_data_json['card_information'],
                                      'central_management_module_table': concern_dashboard_data_json[
                                          'table_information'],
                                      'concern_name': concern_name,
                                      'module_name': module_name
                                  })
        else:
            return "You Don't have permission"
