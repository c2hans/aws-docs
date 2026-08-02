---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_LatestDeviceJob.html
---

# LatestDeviceJob
<a name="API_LatestDeviceJob"></a>

Returns information about the latest device job.

## Contents
<a name="API_LatestDeviceJob_Contents"></a>

 ** ImageVersion **   <a name="panorama-Type-LatestDeviceJob-ImageVersion"></a>
The target version of the device software.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: No

 ** JobType **   <a name="panorama-Type-LatestDeviceJob-JobType"></a>
The job's type.
Type: String
Valid Values: `OTA | REBOOT`
Required: No

 ** Status **   <a name="panorama-Type-LatestDeviceJob-Status"></a>
Status of the latest device job.
Type: String
Valid Values: `PENDING | IN_PROGRESS | VERIFYING | REBOOTING | DOWNLOADING | COMPLETED | FAILED`
Required: No

## See Also
<a name="API_LatestDeviceJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/LatestDeviceJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/LatestDeviceJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/LatestDeviceJob)
