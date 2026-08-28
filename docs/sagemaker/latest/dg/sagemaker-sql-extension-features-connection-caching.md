---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-connection-caching.html
---

# SQL extension connection caching
<a name="sagemaker-sql-extension-features-connection-caching"></a>

The SQL extension extension defaults to caching connections to prevent the creation of multiple connections for the same set of connection properties. The cached connections can be managed using the `%sm_sql_manage` magic command.

The following topics describe how to manage your cached connections.

**Topics**
+ [Create cached connections](sagemaker-sql-extension-features-create-cached-connection.md)
+ [List cached connections](sagemaker-sql-extension-features-list-cached-connection.md)
+ [Clear cached connections](sagemaker-sql-extension-features-clear-cached-connection.md)
+ [Disable cached connections](sagemaker-sql-extension-features-disable-cached-connection.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
