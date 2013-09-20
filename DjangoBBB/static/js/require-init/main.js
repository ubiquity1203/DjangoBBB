// Filename: main.js

// Require.js allows us to configure shortcut alias
require.config({
  deps: ['main'],

  baseUrl: 'js',

  paths: {
    jquery: 'libs/jquery/jquery.min',
    underscore: 'libs/underscore/underscore.min',
    backbone: 'libs/backbone/backbone.min',
    parse: 'libs/parse/parse.min',
    require: 'libs/require/require.jquery',
    templates: '../templates'
  },
  shim: {
    'underscore': {
      exports: '_'
    },
    'backbone': {
      deps: [
        'underscore',
        'jquery'
      ],
      exports: 'Backbone'
    },
    'parse':{
      deps:[
        'require',
        'underscore',
        'jquery'
      ],
      exports: 'Parse'
    }
  }

});

require([
  // Load our app module and pass it to our definition function
  '../app'
], function(App){
  //console.log('main.js');

  // The "app" dependency is passed in as "App"
  // Again, the other dependencies passed in are not "AMD" therefore don't pass a parameter to this function
  App.initialize();
});