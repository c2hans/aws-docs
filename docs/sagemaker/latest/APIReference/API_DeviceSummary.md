---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeviceSummary.html
---

# DeviceSummary
<a name="API_DeviceSummary"></a>

Summary of the device.

## Contents
<a name="API_DeviceSummary_Contents"></a>

 ** DeviceArn **   <a name="sagemaker-Type-DeviceSummary-DeviceArn"></a>
Amazon Resource Name (ARN) of the device.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:[a-z\-]*:[a-z\-]*:\d{12}:[a-z\-]*/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** DeviceName **   <a name="sagemaker-Type-DeviceSummary-DeviceName"></a>
The unique identifier of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** AgentVersion **   <a name="sagemaker-Type-DeviceSummary-AgentVersion"></a>
Edge Manager agent version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\ \_\.]+`
Required: No

 ** Description **   <a name="sagemaker-Type-DeviceSummary-Description"></a>
A description of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[-a-zA-Z0-9_.,;:! ]*`
Required: No

 ** DeviceFleetName **   <a name="sagemaker-Type-DeviceSummary-DeviceFleetName"></a>
The name of the fleet the device belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** IotThingName **   <a name="sagemaker-Type-DeviceSummary-IotThingName"></a>
The AWS Internet of Things (IoT) object thing name associated with the device..
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** LatestHeartbeat **   <a name="sagemaker-Type-DeviceSummary-LatestHeartbeat"></a>
The last heartbeat received from the device.
Type: Timestamp
Required: No

 ** Models **   <a name="sagemaker-Type-DeviceSummary-Models"></a>
Models on the device.
Type: Array of [EdgeModelSummary](API_EdgeModelSummary.md) objects
Required: No

 ** RegistrationTime **   <a name="sagemaker-Type-DeviceSummary-RegistrationTime"></a>
The timestamp of the last registration or de-reregistration.
Type: Timestamp
Required: No

## See Also
<a name="API_DeviceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeviceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeviceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeviceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
