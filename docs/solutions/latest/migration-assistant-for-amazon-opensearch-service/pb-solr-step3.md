---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-solr-step3.html
---

# Step 3: Submit and monitor the workflow
<a name="pb-solr-step3"></a>

Run a pilot first. Narrow the configuration to a small subset of collections or a single representative collection, then submit and watch the run:

```
workflow submit
workflow manage
```

 `workflow manage` is the interactive interface for monitoring progress and approving gated steps. For a non-interactive view or to follow logs, use:

```
workflow status
workflow log all --follow
```

When you run the workflow for an Apache Solr source, Migration Assistant performs these phases automatically in order:

1.  **Read the backup** — RFS reads the Apache Solr backup files from the Amazon S3 location you configured in `snapshotInfo`.

1.  **Translate the schema** — Metadata migration parses the Solr `schema.xml` and translates field types into OpenSearch index settings and mappings (see the table in [Schema translation reference](pb-solr-schema.md)). If approvals are enabled, the workflow pauses at the `evaluateMetadata` and `migrateMetadata` gates.

1.  **Bulk-index documents** — The document backfill phase reconstructs Apache Solr documents from Lucene stored fields in the backup and indexes them into the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection, fanned out across the `podReplicas` you configured.

Approve any gated steps from `workflow manage` (or with `workflow approve step <PATTERN>`) only after you have reviewed the evaluated metadata. When the pilot succeeds and validation passes, widen the configuration to the full set of collections and submit again:

```
workflow configure edit
workflow submit
workflow manage
```
