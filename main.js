const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

var mainWindow = null;

app.on('window-all-closed', function() {
  // Close application when all windows are closed
  app.quit();
});

app.on('ready', function() {
  // Call python/Flask portion of program in main.py
  var pymain = require('child_process').spawn('python', ['./src/main.py']);
  // Initialize request-promise
  var reqprm = require('request-promise');
  // Set address for python/Flask backend
  var mainAddr = "http://127.0.0.1:5000";

  var openWindow = function() {
    mainWindow = new BrowserWindow({title: "peyl", width: 800, height: 600});
    mainWindow.loadURL(mainAddr);
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
