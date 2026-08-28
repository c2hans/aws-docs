---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/migrating-configuration.html
---

# Migrating your configuration
<a name="migrating-configuration"></a>

This section describes how to migrate your Apache Solr configuration (`solrconfig.xml`) to index settings and equivalent features in Amazon OpenSearch Service.

**Prerequisites**

Before starting the configuration migration, make sure that you have:
+ Access to your Solr configuration file (`solrconfig.xml`).
+ A complete understanding of your current configuration settings.
+ An inventory of your Solr request handlers and search components.
+ Knowledge of your commit and performance settings.
+ A test environment with Amazon OpenSearch Service deployed for validation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
