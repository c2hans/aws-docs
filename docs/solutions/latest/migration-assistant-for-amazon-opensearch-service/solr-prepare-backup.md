---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/solr-prepare-backup.html
---

# Prepare a Solr backup
<a name="solr-prepare-backup"></a>

Before you run the backfill workflow, choose how the Solr backup will be created:
+  **Workflow-managed backup creation** - Migration Assistant calls the Solr backup API during the workflow. Use this when the Migration Console can reach the Solr endpoint and you want the workflow to create the point-in-time backup.
+  **Externally managed backup** - You create the Solr backup yourself, stage it in Amazon S3, and configure the workflow with `externallyManagedSnapshotName`. Use this when you need custom backup commands, a narrower source-side collection set, or an already-created backup.

For workflow-managed backup creation, and for manual backups that write directly to Amazon S3, configure your Solr nodes with an S3 backup repository first. See [S3 repository prerequisites](solr-s3-prereqs.md). If you create a manual filesystem backup and sync it to Amazon S3 afterward, make sure the filesystem backup path is reachable by every Solr node that owns a shard.

## Workflow-managed Solr backup
<a name="solr-workflow-managed-backup"></a>

To let the workflow create the backup, configure the Solr source with an `endpoint`, a `snapshotInfo.repos` entry for the Amazon S3 location, and a snapshot `config.createSnapshotConfig` entry. The `CreateSnapshot` step detects Solr from the source endpoint, determines whether the source is SolrCloud or standalone, and auto-discovers collections or cores. The workflow configuration does not expose the manual `CreateSnapshot --solr-collections` option.

For SolrCloud, Migration Assistant backs up each discovered collection with the Collections API and writes it under `s3RepoPathUri/generatedSnapshotName/collection/`. For standalone Solr, Migration Assistant backs up each discovered core with the replication handler.

The workflow-managed path currently backs up every collection or core it discovers. `createSnapshotConfig.indexAllowlist` is an Elasticsearch/OpenSearch snapshot filter and does not select Solr collections. To migrate only some collections after a full Solr backup, use `metadataMigrationConfig.indexAllowlist` and `documentBackfillConfig.indexAllowlist` with exact collection or core names. The Solr backup reader does not apply `regex:` allowlist patterns. To avoid backing up the other collections at all in a workflow run, create an externally managed backup for only the desired collections and reference it with `externallyManagedSnapshotName`.

## Manual SolrCloud backup
<a name="solr-backup-cloud"></a>

If you create the backup yourself, trigger an asynchronous collection backup with the Collections API, then poll for completion with the `REQUESTSTATUS` action:

```
# Start the backup (asynchronous)
curl "http://SOLR_HOST:8983/solr/admin/collections?action=BACKUP\
name=SNAPSHOT_NAME\
collection=COLLECTION\
repository=s3\
location=SUBPATH\
async=ASYNC_IDwt=json"

# Poll until the request reports completed
curl "http://SOLR_HOST:8983/solr/admin/collections?action=REQUESTSTATUS\
requestid=ASYNC_IDwt=json"
```

For a SolrCloud source with multiple collections, create each collection backup under the same snapshot root. Use the collection name as the Solr backup `name` and put the shared snapshot name in the `location`, for example `location=SUBPATH/SNAPSHOT_NAMEname=COLLECTION`. Then configure `s3RepoPathUri` as `s3://BUCKET/SUBPATH` and `externallyManagedSnapshotName` as `SNAPSHOT_NAME`. The staged backup should have one top-level directory per collection under `SUBPATH/SNAPSHOT_NAME/`. This matches the layout that workflow-managed backups create and avoids Solr 8 incremental backup behavior that treats a backup name as belonging to one collection.

## Manual standalone Solr backup
<a name="solr-backup-standalone"></a>

If you create the backup yourself for standalone Solr, trigger the backup with the replication handler, then check status with the `details` command. Monitor `details.backup.status` until it reports `success`:

```
# Start the backup
curl "http://SOLR_HOST:8983/solr/CORE_NAME/replication?command=backup\
repository=s3\
location=SUBPATH\
name=SNAPSHOT_NAMEwt=json"

# Check status (look for details.backup.status: success)
curl "http://SOLR_HOST:8983/solr/CORE_NAME/replication?command=detailswt=json"
```

## Stage the backup in Amazon S3
<a name="solr-stage-s3"></a>

For externally managed backups, if you back up to a local path instead of directly to Amazon S3, copy the completed backup to your Amazon S3 bucket so the backfill workers can read it. Sync the parent directory that contains the `SNAPSHOT_NAME` backup directory:

```
aws s3 sync LOCAL_BACKUP_PATH s3://BUCKET/SUBPATH/
```

Record the resulting `s3://BUCKET/SUBPATH` parent location — you reference it in the workflow configuration as `s3RepoPathUri` (see [Configure and run the backfill workflow](solr-run-workflow.md)). Do not include `SNAPSHOT_NAME` in `s3RepoPathUri`; set that value separately with `externallyManagedSnapshotName`.

## Verify the Solr backup layout
<a name="solr-backup-layout"></a>

For Solr backfill, the workflow treats `s3RepoPathUri` as the repository parent and appends the generated snapshot name or `externallyManagedSnapshotName`. The Solr reader then discovers collections or cores under:

```
s3://BUCKET/SUBPATH/SNAPSHOT_NAME/
```

That snapshot root should contain one top-level directory per collection or core. Do not point `s3RepoPathUri` at a collection directory, a `zk_backup_N` directory, or an inner incremental-backup data directory.

Inside each collection directory, the reader accepts the common Solr backup layouts:
+ Numbered SolrCloud backups with `zk_backup_0/`, `backup_0.properties`, `shard_backup_metadata/`, and `index/`.
+ Successive backups to the same Solr backup location, such as `zk_backup_0/`, `zk_backup_1/`, `backup_0.properties`, and `backup_1.properties`. The reader uses the highest numbered `zk_backup_N` and latest shard metadata.
+ Older Solr 6/7 layouts with a bare `zk_backup/`, `backup.properties`, and `snapshot.shardN/` or direct `index/` data.
+ One-level nested Solr 8/9 incremental layouts, such as `collection/innerName/zk_backup_N/`. The reader detects the nested data directory automatically.

For metadata migration, the latest ZooKeeper backup for each collection must contain a config directory with one of `managed-schema.xml`, `managed-schema`, or `schema.xml`. If the schema file is missing, metadata migration falls back to an empty schema for that collection.
