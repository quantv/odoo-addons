# Copyright 2017-2019 Onestein (<https://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from lxml import etree

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    country_id = fields.Many2one(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    passport_id = fields.Char(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    bank_account_id = fields.Many2one(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    address_home_id = fields.Many2one(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    gender = fields.Selection(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    marital = fields.Selection(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    spouse_complete_name = fields.Char(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    spouse_birthdate = fields.Date(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    children = fields.Integer(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    place_of_birth = fields.Char(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    country_of_birth = fields.Many2one(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    birthday = fields.Date(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    ssnid = fields.Char(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    sinid = fields.Char(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    identification_id = fields.Char(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    permit_no = fields.Char(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    visa_no = fields.Char(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    visa_expire = fields.Date(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    additional_note = fields.Text(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    certificate = fields.Selection(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    study_field = fields.Char(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    study_school = fields.Char(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    emergency_contact = fields.Char(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    emergency_phone = fields.Char(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    km_home_work = fields.Integer(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")
    google_drive_link = fields.Char(groups="hr.group_hr_user,hr_selfservice.group_hr_employee")

    @api.depends('user_id')
    def _compute_display_personal_data(self):
        for employee in self:
            employee.employee_display_personal_data = False
            if self.user_has_groups('hr.group_hr_user'):
                employee.employee_display_personal_data = True
            elif employee.user_id == self.env.user:
                employee.employee_display_personal_data = True

    employee_display_personal_data = fields.Boolean(
        compute='_compute_display_personal_data'
    )
