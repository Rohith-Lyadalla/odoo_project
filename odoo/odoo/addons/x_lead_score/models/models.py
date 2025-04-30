# models/lead_scoring.py

from odoo import models, fields, api

class Lead(models.Model):
    _inherit = 'crm.lead'

    x_industry = fields.Selection([
        ('it', 'IT'),
        ('manufacturing', 'Manufacturing'),
        ('finance', 'Finance'),
        ('healthcare', 'Healthcare'),
    ], string="Industry")

    x_location = fields.Selection([
        ('us', 'United States'),
        ('eu', 'Europe'),
        ('asia', 'Asia'),
    ], string="Location")

    x_company_size = fields.Selection([
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ], string="Company Size")

    x_lead_score = fields.Integer(string="Lead Score", compute='_compute_lead_score', store=True)

    @api.depends('x_industry', 'x_location', 'x_company_size')
    def _compute_lead_score(self):
        for lead in self:
            score = 0

            # Scoring by x_industry
            if lead.x_industry == 'it':
                score += 30
            elif lead.x_industry == 'manufacturing':
                score += 20
            elif lead.x_industry == 'finance':
                score += 25
            elif lead.x_industry == 'healthcare':
                score += 15

            # Scoring by x_location
            if lead.x_location == 'us':
                score += 30
            elif lead.x_location == 'eu':
                score += 20
            elif lead.x_location == 'asia':
                score += 15

            # Scoring by company size
            if lead.x_company_size == 'large':
                score += 40
            elif lead.x_company_size == 'medium':
                score += 25
            elif lead.x_company_size == 'small':
                score += 10

            lead.x_lead_score = score
