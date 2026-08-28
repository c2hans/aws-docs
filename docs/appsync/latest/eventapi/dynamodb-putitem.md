---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-putitem.html
---

# PutItem
<a name="dynamodb-putitem"></a>

**Note**
We recommend using the DynamoDB built-in module to generate your request. For more information, see [Amazon DynamoDB built-in module](built-in-modules.md#DDB-built-in-module).

The `PutItem` request enables you to create or replace items in DynamoDB through AWS AppSync. The request specifies the following:
+ Item Key: The unique identifier for the DynamoDB item
+ Item Contents: The complete item data, including both the `key` and `attributeValues`
+ Operation Conditions (optional): Rules that must be met for the operation to proceed

The `PutItem` request has the following structure:

```
type DynamoDBPutItemRequest = {
  operation: 'PutItem';
  key: { [key: string]: any };
  attributeValues: { [key: string]: any};
  condition?: ConditionCheckExpression;
  customPartitionKey?: string;
  populateIndexFields?: boolean;
  _version?: number;
};
```

The TypeScript definition above shows all available fields for the request. While you can construct this request manually, we recommend using the DynamoDB built-in module for generating accurate and efficient requests.

## PutItem fields
<a name="js-putitem-list"></a>

 **`operation`**
The DynamoDB operation to perform. To perform the `PutItem` DynamoDB operation, this must be set to `PutItem`. This value is required.

 **`key`**
The key of the item in DynamoDB. DynamoDB items may have a single hash key, or a hash key and sort key, depending on the table structure. For more information about how to specify a “typed value”, see [Type system (request mapping)](dynamodb-typed-values-request.md). This value is required.

 **`attributeValues`**
The rest of the attributes of the item to be put into DynamoDB. For more information about how to specify a “typed value”, see [Type system (request mapping)](dynamodb-typed-values-request.md). This field is optional.

 **`condition`**
A condition to determine if the request should succeed or not, based on the state of the object already in DynamoDB. If no condition is specified, the `PutItem` request overwrites any existing entry for that item. For more information about conditions, see [Condition expressions](dynamodb-condition-expressions.md). This value is optional.

 **`_version`**
A numeric value that represents the latest known version of an item. This value is optional. This field is used for *Conflict Detection* and is only supported on versioned data sources.

**`customPartitionKey`**
When enabled, this string value modifies the format of the `ds_sk` and `ds_pk` records used by the delta sync table when versioning has been enabled (for more information, see [Conflict detection and sync](https://docs.aws.amazon.com/appsync/latest/devguide/conflict-detection-and-sync.html) in the *AWS AppSync Developer Guide*). When enabled, the processing of the `populateIndexFields` entry is also enabled. This field is optional.
*Not supported in AWS AppSync Events*

**`populateIndexFields`**
A boolean value that, when enabled **along with the `customPartitionKey`**, creates new entries for each record in the delta sync table, specifically in the `gsi_ds_pk` and `gsi_ds_sk` columns. For more information, see [Conflict detection and sync](https://docs.aws.amazon.com/appsync/latest/devguide/conflict-detection-and-sync.html) in the *AWS AppSync Developer Guide*. This field is optional.
The item written to DynamoDB is automatically converted to JSON primitive types and is available in the context result (`context.result`).

For more information about DynamoDB type conversion, see [Type system (response mapping)](dynamodb-typed-values-responses.md).

For more information about the DynamoDB `PutItem` API, see the [DynamoDB API documentation](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
