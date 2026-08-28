---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/catalog-integration-glue-agentic.html
---

# Using the agentic experience with AWS Glue Data Catalog
<a name="catalog-integration-glue-agentic"></a>

After you connect to AWS Glue Data Catalog, choose **Explore data** on the data source to launch the agentic experience.

The agentic experience provides the following capabilities for Data Catalog:
+ **Natural language discovery** – Describe your use case and the AI agent finds relevant tables from your catalog metadata.
+ **Bulk create assets** – Create multiple datasets in a single conversational flow.
+ **Semantic inheritance** – Table and column descriptions are automatically inherited from Glue onto the created datasets.

**Note**
AWS Glue Data Catalog does not store primary and foreign key relationships. However, the agent can recommend inferred relationships to create multi-dataset topics. Review these recommendations before accepting them.

For details on the full agentic flow including discovery, creation, relationships, and semantic inheritance, see [The agentic catalog experience](catalog-integration-agentic-flow.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
