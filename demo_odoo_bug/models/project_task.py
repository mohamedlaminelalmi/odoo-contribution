# -*- coding: utf-8 -*-
from odoo import _, api, fields, models, Command
from odoo.exceptions import ValidationError

class DemoTemplate(models.Model):
    _name = 'demo.template'
    _description = 'Demo Template'

    name = fields.Char(
        string='Name',
        required=True,
    )
    line_ids = fields.One2many(
        comodel_name='demo.template.line',
        inverse_name='template_id',
    )


class DemoTemplateLine(models.Model):
    _name = 'demo.template.line'
    _description = 'Demo Template Line'

    template_id = fields.Many2one(
        comodel_name='demo.template',
    )
    name = fields.Char(
        string='Name',
        required=True,
    )


class ProjectTask(models.Model):
    _inherit = 'project.task'

    template_id = fields.Many2one(
        comodel_name='demo.template',
    )
    line_ids = fields.One2many(
        comodel_name='demo.line',
        inverse_name='task_id',
    )

    @api.onchange('template_id')
    def _onchange_template_id(self):
        lines = [fields.Command.clear()]
        lines += [
            fields.Command.create({
                'template_line_id': line.id,
            })
            for line in self.template_id.line_ids
        ]
        self.line_ids = lines


class DemoLine(models.Model):
    _name = 'demo.line'
    _description = 'Demo Line'

    task_id = fields.Many2one(
        comodel_name='project.task',
    )
    template_line_id = fields.Many2one(
        comodel_name='demo.template.line',
    )
