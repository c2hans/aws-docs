---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SnapshotTaskDetail.html
---

# SnapshotTaskDetail
<a name="API_SnapshotTaskDetail"></a>

Details about the import snapshot task.

## Contents
<a name="API_SnapshotTaskDetail_Contents"></a>

 ** description **
The description of the disk image being imported.
Type: String
Required: No

 ** diskImageSize **
The size of the disk in the snapshot, in GiB.
Type: Double
Required: No

 ** encrypted **
Indicates whether the snapshot is encrypted.
Type: Boolean
Required: No

 ** format **
The format of the disk image from which the snapshot is created.
Type: String
Required: No

 ** kmsKeyId **
The identifier for the KMS key that was used to create the encrypted snapshot.
Type: String
Required: No

 ** progress **
The percentage of completion for the import snapshot task.
Type: String
Required: No

 ** snapshotId **
The snapshot ID of the disk being imported.
Type: String
Required: No

 ** status **
A brief status for the import snapshot task.
Type: String
Required: No

 ** statusMessage **
A detailed status message for the import snapshot task.
Type: String
Required: No

 ** url **
The URL of the disk image from which the snapshot is created.
Type: String
Required: No

 ** userBucket **
The Amazon S3 bucket for the disk image.
Type: [UserBucketDetails](API_UserBucketDetails.md) object
Required: No

## See Also
<a name="API_SnapshotTaskDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SnapshotTaskDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SnapshotTaskDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SnapshotTaskDetail)
