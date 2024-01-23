# -*- coding: utf-8 -*-

from odoo import models, fields, api
import json

from datetime import datetime, timedelta

from xmlrpc import client as xmlrpc_client
import ssl
import requests
import json

import logging

LOGGER = logging.getLogger(__name__)


class send_subject_inherit(models.Model):
    _inherit = 'school.subject'

    def send_subject_to_systems(self, subject_data):
        #
        url = 'http://localhost:8015'
        db = 'shamel_receive'
        username = 'receive'
        password = '1'

        # auth with db
        authenticated = self.auth_with_db(url, username, password, db)
        if authenticated:
            url = url + "/object/school.subject/create_subject"

            payload = {
                "params": {
                    "args": [],
                    "kwargs":  subject_data

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

    @api.model
    def create(self, vals):
        record = super(send_subject_inherit, self).create(vals)


        #for rec in record.student_ids:


        self.send_subject_to_systems({'subject_name': record.subject_name, 'year_id': record.year_id.year, 'student_ids': [x.student_no for x in record.student_ids] })

        return record
