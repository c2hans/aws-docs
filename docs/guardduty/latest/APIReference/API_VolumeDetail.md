---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_VolumeDetail.html
---

# VolumeDetail
<a name="API_VolumeDetail"></a>

Contains EBS volume details.

## Contents
<a name="API_VolumeDetail_Contents"></a>

 ** deviceName **   <a name="guardduty-Type-VolumeDetail-deviceName"></a>
The device name for the EBS volume.
Type: String
Required: No

 ** encryptionType **   <a name="guardduty-Type-VolumeDetail-encryptionType"></a>
EBS volume encryption type.
Type: String
Required: No

 ** kmsKeyArn **   <a name="guardduty-Type-VolumeDetail-kmsKeyArn"></a>
KMS key ARN used to encrypt the EBS volume.
Type: String
Required: No

 ** snapshotArn **   <a name="guardduty-Type-VolumeDetail-snapshotArn"></a>
Snapshot ARN of the EBS volume.
Type: String
Required: No

 ** volumeArn **   <a name="guardduty-Type-VolumeDetail-volumeArn"></a>
EBS volume ARN information.
Type: String
Required: No

 ** volumeSizeInGB **   <a name="guardduty-Type-VolumeDetail-volumeSizeInGB"></a>
EBS volume size in GB.
Type: Integer
Required: No

 ** volumeType **   <a name="guardduty-Type-VolumeDetail-volumeType"></a>
The EBS volume type.
Type: String
Required: No

## See Also
<a name="API_VolumeDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/VolumeDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/VolumeDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/VolumeDetail)
