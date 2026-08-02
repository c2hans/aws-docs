---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrate-dynamodb-doc-client.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# DynamoDB document client
<a name="migrate-dynamodb-doc-client"></a>

## Basic usage of DynamoDB document client in v3
<a name="basic-usage-of-dynamodb-document-client-in-v3"></a>
+  In v2, you can use the [https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB/DocumentClient.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB/DocumentClient.html) class to call DynamoDB APIs with native JavaScript types like Array, Number, and Object. It thus simplifies working with items in Amazon DynamoDB by abstracting away the notion of attribute values.
+  In v3, the equivalent [https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_lib_dynamodb.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/modules/_aws_sdk_lib_dynamodb.html) client is available. It's similar to normal service clients from v3 SDK, with the difference that it takes a basic DynamoDB client in its constructor.

 Example:

```
import { DynamoDBClient } from "@aws-sdk/client-dynamodb"; // ES6 import
// const { DynamoDBClient } = require("@aws-sdk/client-dynamodb"); // CommonJS import
import { DynamoDBDocumentClient, PutCommand } from "@aws-sdk/lib-dynamodb"; // ES6 import
// const { DynamoDBDocumentClient, PutCommand } = require("@aws-sdk/lib-dynamodb"); // CommonJS import

// Bare-bones DynamoDB Client
const client = new DynamoDBClient({});

// Bare-bones document client
const ddbDocClient = DynamoDBDocumentClient.from(client); // client is DynamoDB client

await ddbDocClient.send(
  new PutCommand({
    TableName,
    Item: {
      id: "1",
      content: "content from DynamoDBDocumentClient",
    },
  })
);
```

## `Undefined` values in when marshalling
<a name="undefined-values-in-when-marshalling"></a>
+  In v2, `undefined` values in objects were automatically omitted during the marshalling process to DynamoDB.
+  In v3, the default marshalling behavior in `@aws-sdk/lib-dynamodb` has changed: objects with `undefined` values are no longer omitted. To align with v2's functionality, developers must explicitly set the `removeUndefinedValues` to `true` in the `marshallOptions` of the DynamoDB Document Client.

 Example:

```
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, PutCommand } from "@aws-sdk/lib-dynamodb";

const client = new DynamoDBClient({});

// The DynamoDBDocumentClient is configured to handle undefined values properly
const ddbDocClient = DynamoDBDocumentClient.from(client, {
  marshallOptions: {
    removeUndefinedValues: true
  }
});

await ddbDocClient.send(
  new PutCommand({
    TableName,
    Item: {
      id: "123",
      content: undefined // This value will be automatically omitted.
      array: [1, undefined], // The undefined value will be automatically omitted.
      map: { key: undefined }, // The "key" will be automatically omitted.
      set: new Set([1, undefined]), // The undefined value will be automatically omitted.
    };
  })
);
```

 More examples and configurations are available in the [package README](https://github.com/aws/aws-sdk-js-v3/blob/main/lib/lib-dynamodb/README.md).
