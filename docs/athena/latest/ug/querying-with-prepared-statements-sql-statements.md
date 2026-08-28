---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-sql-statements.html
---

# SQL syntax for prepared statements
<a name="querying-with-prepared-statements-sql-statements"></a>

You can use the `PREPARE`, `EXECUTE` and `DEALLOCATE PREPARE` SQL statements to run parameterized queries in the Athena console query editor.

+ To specify parameters where you would normally use literal values, use question marks in the `PREPARE` statement.
+ To replace the parameters with values when you run the query, use the `USING` clause in the `EXECUTE` statement.
+ To remove a prepared statement from the prepared statements in a workgroup, use the `DEALLOCATE PREPARE` statement.

The following sections provide additional detail about each of these statements.

**Topics**
+ [PREPARE](querying-with-prepared-statements-prepare.md)
+ [EXECUTE](querying-with-prepared-statements-execute.md)
+ [DEALLOCATE PREPARE](querying-with-prepared-statements-deallocate-prepare.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
