---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-conditions.html
---

# Condition Clause
<a name="sql-reference-conditions"></a>

Referenced by:
+ SELECT clauses: [HAVING clause](sql-reference-having-clause.md), [WHERE clause](sql-reference-where-clause.md), and [JOIN clause](sql-reference-join-clause.md). (See also the SELECT chart and its [SELECT clause](sql-reference-select-clause.md).)
+ DELETE

A condition is any value expression of type BOOLEAN, such as the following examples:
+ 2<4
+ TRUE
+ FALSE
+ expr\_17 IS NULL
+ NOT expr\_19 IS NULL AND expr\_23 < expr>29
+ expr\_17 IS NULL OR ( NOT expr\_19 IS NULL AND expr\_23 < expr>29 )

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
