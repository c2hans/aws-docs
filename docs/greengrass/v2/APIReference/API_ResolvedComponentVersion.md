---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ResolvedComponentVersion.html
---

# ResolvedComponentVersion
<a name="API_ResolvedComponentVersion"></a>

Contains information about a component version that is compatible to run on a Greengrass core device.

## Contents
<a name="API_ResolvedComponentVersion_Contents"></a>

 ** arn **   <a name="greengrassv2-Type-ResolvedComponentVersion-arn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the component version.
Type: String
Pattern: `arn:[^:]*:greengrass:[^:]*:(aws|[0-9]+):components:[^:]+:versions:[^:]+`
Required: No

 ** componentName **   <a name="greengrassv2-Type-ResolvedComponentVersion-componentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** componentVersion **   <a name="greengrassv2-Type-ResolvedComponentVersion-componentVersion"></a>
The version of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** message **   <a name="greengrassv2-Type-ResolvedComponentVersion-message"></a>
A message that communicates details about the vendor guidance state of the component version. This message communicates why a component version is discontinued or deleted.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** recipe **   <a name="greengrassv2-Type-ResolvedComponentVersion-recipe"></a>
The recipe of the component version.
Type: Base64-encoded binary data object
Required: No

 ** vendorGuidance **   <a name="greengrassv2-Type-ResolvedComponentVersion-vendorGuidance"></a>
The vendor guidance state for the component version. This state indicates whether the component version has any issues that you should consider before you deploy it. The vendor guidance state can be:
+  `ACTIVE` – This component version is available and recommended for use.
+  `DISCONTINUED` – This component version has been discontinued by its publisher. You can deploy this component version, but we recommend that you use a different version of this component.
+  `DELETED` – This component version has been deleted by its publisher, so you can't deploy it. If you have any existing deployments that specify this component version, those deployments will fail.
Type: String
Valid Values: `ACTIVE | DISCONTINUED | DELETED`
Required: No

## See Also
<a name="API_ResolvedComponentVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/ResolvedComponentVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/ResolvedComponentVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/ResolvedComponentVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
