# -*- coding: utf-8 -*-
# Copyright 2014 Anubía, soluciones en la nube,SL (http://www.anubia.es)
# Copyright Juan Formoso <jfv@anubia.es>
# Copyright Alejandro Santana <alejandrosantana@anubia.es>
# Copyright Pedro M. Baeza <pedro.baeza@tecnativa.com>
# Copyright 2017 valentin vinagre  <valentin.vinagre@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import models


class PrintWizard(models.TransientModel):
    _inherit = 'account.balance.reporting.print.wizard'

    def xlsx_export(self):
        self.ensure_one()
        data = self.read()[0]
        report_name = 'account_balance_reporting_xlsx.generic_report'
        return {
            'type': 'ir.actions.report.xml',
            'report_name': report_name,
            'report_type': 'xlsx',
            'datas': data,
        }
