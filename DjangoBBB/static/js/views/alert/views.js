/**
 * Created with PyCharm.
 * User: tobia
 * Date: 05/09/13
 * Time: 18:45
 * To change this template use File | Settings | File Templates.
 */

/*
* Alert view
*/
App.Views.AlertView = Backbone.View.extend({
    initialize: function() {
        window.setTimeout(function() {
            $(".alert").fadeTo(500, 0).slideUp(500, function(){
                $(this).remove();
            });
            //$('.alert').alert('close')
        }, 2000);
    },

    render: function() {
        this.$el.html(this.template(this.model.attributes));
        return this;
    }
});
