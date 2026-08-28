---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ComponentSummary.html
---

# ComponentSummary
<a name="API_ComponentSummary"></a>

An object that returns information about a component summary.

## Contents
<a name="API_ComponentSummary_Contents"></a>

 ** componentName **   <a name="tm-Type-ComponentSummary-componentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\-0-9]+`
Required: Yes

 ** componentTypeId **   <a name="tm-Type-ComponentSummary-componentTypeId"></a>
The ID of the component type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`
Required: Yes

 ** status **   <a name="tm-Type-ComponentSummary-status"></a>
The status of the component type.
Type: [Status](API_Status.md) object
Required: Yes

 ** componentPath **   <a name="tm-Type-ComponentSummary-componentPath"></a>
This string specifies the path to the composite component, starting from the top-level component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z_\-0-9/]+`
Required: No

 ** definedIn **   <a name="tm-Type-ComponentSummary-definedIn"></a>
The name of the property definition set in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

 ** description **   <a name="tm-Type-ComponentSummary-description"></a>
The description of the component request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** propertyGroups **   <a name="tm-Type-ComponentSummary-propertyGroups"></a>
The property groups.
Type: String to [ComponentPropertyGroupResponse](API_ComponentPropertyGroupResponse.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** syncSource **   <a name="tm-Type-ComponentSummary-syncSource"></a>
The `syncSource` of the sync job, if this entity was created by a sync job.
Type: String
Pattern: `[a-zA-Z_0-9]+`
Required: No

## See Also
<a name="API_ComponentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ComponentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ComponentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ComponentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
