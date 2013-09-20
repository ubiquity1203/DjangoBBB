/**
 * Created with PyCharm.
 * User: tobia
 * Date: 09/09/13
 * Time: 17:46
 * To change this template use File | Settings | File Templates.
 */

App.Views.ProfileView = Backbone.View.extend({
    model: App.Models.Profile,
    tagName: 'div',
    className: 'profile',

    initialize: function() {
        console.log('Profile View initialized');
    },

    events: {
        'submit #showLocation': 'showLocation'
    },

    showLocation: function() {

    },

    render: function() {
        this.$el.html(this.template(this.model.attributes));
        return this;
    }
});