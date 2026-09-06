---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-batchgetitem.html
---

# BatchGetItem
<a name="dynamodb-batchgetitem"></a>

**Note**
We recommend using the DynamoDB built-in module to generate your request. For more information, see [Amazon DynamoDB built-in module](built-in-modules.md#DDB-built-in-module).

The `BatchGetItem` request object enables you to retrieve multiple items, potentially across multiple DynamoDB tables. For this request object, you must specify the following:
+ The names of the table to retrieve the items from
+ The keys of the items to retrieve from each table

The DynamoDB `BatchGetItem` limits apply and **no condition expression** can be provided.

The `BatchGetItem` request object has the following structure:

```
type DynamoDBBatchGetItemRequest = {
  operation: 'BatchGetItem';
  tables: {
    [tableName: string]: {
      keys: { [key: string]: any }[];
      consistentRead?: boolean;
      projection?: {
        expression: string;
        expressionNames?: { [key: string]: string };
      };
    };
  };
};
```

The TypeScript definition above shows all available fields for the request. While you can construct this request manually, we recommend using the DynamoDB built-in module for generating accurate and efficient requests.

## BatchGetItem fields
<a name="js-BatchGetItem-list"></a>

** `operation` **
The DynamoDB operation to perform. To perform the `BatchGetItem` DynamoDB operation, this must be set to `BatchGetItem`. This value is required.

** `tables` **
The DynamoDB tables to retrieve the items from. The value is a map where table names are specified as the keys of the map. At least one table must be provided. This `tables` value is required.
** `keys` **
List of DynamoDB keys representing the primary key of the items to retrieve. DynamoDB items may have a single hash key, or a hash key and sort key, depending on the table structure. For more information about how to specify a “typed value”, see [Type system (request mapping)](dynamodb-typed-values-request.md).
** `consistentRead` **
Whether to use a consistent read when executing a *GetItem* operation. This value is optional and defaults to *false*.
**`projection`**
A projection that's used to specify the attributes to return from the DynamoDB operation. For more information about projections, see [Projections](dynamodb-projections.md). This field is optional.

Things to remember:
+ If an item has not been retrieved from the table, a *null* element appears in the data block for that table.
+ Invocation results are sorted per table, based on the order in which they were provided inside the request object.
+ Each `Get` command inside a `BatchGetItem` is atomic, however, a batch can be partially processed. If a batch is partially processed due to an error, the unprocessed keys are returned as part of the invocation result inside the *unprocessedKeys* block.
+  `BatchGetItem` is limited to 100 keys.

Response structure

```
type Response = {
  data: {
    [tableName: string]: {[key: string]: any}[]
  }
  unprocessedKeys: {
    [tableName: string]: {[key: string]: string}[]
  }
}
```
