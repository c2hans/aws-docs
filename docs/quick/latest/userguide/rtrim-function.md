---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/rtrim-function.html
---

# Rtrim
<a name="rtrim-function"></a>

`rtrim` removes following blank space from a string.

## Syntax
<a name="rtrim-function-syntax"></a>

```
rtrim({{expression}})
```

## Arguments
<a name="rtrim-function-arguments"></a>

 *expression*
The expression must be a string. It can be the name of a field that uses the string data type, a literal value like **'12 Main Street'**, or a call to another function that outputs a string.

## Return type
<a name="rtrim-function-return-type"></a>

String

## Example
<a name="rtrim-function-example"></a>

The following example removes the following spaces from a string.

```
rtrim('Seattle Store #14   ')
```

For these field values, the following values are returned.

```
Seattle Store #14
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
