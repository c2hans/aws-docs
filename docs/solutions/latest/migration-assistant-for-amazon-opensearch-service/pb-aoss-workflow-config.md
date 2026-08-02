---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-aoss-workflow-config.html
---

# Step 6: Complete the workflow configuration
<a name="pb-aoss-workflow-config"></a>

Extend the configuration with the snapshot, metadata, and document-backfill settings. The snapshot repository and snapshot belong under `sourceClusters.source.snapshotInfo`. For a full-domain migration, set `documentBackfillConfig.indexAllowlist` to an empty array to include every index, and set `includeGlobalState` under the snapshot’s `createSnapshotConfig` so legacy and composable templates come across:

```
{
  "sourceClusters": {
    "source": {
      "snapshotInfo": {
        "repos": {
          "default": {
            "awsRegion": "<REGION>",
            "s3RepoPathUri": "s3://migrations-default-<ACCOUNT_ID>-<STAGE>-<REGION>/vector-search-snapshot"
          }
        },
        "snapshots": {
          "migration-snapshot": {
            "config": {
              "createSnapshotConfig": {
                "includeGlobalState": true
              }
            },
            "repoName": "default"
          }
        }
      }
    }
  },
  "snapshotMigrationConfigs": [
    {
      "fromSource": "source",
      "toTarget": "target",
      "perSnapshotConfig": {
        "migration-snapshot": [
          {
            "metadataMigrationConfig": {},
            "documentBackfillConfig": {
              "podReplicas": 5,
              "documentsSizePerBulkRequest": 10485760,
              "documentsPerBulkRequest": 1000,
              "indexAllowlist": []
            }
          }
        ]
      }
    }
  ]
}
```

The values that matter for an Amazon OpenSearch Serverless NextGen target:
+  `documentBackfillConfig.indexAllowlist: []` — an empty list migrates all indexes. To pilot first, list one or two index names instead, then widen later.
+  `includeGlobalState` (under the snapshot’s `createSnapshotConfig`) — carries cluster-level metadata such as templates into metadata migration.
+  `documentBackfillConfig.podReplicas` — the number of RFS worker pods. Start small and scale up while watching the collection.
+  `documentsSizePerBulkRequest` — the maximum aggregate document bytes per bulk request. Keep it modest so each request stays within the collection’s payload limit.
+  `documentsPerBulkRequest` — the maximum number of documents RFS sends in each bulk request. Lower it when many small documents still produce oversized requests.

Because replay is not part of a backfill-only run, you do not configure `speedupFactor` here. If you later add Capture and Replay, `speedupFactor` (default `1.1`) governs how fast captured traffic is replayed; see [Replay tuning](replay-tuning.md).

Review the assembled configuration:

```
workflow configure view
```
