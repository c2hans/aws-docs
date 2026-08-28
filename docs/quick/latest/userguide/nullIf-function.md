---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/nullIf-function.html
---

# nullIf
<a name="nullIf-function"></a>

`nullIf` compares two expressions. If they are equal, the function returns null. If they are not equal, the function returns the first expression.

## Syntax
<a name="nullIf-function-syntax"></a>

```
nullIf({{expression1}}, {{expression2}})
```

## Arguments
<a name="nullIf-function-arguments"></a>

`nullIf` takes two expressions as arguments.

 *expression*
The expression can be numeric, datetime, or string. It can be a field name, a literal value, or another function.

## Return type
<a name="nullIf-function-return-type"></a>

String

## Example
<a name="nullIf-function-example"></a>

The following example returns nulls if the reason for a shipment delay is unknown.

```
nullIf(delayReason, 'unknown')
```

The following are the given field values.

```
delayReason
============
unknown
back ordered
weather delay
```

For these field values, the following values are returned.

```
(null)
back ordered
weather delay
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
