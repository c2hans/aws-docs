---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-functions.attribute_type.html
---

# Using the ATTRIBUTE\_TYPE function with PartiQL for DynamoDB
<a name="ql-functions.attribute_type"></a>

Returns `TRUE` if the attribute at the specified path is of a particular data type.

## Syntax
<a name="ql-functions.attribute_type.syntax"></a>

```
attribute_type( {{attributename}}, {{type}} )
```

## Arguments
<a name="ql-functions.attribute_type.arguments"></a>

{{attributename}}
(Required) The attribute name to use.

{{type}}
(Required) The attribute type to check for. For a list of valid values, see DynamoDB [attribute\_type](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.OperatorsAndFunctions.html#Expressions.OperatorsAndFunctions.Functions).

## Return type
<a name="ql-functions.attribute_type.return-type"></a>

`bool`

## Examples
<a name="ql-functions.attribute_type.examples"></a>

```
SELECT * FROM "Music" WHERE attribute_type("Artist", 'S')
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
