from openupgradelib import openupgrade


def _merge_employee_contact(env):
    """
    Performing merge 'address_home_id' into 'work_contact_id'
    """
    partner_merge_wizard = env["base.partner.merge.automatic.wizard"]
    partner = env["res.partner"]
    env.cr.execute(
        """
        SELECT address_home_id, work_contact_id
        FROM hr_employee
        """
    )
    for address_home_id, work_contact_id in env.cr.fetchall():
        partner_merge_wizard._merge(
            [address_home_id, work_contact_id], partner.browse(work_contact_id)
        )


def _remove_address_home_id_from_views(env):
    """
    Remove references to the 'address_home_id' field in the views.
    """
    env.cr.execute(
        """
        SELECT id, arch_db
        FROM ir_ui_view
        WHERE arch_db->>'en_US' LIKE '%address_home_id%'
    """
    )
    views = env.cr.fetchall()

    for view_id, arch in views:
        updated_arch = arch.replace("address_home_id", "")
        env.cr.execute(
            """
            UPDATE ir_ui_view
            SET arch_db->>'en_US' = %s
            WHERE id = %s
        """,
            (updated_arch, view_id),
        )


def _final_remove_address_home_id(env):
    """
    Completely remove the 'address_home_id' field after migration.
    """
    # Remove references from the model and views, if they still exist.
    env.cr.execute(
        """
        DELETE FROM ir_model_fields
        WHERE name = 'address_home_id' AND model = 'hr.employee';
    """
    )

    # Update the views that may still contain the field
    env.cr.execute(
        """
        UPDATE ir_ui_view
        SET arch_db = jsonb_set(
            arch_db,
            ARRAY['en_US'],
            to_jsonb(REPLACE(arch_db->>'en_US', 'address_home_id', ''))
        )
        WHERE arch_db->>'en_US' LIKE '%address_home_id%';
    """
    )


@openupgrade.migrate()
def migrate(env, version):
    _merge_employee_contact(env)
    _remove_address_home_id_from_views(env)
    _final_remove_address_home_id(env)
