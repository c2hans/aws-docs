---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-querying.html
---

# Use prepared statements
<a name="querying-with-prepared-statements-querying"></a>

You can use a prepared statement for repeated execution of the same query with different query parameters. A prepared statement contains parameter placeholders whose values are supplied at execution time.

**Note**
The maximum number of prepared statements in a workgroup is 1000.

**Topics**
+ [SQL syntax](querying-with-prepared-statements-sql-statements.md)
+ [Use the Athena console](querying-with-prepared-statements-executing-prepared-statements-without-the-using-clause-athena-console.md)
+ [Use the AWS CLI](querying-with-prepared-statements-cli-section.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
