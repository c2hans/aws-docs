---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-credentials.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Set credentials
<a name="setting-credentials"></a>

AWS uses credentials to identify who is calling services and whether access to the requested resources is allowed.

Whether running in a web browser or in a Node.js server, your JavaScript code must obtain valid credentials before it can access services through the API. Credentials can be set per service, by passing credentials directly to a service object.

There are several ways to set credentials that differ between Node.js and JavaScript in web browsers. The topics in this section describe how to set credentials in Node.js or web browsers. In each case, the options are presented in recommended order.

## Best practices for credentials
<a name="credentials-best-practices"></a>

Properly setting credentials ensures that your application or browser script can access the services and resources needed while minimizing exposure to security issues that may impact mission critical applications or compromise sensitive data.

An important principle to apply when setting credentials is to always grant the least privilege required for your task. It's more secure to provide minimal permissions on your resources and add further permissions as needed, rather than provide permissions that exceed the least privilege and, as a result, be required to fix security issues you might discover later. For example, unless you have a need to read and write individual resources, such as objects in an Amazon S3 bucket or a DynamoDB table, set those permissions to read only.

For more information about granting the least privilege, see the [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) section of the Best Practices topic in the * IAM User Guide*.

**Topics**
+ [Best practices for credentials](#credentials-best-practices)
+ [Set credentials in Node.js](setting-credentials-node.md)
+ [Set credentials in a web browser](setting-credentials-browser.md)
