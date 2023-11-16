# Copyright 2018 Tecnativa - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    product_brand_id = fields.Many2one(comodel_name="product.brand", string="Brand")

    @property
    def _table_query(self):
        return '%s %s %s %s' % (self._select(), self._from(), self._where(), self._group_by())

    @api.model
    def _select(self):
        select_str = super()._select()
        select_str += """
            , template.product_brand_id as product_brand_id
            """
        return select_str

    @api.model
    def _group_by(self):
        return '''
            GROUP BY
                line.id,
                line.move_id,
                line.product_id,
                line.account_id,
                line.analytic_account_id,
                line.journal_id,
                line.company_id,
                line.currency_id,
                line.partner_id,
                move.name,
                move.state,
                move.move_type,
                move.amount_residual_signed,
                move.amount_total_signed,
                move.partner_id,
                move.invoice_user_id,
                move.fiscal_position_id,
                move.invoice_date,
                move.date,
                move.invoice_date_due,
                move.invoice_payment_term_id,
                move.payment_state,
                move.team_id,
                move.l10n_latam_document_type_id,
                uom_template.id,
                uom_line.factor,
                template.categ_id,
                COALESCE(partner.country_id, commercial_partner.country_id),
                currency_table.rate,
                contact_partner.state_id,
                template.product_brand_id
            '''
