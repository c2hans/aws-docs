---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeviceSelectionConfig.html
---

# DeviceSelectionConfig
<a name="API_DeviceSelectionConfig"></a>

Contains information about the configurations of selected devices.

## Contents
<a name="API_DeviceSelectionConfig_Contents"></a>

 ** DeviceSubsetType **   <a name="sagemaker-Type-DeviceSelectionConfig-DeviceSubsetType"></a>
Type of device subsets to deploy to the current stage.
Type: String
Valid Values: `PERCENTAGE | SELECTION | NAMECONTAINS`
Required: Yes

 ** DeviceNameContains **   <a name="sagemaker-Type-DeviceSelectionConfig-DeviceNameContains"></a>
A filter to select devices with names containing this name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** DeviceNames **   <a name="sagemaker-Type-DeviceSelectionConfig-DeviceNames"></a>
List of devices chosen to deploy.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** Percentage **   <a name="sagemaker-Type-DeviceSelectionConfig-Percentage"></a>
Percentage of devices in the fleet to deploy to the current stage.
Type: Integer
Valid Range: Maximum value of 100.
Required: No

## See Also
<a name="API_DeviceSelectionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeviceSelectionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeviceSelectionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeviceSelectionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
