---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-the-jssdk.html
---

The AWS SDK for JavaScript v2 has reached end-of-support. We recommend that you migrate to [AWS SDK for JavaScript v3](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-javascript-v2/).

# Loading the SDK for JavaScript
<a name="loading-the-jssdk"></a>

How you load the SDK for JavaScript depends on whether you are loading it to run in a web browser or in Node.js.

Not all services are immediately available in the SDK. To find out which services are currently supported by the AWS SDK for JavaScript, see [https://github.com/aws/aws-sdk-js/blob/master/SERVICES.md](https://github.com/aws/aws-sdk-js/blob/master/SERVICES.md)

------
#### [ Node.js ]

After you install the SDK, you can load the AWS package in your node application using `require`.

```
var AWS = require('aws-sdk');
```

------
#### [ React Native ]

To use the SDK in a React Native project, first install the SDK using npm:

```
npm install aws-sdk
```

In your application, reference the React Native compatible version of the SDK with the following code:

```
var AWS = require('aws-sdk/dist/aws-sdk-react-native');
```

------
#### [ Browser ]

The quickest way to get started with the SDK is to load the hosted SDK package directly from Amazon Web Services. To do this, add a `<script>` element to your HTML pages in the following form:

```
<script src="https://sdk.amazonaws.com/js/aws-sdk-{{SDK_VERSION_NUMBER}}.min.js"></script>
```

To find the current SDK\_VERSION\_NUMBER, see the API Reference for the SDK for JavaScript at [AWS SDK for JavaScript API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/).

After the SDK loads in your page, the SDK is available from the global variable `AWS` (or `window.AWS`).

If you bundle your code and module dependencies using [browserify](http://browserify.org), you load the SDK using `require`, just as you do in Node.js.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for JavaScript SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-javascript` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
