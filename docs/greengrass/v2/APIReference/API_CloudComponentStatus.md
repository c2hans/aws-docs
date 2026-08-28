---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CloudComponentStatus.html
---

# CloudComponentStatus
<a name="API_CloudComponentStatus"></a>

Contains the status of a component version in the AWS IoT Greengrass service.

## Contents
<a name="API_CloudComponentStatus_Contents"></a>

 ** componentState **   <a name="greengrassv2-Type-CloudComponentStatus-componentState"></a>
The state of the component version.
Type: String
Valid Values: `REQUESTED | INITIATED | DEPLOYABLE | FAILED | DEPRECATED`
Required: No

 ** errors **   <a name="greengrassv2-Type-CloudComponentStatus-errors"></a>
A dictionary of errors that communicate why the component version is in an error state. For example, if AWS IoT Greengrass can't access an artifact for the component version, then `errors` contains the artifact's URI as a key, and the error message as the value for that key.
Type: String to string map
Key Length Constraints: Minimum length of 1.
Value Length Constraints: Minimum length of 1.
Required: No

 ** message **   <a name="greengrassv2-Type-CloudComponentStatus-message"></a>
A message that communicates details, such as errors, about the status of the component version.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** vendorGuidance **   <a name="greengrassv2-Type-CloudComponentStatus-vendorGuidance"></a>
The vendor guidance state for the component version. This state indicates whether the component version has any issues that you should consider before you deploy it. The vendor guidance state can be:
+  `ACTIVE` – This component version is available and recommended for use.
+  `DISCONTINUED` – This component version has been discontinued by its publisher. You can deploy this component version, but we recommend that you use a different version of this component.
+  `DELETED` – This component version has been deleted by its publisher, so you can't deploy it. If you have any existing deployments that specify this component version, those deployments will fail.
Type: String
Valid Values: `ACTIVE | DISCONTINUED | DELETED`
Required: No

 ** vendorGuidanceMessage **   <a name="greengrassv2-Type-CloudComponentStatus-vendorGuidanceMessage"></a>
A message that communicates details about the vendor guidance state of the component version. This message communicates why a component version is discontinued or deleted.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_CloudComponentStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/CloudComponentStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/CloudComponentStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/CloudComponentStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
