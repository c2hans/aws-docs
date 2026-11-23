---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/invoke-apis.html
---

# Configuring the AWS SDK to invoke the APIs for the Amazon Chime SDK

This code sample shows you how to pass credentials to the AWS SDK, and set a region and endpoint.

```javascript
    AWS.config.credentials = new AWS.Credentials(accessKeyId, secretAccessKey, null);
    const chime = new AWS.Chime({ region: '{{us-east-1}}' });
    chime.endpoint = new AWS.Endpoint('https://service.chime.aws.amazon.com/console');
```
