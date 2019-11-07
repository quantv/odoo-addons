odoo.define('hr_selfservice.action_conditionable', function (require) {
    "use strict";
    var View = require('web.FormController');
    View.include({
        on_attach_callback: function(action) {
            this._super();
            if (this.modelName === 'hr.employee'){
                var access = this.model.get(this.handle).data.employee_display_personal_data === false ? 'none' : 'inline-block'
                this.$buttons.find('.o_form_button_edit').css('display', access);
            }
        }
    });
});