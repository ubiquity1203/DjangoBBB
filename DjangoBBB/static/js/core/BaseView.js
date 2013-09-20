/**
* Created with PyCharm.
* User: tobia
* Date: 13/09/13
* Time: 16:32
* To change this template use File | Settings | File Templates.
*/

App.Views.BaseView = Backbone.View.extend({
    close : function(){
        if(this.childViews){
            this.childViews.close();
        }
        this.remove();
    }
});