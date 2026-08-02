---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_DeviceJob.html
---

# DeviceJob
<a name="API_DeviceJob"></a>

A job that runs on a device.

## Contents
<a name="API_DeviceJob_Contents"></a>

 ** CreatedTime **   <a name="panorama-Type-DeviceJob-CreatedTime"></a>
When the job was created.
Type: Timestamp
Required: No

 ** DeviceId **   <a name="panorama-Type-DeviceJob-DeviceId"></a>
The ID of the target device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** DeviceName **   <a name="panorama-Type-DeviceJob-DeviceName"></a>
The name of the target device
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** JobId **   <a name="panorama-Type-DeviceJob-JobId"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** JobType **   <a name="panorama-Type-DeviceJob-JobType"></a>
The job's type.
Type: String
Valid Values: `OTA | REBOOT`
Required: No

## See Also
<a name="API_DeviceJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/DeviceJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/DeviceJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/DeviceJob)
