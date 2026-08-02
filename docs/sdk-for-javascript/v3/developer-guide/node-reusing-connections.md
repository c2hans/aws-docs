---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/node-reusing-connections.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Reuse connections with keep-alive in Node.js
<a name="node-reusing-connections"></a>

The default Node.js HTTP/HTTPS agent creates a new TCP connection for every new request. To avoid the cost of establishing a new connection, the AWS SDK for JavaScript reuses TCP connections *by default*.

For short-lived operations, such as Amazon DynamoDB queries, the latency overhead of setting up a TCP connection might be greater than the operation itself. Additionally, since DynamoDB [encryption at rest](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/encryption.howitworks.html) is integrated with [AWS KMS](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/encryption.howitworks.html), you may experience latencies from the database having to re-establish new AWS KMS cache entries for each operation.

If you do not want to reuse TCP connections, you can disable reusing these connections alive with `keepAlive` on a per-service client basis as shown in the following example for a DynamoDB client.

```
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { NodeHttpHandler } from "@smithy/node-http-handler";
import { Agent } from "https";

const dynamodbClient = new DynamoDBClient({
    requestHandler: new NodeHttpHandler({
        httpsAgent: new Agent({ keepAlive: false })
    })
});
```

If `keepAlive` is enabled, you can also set the initial delay for TCP Keep-Alive packets with `keepAliveMsecs`, which by default is 1000 ms. See the [Node.js documentation](https://nodejs.org/api/http.html#new-agentoptions) for details.
