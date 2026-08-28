---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/catalog-integration-databricks-connection.html
---

# Setting up the Databricks connection
<a name="catalog-integration-databricks-connection"></a>

The Databricks connector supports catalog integration without requiring a new connector. The following connection options are available:
+ The agentic experience (**Explore Data**) is available for existing Databricks data sources that use a Personal Access Token (PAT).
+ A single Databricks connection provides access to both metadata and data. This differs from AWS Glue Data Catalog, which requires two separate connections.
+ Supported authentication options: Personal Access Token (PAT) or OAuth 3LO.

To create a Databricks data source, navigate to **Create Data Source** and select **Databricks**. Choose your preferred authentication method and enter the connection details.

**Note**
Databricks Metrics Views are not yet supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
