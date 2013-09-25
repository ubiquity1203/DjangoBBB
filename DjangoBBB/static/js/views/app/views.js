/**
 * Created with PyCharm.
 * User: tobia
 * Date: 05/09/13
 * Time: 18:39
 * To change this template use File | Settings | File Templates.
 */

/*
* Global app view
*/
App.Views.AppView = Backbone.View.extend({

    initialize: function() {
    },

    render: function() {
        var session = new App.Models.Session();
        var user = session.get('user');
        console.log('user: '+user);
        this.$el.html(this.template({
            user: user
        }));
        return this;
    },

    selectMenuItem: function(menuItem) {
        $('.navbar .nav li').removeClass('active');
        if (menuItem) {
            $('.' + menuItem).addClass('active');
        }
    },

    addBreadcrumb: function(crumb) {
        var breadcrumb = $('#breadcrumb');
        if (breadcrumb.length > 0)
            breadcrumb.append(" > ").append(crumb);
        else
            breadcrumb.append(crumb);
    },

    removeBreadcrumb: function(crumb) {
        var breadcrumb = $('#breadcrumb');
        if (breadcrumb.length > 0)
            breadcrumb.append(" > ").append(crumb);
        else
            breadcrumb.append(crumb);
    },

    events: {

    }
});
