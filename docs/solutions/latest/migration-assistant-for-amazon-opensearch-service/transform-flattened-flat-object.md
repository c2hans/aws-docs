---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/transform-flattened-flat-object.html
---

# Transform flattened fields to flat\_object
<a name="transform-flattened-flat-object"></a>

When you migrate from Elasticsearch to OpenSearch, the Migration Assistant for Amazon OpenSearch Service solution automatically converts the Elasticsearch `flattened` field type (introduced in Elasticsearch 7.3) to the OpenSearch `flat_object` field type (introduced in OpenSearch 2.7). This is one of the built-in metadata transformations the solution applies during the metadata migration phase, so in most cases you do not need to configure anything. This page explains the built-in behavior, how to confirm which indexes are affected, and how to validate the result on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

This transformation runs as part of metadata migration. For the broader metadata phase and how to evaluate and run it, see [Migrate metadata](migrate-metadata.md).
