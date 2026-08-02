---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/configuring-the-jssdk.html
---

The AWS SDK for JavaScript v2 has reached end-of-support. We recommend that you migrate to [AWS SDK for JavaScript v3](https://docs.aws.amazon.com//sdk-for-javascript/v3/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs//developer/announcing-end-of-support-for-aws-sdk-for-javascript-v2/).

# Configuring the SDK for JavaScript
<a name="configuring-the-jssdk"></a>

Before you use the SDK for JavaScript to invoke web services using the API, you must configure the SDK. At a minimum, you must configure these settings:
+ The Region in which you will request services.
+ The *credentials* that authorize your access to SDK resources.

In addition to these settings, you may also have to configure permissions for your AWS resources. For example, you can limit access to an Amazon S3 bucket or restrict an Amazon DynamoDB table for read-only access.

The [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/) also contains settings, features, and other foundational concepts common among many of the AWS SDKs.

The topics in this section describe various ways to configure the SDK for JavaScript for Node.js and JavaScript running in a web browser.

**Topics**
+ [Using the Global Configuration Object](global-config-object.md)
+ [Setting the AWS Region](setting-region.md)
+ [Specifying Custom Endpoints](specifying-endpoints.md)
+ [SDK authentication with AWS](getting-your-credentials.md)
+ [Setting Credentials](setting-credentials.md)
+ [Locking API Versions](locking-api-versions.md)
+ [Node.js Considerations](node-js-considerations.md)
+ [Browser Script Considerations](browser-js-considerations.md)
+ [Bundling Applications with Webpack](webpack.md)
