---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-transaction-condition-expressions.html
---

# Transaction condition expressions
<a name="dynamodb-transaction-condition-expressions"></a>

Transaction condition expressions are available in requests of all four types of operations in `TransactWriteItems`, namely, `PutItem`, `DeleteItem`, `UpdateItem`, and `ConditionCheck`.

For `PutItem`, `DeleteItem`, and `UpdateItem`, the transaction condition expression is optional. For `ConditionCheck`, the transaction condition expression is required.

## Example 1
<a name="js-id22"></a>

The following transactional `DeleteItem` function request handler does not have a condition expression. As a result, it deletes the item in DynamoDB.

```
export const onPublish = {
  request(ctx) {
    const table = "events"
    return ddb.transactWrite({
      items: ctx.events.map(({ payload }) => ({
        deleteItem: { table, key: { id: payload.id } }
      }))
    })
  },
  response: (ctx) => ctx.events
}
```

## Example 2
<a name="js-id23"></a>

The following transactional `DeleteItem` function request handler does have a transaction condition expression that allows the operation succeed only if the author of that post equals a certain name.

```
export const onPublish = {
  request(ctx) {
    return ddb.remove({
      items: ctx.events.map(({ payload }) => ({
        deleteItem: {
          table: 'events',
          key: { id: payload.id },
          condition: { owner: { eq: payload.owner } }
        }
      }))
    })
  },
  response: (ctx) => ctx.events
}
```

If the condition check fails, it will cause `TransactionCanceledException` and the error detail will be returned in `ctx.result.cancellationReasons`.
