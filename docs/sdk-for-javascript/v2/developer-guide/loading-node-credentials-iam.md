---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-node-credentials-iam.html
---

The AWS SDK for JavaScript v2 has reached end-of-support. We recommend that you migrate to [AWS SDK for JavaScript v3](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-javascript-v2/).

# Loading Credentials in Node.js from IAM roles for Amazon EC2
<a name="loading-node-credentials-iam"></a>

If you run your Node.js application on an Amazon EC2 instance, you can leverage IAM roles for Amazon EC2 to automatically provide credentials to the instance. If you configure your instance to use IAM roles, the SDK automatically selects the IAM credentials for your application, eliminating the need to manually provide credentials.

For more information on adding IAM roles to an Amazon EC2 instance, see [Using IAM roles for Amazon EC2 instances](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-roles-for-ec2.html) in the *AWS SDKs and Tools Reference Guide*.
