---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Boolean_literals-spark.html
---

# Boolean literals
<a name="Boolean_literals-spark"></a>

The following rules are for working with Boolean literals that are supported by AWS Clean Rooms Spark SQL.

Use a Boolean literal to specify a Boolean value, such as `TRUE` or `FALSE`.

## Syntax
<a name="boolean_literals_syntax"></a>

```
TRUE | FALSE
```

## Example
<a name="boolean_literals_example"></a>

The following example shows a column with a specified value of `TRUE` .

```
SELECT TRUE AS col;
+----+
| col|
+----+
|true|
+----+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
