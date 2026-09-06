---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/build-from-snapshot.html
---

# 1. Building from a snapshot
<a name="build-from-snapshot"></a>

When you use the snapshot-restore approach, you copy data from the source Elasticsearch or OpenSearch cluster to target Amazon OpenSearch Service domain.

Broadly, the snapshot-restore process consists of the following steps:

1. Take a snapshot of the necessary data (indexes) from the existing cluster, and upload the snapshot to an S3 bucket.

1. Create an Amazon OpenSearch Service domain.

1. Give Amazon OpenSearch Service permissions to access the bucket, and give your user account permissions to work with snapshots. Create a snapshot repository and point that to your bucket.

1. Restore the snapshot on the Amazon OpenSearch Service domain.

1. Point your client applications to the Amazon OpenSearch Service domain.

1. Create Index State Management (ISM) policies for configuring retention (optional).

Snapshots are incremental. Therefore, a snapshot can be run and restored incrementally. By using snapshots, you can extract data in bulk as files on a storage system (for example, Amazon S3). You can then load these files in the target environment by using the `_restore` API operation. This eliminates the need for reindexing, which is time consuming, and it also reduces network traffic.

## Snapshot considerations
<a name="snapshot-considerations"></a>

When using the snapshot-restore approach, consider the following:
+ You can't search or reindex while an index is being restored. However, you can search and reindex an index while the snapshot is being taken.
+ The source and target Elasticsearch or OpenSearch versions must be compatible. A snapshot of an index that was created in:
  + 5.x can be restored to 6.x
  + 2.x can be restored to 5.x
  + 1.x can be restored to 2.x
+ Because this is a point-in-time restoration of the Elasticsearch or OpenSearch snapshot, subsequent changes in the source cluster won't be replicated to the target Amazon OpenSearch Service domain. You can stop ingestion of the data into the source Elasticsearch or OpenSearch cluster until the restoration is done, or you can repeat the snapshot restore process a few times. Because the snapshot is incremental, only the changes will be copied and restored in the target environment in less time than the first restore. After restoration is successfully finished, you point the ingestion applications to the Amazon OpenSearch Service domain.
+ Taking a snapshot includes, by default, a snapshot of the cluster state and all indexes. When migrating from Elasticsearch, you might need to create equivalent index lifecycle policies in the target environment using the ISM feature in OpenSearch. Elasticsearch Index Lifecycle Management (ILM) is not supported in Amazon OpenSearch Service.
+ You can't restore a snapshot to an earlier version of Elasticsearch or OpenSearch. For example, you can't restore a snapshot of version 7.10 to 7.9. Similarly, you can't restore snapshots from Elasticsearch 7.11 or later to an Amazon OpenSearch Service domain. If you have migrated your self-managed Elasticsearch environment to version 7.11 or later, you can use Logstash to load data from the Elasticsearch cluster and write it to the OpenSearch domain.
+ You export a snapshot to a designated storage location called a repository. Elasticsearch or OpenSearch creates a number of files in the repository. You can't modify or delete these files. Doing so might create inconsistencies or cause the restore process to fail.
