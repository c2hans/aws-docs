---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SnapshotDetail.html
---

# SnapshotDetail
<a name="API_SnapshotDetail"></a>

Describes the snapshot created from the imported disk.

## Contents
<a name="API_SnapshotDetail_Contents"></a>

 ** description **
A description for the snapshot.
Type: String
Required: No

 ** deviceName **
The block device mapping for the snapshot.
Type: String
Required: No

 ** diskImageSize **
The size of the disk in the snapshot, in GiB.
Type: Double
Required: No

 ** format **
The format of the disk image from which the snapshot is created.
Type: String
Required: No

 ** progress **
The percentage of progress for the task.
Type: String
Required: No

 ** snapshotId **
The snapshot ID of the disk being imported.
Type: String
Required: No

 ** status **
A brief status of the snapshot creation.
Type: String
Required: No

 ** statusMessage **
A detailed status message for the snapshot creation.
Type: String
Required: No

 ** url **
The URL used to access the disk image.
Type: String
Required: No

 ** userBucket **
The Amazon S3 bucket for the disk image.
Type: [UserBucketDetails](API_UserBucketDetails.md) object
Required: No

## See Also
<a name="API_SnapshotDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SnapshotDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SnapshotDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SnapshotDetail)
