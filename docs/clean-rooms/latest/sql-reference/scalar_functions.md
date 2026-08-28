---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/scalar_functions.html
---

# Scalar functions
<a name="scalar_functions"></a>

This section describes the scalar functions supported in AWS Clean Rooms Spark SQL. A scalar function is a function that takes one or more values as input and returns a single value as output. Scalar functions operate on individual rows or elements and produce a single result for each input.

Scalar functions, such as SIZE, are different from other types of SQL functions, such as aggregate functions (count, sum, avg) and table-generating functions (explode, flatten). These other function types operate on multiple rows or generate multiple rows, whereas scalar functions work on individual rows or elements.

**Topics**
+ [SIZE function](size.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
