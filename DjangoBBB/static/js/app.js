/**
 * Created with PyCharm.
 * User: tobia
 * Date: 05/09/13
 * Time: 18:27
 * To change this template use File | Settings | File Templates.
 */

(function() {
  var _sync = Backbone.sync;
  Backbone.sync = function(method, model, options){
    options.beforeSend = function(xhr){
      var token = $('meta[name="csrf-token"]').attr('content');
      xhr.setRequestHeader('X-CSRFToken', token);
    };
    return _sync(method, model, options);
  };
})();

var App = {
    Models: {},
    Collections: {},
    Views: {},
    Helpers: {},
    Routers: {},

    loadTemplates: function(views, callback) {

        var deferreds = [];

        $.each(views, function(index, view) {
            if (App.Views[view]) {
                console.log('Loading ' + view);
                deferreds.push($.get('/static/tpl/' + view + '.html', function(data) {
                    App.Views[view].prototype.template = _.template(data);
                }, 'html'));
            } else {
                alert(view + " not found");
            }
        });

        $.when.apply(null, deferreds).done(callback);
    }
};

//$(document).on("ready",function() {
//
//    App.loadTemplates([
//        'AppView',
//        'AlertView',
//        'UserView',
//        'UsersView',
//        'ProfileView'
//    ], function() {
//        App.router = new App.Router();
//        Backbone.history.start();
//    });
//});

$(document).on("ready",function() {
    var Application = new App.Models.Application();
    App.loadTemplates([
        'AppView',
        'LoginView',
        'AlertView',
        'SearchView',
        'HomeView',
        'ProfileView'
    ], function(){
        Application.start()
    });
});
