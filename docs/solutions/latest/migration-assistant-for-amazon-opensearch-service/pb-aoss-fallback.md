---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-aoss-fallback.html
---

# Step 9: Fallback guidance
<a name="pb-aoss-fallback"></a>

If validation fails or the collection does not behave as expected, you have a clean fallback because the migration is non-destructive to the source — the source domain is only read once, during the snapshot.
+  **Keep serving from the source.** Until you redirect application traffic, the source Amazon OpenSearch Service domain remains the live system. There is no cutover until you change clients.
+  **Re-run a phase rather than the whole migration.** RFS resumes from its last checkpoint and skips already-migrated shards, so you can correct a transform or mapping and restart backfill without duplicating data.
+  **Clear and retry the target if metadata is wrong.** If a mapping landed incorrectly on the collection, delete the affected index on the target, fix the metadata transform, then re-run metadata migration and backfill. Use `console clusters clear-indices --cluster target --acknowledge-risk` only when you intend to wipe the target collection’s indexes.
+  **Hold the rollback window.** Keep the source domain available for a rollback window (typically 24-72 hours) after you redirect traffic, in case you need to point clients back.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
