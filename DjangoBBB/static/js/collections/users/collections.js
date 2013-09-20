/**
 * Created with PyCharm.
 * User: tobia
 * Date: 06/09/13
 * Time: 12:42
 * To change this template use File | Settings | File Templates.
 */


App.Collections.Users = Backbone.Collection.extend({
    model: App.Models.User,
    url: '/api/users/'
});
