---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tft-validate.html
---

# Validate the transformed metadata
<a name="tft-validate"></a>

After metadata migration completes, confirm that the field types on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection match what you expect. Use the Migration Console to retrieve the mapping for a migrated index directly from the target:

```
console clusters curl target /<INDEX>/_mapping?pretty
```

Replace `<INDEX>` with the name of an index you migrated. Inspect the returned mapping and confirm that:
+ No deprecated source field types remain — for example, no `string`, `flattened`, or `dense_vector` types where the target expects `text`/`keyword`, `flat_object`, or `knn_vector`.
+ Any field types handled by your custom transformer were rewritten to the intended target types, and properties you removed (such as `index`) are gone.
+ Vector fields carry the expected similarity mapping and HNSW parameters when `dense_vector` was converted to `knn_vector`.

You can also retrieve the index settings to confirm the sharding strategy and other index-level definitions migrated as expected:

```
console clusters curl target /<INDEX>/_settings?pretty
```

If a field type is still incorrect, refine the rules in your custom transformer, re-run the metadata migration on the pilot index allowlist, and validate again before migrating the full index set. For where metadata migration sits in the end-to-end workflow and how to gate it with approvals, see [Migrate metadata](migrate-metadata.md).
