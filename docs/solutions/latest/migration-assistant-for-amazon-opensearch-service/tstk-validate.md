---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tstk-validate.html
---

# Validating query behavior after migration
<a name="tstk-validate"></a>

The split from `string` into `text` and `keyword` changes how fields respond to several common operations, so validate the affected query patterns against the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection before you cut over production traffic. Run representative queries from the Migration Console pod with `console clusters curl target`, and confirm the following:
+  **Term queries** — A `term` query expects an exact, non-analyzed value. It works against `keyword` fields but typically returns no results against a `text` field, because the indexed tokens are lowercased and tokenized. If a field that you query with `term` migrated to `text`, switch to a `match` query or target a `keyword` sub-field.
+  **Aggregations** — Aggregations and `sort` require doc values, which `keyword` fields provide by default but `text` fields do not. Aggregating or sorting on a field that became `text` fails unless `fielddata` is enabled (not recommended) or you aggregate on a `keyword` sub-field instead.
+  **Sorting** — Confirm that fields you sort on resolve to `keyword` (or a `keyword` sub-field). Sorting directly on a `text` field is rejected for the same doc-values reason.
+  **Case-sensitive matching** — Analyzed `text` fields are lowercased by the standard analyzer, so case-sensitive exact matches must use the `keyword` representation of the field. Verify that any case-sensitive lookups still return the expected results.

```
console clusters curl target /<INDEX>/_mapping?pretty
console clusters curl target /<INDEX>/_search?pretty
```

If your indexes use multi-fields (for example, a `text` field with a `.keyword` sub-field), confirm those sub-fields exist on the target and that your application references the correct one for each operation. Running these checks against representative, non-production data first is the safest way to catch mismatched query patterns before cutover.
