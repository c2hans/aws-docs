---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

This section describes the [assessment](#assessment), [Region](#supported-aws-regions), [cost](cost.md), [security](security-1.md), and [quota](quotas.md) considerations for planning your deployment.

## Assessment
<a name="assessment"></a>

Assessment is where you decide whether your migration to Amazon OpenSearch Service or Amazon OpenSearch Serverless NextGen should be simple, staged, or zero-downtime. The goal is not to memorize every breaking change. The goal is to identify the issues that will affect your workflow configuration, your cutover plan, and your application behavior before you start moving data.

### Questions to answer before you migrate
<a name="questions-to-answer-before-migrating"></a>

Before you build the workflow, make sure you can answer:
+ Is your source and target path supported? See the migration matrix in [Solution overview](solution-overview.md).
+ Do you need planned downtime, or do you need capture and replay?
+ Can the source create snapshots, and can Migration Assistant read them from Amazon S3?
+ What authentication model will each source and target use - basic auth, AWS Signature Version 4 (SigV4), or no auth? A single cluster `authConfig` uses one mode.
+ Are there mapping or field transformations you already know you need?
+ Which components need separate manual migration or preparation (security, ISM/ILM, ingest pipelines, OpenSearch Dashboards or Kibana saved objects, data streams)?

### Think in terms of migration risk
<a name="think-in-terms-of-migration-risk"></a>

Most migration risk falls into four buckets:
+  **Application compatibility** — queries, aggregations, index names, aliases, or field names may need to change for the target on Amazon OpenSearch Service or Amazon OpenSearch Serverless NextGen.
+  **Metadata compatibility** — mappings, templates, and settings may need transformations. Built-in transformations cover multi-type mapping union for legacy Elasticsearch indexes, `string` to `text` and `keyword`, `flattened` to `flat_object`, `dense_vector` to `knn_vector`, k-NN vector compatibility for newer OpenSearch and Serverless targets, and analysis-component cleanup for analyzer, tokenizer, char-filter, and token-filter names that changed across versions. Custom metadata transformers can be supplied through the workflow `metadataTransforms` pipeline or, for raw descriptor configurations, through `transformerConfig`.
+  **Data movement** — snapshot creation, source Amazon S3 access, target ingest throughput, and large shards (over 80 GiB by default) may affect runtime.
+  **Operational cutover** — you need to decide whether a write pause is acceptable or whether capture and replay is required.

### Validate the application, not just the cluster
<a name="validate-the-application-not-just-the-cluster"></a>

A migration is only finished when the application behaves correctly on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

Before cutover, plan to validate:
+ representative reads and writes
+ dashboards or saved searches that depend on mappings
+ aggregations or sorts that depend on exact field behavior
+ any client-side assumptions about aliases, index names, or field names

If you are using custom transformations, always run a pilot first.

### Component support
<a name="migration-assistant-component-support"></a>

The following table shows which components are migrated automatically and which require separate work:

| Component | Automatic | Recommendation |
| --- | --- | --- |
| Documents | ✓ | Migrate using Reindex-from-Snapshot (RFS) backfill or Capture and Replay |
| Index settings | ✓ | Migrated automatically |
| Index mappings | ✓ | Migrated automatically |
| Index templates | ✓ | Migrated automatically |
| Component templates | ✓ | Migrated automatically |
| Aliases | ✓ | Migrated automatically |
| Data streams | Partial/manual | Metadata migration does not create data streams. Recreate the target data stream and templates manually; RFS can backfill documents from `.ds-*` backing indexes only when you also configure a backing-index allowlist and data-stream document transform. |
| ISM/ILM policies | ✗ | Manually recreate on target |
| Security configuration | ✗ | Configure separately on target |
| OpenSearch Dashboards / Kibana saved objects | ✗ | Export/import using OpenSearch Dashboards UI |
| Ingest pipelines | ✗ | Manually recreate |
| Cluster settings | ✗ | Configure separately |

## Migration phases
<a name="migration-phases"></a>

A migration follows the same lifecycle regardless of source. Use this list to plan effort and cutover sequencing:

1.  **Assess** — review the questions above, the supported migration paths in [Solution overview](solution-overview.md), and the components that need manual migration.

1.  **Deploy** — deploy Migration Assistant on Amazon EKS. See [Deploy the solution](deploy-the-solution.md).

1.  **Configure** — load the version-matched workflow sample on the Migration Console with `workflow configure sample --load`, then `workflow configure edit`.

1.  **Run a pilot** — use a small index allowlist before scaling up.

1.  **Submit and monitor** — submit the workflow with `workflow submit` and monitor with `workflow manage`.

1.  **Approve** — release gated transitions only after validation.

1.  **Cut over** — redirect clients to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

1.  **Remove infrastructure** — clean up only after the rollback window has passed. See [Uninstall the solution](uninstall-the-solution.md).

## Supported AWS Regions
<a name="supported-aws-regions"></a>

This solution uses Amazon OpenSearch Service and Amazon OpenSearch Serverless NextGen, which are not currently available in all AWS Regions. For the most current availability of AWS services by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

Migration Assistant for Amazon OpenSearch Service is available in the following AWS Regions:

| Region name | Region |
| --- | --- |
| US East (N. Virginia) | us-east-1 |
| US East (Ohio) | us-east-2 |
| US West (N. California) | us-west-1 |
| US West (Oregon) | us-west-2 |
| Africa (Cape Town) | af-south-1 |
| Asia Pacific (Hong Kong) | ap-east-1 |
| Asia Pacific (Hyderabad) | ap-south-2 |
| Asia Pacific (Jakarta) | ap-southeast-3 |
| Asia Pacific (Melbourne) | ap-southeast-4 |
| Asia Pacific (Mumbai) | ap-south-1 |
| Asia Pacific (Osaka) | ap-northeast-3 |
| Asia Pacific (Seoul) | ap-northeast-2 |
| Asia Pacific (Singapore) | ap-southeast-1 |
| Asia Pacific (Sydney) | ap-southeast-2 |
| Asia Pacific (Tokyo) | ap-northeast-1 |
| Canada (Central) | ca-central-1 |
| Canada West (Calgary) | ca-west-1 |
| Europe (Frankfurt) | eu-central-1 |
| Europe (London) | eu-west-2 |
| Europe (Milan) | eu-south-1 |
| Europe (Paris) | eu-west-3 |
| Europe (Spain) | eu-south-2 |
| Europe (Stockholm) | eu-north-1 |
| Europe (Zurich) | eu-central-2 |
| Ireland (eu-west-1) | eu-west-1 |
| Israel (Tel Aviv) | il-central-1 |
| Middle East (Bahrain) | me-south-1 |
| Middle East (UAE) | me-central-1 |
| South America (São Paulo) | sa-east-1 |
| AWS GovCloud (US-East) | us-gov-east-1 |
| AWS GovCloud (US-West) | us-gov-west-1 |
