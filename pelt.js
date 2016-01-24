const electron = require('electron');
const BrowserWindow = electron.BrowserWindow;
const spawn = require('child_process').spawn;

var app = electron.app;
var mainWindow = null;
var pymain;

app.on('window-all-closed', function() {
  // Close application when all windows are closed
  pymain.kill('SIGINT');
  app.quit();
});

app.on('ready', function() {
  // Call python/Flask portion of program in main.py
  pymain = spawn('python', ['./src/main.py']);
  // Initialize request-promise
  var reqprm = require('request-promise');
  // Set address for python/Flask backend
  var mainAddr = "http://127.0.0.1:5000";

  var openWindow = function() {
    mainWindow = new BrowserWindow({title: "pelt", width: 600, height: 400});
    // Modified version of loadURL to avoid issues with caching
    mainWindow.loadURL(mainAddr, {"extraHeaders" : "pragma: no-cache\n"});
    mainWindow.on('closed', function() {
      mainWindow = null;
      pymain.kill('SIGINT');
    });
  };

  // init process
  var init = function() {
    reqprm(mainAddr)
      .then(function() {
        openWindow();
      })
      .catch(function() {
        // Retry init process
        init();
      });
  };

  // Run init
  init();
});
