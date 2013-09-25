/**
 * Created with PyCharm.
 * User: tobia
 * Date: 06/09/13
 * Time: 13:00
 * To change this template use File | Settings | File Templates.
 */

App.Views.HomeView = Backbone.View.extend({
    events:{
        "click #showMeBtn":"showMeBtnClick"
    },

    render:function () {
        this.$el.html(this.template());
        return this;
    },

    showMeBtnClick:function () {
        console.log("showme");
    }

});