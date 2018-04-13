# -*- coding: utf-8 -*-
from odoo import http

# class Agromes(http.Controller):
#     @http.route('/agromes/agromes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agromes/agromes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('agromes.listing', {
#             'root': '/agromes/agromes',
#             'objects': http.request.env['agromes.agromes'].search([]),
#         })

#     @http.route('/agromes/agromes/objects/<model("agromes.agromes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agromes.object', {
#             'object': obj
#         })