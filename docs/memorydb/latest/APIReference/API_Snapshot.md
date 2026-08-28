---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Snapshot.html
---

# Snapshot
<a name="API_Snapshot"></a>

Represents a copy of an entire cluster as of the time when the snapshot was taken.

## Contents
<a name="API_Snapshot_Contents"></a>

 ** ARN **   <a name="MemoryDB-Type-Snapshot-ARN"></a>
The ARN (Amazon Resource Name) of the snapshot.
Type: String
Required: No

 ** ClusterConfiguration **   <a name="MemoryDB-Type-Snapshot-ClusterConfiguration"></a>
The configuration of the cluster from which the snapshot was taken
Type: [ClusterConfiguration](API_ClusterConfiguration.md) object
Required: No

 ** DataTiering **   <a name="MemoryDB-Type-Snapshot-DataTiering"></a>
Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes. For more information, see [Data tiering](https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html).
Type: String
Valid Values: `true | false`
Required: No

 ** KmsKeyId **   <a name="MemoryDB-Type-Snapshot-KmsKeyId"></a>
The ID of the KMS key used to encrypt the snapshot.
Type: String
Required: No

 ** Name **   <a name="MemoryDB-Type-Snapshot-Name"></a>
The name of the snapshot
Type: String
Required: No

 ** Source **   <a name="MemoryDB-Type-Snapshot-Source"></a>
Indicates whether the snapshot is from an automatic backup (automated) or was created manually (manual).
Type: String
Required: No

 ** Status **   <a name="MemoryDB-Type-Snapshot-Status"></a>
The status of the snapshot. Valid values: creating \| available \| restoring \| copying \| deleting.
Type: String
Required: No

## See Also
<a name="API_Snapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/Snapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/Snapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/Snapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
