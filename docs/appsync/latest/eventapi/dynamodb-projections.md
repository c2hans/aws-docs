---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-projections.html
---

# Projections
<a name="dynamodb-projections"></a>

When reading objects in DynamoDB using the `GetItem`, `Scan`, `Query`, `BatchGetItem`, and `TransactGetItems` operations, you can optionally specify a projection that identifies the attributes that you want. The projection property has the following structure, which is similar to filters:

```
type DynamoDBExpression = {
  expression: string;
  expressionNames?: { [key: string]: string}
};
```

The fields are defined as follows:

** `expression` **
The projection expression, which is a string. To retrieve a single attribute, specify its name. For multiple attributes, the names must be comma-separated values. For more information on writing projection expressions, see the [DynamoDB projection expressions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ProjectionExpressions.html) documentation. This field is required.

** `expressionNames` **
The substitutions for expression attribute *name* placeholders in the form of key-value pairs. The key corresponds to a name placeholder used in the `expression`. The value must be a string that corresponds to the attribute name of the item in DynamoDB. This field is optional and should only be populated with substitutions for expression attribute name placeholders used in the `expression`. For more information about `expressionNames`, see the [DynamoDB documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ExpressionAttributeNames.html).

## Example 1
<a name="js-id24"></a>

The following example is a projection section for a JavaScript function in which only the attributes `author` and `id` are returned from DynamoDB.

```
projection : {
    expression : "#author, id",
    expressionNames : {
        "#author" : "author"
    }
}
```

## Example 2
<a name="js-id25"></a>

The following example demonstrates that when you use the built-in DynamoDB module, you can simply pass an array for your projection.

```
export const onPublish = {
  request(ctx) {
    return ddb.batchGet({
      tables: {
        users: {
          keys: ctx.events.map(e => ({id: e.payload.id})),
          projection: ['id', 'name', 'email', 'nested.field']
        }
      }
    })
  },
  response: (ctx) => ctx.events
}
```
