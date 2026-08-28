---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/loc-sdk-client.html
---

# Amazon Location client
<a name="loc-sdk-client"></a>

With AWS SDK v3, the SDK is separated out by service. You can install just the parts that you need. For example, to install the Amazon Location client and the credentials provider for Amazon Cognito, use the following commands.

```
npm install @aws-sdk/client-location
npm install @aws-sdk/credential-providers
```

In order to facilitate using Amazon Location Service in JavaScript web frontend applications, AWS provides a hosted bundle of the Amazon Location library and the credentials provider. To use the bundled client, add it to your HTML in a script tag, as follows:

```
<script src="https://unpkg.com/@aws/amazon-location-client@1.x/dist/amazonLocationClient.js"></script>
```

**Note**
The package is kept up to date and backward compatible for ease of use. Using this script tag or NPM install will always get the latest version.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
