---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.insert.html
---

# PartiQL insert statements for DynamoDB
<a name="ql-reference.insert"></a>

Use the `INSERT` statement to add an item to a table in Amazon DynamoDB.

**Note**
You can only insert one item at a time; you cannot issue a single DynamoDB PartiQL statement that inserts multiple items. For information on inserting multiple items, see [Performing transactions with PartiQL for DynamoDB](ql-reference.multiplestatements.transactions.md) or [Running batch operations with PartiQL for DynamoDB](ql-reference.multiplestatements.batching.md).

**Topics**
+ [Syntax](#ql-reference.insert.syntax)
+ [Parameters](#ql-reference.insert.parameters)
+ [Return value](#ql-reference.insert.return)
+ [Examples](#ql-reference.insert.examples)

## Syntax
<a name="ql-reference.insert.syntax"></a>

Insert a single item.

```
INSERT INTO {{table}} VALUE {{item}}
```

## Parameters
<a name="ql-reference.insert.parameters"></a>

**{{table}}**
(Required) The table where you want to insert the data. The table must already exist.

**{{item}}**
(Required) A valid DynamoDB item represented as a [PartiQL tuple](https://partiql.org/docs.html). You must specify only *one* item and each attribute name in the item is case-sensitive and can be denoted with *single* quotation marks (`'...'`) in PartiQL.
String values are also denoted with *single* quotation marks (`'...'`) in PartiQL.

## Return value
<a name="ql-reference.insert.return"></a>

This statement does not return any values.

**Note**
If the DynamoDB table already has an item with the same primary key as the primary key of the item being inserted, `DuplicateItemException` is returned.

## Examples
<a name="ql-reference.insert.examples"></a>

```
INSERT INTO "Music" value {'Artist' : 'Acme Band','SongTitle' : 'PartiQL Rocks'}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
