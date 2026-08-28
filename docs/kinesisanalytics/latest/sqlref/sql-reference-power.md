---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-power.html
---

# POWER
<a name="sql-reference-power"></a>

```
 POWER ( <base>, <exponent> )
 <base> := <number-expression>
 <exponent> := <number-expression>
```

Returns the value of the first argument (the base) raised to the power of the second argument (the exponent). Returns null if either the base or the exponent is null, and raises an exception if the base is zero and the exponent is negative, or if the base is negative and the exponent is not a whole number.

## Examples
<a name="sql-reference-power-examples"></a>

| Function | Result |
| --- | --- |
| POWER(3,2) | 9 |
| POWER(-2,3) | -8 |
| POWER(4,-2) | 1/16 ..or.. 0.0625 |
| POWER(10.1,2.5) | 324.19285157140644 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
