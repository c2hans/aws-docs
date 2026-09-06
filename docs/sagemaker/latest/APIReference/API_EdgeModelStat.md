---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EdgeModelStat.html
---

# EdgeModelStat
<a name="API_EdgeModelStat"></a>

Status of edge devices with this model.

## Contents
<a name="API_EdgeModelStat_Contents"></a>

 ** ActiveDeviceCount **   <a name="sagemaker-Type-EdgeModelStat-ActiveDeviceCount"></a>
The number of devices that have this model version, a heart beat, and are currently running.
Type: Long
Required: Yes

 ** ConnectedDeviceCount **   <a name="sagemaker-Type-EdgeModelStat-ConnectedDeviceCount"></a>
The number of devices that have this model version and have a heart beat.
Type: Long
Required: Yes

 ** ModelName **   <a name="sagemaker-Type-EdgeModelStat-ModelName"></a>
The name of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ModelVersion **   <a name="sagemaker-Type-EdgeModelStat-ModelVersion"></a>
The model version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\ \_\.]+`
Required: Yes

 ** OfflineDeviceCount **   <a name="sagemaker-Type-EdgeModelStat-OfflineDeviceCount"></a>
The number of devices that have this model version and do not have a heart beat.
Type: Long
Required: Yes

 ** SamplingDeviceCount **   <a name="sagemaker-Type-EdgeModelStat-SamplingDeviceCount"></a>
The number of devices with this model version and are producing sample data.
Type: Long
Required: Yes

## See Also
<a name="API_EdgeModelStat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EdgeModelStat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EdgeModelStat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EdgeModelStat)
