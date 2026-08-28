---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/solr-configuration.html
---

# Solr configuration
<a name="solr-configuration"></a>

The configuration for a Solr collection is defined in `solrconfig.xml`, which contains configuration settings that determine index location and formatting, caching, codec factory, circuit breaks, commits, transaction logs (tlogs), query performance, request handlers, update processing chains, and other settings.

You can manage the configuration in two ways: through the Config API or through a file-based approach. When you use the API to change the configuration, it automatically creates *configuration overlays* (`configoverlay.json`) to override the values in `solrconfig.xml`. Alternatively, you can define the configuration in a file that you can edit directly to modify settings.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
