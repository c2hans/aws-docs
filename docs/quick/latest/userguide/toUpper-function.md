---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/toUpper-function.html
---

# toUpper
<a name="toUpper-function"></a>

`toUpper` formats a string in all uppercase. `toUpper` skips rows containing null values.

## Syntax
<a name="toUpper-function-syntax"></a>

```
toUpper({{expression}})
```

## Arguments
<a name="toUpper-function-arguments"></a>

 *expression*
The expression must be a string. It can be the name of a field that uses the string data type, a literal value like **'12 Main Street'**, or a call to another function that outputs a string.

## Return type
<a name="toUpper-function-return-type"></a>

String

## Example
<a name="toUpper-function-example"></a>

The following example converts a string value into uppercase.

```
toUpper('Seattle Store #14')
```

The following value is returned.

```
SEATTLE STORE #14
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
