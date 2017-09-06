# Copyright (c) 2017, DOKOS and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

def execute():
    if frappe.db.exists("Address Template", "Switzerland"):
        updated_template = frappe.get_doc("Address Template", "Switzerland")
        updated_template.update({"template": "{{ address_line1 }}<br>{% if address_line2 %}{{ address_line2 }}<br>{% endif -%}\n{% if pincode %}{{ pincode }} {% endif -%}{{ city }}<br>\n{{ country }}"})
        updated_template.save()

    else:
        new_template = frappe.get_doc({
                    "doctype": "Address Template",
                    "country": "Switzerland",
                    "template": "{{ address_line1 }}<br>{% if address_line2 %}{{ address_line2 }}<br>{% endif -%}\n{% if pincode %}{{ pincode }} {% endif -%}{{ city }}"
                    })
        new_template.insert()
        new_template.save()

    frappe.db.commit()
