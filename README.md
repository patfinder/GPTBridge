
## GPTBridge

- Server Repo: git@github.com:patfinder/GPTBridge.git
- App repo: git@github.com:patfinder/GPTBridge-app.git

- ChatGPT bridge is an application supports submitting a prompt to ChatGPT and retrieve the result.
- It uses Selenium to control a ChatGPT website.
- The web server to receive the UI request is Python http.server. The app UI is a React app.

### UI App

- App is configured to be hosted on the same web server as GPTBridge server.
    The folder is /app. Open /app/index.html

## Notes

- To serve React app from the same server, build React app:
    npm run build
- Then create link to build folder of React app.
    ln -s ../GPTBridge-app/build/ app 

## Step to start app

### Start GPTBridge server

- NOTE: This is tested and worked for Firefox on Ubuntu.
    - Chrome seem not working (properly because of Chrome security block to automation)

- Open Firefox with the profile used for running Selenium
  (This profile folder must be the same as FirefoxProfile() option in code.)

firefox --profile /home/vuong/tmp/FirefoxProfile

- Go to GPTBridge folder.
- Start GPTBridge python server with below command:

```shell
python main.py
```

A Firefox browser will be launched with ChatGPT opened. 

- Login to ChatGPT using your account if you haven't.

### Open UI app (GPTBridge-app)

- Open UI app with this URL: http://localhost:8000/app/index.html
  (See below for how to host on Internet)

- You can now start send query to ChatGPT and view response.

### Expose your server to Internet

If you want to expose your app to Internet, follow below steps:

- Register account and login to ngrok.com. This tool will help you to expose the local server to the Internet.
- On dashboard.ngrok.com, open Getting Started > Setup & Installation; Follow instructions there. Major steps .
- Install ngrok to local machine.
- Follow the instructions there to configure (authenticate) your local ngrok.

```shell
ngrok config add-authtoken 2V5xp6i......_....USNVA
```

- Run below command to expose your server to Internet

```shell
ngrok http http://localhost:8000
```

Ngrok console will display the status of the server, with one line similar to below:

```console
...
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://ed64-2607-fea8-4f41-6700-c314-5b14-2762-2d50.ngrok-free.app -> http://localhost:8000
...

```

Now you can open the URL on the "Forwarding" line above to access your server from Internet.


## TODO

- Authenticate access with password?
- Lock Selenium to avoid multiple concurrent queries.
- Write log of user's queries, with IP address.
- Keep previous query on UI, write new query and result on top.

