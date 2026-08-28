---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/COT.html
---

# COT function
<a name="COT"></a>

COT is a trigonometric function that returns the cotangent of a number. The input parameter must be nonzero.

## Syntax
<a name="COT-synopsis"></a>

```
COT(number)
```

## Argument
<a name="COT-argument"></a>

 *number*
The input parameter is a `DOUBLE PRECISION` number.

## Return type
<a name="COT-return-type"></a>

`DOUBLE PRECISION`

## Examples
<a name="COT-examples"></a>

To return the cotangent of 1, use the following example.

```
SELECT COT(1);

+--------------------+
|        cot         |
+--------------------+
| 0.6420926159343306 |
+--------------------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
