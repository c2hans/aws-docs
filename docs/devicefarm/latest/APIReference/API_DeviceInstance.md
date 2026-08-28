---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeviceInstance.html
---

# DeviceInstance
<a name="API_DeviceInstance"></a>

Represents the device instance.

## Contents
<a name="API_DeviceInstance_Contents"></a>

 ** arn **   <a name="devicefarm-Type-DeviceInstance-arn"></a>
The Amazon Resource Name (ARN) of the device instance.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** deviceArn **   <a name="devicefarm-Type-DeviceInstance-deviceArn"></a>
The ARN of the device.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** instanceProfile **   <a name="devicefarm-Type-DeviceInstance-instanceProfile"></a>
A object that contains information about the instance profile.
Type: [InstanceProfile](API_InstanceProfile.md) object
Required: No

 ** labels **   <a name="devicefarm-Type-DeviceInstance-labels"></a>
An array of strings that describe the device instance.
Type: Array of strings
Required: No

 ** status **   <a name="devicefarm-Type-DeviceInstance-status"></a>
The status of the device instance. Valid values are listed here.
Type: String
Valid Values: `IN_USE | PREPARING | AVAILABLE | NOT_AVAILABLE`
Required: No

 ** udid **   <a name="devicefarm-Type-DeviceInstance-udid"></a>
Unique device identifier for the device instance.
Type: String
Required: No

## See Also
<a name="API_DeviceInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/DeviceInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/DeviceInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/DeviceInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
