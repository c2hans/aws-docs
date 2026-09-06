---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tdvk-validation.html
---

# Post-migration validation
<a name="tdvk-validation"></a>

After metadata migration completes, confirm that vector fields were transformed correctly on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection before you backfill documents and switch traffic.

1. Verify the transformed mapping on the target. Confirm each former `dense_vector` field is now a `knn_vector` field with the expected `dimension` and `method`:

   ```
   console clusters curl target /<INDEX>/_mapping?pretty
   ```

1. Compare the target `dimension` and `space_type` against the source values you recorded in [Identifying dense\_vector fields before you migrate](tdvk-identify-fields.md). The dimension must match exactly.

1. After document backfill, run a representative vector query against the target and confirm that results return and that the top matches are reasonable for your data:

   ```
   console clusters curl target /<INDEX>/_search?pretty -X POST -H 'Content-Type: application/json' -d '<KNN_QUERY_BODY>'
   ```

1. Compare result quality and, where it matters to your application, score values against the source. If ranking or scores differ in ways your application cannot tolerate, revisit the produced `method` and `space_type` and plan client-side adjustments before cutover.

If the transformed mapping is not what you need — for example, you require a specific engine, space type, or HNSW tuning that the built-in transformation does not produce — you can supply a custom metadata transformer through `metadataTransforms` in the workflow configuration. Raw descriptor configurations can also use `transformerConfig`, `transformerConfigBase64`, or `transformerConfigFile`. For how custom transformers compose with the built-in ones, see [Migrate metadata](migrate-metadata.md).
