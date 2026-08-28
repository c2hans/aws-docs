---
source_url: https://docs.aws.amazon.com/dcv/latest/websdkguide/render-ui.html
---

# Use Amazon DCV Web UI SDK
<a name="render-ui"></a>

 The following tutorial shows you how to authenticate against the Amazon DCV server, connect to it and render the `DCVViewer` React component from the Amazon DCV Web UI SDK.

**Topics**
+ [Prerequisites](#prerequisites)
+ [Step 1: Prepare your HTML page](#prep-html-ui)
+ [Step 2: Authenticate, connect and render the `DCVViewer` React component.](#auth-conn-render)
+ [Updating from AWS-UI to Cloudscape Design System](#updateawsuitocloudscape)

## Prerequisites
<a name="prerequisites"></a>

 You need to install `React` , `ReactDOM` , `Cloudscape Design Components React` , `Cloudscape Design Global Styles` and `Cloudscape Design Design Tokens` .

```
$ npm i react react-dom @cloudscape-design/components @cloudscape-design/global-styles @cloudscape-design/design-tokens
```

 You would also need to download `Amazon DCV Web Client SDK` . See [Getting started with the Amazon DCV Web Client SDK](getting-started.md) to read the step-by-step guide on how to do that.

You must create an alias for importing the `dcv` module, since it is an external dependency for Amazon DCV Web UI SDK. For instance, if you are using webpack to bundle your web app, you can use the [ resolve.alias](https://webpack.js.org/configuration/resolve/#resolvealias) option like so:

```
const path = require('path');

module.exports = {
  //...
  resolve: {
    alias: {
      dcv: path.resolve('path', 'to', 'dcv.js'),
    },
  },
};
```

If you are using rollup for bundling, you can install [ @rollup/plugin-alias](https://www.npmjs.com/package/@rollup/plugin-alias), and use it like so:

```
import alias from '@rollup/plugin-alias';
const path = require('path');

module.exports = {
  //...
  plugins: [
    alias({
      entries: [
        { find: 'dcv', replacement: path.resolve('path', 'to', 'dcv.js') },
      ]
    })
  ]
};
```

## Step 1: Prepare your HTML page
<a name="prep-html-ui"></a>

 In your web page, you must load the required JavaScript modules and you should have a `<div>` HTML element with a valid `id` where the entry component of your app will be rendered.

For example:

```
<!DOCTYPE html>
<html lang="en" style="height: 100%;">
  <head>
    <title>DCV first connection</title>
  </head>
  <body style="height: 100%;">
    <div id="root" style="height: 100%;"></div>
    <script type="module" src="index.js"></script>
  </body>
</html>
```

## Step 2: Authenticate, connect and render the `DCVViewer` React component.
<a name="auth-conn-render"></a>

 This section shows how to complete the user authentication process, how to connect the Amazon DCV server, and how to render the `DCVViewer` React component.

 First, from the `index.js` file, import `React` , `ReactDOM` and your top level `App` component.

```
import React from "react";
import ReactDOM from 'react-dom';
import App from './App';
```

Render the top level container node of your app.

```
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
```

 In the `App.js` file, import the Amazon DCV Web Client SDK as a ESM module, the `DCVViewer` React component from the Amazon DCV Web UI SDK, `React` and the `Cloudscape Design Global Styles` package.

```
import React from "react";
import dcv from "dcv";
import "@cloudscape-design/global-styles/index.css";
import {DCVViewer} from "./dcv-ui/dcv-ui.js";
```

 Following is an example showing how to authenticate against the Amazon DCV Server and render the `DCVViewer` React component from Amazon DCV Web UI SDK, provided the authentication was successful.

```
const LOG_LEVEL = dcv.LogLevel.INFO;
const SERVER_URL = "https://your-dcv-server-url:port/";
const BASE_URL = "/static/js/dcvjs";

let auth;

function App() {
  const [authenticated, setAuthenticated] = React.useState(false);
  const [sessionId, setSessionId] = React.useState('');
  const [authToken, setAuthToken] = React.useState('');
  const [credentials, setCredentials] = React.useState({});

  const onSuccess = (_, result) => {
    var { sessionId, authToken } = { ...result[0] };

    console.log("Authentication successful.");

    setSessionId(sessionId);
    setAuthToken(authToken);
    setAuthenticated(true);
    setCredentials({});
  }

  const onPromptCredentials = (_, credentialsChallenge) => {
    let requestedCredentials = {};

    credentialsChallenge.requiredCredentials.forEach(challenge => requestedCredentials[challenge.name] = "");
    setCredentials(requestedCredentials);
  }

  const authenticate = () => {
    dcv.setLogLevel(LOG_LEVEL);

    auth = dcv.authenticate(
      SERVER_URL,
      {
        promptCredentials: onPromptCredentials,
        error: onError,
        success: onSuccess
      }
    );
  }

  const updateCredentials = (e) => {
    const { name, value } = e.target;
    setCredentials({
      ...credentials,
      [name]: value
    });
  }

  const submitCredentials = (e) => {
    auth.sendCredentials(credentials);
    e.preventDefault();
  }

  React.useEffect(() => {
    if (!authenticated) {
      authenticate();
    }
  }, [authenticated]);

  const handleDisconnect = (reason) => {
    console.log("Disconnected: " + reason.message + " (code: " + reason.code + ")");
    auth.retry();
    setAuthenticated(false);
  }

  return (
    authenticated ?
    <DCVViewer
      dcv={{
        sessionId: sessionId,
        authToken: authToken,
        serverUrl: SERVER_URL,
        baseUrl: BASE_URL,
        onDisconnect: handleDisconnect,
        logLevel: LOG_LEVEL
      }}
      uiConfig={{
        toolbar: {
          visible: true,
          fullscreenButton: true,
          multimonitorButton: true,
        },
      }}
    />
    :
    <div
      style={{
        height: window.innerHeight,
        backgroundColor: "#373737",
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      <form>
        <fieldset>
          {Object.keys(credentials).map((cred) => (
            <input
              key={cred}
              name={cred}
              placeholder={cred}
              type={cred === "password" ? "password" : "text"}
              onChange={updateCredentials}
              value={credentials[cred]}
            />
          ))}
        </fieldset>
        <button
          type="submit"
          onClick={submitCredentials}
        >
          Login
        </button>
      </form>
    </div>
  );
}

const onError = (_, error) => {
  console.log("Error during the authentication: " + error.message);
}

export default App;
```

 The `promptCredentials` , `error` , and `success` functions are mandatory callback functions that must be defined in the authentication process.

 If the Amazon DCV server prompts for credentials, the `promptCredentials` callback function receives the requested credential challenge from the Amazon DCV server. If the Amazon DCV server is configured to use system authentication, then the credentials must be provided in the form of a user name and a password.

 If authentication fails, the `error` callback function receives an error object from the Amazon DCV server.

 If the authentication succeeds, the `success` callback function receives an array of couples that includes the session id ( `sessionId` ) and authorization tokens ( `authToken` ) for each session that the user is allowed to connect to on the Amazon DCV server. The code sample above updates the React state to render the `DCVViewer` component on successful authentication.

 To know more about the properties accepted by this component, see the [ Amazon DCV Web UI SDK reference](https://docs.aws.amazon.com/dcv/latest/websdkguide/dcv-viewer.html#DCVViewer).

 To know more about self-signed certificates, see the [ Redirection clarifications with self-signed certificates](https://docs.aws.amazon.com/dcv/latest/adminguide/redirection-clarifications-with-self-signed-certs.html).

## Updating from AWS-UI to Cloudscape Design System
<a name="updateawsuitocloudscape"></a>

 Starting SDK version 1.3.0 we updated our `DCVViewer` component from AWS-UI to its evolution: [Cloudscape Design](https://cloudscape.design/).

 Cloudscape uses a different visual theme than AWS-UI, but the underlying code base remains the same. Thus, migrating your application based on the `DCVViewer` should be easy. To migrate, replace the AWS-UI related NPM packages you've installed with the associated Cloudscape packages:

| AWS-UI package name | Cloudscape package name |
| --- | --- |
| @awsui/components-react | @cloudscape-design/components |
| @awsui/global-styles | @cloudscape-design/global-styles |
| @awsui/collection-hooks | @cloudscape-design/collection-hooks |
| @awsui/design-tokens | @cloudscape-design/design-tokens |

 For further details on the migration please refear to the [AWS-UI GitHub documentation page](https://github.com/aws/awsui-documentation).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
