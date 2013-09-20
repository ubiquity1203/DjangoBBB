/**
 * Created with PyCharm.
 * User: tobia
 * Date: 13/09/13
 * Time: 14:09
 * To change this template use File | Settings | File Templates.
 */


App.Models.Application = Backbone.Model.extend({
    start : function(){
        var session = new App.Models.Session();
        session.getAuth(function(response){
            var router = new App.Routers.Router();
            Backbone.history.start();
        });
    }
});