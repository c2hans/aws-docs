---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-solr-step2.html
---

# Step 2: Configure the workflow
<a name="pb-solr-step2"></a>

Open the workflow configuration on the Migration Console pod:

```
workflow configure edit
```

Set the source to your Apache Solr deployment. The `version` string uses the form `SOLR <major>.<minor>.<patch>` (for example, `SOLR 8.11.4` or `SOLR 9.7.0`). The snapshot configuration belongs under `sourceClusters.solr-source.snapshotInfo`: define the Amazon S3 repository under `repos` (the repository name is the map key) and reference it from a snapshot under `snapshots`. Because this playbook synced the Solr backup to Amazon S3 manually, reference it as an externally managed snapshot:

```
{
  "sourceClusters": {
    "solr-source": {
      "version": "SOLR 8.11.4",
      "snapshotInfo": {
        "repos": {
          "solr-backup-repo": {
            "awsRegion": "<REGION>",
            "s3RepoPathUri": "s3://<BUCKET>/solr-backup"
          }
        },
        "snapshots": {
          "solr-snapshot": {
            "config": {
              "externallyManagedSnapshotName": "<BACKUP_NAME>"
            },
            "repoName": "solr-backup-repo"
          }
        }
      }
    }
  }
}
```

To have the workflow create the Solr backup instead, include the live Solr `endpoint` and replace the snapshot `config` with `createSnapshotConfig`:

```
{
  "sourceClusters": {
    "solr-source": {
      "endpoint": "http://<SOLR_HOST>:<SOLR_PORT>",
      "version": "SOLR 8.11.4",
      "snapshotInfo": {
        "repos": {
          "solr-backup-repo": {
            "awsRegion": "<REGION>",
            "s3RepoPathUri": "s3://<BUCKET>/solr-backup"
          }
        },
        "snapshots": {
          "solr-snapshot": {
            "config": {
              "createSnapshotConfig": {
                "snapshotPrefix": "solr"
              }
            },
            "repoName": "solr-backup-repo"
          }
        }
      }
    }
  }
}
```

The workflow-managed path backs up every discovered collection or core. The workflow JSON does not expose the manual `CreateSnapshot --solr-collections` option. `createSnapshotConfig.indexAllowlist` does not limit Solr backup creation; use `metadataMigrationConfig.indexAllowlist` and `documentBackfillConfig.indexAllowlist` with exact collection or core names if you want to migrate only part of a full Solr backup. The Solr backup reader does not apply `regex:` allowlist patterns. To avoid backing up other Solr collections at all, create an externally managed backup for only the desired collections and reference it with `externallyManagedSnapshotName`.

Set the target to your Amazon OpenSearch Service domain, using SigV4 authentication. For an Amazon OpenSearch Service domain, set `service: es`:

```
{
  "targetClusters": {
    "target": {
      "endpoint": "https://<domain-endpoint>",
      "authConfig": {
        "sigv4": {
          "region": "<REGION>",
          "service": "es"
        }
      }
    }
  }
}
```

For an Amazon OpenSearch Serverless NextGen collection, set `service: aoss` instead and add the migration IAM role (`<eks-cluster-name>-migrations-role`) to the collection’s data access policy with both collection-level and index-level permissions. See [Configure and run workflows](use-the-solution.md) for the full target configuration examples.

For the backfill path in this playbook, configure the snapshot migration with a metadata migration phase and a document backfill phase. The `metadataMigrationConfig` block controls the approval gates around schema translation. Set `documentBackfillConfig.podReplicas` to the number of RFS workers you want running in parallel:

```
{
  "snapshotMigrationConfigs": [
    {
      "fromSource": "solr-source",
      "toTarget": "target",
      "perSnapshotConfig": {
        "solr-snapshot": [
          {
            "metadataMigrationConfig": {
              "skipEvaluateApproval": false,
              "skipMigrateApproval": false
            },
            "documentBackfillConfig": {
              "podReplicas": 4
            }
          }
        ]
      }
    }
  ]
}
```

Leave `skipEvaluateApproval` and `skipMigrateApproval` set to `false` for your first run so the workflow pauses at the metadata gates and lets you inspect the translated mappings before they are written to the target. Set them to `true` only after you have validated the translation on a pilot.

**Note**
For a backfill-only run, do not configure a `replayerConfig` or any Capture and Replay phase. For a SolrCloud source where you need live write capture, configure the `traffic` section, `SolrToOpenSearchTransformProvider`, and `SolrTupleTransformProvider` as described in [Capture and replay live traffic from Solr](solr-capture-replay.md).
