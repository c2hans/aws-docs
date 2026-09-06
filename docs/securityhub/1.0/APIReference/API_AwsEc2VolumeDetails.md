---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2VolumeDetails.html
---

# AwsEc2VolumeDetails
<a name="API_AwsEc2VolumeDetails"></a>

Details about an EC2 volume.

## Contents
<a name="API_AwsEc2VolumeDetails_Contents"></a>

 ** Attachments **   <a name="securityhub-Type-AwsEc2VolumeDetails-Attachments"></a>
The volume attachments.
Type: Array of [AwsEc2VolumeAttachment](API_AwsEc2VolumeAttachment.md) objects
Required: No

 ** CreateTime **   <a name="securityhub-Type-AwsEc2VolumeDetails-CreateTime"></a>
Indicates when the volume was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** DeviceName **   <a name="securityhub-Type-AwsEc2VolumeDetails-DeviceName"></a>
The device name for the volume that is attached to the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Encrypted **   <a name="securityhub-Type-AwsEc2VolumeDetails-Encrypted"></a>
Specifies whether the volume is encrypted.
Type: Boolean
Required: No

 ** KmsKeyId **   <a name="securityhub-Type-AwsEc2VolumeDetails-KmsKeyId"></a>
The ARN of the AWS KMS key that was used to protect the volume encryption key for the volume.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Size **   <a name="securityhub-Type-AwsEc2VolumeDetails-Size"></a>
The size of the volume, in GiBs.
Type: Integer
Required: No

 ** SnapshotId **   <a name="securityhub-Type-AwsEc2VolumeDetails-SnapshotId"></a>
The snapshot from which the volume was created.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsEc2VolumeDetails-Status"></a>
The volume state. Valid values are as follows:
+  `available`
+  `creating`
+  `deleted`
+  `deleting`
+  `error`
+  `in-use`
Type: String
Pattern: `.*\S.*`
Required: No

 ** VolumeId **   <a name="securityhub-Type-AwsEc2VolumeDetails-VolumeId"></a>
The ID of the volume.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VolumeScanStatus **   <a name="securityhub-Type-AwsEc2VolumeDetails-VolumeScanStatus"></a>
Indicates whether the volume was scanned or skipped.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VolumeType **   <a name="securityhub-Type-AwsEc2VolumeDetails-VolumeType"></a>
The volume type.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2VolumeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2VolumeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2VolumeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2VolumeDetails)
