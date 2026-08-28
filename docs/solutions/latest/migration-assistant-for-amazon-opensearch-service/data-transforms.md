---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/data-transforms.html
---

# Transform data and requests
<a name="data-transforms"></a>

Migration Assistant can transform metadata, field mappings, and captured request traffic during migration to make source behavior compatible with the target. Use this section when an upgrade path, target type, or source platform requires compatibility changes.
+  [Transform type mappings](transform-type-mappings.md) - handle multi-type indexes from Elasticsearch 6.x and earlier.
+  [Transform field types](transform-field-types.md) - convert field types that differ between source and target versions.
+  [Transform flattened fields](transform-flattened-flat-object.md) - convert `flattened` fields to OpenSearch `flat_object`.
+  [Transform string fields](transform-string-text-keyword.md) - split Elasticsearch `string` fields into `text` and `keyword`.
+  [Transform dense\_vector fields](transform-dense-vector-knn.md) - convert `dense_vector` to OpenSearch `knn_vector`.
+  [Transform live traffic](transform-replayer.md) - Traffic Replayer transformation options including Elasticsearch content-type header compatibility.
+  [Transform Solr traffic](transform-solr.md) - Solr-to-OpenSearch request translation reference for write operations, queries, and behavioral differences.

Metadata migration also applies built-in compatibility transforms that do not require a dedicated workflow field, including legacy multi-type mapping union, k-NN method and engine compatibility, Serverless-compatible vector mappings, and analyzer/tokenizer/filter cleanup. See [Built-in transformations](migrate-metadata.md#meta-builtin-transforms) for the complete metadata list.

## Workflow transform pipeline model
<a name="transform-pipeline-model"></a>

Custom transform fields use the same workflow pipeline shape across metadata migration, document backfill, traffic replay, and tuple audit records:

| Pipeline field | Used by |
| --- | --- |
|  `metadataMigrationConfig.metadataTransforms`  | Metadata documents before mappings, settings, templates, and aliases are applied to the target. |
|  `documentBackfillConfig.documentTransforms`  | Documents emitted by Reindex-from-Snapshot before bulk indexing to the target. |
|  `replayerConfig.requestTransforms`  | Captured requests before the Traffic Replayer sends them to the target. |
|  `replayerConfig.tupleTransforms`  | Tuple audit records written by the Traffic Replayer for validation and comparison. |

Each pipeline accepts either one transform object or an ordered array of transform objects. Each transform object must choose exactly one selector:
+  `entryPoint` - use workflow-managed JavaScript or Python. Valid forms are `javascript`, `javascriptFile`, `python`, and `pythonFile`.
+  `transformName` - use a named transform provider that is already available in the relevant migration container, such as a built-in or packaged provider.

File-backed entry points use `configMap` or `image` references. For ConfigMaps, `path` is the ConfigMap key and cannot contain nested directories. For images, `path` is relative to the mounted image root; absolute paths and `..` traversal are rejected. Image references can include `pullPolicy`, which defaults to `IfNotPresent`.

Use `context` when a transform needs configuration. It can be either a raw string or an object with named values:
+  `context.values.<name>.value` supplies an inline JSON-compatible value.
+  `context.values.<name>.fromFile` loads one named value from a ConfigMap key or image file.
+  `context.valueDirectories` loads the immediate files from a ConfigMap or image directory as context values. For ConfigMaps, the whole ConfigMap is used as the directory. For images, set `path` to a directory under the mounted image root, or omit `path` to use the image root.

For JavaScript and Python entry points, object context is passed to the script provider as `bindingsObject`, `bindingsObjectFiles`, and `bindingsObjectDirs`. For named providers, object context is passed as provider configuration, with file-backed values under `providerConfigFiles` and directories under `providerConfigDirs`. A raw string context is passed through as the script binding string or the named provider configuration string.

When context values are loaded from files, the provider type controls materialization. JavaScript and Python script providers read file-backed context as UTF-8 text; parse JSON or other structured formats in the script, or use `context.values.<name>.value` for inline structured values. Named providers can declare the expected materialization for each key, such as text, JSON, bytes, Base64, or a resolved file path. Directory-loaded context uses the immediate file name as the context key and ignores nested directories. If the same key appears in multiple places, later sources override earlier ones: directory values first, then individually named `fromFile` values, then inline `value` entries.

The workflow generates the container volume and mount fields for any `configMap` or `image` file references you declare in `entryPoint`, `context.values.fromFile`, or `context.valueDirectories`. Do not set `fileSourceVolumes` or `fileSourceVolumeMounts` manually unless you are bypassing the workflow pipeline and using raw transformer configuration files that you mount yourself.

```
{
  "entryPoint": {
    "javascriptFile": {
      "configMap": "metadata-transforms",
      "path": "field-type-converter.js"
    }
  },
  "context": {
    "values": {
      "mode": { "value": "pilot" },
      "rules": {
        "fromFile": {
          "configMap": "metadata-transforms",
          "path": "rules.json"
        }
      }
    }
  }
}
```

For workflow configurations, prefer these pipeline fields over the phase-specific raw fields, such as `transformerConfig`, `transformerConfigBase64` for metadata, `transformerConfigEncoded` for replay, `docTransformerConfig`, `tupleTransformerConfig`, and their Base64 or file variants. The raw fields remain useful for manual runs and expert configurations where files are already mounted in the container.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
