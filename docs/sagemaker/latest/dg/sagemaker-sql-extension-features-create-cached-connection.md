---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-create-cached-connection.html
---

# Create cached connections
<a name="sagemaker-sql-extension-features-create-cached-connection"></a>

You can create cached connections by specifying a connection name in the `--connection-name` parameter of your connection string. This is particularly useful when multiple connection properties are overridden for a specific use case, and there's a need to reuse the same properties without retyping them.

For example, the code below saves an Athena connection with an overridden schema connection property using the name `--connection-name my_athena_conn_with_schema`, and then reuses it in another cell:

```
%%sm_sql --connection-name my_athena_conn_with_schema --connection-properties '{"schema_name": "sm-sql-private-beta-db"}' --metastore-id sm-sql-private-beta-athena-connection --metastore-type GLUE_CONNECTION
SELECT * FROM "covid_table" LIMIT 2
```

```
%%sm_sql --connection-name my_athena_conn_with_schema
SELECT * FROM "covid_table" LIMIT 2
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
