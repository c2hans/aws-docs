---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Snapshot.html
---

# Snapshot
<a name="API_Snapshot"></a>

Describes a snapshot.

## Contents
<a name="API_Snapshot_Contents"></a>

 ** availabilityZone **
The Availability Zone or Local Zone of the snapshot. For example, `us-west-1a` (Availability Zone) or `us-west-2-lax-1a` (Local Zone).
Type: String
Required: No

 ** completionDurationMinutes **
Only for snapshot copies created with time-based snapshot copy operations.
The completion duration requested for the time-based snapshot copy operation.
Type: Integer
Required: No

 ** completionTime **
The time stamp when the snapshot was completed.
Type: Timestamp
Required: No

 ** dataEncryptionKeyId **
The data encryption key identifier for the snapshot. This value is a unique identifier that corresponds to the data encryption key that was used to encrypt the original volume or snapshot copy. Because data encryption keys are inherited by volumes created from snapshots, and vice versa, if snapshots share the same data encryption key identifier, then they belong to the same volume/snapshot lineage. This parameter is only returned by [DescribeSnapshots](API_DescribeSnapshots.md).
Type: String
Required: No

 ** description **
The description for the snapshot.
Type: String
Required: No

 ** encrypted **
Indicates whether the snapshot is encrypted.
Type: Boolean
Required: No

 ** fullSnapshotSizeInBytes **
The full size of the snapshot, in bytes.
This is **not** the incremental size of the snapshot. This is the full snapshot size and represents the size of all the blocks that were written to the source volume at the time the snapshot was created.
Type: Long
Required: No

 ** kmsKeyId **
The Amazon Resource Name (ARN) of the AWS KMS key that was used to protect the volume encryption key for the parent volume.
Type: String
Required: No

 ** outpostArn **
The ARN of the Outpost on which the snapshot is stored. For more information, see [Amazon EBS local snapshots on Outposts](https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html) in the *Amazon EBS User Guide*.
Type: String
Required: No

 ** ownerAlias **
The AWS owner alias, from an Amazon-maintained list (`amazon`). This is not the user-configured AWS account alias set using the IAM console.
Type: String
Required: No

 ** ownerId **
The ID of the AWS account that owns the EBS snapshot.
Type: String
Required: No

 ** progress **
The progress of the snapshot, as a percentage.
Type: String
Required: No

 ** restoreExpiryTime **
Only for archived snapshots that are temporarily restored. Indicates the date and time when a temporarily restored snapshot will be automatically re-archived.
Type: Timestamp
Required: No

 ** snapshotId **
The ID of the snapshot. Each snapshot receives a unique identifier when it is created.
Type: String
Required: No

 ** sseType **
Reserved for future use.
Type: String
Valid Values: `sse-ebs | sse-kms | none`
Required: No

 ** startTime **
The time stamp when the snapshot was initiated.
Type: Timestamp
Required: No

 ** status **
The snapshot state.
Type: String
Valid Values: `pending | completed | error | recoverable | recovering`
Required: No

 ** statusMessage **
Encrypted Amazon EBS snapshots are copied asynchronously. If a snapshot copy operation fails (for example, if the proper AWS KMS permissions are not obtained) this field displays error state details to help you diagnose why the error occurred. This parameter is only returned by [DescribeSnapshots](API_DescribeSnapshots.md).
Type: String
Required: No

 ** storageTier **
The storage tier in which the snapshot is stored. `standard` indicates that the snapshot is stored in the standard snapshot storage tier and that it is ready for use. `archive` indicates that the snapshot is currently archived and that it must be restored before it can be used.
Type: String
Valid Values: `archive | standard`
Required: No

 ** TagSet.N **
Any tags assigned to the snapshot.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** transferType **
Only for snapshot copies.
Indicates whether the snapshot copy was created with a standard or time-based snapshot copy operation. Time-based snapshot copy operations complete within the completion duration specified in the request. Standard snapshot copy operations are completed on a best-effort basis.
+  `standard` - The snapshot copy was created with a standard snapshot copy operation.
+  `time-based` - The snapshot copy was created with a time-based snapshot copy operation.
Type: String
Valid Values: `time-based | standard`
Required: No

 ** volumeId **
The ID of the volume that was used to create the snapshot. Snapshots created by a copy snapshot operation have an arbitrary volume ID that you should not use for any purpose.
Type: String
Required: No

 ** volumeSize **
The size of the volume, in GiB.
Type: Integer
Required: No

## See Also
<a name="API_Snapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Snapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Snapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Snapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
