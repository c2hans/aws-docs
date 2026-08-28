---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-aoss-run-monitor.html
---

# Step 7: Run and monitor the workflow
<a name="pb-aoss-run-monitor"></a>

Before submitting, confirm both clusters are reachable and authenticated:

```
console clusters connection-check
```

Submit the workflow and watch it through the interactive manager, approving any gated steps after you have inspected them:

```
workflow submit
workflow manage
```

The workflow snapshots the source domain, runs the `evaluateMetadata` and `migrateMetadata` phases, then bulk-indexes documents into the collection. Use the non-interactive status and log views if you prefer to script monitoring:

```
workflow status --live-status
workflow log all --follow
```

To increase backfill throughput, increase `documentBackfillConfig.podReplicas`, resubmit the workflow, and watch the collection’s OCU usage so you do not oversaturate it:

```
workflow configure edit
workflow submit
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
