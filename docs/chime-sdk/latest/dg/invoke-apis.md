---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/invoke-apis.html
---

# Configuring the AWS SDK to invoke the APIs for the Amazon Chime SDK
<a name="invoke-apis"></a>

This code sample shows you how to pass credentials to the AWS SDK, and set a region and endpoint.

```
    AWS.config.credentials = new AWS.Credentials(accessKeyId, secretAccessKey, null);
    const chime = new AWS.Chime({ region: '{{us-east-1}}' });
    chime.endpoint = new AWS.Endpoint('https://service.chime.aws.amazon.com/console');
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
