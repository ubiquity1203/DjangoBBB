/**
* Created with PyCharm.
* User: tobia
* Date: 13/09/13
* Time: 16:31
* To change this template use File | Settings | File Templates.
*/

App.Routers.BaseRouter = Backbone.Router.extend({
    before: function(){},
    after: function(){},
    route : function(route, name, callback){
        if (!_.isRegExp(route)) route = this._routeToRegExp(route);
        if (_.isFunction(name)) {
            callback = name;
            name = '';
        }
        if (!callback) callback = this[name];

        var router = this;

        Backbone.history.route(route, function(fragment) {
            var args = router._extractParameters(route, fragment);
            var next = function(){
                callback && callback.apply(router, args);
                router.trigger.apply(router, ['route:' + name].concat(args));
                router.trigger('route', name, args);
                Backbone.history.trigger('route', router, name, args);
                router.after.apply(router, args);
            }
            router.before.apply(router, [args, next]);
        });
        return this;
    }
});