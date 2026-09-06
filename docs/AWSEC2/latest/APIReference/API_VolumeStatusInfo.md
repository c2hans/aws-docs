---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VolumeStatusInfo.html
---

# VolumeStatusInfo
<a name="API_VolumeStatusInfo"></a>

Describes the status of a volume.

## Contents
<a name="API_VolumeStatusInfo_Contents"></a>

 ** Details.N **
The details of the volume status.
Type: Array of [VolumeStatusDetails](API_VolumeStatusDetails.md) objects
Required: No

 ** status **
The status of the volume.
Type: String
Valid Values: `ok | impaired | insufficient-data | warning`
Required: No

## See Also
<a name="API_VolumeStatusInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VolumeStatusInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VolumeStatusInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VolumeStatusInfo)
