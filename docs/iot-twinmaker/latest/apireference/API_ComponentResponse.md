---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ComponentResponse.html
---

# ComponentResponse
<a name="API_ComponentResponse"></a>

An object that returns information about a component type create or update request.

## Contents
<a name="API_ComponentResponse_Contents"></a>

 ** areAllCompositeComponentsReturned **   <a name="tm-Type-ComponentResponse-areAllCompositeComponentsReturned"></a>
This flag notes whether all `compositeComponents` are returned in the API response.
Type: Boolean
Required: No

 ** areAllPropertiesReturned **   <a name="tm-Type-ComponentResponse-areAllPropertiesReturned"></a>
This flag notes whether all properties of the component are returned in the API response. The maximum number of properties returned is 800.
Type: Boolean
Required: No

 ** componentName **   <a name="tm-Type-ComponentResponse-componentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** componentTypeId **   <a name="tm-Type-ComponentResponse-componentTypeId"></a>
The ID of the component type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`
Required: No

 ** compositeComponents **   <a name="tm-Type-ComponentResponse-compositeComponents"></a>
This lists objects that contain information about the `compositeComponents`.
Type: String to [ComponentSummary](API_ComponentSummary.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** definedIn **   <a name="tm-Type-ComponentResponse-definedIn"></a>
The name of the property definition set in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

 ** description **   <a name="tm-Type-ComponentResponse-description"></a>
The description of the component type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** properties **   <a name="tm-Type-ComponentResponse-properties"></a>
An object that maps strings to the properties to set in the component type. Each string in the mapping must be unique to this object.
Type: String to [PropertyResponse](API_PropertyResponse.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** propertyGroups **   <a name="tm-Type-ComponentResponse-propertyGroups"></a>
The property groups.
Type: String to [ComponentPropertyGroupResponse](API_ComponentPropertyGroupResponse.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** status **   <a name="tm-Type-ComponentResponse-status"></a>
The status of the component type.
Type: [Status](API_Status.md) object
Required: No

 ** syncSource **   <a name="tm-Type-ComponentResponse-syncSource"></a>
The syncSource of the sync job, if this entity was created by a sync job.
Type: String
Pattern: `[a-zA-Z_0-9]+`
Required: No

## See Also
<a name="API_ComponentResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ComponentResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ComponentResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ComponentResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
