---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tstk-identify-fields.html
---

# Identifying string fields before migration
<a name="tstk-identify-fields"></a>

Before you migrate, inspect the source cluster mappings so you know which fields will be converted and which target type each will receive. From the Migration Console pod (`migration-console-0`), query the source `_mapping` API:

```
console clusters curl source /<INDEX>/_mapping?pretty
```

To review mappings across every index at once:

```
console clusters curl source /_mapping?pretty
```

In the output, look for fields whose `type` is `string` and note their `index` setting. For example, the following source field becomes `text` because it is analyzed:

```
{
  "title": {
    "type": "string",
    "index": "analyzed"
  }
}
```

The next field becomes `keyword` because it is explicitly not analyzed:

```
{
  "status_code": {
    "type": "string",
    "index": "not_analyzed"
  }
}
```

Pay particular attention to fields that omit the `index` property. In Elasticsearch 1.x–5.x these defaulted to `analyzed`, so they migrate to `text`. If your application uses any of those fields for exact matching, sorting, or aggregations, plan to validate those queries on the target — `text` fields behave differently from `keyword` fields for those operations.

**Tip**
You can preview the full set of items Migration Assistant will migrate, including the transformed mappings, by running `console metadata evaluate` before you migrate. See [Migrate metadata](migrate-metadata.md).
