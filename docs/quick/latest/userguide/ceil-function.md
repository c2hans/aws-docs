---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/ceil-function.html
---

# Ceil
<a name="ceil-function"></a>

`ceil` rounds a decimal value to the next highest integer. For example, `ceil(29.02)` returns `30`.

## Syntax
<a name="ceil-function-syntax"></a>

```
ceil({{decimal}})
```

## Arguments
<a name="ceil-function-arguments"></a>

 *decimal*
A field that uses the decimal data type, a literal value like **17.62**, or a call to another function that outputs a decimal.

## Return type
<a name="ceil-function-return-type"></a>

Integer

## Example
<a name="ceil-function-example"></a>

The following example rounds a decimal field to the next highest integer.

```
ceil(salesAmount)
```

The following are the given field values.

```
20.13
892.03
57.54
```

For these field values, the following values are returned.

```
21
893
58
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
