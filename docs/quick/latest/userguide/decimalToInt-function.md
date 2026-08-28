---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/decimalToInt-function.html
---

# decimalToInt
<a name="decimalToInt-function"></a>

`decimalToInt` converts a decimal value to the integer data type by stripping off the decimal point and any numbers after it. `decimalToInt` does not round up. For example, `decimalToInt(29.99)` returns `29`.

## Syntax
<a name="decimalToInt-function-syntax"></a>

```
decimalToInt({{decimal}})
```

## Arguments
<a name="decimalToInt-function-arguments"></a>

 *decimal*
A field that uses the decimal data type, a literal value like **17.62**, or a call to another function that outputs a decimal.

## Return type
<a name="decimalToInt-function-return-type"></a>

Integer

## Example
<a name="decimalToInt-function-example"></a>

The following example converts a decimal field to an integer.

```
decimalToInt(salesAmount)
```

The following are the given field values.

```
 20.13
892.03
 57.54
```

For these field values, the following values are returned.

```
 20
892
 57
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
