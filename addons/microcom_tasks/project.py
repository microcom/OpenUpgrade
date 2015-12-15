from openerp import api, fields, models
from openerp import exceptions
from openerp.tools.translate import _


class project(models.Model):
    _inherit = "project.task"

    planned_hours = fields.Float('Planned')
    priority = fields.Selection(selection=[('0', _('None')), ('1', _('Nice to have')), ('2', _('Low')),
                                           ('3', _('Normal')), ('4', _('High')), ('5', _('Very High'))],
                                track_visibility='onchange',
                                help="A task's priority indicates when the task should be done:\n"
                                     " 5 - Extremely High (Down situation. Should be done immediately)\n"
                                     " 4 - High (It is urgent but it can wait until we finish what we've started)\n"
                                     " 3 - Normal (Do in sequence order and after higher priority's tasks)\n"
                                     " 2 - Low (To do when there's a lack of tasks)\n"
                                     " 1 - Nice to have (Task not very time-consuming to be done while in the module)"
                                     " 0 - No priority set"
                                )

    # Prevents users from moving a task without setting a priority level first.
    @api.constrains('stage_id')
    def onchange_stage_id(self):
        if self.priority == '0' and self.stage_id.sequence != 2:  # SIGNALE
            raise exceptions.RedirectWarning(_("You must specify a task priority in order to change the task's stage."))
