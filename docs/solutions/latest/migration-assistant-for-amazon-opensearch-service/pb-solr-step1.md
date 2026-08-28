---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-solr-step1.html
---

# Step 1: Create an Apache Solr backup and sync it to Amazon S3
<a name="pb-solr-step1"></a>

First, stop or pause writes to the Apache Solr source so the backup is a consistent point-in-time copy. This playbook shows the externally managed backup path: you create a backup using the API for your deployment topology, write it to a path that the Migration Assistant can later read, and sync that path to your Amazon S3 migration bucket.

**Note**
Migration Assistant can also create the Solr backup during the workflow when the Solr endpoint is reachable from the Migration Console and the Solr S3 backup repository is configured. That path auto-discovers all collections or cores. If you want to use workflow-managed backup creation, skip the manual `curl` commands here and use the `createSnapshotConfig` form in [Step 2](pb-solr-step2.md).

 **SolrCloud.** Trigger an asynchronous collection backup, then poll for completion before continuing:

```
curl "http://<SOLR_HOST>:<SOLR_PORT>/solr/admin/collections?action=BACKUP&name=<BACKUP_NAME>&collection=<COLLECTION>&location=/path/to/backup&async=backup-1"

curl "http://<SOLR_HOST>:<SOLR_PORT>/solr/admin/collections?action=REQUESTSTATUS&requestid=backup-1&wt=json"
```

Wait until the `REQUESTSTATUS` response reports the backup as completed before moving on.

For multiple SolrCloud collections, repeat the backup request for each collection under one shared snapshot root. Use the collection name as the Solr backup `name` and include the shared backup name in the `location`, for example `location=/path/to/backup/<BACKUP_NAME>&name=<COLLECTION>`. After sync, the Amazon S3 path should contain one top-level directory per collection under `<BACKUP_NAME>/`, and the workflow should set `s3RepoPathUri` to the parent path and `externallyManagedSnapshotName` to `<BACKUP_NAME>`.

 **Standalone (single-core) Solr.** Trigger a replication-handler backup, then confirm it finished:

```
curl "http://<SOLR_HOST>:<SOLR_PORT>/solr/<CORE>/replication?command=backup&name=<BACKUP_NAME>&location=/path/to/backup"

curl "http://<SOLR_HOST>:<SOLR_PORT>/solr/<CORE>/replication?command=details&wt=json"
```

The `details` response includes a `backup` section that reports the status of the most recent backup. Wait until it reports success.

**Note**
For SolrCloud, the backup `location` must be a path that is reachable from every node that holds a shard — typically a shared filesystem mounted on all nodes, or an Amazon S3-backed backup repository configured in `solr.xml`. A backup written to local disk on a single node is incomplete for a multi-node collection.

After the backup completes, sync the parent backup directory to your Amazon S3 migration bucket so RFS can read it. The synced directory should contain the `<BACKUP_NAME>` directory:

```
aws s3 sync /path/to/backup s3://<BUCKET>/solr-backup/
```

You can use the default Migration Assistant bucket (`s3://migrations-default-<ACCOUNT_ID>-<STAGE>-<REGION>`) or any bucket the migration IAM role can read. Record the resulting parent Amazon S3 URI — you supply it as `s3RepoPathUri` in the next step. The workflow appends `externallyManagedSnapshotName`, so do not include `<BACKUP_NAME>` in `s3RepoPathUri`.

Before configuring the workflow, check the S3 layout:

```
aws s3 ls s3://<BUCKET>/solr-backup/<BACKUP_NAME>/
```

The listing should show collection or core directories, not `zk_backup_0/` directly. Inside each collection directory, RFS can read numbered `zk_backup_N/` backups, older bare `zk_backup/` backups, and one-level nested Solr 8/9 incremental layouts. The latest ZooKeeper backup for each collection must include `managed-schema.xml`, `managed-schema`, or `schema.xml` under `configs/<CONFIGSET>/` so metadata migration can translate the schema.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
