---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-functions.missing.html
---

# Using the MISSING function with PartiQL for DynamoDB
<a name="ql-functions.missing"></a>

Returns `TRUE` if the item does not contain the attribute specified. Only equality and inequality operators can be used with this function.

## Syntax
<a name="ql-functions.missing.syntax"></a>

```
 {{attributename}} IS | IS NOT  MISSING
```

## Arguments
<a name="ql-functions.missing.arguments"></a>

{{attributename}}
(Required) The attribute name to look for.

## Return type
<a name="ql-functions.missing.return-type"></a>

`bool`

## Examples
<a name="ql-functions.missing.examples"></a>

```
SELECT * FROM Music WHERE "Awards" is MISSING
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
