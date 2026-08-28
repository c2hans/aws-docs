---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-functions.beginswith.html
---

# Using the BEGINS\_WITH function with PartiQL for DynamoDB
<a name="ql-functions.beginswith"></a>

Returns `TRUE` if the attribute specified begins with a particular substring.

## Syntax
<a name="ql-functions.beginswith.syntax"></a>

```
begins_with({{path}}, {{value}} )
```

## Arguments
<a name="ql-functions.beginswith.arguments"></a>

{{path}}
(Required) The attribute name or document path to use.

{{value}}
(Required) The string to search for.

## Return type
<a name="ql-functions.beginswith.return-type"></a>

`bool`

## Examples
<a name="ql-functions.beginswith.examples"></a>

```
SELECT * FROM "Orders" WHERE "OrderID"=1 AND begins_with("Address", '7834 24th')
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
