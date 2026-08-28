---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/strlen-function.html
---

# Strlen
<a name="strlen-function"></a>

`strlen` returns the number of characters in a string, including spaces.

## Syntax
<a name="strlen-function-syntax"></a>

```
strlen({{expression}})
```

## Arguments
<a name="strlen-function-arguments"></a>

 *expression*
An expression can be the name of a field that uses the string data type like **address1**, a literal value like **'Unknown'**, or another function like `substring(field_name,0,5)`.

## Return type
<a name="strlen-function-return-type"></a>

Integer

## Example
<a name="strlen-function-example"></a>

The following example returns the length of the specified string.

```
strlen('1421 Main Street')
```

The following value is returned.

```
16
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
