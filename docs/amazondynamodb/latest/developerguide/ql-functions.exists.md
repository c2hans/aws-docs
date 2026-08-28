---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-functions.exists.html
---

# Using the EXISTS function with PartiQL for DynamoDB
<a name="ql-functions.exists"></a>

You can use EXISTS to perform the same function as `ConditionCheck` does in the [TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transaction-apis.html#transaction-apis-txwriteitems) API. The EXISTS function can only be used in transactions.

Given a value, returns `TRUE` if the value is a non-empty collection. Otherwise, returns `FALSE`.

**Note**
This function can only be used in transactional operations.

## Syntax
<a name="ql-functions.exists.syntax"></a>

```
EXISTS ( {{statement}} )
```

## Arguments
<a name="ql-functions.exists.arguments"></a>

{{statement}}
(Required) The SELECT statement that the function evaluates.
The SELECT statement must specify a full primary key and one other condition.

## Return type
<a name="ql-functions.exists.return-type"></a>

`bool`

## Examples
<a name="ql-functions.exists.examples"></a>

```
EXISTS(
    SELECT * FROM "Music"
    WHERE "Artist" = 'Acme Band' AND "SongTitle" = 'PartiQL Rocks')
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
