---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/ttm-restart-required.html
---

# Apply a changed transformer configuration
<a name="ttm-restart-required"></a>

**Important**
Whenever you change the type-mapping transformer configuration for a workflow-managed run, edit the workflow configuration and resubmit the workflow so metadata migration, backfill, and replay use the same behavior. Previously migrated data and metadata may also need to be cleared first to avoid an inconsistent state, because indexes and documents that were already written using the old configuration will not be rewritten automatically.

To apply a configuration change cleanly, edit the workflow configuration, clear any affected data on the target when no workflow pod is writing to it, and resubmit:

```
workflow configure edit
console clusters clear-indices --cluster target --acknowledge-risk
workflow submit
```

 `workflow submit` stops and replaces an existing workflow with the same name before submitting the next run, but it does not clear indexes or documents that were already written to the target. If an abandoned run left migration custom resources that block resubmission, use `workflow reset` to remove those resources before you resubmit.

**Warning**
 `console clusters clear-indices --cluster target --acknowledge-risk` is destructive — it deletes all indexes on the named cluster. Run it only against the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection you are migrating into, and only when you intend to re-run the migration from a clean state.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
