---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/PI.html
---

# PI function
<a name="PI"></a>

The PI function returns the value of pi to 14 decimal places.

## Syntax
<a name="PI-synopsis"></a>

```
PI()
```

## Return type
<a name="PI-return-type"></a>

`DOUBLE PRECISION`

## Examples
<a name="PI-examples"></a>

To return the value of pi, use the following example.

```
SELECT PI();

+-------------------+
|        pi         |
+-------------------+
| 3.141592653589793 |
+-------------------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
