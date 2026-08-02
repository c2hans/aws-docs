---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/building-sdk-for-browsers.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Build the SDK for Browsers
<a name="building-sdk-for-browsers"></a>

Unlike SDK for JavaScript version 2 (V2), V3 is not provided as a JavaScript file with support included for a default set of services. Instead V3 enables you to bundle and include in the browser only the SDK for JavaScript files you require, reducing overhead. We recommend using Webpack to bundle the required SDK for JavaScript files, and any additional third-party packages your require, into a single `Javascript` file, and load it into browser scripts using a `<script>` tag. For more information about Webpack, see [Bundle applications with webpack](webpack.md).

If you work with the SDK outside of an environment that enforces CORS in your browser and if you want access to all services provided by the SDK for JavaScript, you can build a custom copy of the SDK locally by cloning the repository and running the same build tools that build the default hosted version of the SDK. The following sections describe the steps to build the SDK with extra services and API versions.

## Use the SDK Builder to build the SDK for JavaScript
<a name="using-the-sdk-builder"></a>

**Note**
Amazon Web Services version 3 (V3) no longer supports Browser Builder. To minimize bandwidth usage of browser applications, we recommend you import named modules, and bundle them to reduce size. For more information about bundling, see [Bundle applications with webpack](webpack.md).
