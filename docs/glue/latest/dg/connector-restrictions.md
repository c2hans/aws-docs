---
source_url: https://docs.aws.amazon.com/glue/latest/dg/connector-restrictions.html
---

# Restrictions for using connectors and connections in AWS Glue Studio
<a name="connector-restrictions"></a>

When you're using custom connectors or connectors from AWS Marketplace, take note of the following restrictions:
+ The testConnection API isn't supported with connections created for custom connectors.
+ Data Catalog connection password encryption isn't supported with custom connectors.
+ You can't use job bookmarks if you specify a filter predicate for a data source node that uses a JDBC connector.
+  Creating a Marketplace connection is not supported outside of the AWS Glue Studio user interface.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
