from odoo import models

class FilaReport(models.AbstractModel):
    _name = 'report.resource.resource_booking_report'
    _description = 'Informe Cita'

    def _get_report_values(self, docids, data=None):
        docs = self.env['resource.booking'].browse(docids)
        return {'docs': docs}
