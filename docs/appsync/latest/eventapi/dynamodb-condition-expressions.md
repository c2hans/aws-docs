---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-condition-expressions.html
---

# Condition expressions
<a name="dynamodb-condition-expressions"></a>

When you mutate objects in DynamoDB by using the `PutItem`, `UpdateItem`, and `DeleteItem` DynamoDB operations, you can optionally specify a condition expression that controls whether the request should succeed or not, based on the state of the object already in DynamoDB before the operation is performed.

While you can construct requests manually, we recommend using the DynamoDB built-in module to generate accurate and efficient requests. In the following examples, we use the built-in module to generate requests with conditions.

The AWS AppSync DynamoDB function allows a condition expression to be specified in `PutItem`, `UpdateItem`, and `DeleteItem` request objects, and also a strategy to follow if the condition fails and the object was not updated.

## Example 1
<a name="js-id19"></a>

The following `PutItem` request object doesn’t have a condition expression. As a result, it puts an item in DynamoDB even if an item with the same key already exists, which overwrites the existing item.

```
import { util } from '@aws-appsync/utils';
import * as ddb from '@aws-appsync/utils/dynamodb';

export const onPublish = {
  request(ctx) {
    const {id, payload: item} = ctx.events[0]
    return ddb.put({ key: { id }, item })
  },
  response: (ctx) => ctx.events
}
```

## Example 2
<a name="js-id20"></a>

The following `PutItem` object does have a condition expression that allows the operation to succeed only if an item with the same key does *not* exist in DynamoDB.

```
import { util } from '@aws-appsync/utils';
import * as ddb from '@aws-appsync/utils/dynamodb';

export const onPublish = {
  request(ctx) {
    const {id, payload: item} = ctx.events[0]
    return ddb.put({
      key: { id },
      item,
      condition: {id: {attributeExists: false}}
    })
  },
  response: (ctx) => ctx.events
}
```

For more information about DynamoDB conditions expressions, see the [DynamoDB ConditionExpressions documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html) .

## Specifying a condition
<a name="dynamodb-condition-specification"></a>

The `PutItem`, `UpdateItem`, and `DeleteItem` request objects all allow an optional `condition` section to be specified. If omitted, no condition check is made. If specified, the condition must be true for the operation to succeed.

The built-in module functions create a `condition` object that has the following structure.

```
type ConditionCheckExpression = {
  expression: string;
  expressionNames?: { [key: string]: string};
  expressionValues?: { [key: string]: any};
};
```

The following fields specify the condition:

** `expression` **
The update expression itself. For more information about how to write condition expressions, see the [DynamoDB ConditionExpressions documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html) . This field must be specified.

** `expressionNames` **
The substitutions for expression attribute name placeholders, in the form of key-value pairs. The key corresponds to a name placeholder used in the *expression*, and the value must be a string corresponding to the attribute name of the item in DynamoDB. This field is optional, and should only be populated with substitutions for expression attribute name placeholders used in the *expression*.

** `expressionValues` **
The substitutions for expression attribute value placeholders, in the form of key-value pairs. The key corresponds to a value placeholder used in the expression, and the value must be a typed value. For more information about how to specify a “typed value”, see [Type system (request mapping)](dynamodb-typed-values-request.md). This must be specified. This field is optional, and should only be populated with substitutions for expression attribute value placeholders used in the expression.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
