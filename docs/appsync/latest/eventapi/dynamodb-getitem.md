---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-getitem.html
---

# GetItem
<a name="dynamodb-getitem"></a>

**Note**
We recommend using the DynamoDB built-in module to generate your request. For more information, see [Amazon DynamoDB built-in module](built-in-modules.md#DDB-built-in-module).

The `GetItem` request lets you tell the AWS AppSync DynamoDB function to make a `GetItem` request to DynamoDB, and enables you to specify:
+ The key of the item in DynamoDB
+ Whether to use a consistent read or not

The `GetItem` request has the following structure:

```
type DynamoDBGetItem = {
  operation: 'GetItem';
  key: { [key: string]: any };
  consistentRead?: ConsistentRead;
  projection?: {
    expression: string;
    expressionNames?: { [key: string]: string };
  };
};
```

The TypeScript definition above shows all available fields for the request. While you can construct this request manually, using the DynamoDB built-in module is the recommended approach for generating accurate and efficient requests.

## GetItem fields
<a name="js-getitem-list"></a>

 **`operation`**
The DynamoDB operation to perform. To perform the `GetItem` DynamoDB operation, this must be set to `GetItem`. This value is required.

 **`key`**
The key of the item in DynamoDB. DynamoDB items may have a single hash key, or a hash key and sort key, depending on the table structure. For more information about how to specify a “typed value”, see [Type system (request mapping)](dynamodb-typed-values-request.md). This value is required.

 **`consistentRead`**
Whether or not to perform a strongly consistent read with DynamoDB. This is optional, and defaults to `false`.

**`projection`**
A projection that's used to specify the attributes to return from the DynamoDB operation. For more information about projections, see [Projections](dynamodb-projections.md). This field is optional.

For more information about DynamoDB type conversion, see [Type system (response mapping)](dynamodb-typed-values-responses.md).

## Examples
<a name="js-example"></a>

```
export const onPublish = {
  request: (ctx) => ({
    operation : "GetItem",
    key : util.dynamodb.toMapValues({
      channel: ctx.info.channelNamespace.name,
      id: ctx.events[0].payload.id}),
    consistentRead : true
  }),
  response(ctx) {
    return [{
      id: ctx.event[0].id,
      payload: ctx.result
    }]
  }
}
```

The following example demonstrates DynamoDB utils.

```
import * as ddb from '@aws-appsync/utils/dynamodb'
export const onPublish = {
  request: (ctx) => ddb.get({
    key: {
      channel: ctx.info.channelNamespace.name,
      id: ctx.events[0].payload.id
    },
    consistentRead: true
  }),
  response(ctx) {
    return [{
      id: ctx.event[0].id,
      payload: ctx.result
    }]
  }
}
```

For more information about the DynamoDB `GetItem` API, see the [DynamoDB API documentation](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html).
