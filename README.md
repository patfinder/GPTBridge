
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

## TODO

- Authenticate access with password?
- Lock Selenium to avoid multiple concurrent queries.
- Write log of user's queries, with IP address.
- Keep previous query on UI, write new query and result on top.

