---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-updateitem.html
---

# UpdateItem
<a name="dynamodb-updateitem"></a>

**Note**
We recommend using the DynamoDB built-in module to generate your request. For more information, see [Amazon DynamoDB built-in module](built-in-modules.md#DDB-built-in-module).

The `UpdateItem` request enables you to modify existing items in DynamoDB through AWS AppSync. The request specifies the following:
+ Item Key: The unique identifier for the DynamoDB item to update
+ Item Expression: Describes how to modify the item in DynamoDB
+ Operation Conditions (optional): Rules that must be met for the update to proceed

The `UpdateItem` request has the following structure:

```
type DynamoDBUpdateItemRequest = {
  operation: 'UpdateItem';
  key: { [key: string]: any };
  update: {
    expression: string;
    expressionNames?: { [key: string]: string };
    expressionValues?: { [key: string]: any };
  };
  condition?: ConditionCheckExpression;
  customPartitionKey?: string;
  populateIndexFields?: boolean;
  _version?: number;
};
```

The TypeScript definition above shows all available fields for the request. While you can construct this request manually, we recommend using the DynamoDB built-in module for generating accurate and efficient requests.

## UpdateItem fields
<a name="js-updateitem-list"></a>

 **`operation`**
The DynamoDB operation to perform. To perform the `UpdateItem` DynamoDB operation, this must be set to `UpdateItem`. This value is required.

 **`key`**
The key of the item in DynamoDB. DynamoDB items may have a single hash key, or a hash key and sort key, depending on the table structure. For more information about specifying a “typed value”, see [Type system (request mapping)](dynamodb-typed-values-request.md). This value is required.

 **`update`**
The `update` section lets you specify an update expression that describes how to update the item in DynamoDB. For more information about how to write update expressions, see the [DynamoDB UpdateExpressions documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.UpdateExpressions.html). This section is required.
The `update` section has three components:
** `expression` **
The update expression. This value is required.
** `expressionNames` **
The substitutions for expression attribute *name* placeholders, in the form of key-value pairs. The key corresponds to a name placeholder used in the `expression`, and the value must be a string corresponding to the attribute name of the item in DynamoDB. This field is optional, and should only be populated with substitutions for expression attribute name placeholders used in the `expression`.
** `expressionValues` **
The substitutions for expression attribute *value* placeholders, in the form of key-value pairs. The key corresponds to a value placeholder used in the `expression`, and the value must be a typed value. For more information about how to specify a “typed value”, see [Type system (request mapping)](dynamodb-typed-values-request.md). This must be specified. This field is optional, and should only be populated with substitutions for expression attribute value placeholders used in the `expression`.

 **`condition`**
A condition to determine if the request should succeed or not, based on the state of the object already in DynamoDB. If no condition is specified, the `UpdateItem` request updates the existing entry regardless of its current state. For more information about conditions, see [Condition expressions](dynamodb-condition-expressions.md). This value is optional.

 **`_version`**
A numeric value that represents the latest known version of an item. This value is optional. This field is used for *Conflict Detection* and is only supported on versioned data sources.
*Not supported in AWS AppSync Events*

**`customPartitionKey`**
When enabled, this string value modifies the format of the `ds_sk` and `ds_pk` records used by the delta sync table when versioning has been enabled (for more information, see [Conflict detection and sync](https://docs.aws.amazon.com/appsync/latest/devguide/conflict-detection-and-sync.html) in the *AWS AppSync Developer Guide*). When enabled, the processing of the `populateIndexFields` entry is also enabled. This field is optional.
*Not supported in AWS AppSync Events*

**`populateIndexFields`**
A boolean value that, when enabled **along with the `customPartitionKey`**, creates new entries for each record in the delta sync table, specifically in the `gsi_ds_pk` and `gsi_ds_sk` columns. For more information, see [Conflict detection and sync](https://docs.aws.amazon.com/appsync/latest/devguide/conflict-detection-and-sync.html) in the *AWS AppSync Developer Guide*. This field is optional.
*Not supported in AWS AppSync Events*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
