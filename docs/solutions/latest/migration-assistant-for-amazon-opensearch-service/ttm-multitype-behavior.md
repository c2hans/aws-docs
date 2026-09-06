---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/ttm-multitype-behavior.html
---

# Configuring multi-type behavior
<a name="ttm-multitype-behavior"></a>

For most migrations, you do not need to configure anything. By default, Migration Assistant applies a built-in transformer that unions all mapping types of a multi-type index into a single target index on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. This default is applied automatically to every multi-type index it encounters, with no workflow configuration field required.

To adjust the default behavior, supply a `TypeMappingSanitizationTransformerProvider` transformer configuration as described in [Custom type transformer](ttm-custom-transformer.md). The provider supports the following routing mechanisms:

| Configuration | What it does and when to use it |
| --- | --- |
| No custom configuration | Unions all types in each source index into a single target index with the same name. This is the default and works when the types share compatible field definitions. |
|  `staticMappings`  | Maps exact source index and type names to target index names. Use this for deliberate renames, merges, or drops for known indexes. In standard workflow metadata migration, include an `_doc` entry because the built-in metadata union normalizes legacy types before user metadata transforms run. If a source index is present in `staticMappings`, omitted types are dropped by that transform stage. |
|  `regexMappings`  | Maps source index and type patterns to target index name patterns. Use this when the same routing rule applies across many indexes. Regex rules apply only when the source index is not present in `staticMappings`. |

Migration Assistant applies the union strategy by default for any Elasticsearch 6.x or earlier source migrating to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. There is no separate `multiTypeBehavior` workflow field. To change routing after union — for example, to rename the merged target index or to drop specific routed documents — configure `TypeMappingSanitizationTransformerProvider` directly.

After editing the configuration, resubmit the workflow:

```
workflow configure edit
workflow submit
workflow manage
```

**Important**
Unioning types that define the same field name with incompatible field types produces a mapping conflict and fails the migration. If you are unsure whether your types are compatible, keep approvals enabled and review the `evaluateMetadata` output before approving metadata migration. If the union cannot be made compatible, plan a custom migration path that creates compatible target metadata rather than relying on the standard workflow to split one legacy index into multiple target indexes.
