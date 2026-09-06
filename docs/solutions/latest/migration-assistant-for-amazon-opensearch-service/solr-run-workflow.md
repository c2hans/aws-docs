---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/solr-run-workflow.html
---

# Configure and run the backfill workflow
<a name="solr-run-workflow"></a>

After your Solr S3 repository is ready, configure and run the migration from the Migration Console pod (`migration-console-0`) in the `ma` namespace, the same way you would for any other source.

1.  **Load the version-matched sample** as your starting point:

   ```
   workflow configure sample --load
   ```

1.  **Edit the configuration.** Set the source version to your Solr version, point `snapshotInfo` at the Amazon S3 backup location, and set the target authentication. The following example lets the workflow create the Solr backup:

   ```
   {
     "sourceClusters": {
       "source": {
         "endpoint": "http://SOLR_ENDPOINT:8983",
         "version": "SOLR 8.11.4",
         "snapshotInfo": {
           "repos": {
             "s3": {
               "awsRegion": "REGION",
               "s3RepoPathUri": "s3://BUCKET/SUBPATH"
             }
           },
           "snapshots": {
             "snap1": {
               "config": {
                 "createSnapshotConfig": {
                   "snapshotPrefix": "solr"
                 }
               },
               "repoName": "s3"
             }
           }
         }
       }
     },
     "targetClusters": {
       "target": {
         "endpoint": "https://TARGET_ENDPOINT",
         "authConfig": {
           "sigv4": {
             "region": "REGION",
             "service": "es"
           }
         }
       }
     },
     "snapshotMigrationConfigs": [
       {
         "fromSource": "source",
         "toTarget": "target",
         "perSnapshotConfig": {
           "snap1": [
             {
               "metadataMigrationConfig": {},
               "documentBackfillConfig": {
                 "podReplicas": 3,
                 "maxShardSizeBytes": 85899345920
               }
             }
           ]
         }
       }
     ]
   }
   ```

   Use the following Solr-specific settings:
   +  `version` — the source version string in `SOLR major.minor.patch` format (for example, `SOLR 8.11.4`).
   +  `endpoint` — the live Solr endpoint. The workflow uses it for workflow-managed backup creation and Solr detection.
   +  `sourceClusters.source.snapshotInfo.repos.s3.awsRegion` — the AWS Region of the bucket where the Solr backup is written.
   +  `sourceClusters.source.snapshotInfo.repos.s3.s3RepoPathUri` — the `s3://BUCKET/SUBPATH` base location for the Solr backup. For workflow-managed Solr backups, the generated snapshot name is appended under this path. The generated name has the form `sourceLabel_snapshotPrefix_uniqueId`; if `snapshotPrefix` is omitted, the snapshot entry key such as `snap1` is used as the middle component.
   +  `sourceClusters.source.snapshotInfo.repos.s3.endpoint` — optional custom S3 endpoint for LocalStack or S3-compatible storage. Use this only when your Solr S3 repository is also configured for that endpoint.
   +  `sourceClusters.source.snapshotInfo.snapshots.snap1.config.createSnapshotConfig` — tells the workflow to create a Solr backup. The workflow auto-discovers all collections or cores; use exact-name metadata and document backfill allowlists if you want to migrate only a subset from that backup.
   +  `sourceClusters.source.snapshotInfo.snapshots.snap1.repoName` — must match a repository key under `snapshotInfo.repos`, which in turn corresponds to the `repository name="…​"` value in your `solr.xml` (`s3` in the examples above). The bucket configured in `solr.xml` must match the bucket in `s3RepoPathUri`.
   +  `sourceClusters.source.snapshotInfo.serializeSnapshotCreation` — optional control for multiple workflow-created snapshot entries on the same Solr source. When omitted, Solr sources use the parallel snapshot-creation default. Set this to `true` if the Solr deployment or backup repository should run only one backup operation at a time.
   +  `snapshotMigrationConfigs[].perSnapshotConfig.snap1[].metadataMigrationConfig` — runs schema translation before document backfill so target indexes and mappings are created from the Solr backup.
   +  `snapshotMigrationConfigs[].perSnapshotConfig.snap1[].documentBackfillConfig.podReplicas` — number of RFS backfill worker pods running in parallel.
   +  `documentBackfillConfig.maxShardSizeBytes` — the expected maximum shard size in bytes, used to auto-calculate ephemeral storage requirements (`ceil(2.5 * maxShardSizeBytes)`). Set it to match your largest shard so there is enough disk space for Lucene segment processing (default 80 GiB; `85899345920` bytes equals 80 GiB).

     If you created and staged the Solr backup yourself, use an externally managed snapshot instead of `createSnapshotConfig`:

     ```
     "snap1": {
       "config": {
         "externallyManagedSnapshotName": "BACKUP_NAME"
       },
       "repoName": "s3"
     }
     ```

     For an Amazon OpenSearch Serverless NextGen collection, set `authConfig.sigv4.service` to `aoss` instead of `es`, and add the migration IAM role (`eks-cluster-name-migrations-role`) as a principal in the collection’s data access policy. See [Getting started with the Workflow CLI](use-the-solution.md#getting-started) for the full target configuration.

1.  **Submit and monitor** the workflow:

   ```
   workflow submit
   workflow manage
   ```

   Use `workflow manage` to watch the run and approve any gated steps.

1.  **Validate** the document counts on the target after backfill completes:

   ```
   console clusters cat-indices --refresh
   ```

   Compare the document counts on the source and the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection to confirm completeness.
