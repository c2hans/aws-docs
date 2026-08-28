---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tft-recommended-sequence.html
---

# Recommended sequence
<a name="tft-recommended-sequence"></a>

Introduce custom field-type transformation only after you have confirmed that the built-in transformations do not fully cover your source. Follow this sequence to keep custom logic minimal and verifiable:

1.  **Assess the source.** Review your source mappings and run the assessment to identify field types that may need attention. For the broader compatibility review, see [Assessment](plan-your-deployment.md#assessment).

1.  **Review the built-in transformation pages.** Confirm whether the built-in `string` to `text` and `keyword` ([Transform string fields to text and keyword](transform-string-text-keyword.md)), `flattened` to `flat_object` ([Transform flattened fields to flat\_object](transform-flattened-flat-object.md)), `dense_vector` to `knn_vector` ([Transform dense\_vector fields to knn\_vector](transform-dense-vector-knn.md)), k-NN compatibility, and analysis-component compatibility transformations already cover your source. If they do, you do not need a custom transformer.

1.  **Pilot on a small index allowlist.** Run the metadata migration against a small `indexAllowlist` and evaluate the result first. In workflow-managed runs, approve and inspect the `evaluateMetadata` output before `migrateMetadata` applies the metadata changes; for manual runs, use `console metadata evaluate` to preview the changes and `console metadata migrate` to apply them. Inspect the migrated mappings on the target before scaling up.

1.  **Add a custom transformer only if the pilot requires it.** If — and only if — the pilot surfaces a field type the built-ins do not handle, author a custom JavaScript transformer as described in [Custom field type transformer (JavaScript)](tft-custom-transformer.md), then re-run the pilot with the transformer applied before migrating the full index set.

**Tip**
Keep the `rules` array in your custom transformer as small as possible — add a rule only for a field type the built-ins do not already resolve. Re-running the pilot after each change makes it easy to confirm that the transformer produces exactly the mappings you expect on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
