import frappe


@frappe.whitelist()
def firstApi():
    doc = frappe.get_doc('Test', '001')
    doc.first_name = "VIRAJ"
    doc.full_name = doc.first_name + " " + doc.last_name
    doc.save()
    return doc


# @frappe.whitelist
# def read(first_name=None):
#     doc = frappe.db.get_value('Test',{'first_name':first_name},['first_name','last_name','age','email'])
#     return doc


# @frappe.whitelist()
# def update(id=None, fname=None):
#     doc = frappe.get_doc('Test', id)
#     doc.first_name = fname
#     doc.save()
#     return "doctype successful"
