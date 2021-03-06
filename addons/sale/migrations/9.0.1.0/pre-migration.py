# -*- coding: utf-8 -*-
# © 2015 Microcom
# © 2016 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# © 2016 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# © 2016 Opener B.V. - Stefan Rijnhart
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


column_renames = {
    'sale_order': [
        ('section_id', 'team_id'),
    ],
    'account_invoice': [
        ('section_id', 'team_id'),
    ],
    # 'invoice_id' in 8.0 already referred to invoice lines
    'sale_order_line_invoice_rel': [
        ('invoice_id', 'invoice_line_id'),
    ],
}

column_copies = {
    'sale_order': [
        ('state', None, None),
    ],
    'sale_order_line': [
        ('state', None, None),
    ],
}


def map_order_state(cr):
    """ Map values for state field in sale.order and sale.order.line.
    Do this in the pre script because it influences the automatic calculation
    of the computed fields wrt. invoicing """
    openupgrade.map_values(
        cr, openupgrade.get_legacy_name('state'), 'state', [
            ('waiting_date', 'sale'), ('progress', 'sale'),
            ('manual', 'sale'), ('shipping_except', 'sale'),
            ('invoice_except', 'sale')],
        table='sale_order')
    cr.execute("""
        UPDATE sale_order_line sol
        SET state = so.state
        FROM sale_order so
        WHERE sol.order_id = so.id""")


@openupgrade.migrate()
def migrate(cr, version):
    openupgrade.rename_columns(cr, column_renames)
    openupgrade.copy_columns(cr, column_copies)
    map_order_state(cr)
