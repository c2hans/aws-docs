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
