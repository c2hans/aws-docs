---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-functions.size.html
---

# Using the SIZE function with PartiQL for amazon DynamoDB
<a name="ql-functions.size"></a>

Returns a number representing an attribute's size in bytes. The following are valid data types for use with size. For more information, see the DynamoDB [size](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.OperatorsAndFunctions.html#Expressions.OperatorsAndFunctions.Functions) function.

## Syntax
<a name="ql-functions.size.syntax"></a>

```
size( {{path}})
```

## Arguments
<a name="ql-functions.size.arguments"></a>

{{path}}
(Required) The attribute name or document path.
For supported types, see DynamoDB [size](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.OperatorsAndFunctions.html#Expressions.OperatorsAndFunctions.Functions) function.

## Return type
<a name="ql-functions.size.return-type"></a>

`int`

## Examples
<a name="ql-functions.size.examples"></a>

```
 SELECT * FROM "Orders" WHERE "OrderID"=1 AND size("Image") >300
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
