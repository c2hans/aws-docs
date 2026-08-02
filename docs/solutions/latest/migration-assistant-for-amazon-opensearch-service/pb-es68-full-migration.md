---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-full-migration.html
---

# Step 10: Run the full migration
<a name="pb-es68-full-migration"></a>

After the pilot validates cleanly, widen the configuration to cover all indexes by setting `indexAllowlist` to an empty array, then submit again. An empty allowlist means all eligible indexes are migrated.

```
workflow configure edit
```

```
{
  "snapshotMigrationConfigs": [
    {
      "fromSource": "source",
      "toTarget": "target",
      "perSnapshotConfig": {
        "migration-snapshot": [
          {
            "metadataMigrationConfig": {
              "skipEvaluateApproval": false,
              "skipMigrateApproval": false
            },
            "documentBackfillConfig": {
              "podReplicas": 4,
              "indexAllowlist": []
            }
          }
        ]
      }
    }
  ]
}
```

```
workflow submit
workflow manage
```

Approve the metadata gates again as in [Step 8](pb-es68-submit-pilot.md). To speed up the full backfill, increase `documentBackfillConfig.podReplicas` in the workflow configuration and resubmit. Each RFS worker processes one shard at a time from the snapshot in Amazon S3, so scaling up does not add live read load to the source cluster:

```
workflow configure edit
workflow submit
```

Scale up gradually while monitoring the health of the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection so you do not oversaturate it.
