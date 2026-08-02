---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-transactgetitems.html
---

# TransactGetItems
<a name="dynamodb-transactgetitems"></a>

**Note**
We recommend using the DynamoDB built-in module to generate your request. For more information, see [Amazon DynamoDB built-in module](built-in-modules.md#DDB-built-in-module).

The `TransactGetItems` request object retrieves multiple items, potentially across multiple DynamoDB tables in a single transaction. The request specifies the following:
+ The names of the tables to retrieve each item from
+ The key of each request item to retrieve from each table

The DynamoDB `TransactGetItems` limits apply and **no condition expression** can be provided.

The `TransactGetItems` request object has the following structure:

```
type DynamoDBTransactGetItemsRequest = {
  operation: 'TransactGetItems';
  transactItems: { table: string; key: { [key: string]: any }; projection?: { expression: string; expressionNames?: { [key: string]: string }; }[];
  };
};
```

The TypeScript definition above shows all available fields for the request. While you can construct this request manually, we recommend using the DynamoDB built-in module for generating accurate and efficient requests.

## TransactGetItems fields
<a name="js-TransactGetItems-list"></a>

** `operation` **
The DynamoDB operation to perform. To perform the `TransactGetItems` DynamoDB operation, this must be set to `TransactGetItems`. This value is required.

** `transactItems` **
The request items to include. The value is an array of request items. At least one request item must be provided. This `transactItems` value is required.
** `table` **
The DynamoDB table to retrieve the item from. The value is a string of the table name. This `table` value is required.
** `key` **
The DynamoDB key representing the primary key of the item to retrieve. DynamoDB items may have a single hash key, or a hash key and sort key, depending on the table structure. For more information about how to specify a “typed value”, see [Type system (request mapping)](dynamodb-typed-values-request.md).
**`projection`**
A projection that's used to specify the attributes to return from the DynamoDB operation. For more information about projections, see [Projections](dynamodb-projections.md). This field is optional.

Things to remember:
+ If a transaction succeeds, the order of retrieved items in the `items` block will be the same as the order of request items.
+ Transactions are performed in an all-or-nothing way. If any request item causes an error, the whole transaction will not be performed and error details will be returned.
+ A request item being unable to be retrieved is not an error. Instead, a *null* element appears in the *items* block in the corresponding position.
+ If the error of a transaction is *TransactionCanceledException*, the `cancellationReasons` block will be populated. The order of cancellation reasons in `cancellationReasons` block will be the same as the order of request items.
+  `TransactGetItems` is limited to 100 request items.

Response structure (in `ctx.result`)

```
type Response = {
  items?: ({[key: string]: any} | null)[];
  cancellationReasons?: {
    type: string;
    message: string;
  }[]
}
```

The `ctx.error` contains details about the error. The keys **items** and **cancellationReasons** are guaranteed to be present in `ctx.result`.
