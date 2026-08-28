---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-running-queries-with-execution-parameters-using-the-aws-cli.html
---

# Run queries with execution parameters using the AWS CLI
<a name="querying-with-prepared-statements-running-queries-with-execution-parameters-using-the-aws-cli"></a>

To use the AWS CLI to run queries with execution parameters, use the `start-query-execution` command and provide a parameterized query in the `query-string` argument. Then, in the `execution-parameters` argument, provide the values for the execution parameters. The following example illustrates this technique.

```
aws athena start-query-execution
--query-string "SELECT * FROM table WHERE x = ? AND y = ?"
--query-execution-context "Database"="default"
--result-configuration "OutputLocation"="s3://amzn-s3-demo-bucket;/..."
--execution-parameters "1" "2"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
