---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-sql-execution-query-parameters.html
---

# Use query parameters to provide dynamic values in SQL queries
<a name="sagemaker-sql-extension-features-sql-execution-query-parameters"></a>

Query parameters can be used to provide dynamic values in SQL queries.

In the following example, we pass a query parameter to the `WHERE` clause of the query.

```
# How to use '--query-parameters' with ATHENA as a data store
%%sm_sql --metastore-id {{athena-connection-name}} --metastore-type GLUE_CONNECTION --query-parameters '{"parameters":{"name_var": "John Smith"}}'
SELECT * FROM my_db.my_schema.my_table WHERE name = (%(name_var)s);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
