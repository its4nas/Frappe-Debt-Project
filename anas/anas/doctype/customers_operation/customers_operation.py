# Copyright (c) 2023, me and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class CustomersOperation(Document):
	def before_save(self):
		self.get_list()
	
	def get_list(self):
		doc = frappe.db.get_list('Customers Operation', fields=['customer_name','operation_type','price'])
		doc1 = frappe.db.get_list('Customer', fields=['full_name','type'])
		doc2 = frappe.db.get_list('Customer Type', fields=['type_name','max_value'])

		total = 0
		for d in doc:
			if self.customer_name == d.customer_name:
				if d.operation_type == 'عليه':
					total = total - int(d.price)
				else:
					total = total + int(d.price)
		
		type = ""
		for c in doc1:
			if self.customer_name == c.full_name:
				type = c.type

		max_value = 0
		for t in doc2:
			if type == t.type_name:
				max_value = t.max_value
		
		if self.operation_type == 'له':
			if total + int(self.price) > int(max_value):
				frappe.throw("Sorry this customer have to pay thier Debt ... \n total is:" + str(total)+ "\nThe Max amount is: " + str(max_value))
		else:
			pass