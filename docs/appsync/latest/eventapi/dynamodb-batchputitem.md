---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-batchputitem.html
---

# BatchPutItem
<a name="dynamodb-batchputitem"></a>

**Note**
We recommend using the DynamoDB built-in module to generate your request. For more information, see [Amazon DynamoDB built-in module](built-in-modules.md#DDB-built-in-module).

The `BatchPutItem` request enables you to put multiple items, potentially across multiple DynamoDB tables using a `BatchWriteItem` request. The request specifies the following:
+ The names of the tables to put the items in
+ The full list of items to put in each table

The DynamoDB `BatchWriteItem` limits apply and **no condition expression** can be provided.

The `BatchPutItem` request object has the following structure:

```
type DynamoDBBatchPutItemRequest = {
  operation: 'BatchPutItem';
  tables: {
    [tableName: string]: { [key: string]: any}[];
  };
};
```

The TypeScript definition above shows all available fields for the request. While you can construct this request manually, we recommend using the DynamoDB built-in module for generating accurate and efficient requests.

## BatchPutItem fields
<a name="js-BatchPutItem-list"></a>

** `operation` **
The DynamoDB operation to perform. To perform the `BatchPutItem` DynamoDB operation, this must be set to `BatchPutItem`. This value is required.

** `tables` **
The DynamoDB tables to put the items in. Each table entry represents a list of DynamoDB items to insert for this specific table. At least one table must be provided. This value is required.

Things to remember:
+ The fully inserted items are returned in the response, if successful.
+ If an item hasn’t been inserted in the table, a *null* element is displayed in the data block for that table.
+ The inserted items are sorted per table, based on the order in which they were provided inside the request object.
+ Each `Put` command inside a `BatchPutItem` is atomic, however, a batch can be partially processed. If a batch is partially processed due to an error, the unprocessed keys are returned as part of the invocation result inside the *unprocessedKeys* block.
+  `BatchPutItem` is limited to 25 items.
+ This operation **is not** supported when used with conflict detection. Using both at the same time may result in an error.

Response structure (in `ctx.result)`

```
type Response = {
  data: {
    [tableName: string]: {[key: string]: any}[]
  }
  unprocessedItems: {
    [tableName: string]: {[key: string]: any}[]
  }
}
```

The `ctx.error` contains details about the error. The keys **data**, **unprocessedItems**, and each table key that was provided in the request object are guaranteed to be present in the invocation result. Items that have been inserted are in the **data** block. Items that haven’t been processed are marked as *null* inside the data block and are placed inside the **unprocessedItems** block.
