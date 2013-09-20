/**
 * Created with PyCharm.
 * User: tobia
 * Date: 09/09/13
 * Time: 17:44
 * To change this template use File | Settings | File Templates.
 */


App.Models.Profile = Backbone.Model.extend({
    defaults: {
        public_username: 'Public username',
        location: 'No location defined'
    },

    urlRoot: '/api/profile/'
});
