/**
 * Created with PyCharm.
 * User: tobia
 * Date: 12/06/13
 * Time: 17:50
 * To change this template use File | Settings | File Templates.
 */

App.Routers.Router = Backbone.Router.extend({
    routes: {
        '': 'index',
        'login': 'login',
        'logout': 'logout',
        'profile': 'profile',
        'lenses': 'lenses',
        'lens': 'lens',
        'comments': 'comments'
    },

    initialize: function() {
        console.log("Router initialized");
        App.app = new App.Views.AppView();
        $('#content').html(App.app.render().el);
        this.$content = $("#App");
    },

    index: function() {
        this.$content.empty();
        App.app.selectMenuItem('home-menu');
    },

    lenses: function() {
        var lenses = new App.Collections.Lenses();
        var self = this;
        lenses.fetch().then(function(data) {
            self.$content.html(new App.Views.LensView({collection: lenses}).render().el);
        });
        App.app.selectMenuItem('lenses-menu');
    },

    profile: function() {
        var profile = new App.Models.Profile();
        var self = this;
        profile.fetch().then(function(data) {
            self.$content.html(new App.Views.ProfileView({model: profile}).render().el);
        });
        App.app.selectMenuItem('profile-menu');
    },

    addcontact: function() {
        var contacts = new App.Collections.Contacts();
        var self = this;
        contacts.fetch({cache: false}).then(function(data) {
            var addcontact = new App.Views.AddContactView({ collection: contacts});
            self.$content.html(addcontact.render().el);
        });
        //var contact = new App.Models.Contact();
        //ko.applyBindings(App.ViewModels.AddContactView(contact),  $('#kb_observable')[0]);
        App.app.selectMenuItem('addcontact-menu');
    }
});