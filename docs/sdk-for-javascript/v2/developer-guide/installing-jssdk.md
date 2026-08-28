---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/installing-jssdk.html
---

The AWS SDK for JavaScript v2 has reached end-of-support. We recommend that you migrate to [AWS SDK for JavaScript v3](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-javascript-v2/).

# Installing the SDK for JavaScript
<a name="installing-jssdk"></a>

Whether and how you install the AWS SDK for JavaScript depends whether the code executes in Node.js modules or browser scripts.

Not all services are immediately available in the SDK. To find out which services are currently supported by the AWS SDK for JavaScript, see [https://github.com/aws/aws-sdk-js/blob/master/SERVICES.md](https://github.com/aws/aws-sdk-js/blob/master/SERVICES.md)

------
#### [ Node ]

The preferred way to install the AWS SDK for JavaScript for Node.js is to use [npm, the Node.js package manager](https://www.npmjs.com/). To do so, type this at the command line.

```
npm install aws-sdk
```

In the event you see this error message:

```
npm WARN deprecated node-uuid@1.4.8: Use uuid module instead
```

Type these commands at the command line:

```
npm uninstall --save node-uuid
npm install --save uuid
```

------
#### [ Browser ]

You don't have to install the SDK to use it in browser scripts. You can load the hosted SDK package directly from Amazon Web Services with a script in your HTML pages. The hosted SDK package supports the subset of AWS services that enforce cross-origin resource sharing (CORS). For more information, see [Loading the SDK for JavaScript](loading-the-jssdk.md).

You can create a custom build of the SDK in which you select the specific web services and versions that you want to use. You then download your custom SDK package for local development and host it for your application to use. For more information about creating a custom build of the SDK, see [Building the SDK for Browsers](building-sdk-for-browsers.md).

You can download minified and non-minified distributable versions of the current AWS SDK for JavaScript from GitHub at:

[https://github.com/aws/aws-sdk-js/tree/master/dist](https://github.com/aws/aws-sdk-js/tree/master/dist)

------

## Installing Using Bower
<a name="w2aac13c11b9"></a>

[Bower](https://bower.io) is a package manager for the web. After you install Bower, you can use it to install the SDK. To install the SDK using Bower, type the following into a terminal window:

```
bower install aws-sdk-js
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for JavaScript SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-javascript` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
