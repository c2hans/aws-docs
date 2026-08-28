---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SnapshotTierStatus.html
---

# SnapshotTierStatus
<a name="API_SnapshotTierStatus"></a>

Provides information about a snapshot's storage tier.

## Contents
<a name="API_SnapshotTierStatus_Contents"></a>

 ** archivalCompleteTime **
The date and time when the last archive process was completed.
Type: Timestamp
Required: No

 ** lastTieringOperationStatus **
The status of the last archive or restore process.
Type: String
Valid Values: `archival-in-progress | archival-completed | archival-failed | temporary-restore-in-progress | temporary-restore-completed | temporary-restore-failed | permanent-restore-in-progress | permanent-restore-completed | permanent-restore-failed`
Required: No

 ** lastTieringOperationStatusDetail **
A message describing the status of the last archive or restore process.
Type: String
Required: No

 ** lastTieringProgress **
The progress of the last archive or restore process, as a percentage.
Type: Integer
Required: No

 ** lastTieringStartTime **
The date and time when the last archive or restore process was started.
Type: Timestamp
Required: No

 ** ownerId **
The ID of the AWS account that owns the snapshot.
Type: String
Required: No

 ** restoreExpiryTime **
Only for archived snapshots that are temporarily restored. Indicates the date and time when a temporarily restored snapshot will be automatically re-archived.
Type: Timestamp
Required: No

 ** snapshotId **
The ID of the snapshot.
Type: String
Required: No

 ** status **
The state of the snapshot.
Type: String
Valid Values: `pending | completed | error | recoverable | recovering`
Required: No

 ** storageTier **
The storage tier in which the snapshot is stored. `standard` indicates that the snapshot is stored in the standard snapshot storage tier and that it is ready for use. `archive` indicates that the snapshot is currently archived and that it must be restored before it can be used.
Type: String
Valid Values: `archive | standard`
Required: No

 ** TagSet.N **
The tags that are assigned to the snapshot.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** volumeId **
The ID of the volume from which the snapshot was created.
Type: String
Required: No

## See Also
<a name="API_SnapshotTierStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SnapshotTierStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SnapshotTierStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SnapshotTierStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
