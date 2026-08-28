---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-querying-using-execution-parameters.html
---

# Use execution parameters
<a name="querying-with-prepared-statements-querying-using-execution-parameters"></a>

You can use question mark placeholders in any DML query to create a parameterized query without creating a prepared statement first. To run these queries, you can use the Athena console, or use the AWS CLI or the AWS SDK and declare the variables in the `execution-parameters` argument.

**Topics**
+ [Use the Athena console](querying-with-prepared-statements-running-queries-with-execution-parameters-in-the-athena-console.md)
+ [Use the AWS CLI](querying-with-prepared-statements-running-queries-with-execution-parameters-using-the-aws-cli.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
