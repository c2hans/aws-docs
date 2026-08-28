---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/TO_NUMBER.html
---

# TO\_NUMBER
<a name="TO_NUMBER"></a>

TO\_NUMBER converts a string to a numeric (decimal) value.

## Syntax
<a name="TO_NUMBER-synopsis"></a>

```
to_number(string, format)
```

## Arguments
<a name="TO_NUMBER-arguments"></a>

 *string*
String to be converted. The format must be a literal value.

 *format*
The second argument is a format string that indicates how the character string should be parsed to create the numeric value. For example, the format `'99D999'` specifies that the string to be converted consists of five digits with the decimal point in the third position. For example, `to_number('12.345','99D999')` returns `12.345` as a numeric value. For a list of valid formats, see [Numeric format strings](Numeric_formating.md).

## Return type
<a name="TO_NUMBER-return-type"></a>

TO\_NUMBER returns a DECIMAL number.

If the conversion to *format* fails, then an error is returned.

## Examples
<a name="TO_NUMBER-examples"></a>

The following example converts the string `12,454.8-` to a number:

```
select to_number('12,454.8-', '99G999D9S');

to_number
-----------
-12454.8
```

The following example converts the string `$ 12,454.88` to a number:

```
select to_number('$ 12,454.88', 'L 99G999D99');

to_number
-----------
12454.88
```

The following example converts the string `$ 2,012,454.88` to a number:

```
select to_number('$ 2,012,454.88', 'L 9,999,999.99');

to_number
-----------
2012454.88
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
