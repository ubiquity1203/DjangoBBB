/**
 * Created with PyCharm.
 * User: tobia
 * Date: 06/09/13
 * Time: 11:34
 * To change this template use File | Settings | File Templates.
 */

/*
* Authentication views
*
* Register
*/
App.Views.SignupView = Backbone.View.extend({
    id: 'Signup',
    url: '/api/auth/signup',

    initialize: function() {
        console.log("Signup view initialized.")
    },

    events: {
        "blur #inputUsername": "validateUsername",
        "blur #inputPasswordConfirm": "validatePassword",
        "click #signupButton": "signup"
    },

    validateUsername: function() {
        event.preventDefault();
        console.log('Validating username...');
    },

    validatePassword: function() {
        event.preventDefault();
        console.log('Validating password...');
        if ($('#inputPassword').val() != $('#inputPasswordConfirm').val())
            $('#passwordMatch').hide();
        else
            $('#passwordMatch').show();
    },

    signup: function() {
        event.preventDefault();
        console.log('Signing up...');
        var url = self.url;
        console.log('signup url: ' + url);
        var formValues = {
            userName: $('#inputUsername').val(),
            firstName: $('#inputUsername').val(),
            lastName: $('#inputUsername').val(),
            password: $('#inputPassword').val(),
            passwordConfirm: $('#inputPasswordConfirm').val()
        }
        // TODO: post signup values
        // accept and validate response
    },

    render: function() {
        this.$el.html(this.template());
        return this;
    }
});



/*
* Authentication views
*
* Login
*/
App.Views.LoginView = Backbone.View.extend({
    id: 'Login',
    url: '/api/auth/login',

    initialize: function() {
        console.log("Login view initialized.")
    },

    events: {
        "click #loginButton": "login"
    },

    login: function() {
        event.preventDefault();
        console.log('Loggin in...');
        var url = self.url;
        console.log('Login url: ' + url);
        var formValues = {
            username: $('#inputUsername').val(),
            password: $('#inputPassword').val()
        }
    },

    render: function() {
        this.$el.html(this.template());
        return this;
    }
});

/*
* Authentication views
*
* Logout
*/
App.Views.LogoutView = Backbone.View.extend({
    id: 'Logout',
    url: '/api/auth/logout',

    initialize: function() {
        console.log("Logout view initialized.");
    },

    events: {
        "click #logoutButton": "logout"
    },

    logout: function() {
        event.preventDefault();
        console.log('Loggin out...');
        var url = self.url;
        console.log('Logout url: ' + url);
    },

    render: function() {
        this.$el.html(this.template());
        return this;
    }
});