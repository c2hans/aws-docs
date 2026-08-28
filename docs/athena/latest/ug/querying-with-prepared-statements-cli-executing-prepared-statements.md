---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-cli-executing-prepared-statements.html
---

# Execute prepared statements using the AWS CLI
<a name="querying-with-prepared-statements-cli-executing-prepared-statements"></a>

To execute a prepared statement with the AWS CLI, you can supply values for the parameters by using one of the following methods:
+ Use the `execution-parameters` argument.
+ Use the `EXECUTE ... USING` SQL syntax in the `query-string` argument.

## Use the execution-parameters argument
<a name="querying-with-prepared-statements-cli-using-the-execution-parameters-argument"></a>

In this approach, you use the `start-query-execution` command and provide the name of an existing prepared statement in the `query-string` argument. Then, in the `execution-parameters` argument, you provide the values for the execution parameters. The following example shows this method.

```
aws athena start-query-execution
--query-string "Execute PreparedStatement1"
--query-execution-context "Database"="default"
--result-configuration "OutputLocation"="s3://amzn-s3-demo-bucket/..."
--execution-parameters "1" "2"
```

## Use the EXECUTE ... USING SQL syntax
<a name="querying-with-prepared-statements-cli-using-the-execute-using-sql-syntax"></a>

To run an existing prepared statement using the `EXECUTE ... USING` syntax, you use the `start-query-execution` command and place the both the name of the prepared statement and the parameter values in the `query-string` argument, as in the following example:

```
aws athena start-query-execution
--query-string "EXECUTE PreparedStatement1 USING 1"
--query-execution-context '{"Database": "default"}'
--result-configuration '{"OutputLocation": "s3://amzn-s3-demo-bucket/..."}'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
