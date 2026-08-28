---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/ttm-custom-transformer.html
---

# Custom type transformer
<a name="ttm-custom-transformer"></a>

When you need routing beyond the default union strategy, configure the `TypeMappingSanitizationTransformerProvider` directly in a transformation configuration. This lets you map source index/type pairs to target index names and pin the source version so the transformer interprets the mappings correctly.

The following example renames the merged output of an `activity` index to `new_activity` for an Elasticsearch 6.8 source. It includes `_doc` for normalized metadata and the original legacy type names for document backfill or replay paths that still see source document types:

```
[
  {
    "TypeMappingSanitizationTransformerProvider": {
      "staticMappings": {
        "activity": {
          "_doc": "new_activity",
          "user": "new_activity",
          "post": "new_activity"
        }
      },
      "sourceProperties": {
        "version": {
          "major": 6,
          "minor": 8
        }
      }
    }
  }
]
```

In this structure:
+  `staticMappings` maps each source index to an object whose keys are source type names and whose values are the target index names those types are routed to.
+  `sourceProperties.version.major` and `sourceProperties.version.minor` declare the source Elasticsearch version so the transformer applies the correct multi-type interpretation.

**Important**
In the standard workflow, metadata migration still applies the built-in union transform before any user-supplied metadata transform. Do not rely on a custom type-mapping configuration to split one legacy multi-type index into multiple target indexes unless you also have a custom plan to create the corresponding target metadata. For the workflow-managed path, prefer union, merge, whole-index rename, or drop patterns that keep metadata and document routing aligned.

For pattern-based routing, add `regexMappings`. For example, this rule renames every routed type for every source index to `<source-index>_migrated`, which keeps metadata and document routing aligned:

```
"regexMappings": [
  {
    "sourceIndexPattern": "(.+)",
    "sourceTypePattern": "(.+)",
    "targetIndexPattern": "$1_migrated"
  }
]
```

The `TypeMappingSanitizationTransformerProvider` supports these common workflow-safe strategies:
+  **Merge all types into one index** — Combine multiple types into a single index by mapping them all to the same target index name.
+  **Drop specific types** — Selectively migrate only the types you list; any type you omit is not migrated.
+  **Rename a merged index** — Map `_doc` and the source legacy type names to the new target index name.
+  **Preserve source index names while removing the type layer** — Use regex patterns that map all types for a source index back to that source index name.

Apply the same routing intent to each phase that needs it:

| Phase | Where to configure it |
| --- | --- |
| Metadata migration | Use `metadataMigrationConfig.metadataTransforms` in the workflow, or the raw `transformerConfig`, `transformerConfigBase64`, or `transformerConfigFile` fields for manual/expert configurations. |
| Document backfill | Use `documentBackfillConfig.documentTransforms` in the workflow, or the raw `docTransformerConfig`, `docTransformerConfigBase64`, or `docTransformerConfigFile` fields. |
| Traffic replay | Use `replayerConfig.requestTransforms` for captured request routing. This only applies when you are running capture and replay. |

For a manual metadata run, you can pass the raw descriptor file directly:

```
console metadata migrate --transformer-config-file /tmp/transformation.json
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
