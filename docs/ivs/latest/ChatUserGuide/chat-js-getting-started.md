---
source_url: https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-js-getting-started.html
---

# Getting Started with the IVS Chat Client Messaging JavaScript SDK
<a name="chat-js-getting-started"></a>

Before starting, you should be familiar with [Getting Started with Amazon IVS Chat](getting-started-chat.md).

## Add the Package
<a name="chat-js-add-package"></a>

Use either:

```
$ npm install --save amazon-ivs-chat-messaging
```

or:

```
$ yarn add amazon-ivs-chat-messaging
```

## React Native Support
<a name="chat-js-react-native-support"></a>

The IVS Chat Client Messaging JavaScript SDK has a `uuid` dependency which uses the `crypto.getRandomValues` method. Since this method is not supported in React Native, you need to install the additional polyfill `react-native-get-random-value` and import it at the top of the `index.js` file:

```
import 'react-native-get-random-values';
import {AppRegistry} from 'react-native';
import App from './src/App';
import {name as appName} from './app.json';

AppRegistry.registerComponent(appName, () => App);
```

## Set Up Your Backend
<a name="chat-js-setup-backend"></a>

This integration requires endpoints on your server that talk to the [Amazon IVS Chat API](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/Welcome.html). Use the [official AWS libraries](https://aws.amazon.com/developer/tools/) for access to the Amazon IVS API from your server. These libraries are accessible within several languages from the public packages; e.g., [node.js](https://www.npmjs.com/package/aws-sdk), [java](https://github.com/aws/aws-sdk-java), and [go](https://github.com/aws/aws-sdk-go).

Create a server endpoint that talks to the Amazon IVS Chat API [CreateChatToken](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_CreateChatToken.html) operation, to create a chat token for chat users.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
