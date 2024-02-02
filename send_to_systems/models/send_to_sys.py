# -*- coding: utf-8 -*-

from odoo import models, fields, api

import requests
import json

import logging

LOGGER = logging.getLogger(__name__)


class send_to(models.Model):

    def send_to_system(self, data,fun_call):
        #
        url = 'http://localhost:8015'
        db = 'shamel_receive'
        username = 'receive'
        password = '1'

        # auth with db
        authenticated = self.auth_with_db(url, username, password, db)
        if authenticated:
            url = url + "/object/" + fun_call

            payload = {
                "params": {
                    "args": [],
                    "kwargs":  data

                }

            }
            payload = json.dumps(payload)
            headers = {
                'content-type': "application/json",

            }

            response = requests.request("POST", url, data=payload, headers=headers, cookies=authenticated['cookies'])

            print("result response :> ", response.text)




    def auth_with_db(self, url, username, password, db_name):

        url += "/auth"
        payload = {"params": {"login": username, "password": password,
                              "db": db_name}}

        payload = json.dumps(payload)
        headers = {
            'content-type': "application/json",
            # 'cache-control': "no-cache",
            # 'postman-token': "1c96a08b-f55e-d2b0-b63c-a4eb9b412e74"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        cookies = response.cookies
        if response.status_code == 200:
            response = json.loads(response.text)
            if "result" in response and response['result']['uid'] > 0:
                return {'cookies': cookies}
            else:
                return False
        else:
            return False

"""
    def update_system(self,filter ,data,fun_call):
        #
        url = 'http://localhost:8015'
        db = 'shamel_receive'
        username = 'receive'
        password = '1'

        # auth with db
        authenticated = self.auth_with_db(url, username, password, db)
        if authenticated:
            url = url + "/object/" + fun_call

            payload = {
                "params": {
                    "filter": [filter],
                    "args": [],
                    "kwargs":  data

                }

            }
            payload = json.dumps(payload)
            headers = {
                'content-type': "application/json",

            }

            response = requests.request("PUT", url, data=payload, headers=headers, cookies=authenticated['cookies'])

            print("result response :> ", response.text)
"""
