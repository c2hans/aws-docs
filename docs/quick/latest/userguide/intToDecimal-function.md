---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/intToDecimal-function.html
---

# intToDecimal
<a name="intToDecimal-function"></a>

`intToDecimal` converts an integer value to the decimal data type.

## Syntax
<a name="intToDecimal-function-syntax"></a>

```
intToDecimal({{integer}})
```

## Arguments
<a name="intToDecimal-function-arguments"></a>

 *int*
A field that uses the integer data type, a literal value like **14**, or a call to another function that outputs an integer.

## Return type
<a name="intToDecimal-function-return-type"></a>

Decimal(Fixed) in the legacy data preparation experience.

Decimal(Float) in the new data preparation experience.

## Example
<a name="intToDecimal-function-example"></a>

The following example converts an integer field to a decimal.

```
intToDecimal(price)
```

The following are the given field values.

```
20
892
57
```

For these field values, the following values are returned.

```
20.0
892.0
58.0
```

You can apply formatting inside an analysis, for example to format `price` as currency.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
