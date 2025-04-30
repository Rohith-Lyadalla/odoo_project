# -*- coding: utf-8 -*-
# from odoo import http


# class XLeadScore(http.Controller):
#     @http.route('/x_lead_score/x_lead_score', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/x_lead_score/x_lead_score/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('x_lead_score.listing', {
#             'root': '/x_lead_score/x_lead_score',
#             'objects': http.request.env['x_lead_score.x_lead_score'].search([]),
#         })

#     @http.route('/x_lead_score/x_lead_score/objects/<model("x_lead_score.x_lead_score"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('x_lead_score.object', {
#             'object': obj
#         })

