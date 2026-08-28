---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SnapshotInfo.html
---

# SnapshotInfo
<a name="API_SnapshotInfo"></a>

Information about a snapshot.

## Contents
<a name="API_SnapshotInfo_Contents"></a>

 ** availabilityZone **
The Availability Zone or Local Zone of the snapshots. For example, `us-west-1a` (Availability Zone) or `us-west-2-lax-1a` (Local Zone).
Type: String
Required: No

 ** description **
Description specified by the CreateSnapshotRequest that has been applied to all snapshots.
Type: String
Required: No

 ** encrypted **
Indicates whether the snapshot is encrypted.
Type: Boolean
Required: No

 ** outpostArn **
The ARN of the Outpost on which the snapshot is stored. For more information, see [Amazon EBS local snapshots on Outposts](https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html) in the *Amazon EBS User Guide*.
Type: String
Required: No

 ** ownerId **
Account id used when creating this snapshot.
Type: String
Required: No

 ** progress **
Progress this snapshot has made towards completing.
Type: String
Required: No

 ** snapshotId **
Snapshot id that can be used to describe this snapshot.
Type: String
Required: No

 ** sseType **
Reserved for future use.
Type: String
Valid Values: `sse-ebs | sse-kms | none`
Required: No

 ** startTime **
Time this snapshot was started. This is the same for all snapshots initiated by the same request.
Type: Timestamp
Required: No

 ** state **
Current state of the snapshot.
Type: String
Valid Values: `pending | completed | error | recoverable | recovering`
Required: No

 ** TagSet.N **
Tags associated with this snapshot.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** volumeId **
Source volume from which this snapshot was created.
Type: String
Required: No

 ** volumeSize **
Size of the volume from which this snapshot was created.
Type: Integer
Required: No

## See Also
<a name="API_SnapshotInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SnapshotInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SnapshotInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SnapshotInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
