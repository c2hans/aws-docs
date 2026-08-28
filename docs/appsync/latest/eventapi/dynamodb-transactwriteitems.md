---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-transactwriteitems.html
---

# TransactWriteItems
<a name="dynamodb-transactwriteitems"></a>

**Note**
We recommend using the DynamoDB built-in module to generate your request. For more information, see [Amazon DynamoDB built-in module](built-in-modules.md#DDB-built-in-module).

The `TransactWriteItems` request writes multiple items, potentially to multiple DynamoDB tables. The request specifies the following:
+ The destination table name of each request item
+ The operation to perform for each request item. There are four types of operations that are supported: *PutItem*, *UpdateItem*, *DeleteItem*, and *ConditionCheck*
+ The key of each request item to write

The DynamoDB `TransactWriteItems` limits apply.

The `TransactWriteItems` request object has the following structure:

```
type DynamoDBTransactWriteItemsRequest = {
  operation: 'TransactWriteItems';
  transactItems: TransactItem[];
};
type TransactItem =
  | TransactWritePutItem
  | TransactWriteUpdateItem
  | TransactWriteDeleteItem
  | TransactWriteConditionCheckItem;
type TransactWritePutItem = {
  table: string;
  operation: 'PutItem';
  key: { [key: string]: any };
  attributeValues: { [key: string]: string};
  condition?: TransactConditionCheckExpression;
};
type TransactWriteUpdateItem = {
  table: string;
  operation: 'UpdateItem';
  key: { [key: string]: any };
  update: DynamoDBExpression;
  condition?: TransactConditionCheckExpression;
};
type TransactWriteDeleteItem = {
  table: string;
  operation: 'DeleteItem';
  key: { [key: string]: any };
  condition?: TransactConditionCheckExpression;
};
type TransactWriteConditionCheckItem = {
  table: string;
  operation: 'ConditionCheck';
  key: { [key: string]: any };
  condition?: TransactConditionCheckExpression;
};
type TransactConditionCheckExpression = {
  expression: string;
  expressionNames?: { [key: string]: string};
  expressionValues?: { [key: string]: any};
  returnValuesOnConditionCheckFailure: boolean;
};
```

The TypeScript definition above shows all available fields for the request. While you can construct this request manually, we recommend using the DynamoDB built-in module for generating accurate and efficient requests.

## TransactWriteItems fields
<a name="js-TransactWriteItems-list"></a>

**The fields are defined as follows: **
** `operation` **
The DynamoDB operation to perform. To perform the `TransactWriteItems` DynamoDB operation, this must be set to `TransactWriteItems`. This value is required.
** `transactItems` **
The request items to include. The value is an array of request items. At least one request item must be provided. This `transactItems` value is required.
For `PutItem`, the fields are defined as follows:
** `table` **
The destination DynamoDB table. The value is a string of the table name. This `table` value is required.
** `operation` **
The DynamoDB operation to perform. To perform the `PutItem` DynamoDB operation, this must be set to `PutItem`. This value is required.
** `key` **
The DynamoDB key representing the primary key of the item to put. DynamoDB items may have a single hash key, or a hash key and sort key, depending on the table structure. For more information about how to specify a “typed value”, see [Type system (request mapping)](dynamodb-typed-values-request.md). This value is required.
** `attributeValues` **
The rest of the attributes of the item to be put into DynamoDB. For more information about how to specify a “typed value”, see [Type system (request mapping)](dynamodb-typed-values-request.md). This field is optional.
** `condition` **
A condition to determine if the request should succeed or not, based on the state of the object already in DynamoDB. If no condition is specified, the `PutItem` request overwrites any existing entry for that item. You can specify whether to retrieve the existing item back when condition check fails. For more information about transactional conditions, see [Transaction condition expressions](dynamodb-transaction-condition-expressions.md). This value is optional.
For `UpdateItem`, the fields are defined as follows:
** `table` **
The DynamoDB table to update. The value is a string of the table name. This `table` value is required.
** `operation` **
The DynamoDB operation to perform. To perform the `UpdateItem` DynamoDB operation, this must be set to `UpdateItem`. This value is required.
** `key` **
The DynamoDB key representing the primary key of the item to update. DynamoDB items may have a single hash key, or a hash key and sort key, depending on the table structure. For more information about how to specify a “typed value”, see [Type system (request mapping)](dynamodb-typed-values-request.md). This value is required.
** `update` **
The `update` section lets you specify an update expression that describes how to update the item in DynamoDB. For more information about how to write update expressions, see the [DynamoDB UpdateExpressions documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.UpdateExpressions.html). This section is required.
** `condition` **
A condition to determine if the request should succeed or not, based on the state of the object already in DynamoDB. If no condition is specified, the `UpdateItem` request updates the existing entry regardless of its current state. You can specify whether to retrieve the existing item back when condition check fails. For more information about transactional conditions, see [Transaction condition expressions](dynamodb-transaction-condition-expressions.md). This value is optional.
For `DeleteItem`, the fields are defined as follows:
** `table` **
The DynamoDB table in which to delete the item. The value is a string of the table name. This `table` value is required.
** `operation` **
The DynamoDB operation to perform. To perform the `DeleteItem` DynamoDB operation, this must be set to `DeleteItem`. This value is required.
** `key` **
The DynamoDB key representing the primary key of the item to delete. DynamoDB items may have a single hash key, or a hash key and sort key, depending on the table structure. For more information about how to specify a “typed value”, see [Type system (request mapping)](dynamodb-typed-values-request.md). This value is required.
** `condition` **
A condition to determine if the request should succeed or not, based on the state of the object already in DynamoDB. If no condition is specified, the `DeleteItem` request deletes an item regardless of its current state. You can specify whether to retrieve the existing item back when condition check fails. For more information about transactional conditions, see [Transaction condition expressions](dynamodb-transaction-condition-expressions.md). This value is optional.
For `ConditionCheck`, the fields are defined as follows:
** `table` **
The DynamoDB table in which to check the condition. The value is a string of the table name. This `table` value is required.
** `operation` **
The DynamoDB operation to perform. To perform the `ConditionCheck` DynamoDB operation, this must be set to `ConditionCheck`. This value is required.
** `key` **
The DynamoDB key representing the primary key of the item to condition check. DynamoDB items may have a single hash key, or a hash key and sort key, depending on the table structure. For more information about how to specify a “typed value”, see [Type system (request mapping)](dynamodb-typed-values-request.md). This value is required.
** `condition` **
A condition to determine if the request should succeed or not, based on the state of the object already in DynamoDB. You can specify whether to retrieve the existing item back when condition check fails. For more information about transactional conditions, see [Transaction condition expressions](dynamodb-transaction-condition-expressions.md). This value is required.

Things to remember:
+ Only keys of request items are returned in the response, if successful. The order of keys will be the same as the order of request items.
+ Transactions are performed in an all-or-nothing way. If any request item causes an error, the whole transaction will not be performed and error details will be returned.
+ No two request items can target the same item. Otherwise they will cause *TransactionCanceledException* error.
+ If the error of a transaction is *TransactionCanceledException*, the `cancellationReasons` block will be populated. If a request item’s condition check fails **and** you did not specify `returnValuesOnConditionCheckFailure` to be `false`, the item existing in the table will be retrieved and stored in `item` at the corresponding position of `cancellationReasons` block.
+  `TransactWriteItems` is limited to 100 request items.
+ This operation **is not** supported when used with conflict detection. Using both at the same time may result in an error.

Response structure (in `ctx.result`)

```
type Responser = {
  keys?: {[key: string]: string}[];
  cancellationReasons?: {
    item?: { [key: string]: any };
    type: string;
    message;
  }
}
```

The `ctx.error` contains details about the error. The keys **keys** and **cancellationReasons** are guaranteed to be present in `ctx.result`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
