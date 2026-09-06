---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tffo-built-in-behavior.html
---

# Built-in transformation behavior
<a name="tffo-built-in-behavior"></a>

The `flattened` type lets a single field hold an entire JSON object and indexes the nested leaf values as keywords. OpenSearch provides the equivalent `flat_object` type. When the source mapping contains a field of type `flattened` and the target supports `flat_object`, the solution rewrites the field type during metadata migration without any additional configuration.

Keep the following in mind:
+ The transformation is applied automatically whenever a `flattened` field is detected in the source mappings, for both Amazon OpenSearch Service domains and Amazon OpenSearch Serverless NextGen collections that support `flat_object`.
+ It changes the field **type** in the index mapping. It does not alter your documents or the nested keys inside the field.
+ No CLI flag, transformer file, or `transformerConfig` entry is required for the built-in conversion.
