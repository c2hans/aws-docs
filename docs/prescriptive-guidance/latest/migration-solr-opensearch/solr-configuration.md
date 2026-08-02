---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/solr-configuration.html
---

# Solr configuration
<a name="solr-configuration"></a>

The configuration for a Solr collection is defined in `solrconfig.xml`, which contains configuration settings that determine index location and formatting, caching, codec factory, circuit breaks, commits, transaction logs (tlogs), query performance, request handlers, update processing chains, and other settings.

You can manage the configuration in two ways: through the Config API or through a file-based approach. When you use the API to change the configuration, it automatically creates *configuration overlays* (`configoverlay.json`) to override the values in `solrconfig.xml`. Alternatively, you can define the configuration in a file that you can edit directly to modify settings.
