---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-node-credentials-json-file.html
---

The AWS SDK for JavaScript v2 has reached end-of-support. We recommend that you migrate to [AWS SDK for JavaScript v3](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-javascript-v2/).

# Loading Credentials in Node.js from a JSON File
<a name="loading-node-credentials-json-file"></a>

You can load configuration and credentials from a JSON document on disk using `AWS.config.loadFromPath`. The path specified is relative to the current working directory of your process. For example, to load credentials from a `'config.json'` file with the following content:

```
{ "accessKeyId": {{<YOUR_ACCESS_KEY_ID>}}, "secretAccessKey": {{<YOUR_SECRET_ACCESS_KEY>}}, "region": "us-east-1" }
```

Then use the following code:

```
var AWS = require("aws-sdk");
AWS.config.loadFromPath('./config.json');
```

**Note**
Loading configuration data from a JSON document resets all existing configuration data. Add additional configuration data after using this technique. Loading credentials from a JSON document is not supported in browser scripts.
