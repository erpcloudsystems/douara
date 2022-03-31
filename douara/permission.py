from __future__ import unicode_literals
import frappe
import erpnext
from frappe import auth
import datetime
import json, ast
from frappe.share import add

@frappe.whitelist()
def share_lead(doc, method=None):
    '''
    users = frappe.db.sql(""" select owner from `tabToDo` where reference_type = 'Lead' and reference_name = '{name}' """.format(name=doc.reference_name), as_dict=1)
    read = 1
    write = 1
    share = 1
    everyone = 0
    for x in users:
        add('Lead', doc.reference_name, x.user, read, write, share, everyone)
'''