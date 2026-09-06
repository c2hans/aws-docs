---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/metadata-migration-tool-1.html
---

# Metadata Migration
<a name="metadata-migration-tool-1"></a>

Metadata migration moves the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection into a shape that can accept the incoming data and traffic. It handles mappings, templates, aliases, and other index-level definitions before document backfill or replay becomes meaningful. In the workflow model, metadata migration is a configured phase inside the migration workflow, not a separate manual tool run. When `metadataMigrationConfig` is present, the workflow runs two logical steps: `evaluateMetadata` (evaluates what would be applied) and `migrateMetadata` (writes those changes to the target). If approvals are enabled, the workflow can pause between these steps so you can inspect the result before continuing.

Metadata migration handles index settings, index mappings, legacy and composable templates, component templates, and aliases. It also applies built-in transformations to handle upgrades between version-specific behavior, including legacy multi-type mapping union, `string` to `text` and `keyword`, `flattened` to `flat_object`, `dense_vector` to `knn_vector`, k-NN method compatibility for newer Amazon OpenSearch Service and Amazon OpenSearch Serverless NextGen targets, and analysis-component cleanup for analyzer, tokenizer, char-filter, and token-filter names that changed across versions. Advanced users can also supply custom metadata transformers through `metadataTransforms`, or through `transformerConfig`, `transformerConfigBase64`, or `transformerConfigFile` for raw descriptor configurations.

Plan separate work for security configuration, ISM/ILM policies, ingest pipelines, OpenSearch Dashboards or Kibana saved objects, data streams, and cluster-level tuning - these are not migrated automatically. For data streams, Migration Assistant can still backfill documents from source backing indexes when you manually prepare the target data stream and configure the RFS data-stream transform.
