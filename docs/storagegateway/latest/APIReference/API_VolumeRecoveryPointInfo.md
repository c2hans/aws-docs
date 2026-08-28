---
source_url: https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_VolumeRecoveryPointInfo.html
---

# VolumeRecoveryPointInfo
<a name="API_VolumeRecoveryPointInfo"></a>

Describes a storage volume recovery point object.

## Contents
<a name="API_VolumeRecoveryPointInfo_Contents"></a>

 ** VolumeARN **   <a name="StorageGateway-Type-VolumeRecoveryPointInfo-VolumeARN"></a>
The Amazon Resource Name (ARN) of the volume target.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 500.
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`
Required: No

 ** VolumeRecoveryPointTime **   <a name="StorageGateway-Type-VolumeRecoveryPointInfo-VolumeRecoveryPointTime"></a>
The time the recovery point was taken.
Type: String
Required: No

 ** VolumeSizeInBytes **   <a name="StorageGateway-Type-VolumeRecoveryPointInfo-VolumeSizeInBytes"></a>
The size of the volume in bytes.
Type: Long
Required: No

 ** VolumeUsageInBytes **   <a name="StorageGateway-Type-VolumeRecoveryPointInfo-VolumeUsageInBytes"></a>
The size of the data stored on the volume in bytes.
This value is not available for volumes created prior to May 13, 2015, until you store data on the volume.
Type: Long
Required: No

## See Also
<a name="API_VolumeRecoveryPointInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/VolumeRecoveryPointInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/VolumeRecoveryPointInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/VolumeRecoveryPointInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
