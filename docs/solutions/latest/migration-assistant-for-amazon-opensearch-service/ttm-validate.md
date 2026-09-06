---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/ttm-validate.html
---

# Validate the result
<a name="ttm-validate"></a>

After the transformer has run, confirm that the resulting indexes and mappings on the target match the strategy you chose. Use the `console` CLI from the Migration Console pod (`migration-console-0`) to inspect the target.

List the indexes that were created on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection:

```
console clusters cat-indices --refresh
```

Then inspect the mapping of a specific index to confirm the types were routed, merged, or dropped as expected:

```
console clusters curl target /<index>/_mapping?pretty
```

For split routing, verify that each former type now appears as its own index (for example, `new_users` and `new_posts`). For union routing, verify that the single target index contains the combined set of fields from all merged types, with no conflicting field definitions. If the mappings do not match your intent, change the transformer configuration and re-run the migration as described in [Apply a changed transformer configuration](ttm-restart-required.md).

Run representative application queries against the target before cutover so you catch any client-side impact from the reshaped indexes. See [Migrate metadata](migrate-metadata.md) for the rest of the metadata phase.
