---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/ltrim-function.html
---

# Ltrim
<a name="ltrim-function"></a>

`ltrim` removes preceding blank space from a string.

## Syntax
<a name="ltrim-function-syntax"></a>

```
ltrim({{expression}})
```

## Arguments
<a name="ltrim-function-arguments"></a>

 *expression*
The expression must be a string. It can be the name of a field that uses the string data type, a literal value like **'12 Main Street'**, or a call to another function that outputs a string.

## Return type
<a name="ltrim-function-return-type"></a>

String

## Example
<a name="ltrim-function-example"></a>

The following example removes the preceding spaces from a string.

```
ltrim('   Seattle Store #14')
```

The following value is returned.

```
Seattle Store #14
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
