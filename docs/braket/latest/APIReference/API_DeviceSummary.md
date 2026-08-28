---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_DeviceSummary.html
---

# DeviceSummary
<a name="API_DeviceSummary"></a>

Includes information about the device.

## Contents
<a name="API_DeviceSummary_Contents"></a>

 ** deviceArn **   <a name="braket-Type-DeviceSummary-deviceArn"></a>
The ARN of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** deviceName **   <a name="braket-Type-DeviceSummary-deviceName"></a>
The name of the device.
Type: String
Required: Yes

 ** deviceStatus **   <a name="braket-Type-DeviceSummary-deviceStatus"></a>
The status of the device.
Type: String
Valid Values: `ONLINE | OFFLINE | RETIRED`
Required: Yes

 ** deviceType **   <a name="braket-Type-DeviceSummary-deviceType"></a>
The type of the device.
Type: String
Valid Values: `QPU | SIMULATOR`
Required: Yes

 ** providerName **   <a name="braket-Type-DeviceSummary-providerName"></a>
The provider of the device.
Type: String
Required: Yes

## See Also
<a name="API_DeviceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/DeviceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/DeviceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/DeviceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
