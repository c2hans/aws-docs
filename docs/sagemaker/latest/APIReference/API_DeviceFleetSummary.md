---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeviceFleetSummary.html
---

# DeviceFleetSummary
<a name="API_DeviceFleetSummary"></a>

Summary of the device fleet.

## Contents
<a name="API_DeviceFleetSummary_Contents"></a>

 ** DeviceFleetArn **   <a name="sagemaker-Type-DeviceFleetSummary-DeviceFleetArn"></a>
Amazon Resource Name (ARN) of the device fleet.
Type: String
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:device-fleet/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** DeviceFleetName **   <a name="sagemaker-Type-DeviceFleetSummary-DeviceFleetName"></a>
Name of the device fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## See Also
<a name="API_DeviceFleetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeviceFleetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeviceFleetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeviceFleetSummary)
