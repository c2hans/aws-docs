---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/replace-function.html
---

# Replace
<a name="replace-function"></a>

`replace` replaces part of a string with another string that you specify.

## Syntax
<a name="replace-function-syntax"></a>

```
replace({{expression}}, {{substring}}, {{replacement}})
```

## Arguments
<a name="replace-function-arguments"></a>

 *expression*
The expression must be a string. It can be the name of a field that uses the string data type, a literal value like **'12 Main Street'**, or a call to another function that outputs a string.

 *substring*
The set of characters in *expression* that you want to replace. The substring can occur one or more times in *expression*.

 *replacement*
The string you want to have substituted for *substring*.

## Return type
<a name="replace-function-return-type"></a>

String

## Example
<a name="replace-function-example"></a>

The following example replaces the substring 'and' with 'or'.

```
replace('1 and 2 and 3', 'and', 'or')
```

The following string is returned.

```
1 or 2 or 3
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
