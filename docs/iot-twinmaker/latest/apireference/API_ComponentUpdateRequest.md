---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ComponentUpdateRequest.html
---

# ComponentUpdateRequest
<a name="API_ComponentUpdateRequest"></a>

The component update request.

## Contents
<a name="API_ComponentUpdateRequest_Contents"></a>

 ** componentTypeId **   <a name="tm-Type-ComponentUpdateRequest-componentTypeId"></a>
The ID of the component type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`
Required: No

 ** description **   <a name="tm-Type-ComponentUpdateRequest-description"></a>
The description of the component type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** propertyGroupUpdates **   <a name="tm-Type-ComponentUpdateRequest-propertyGroupUpdates"></a>
The property group updates.
Type: String to [ComponentPropertyGroupRequest](API_ComponentPropertyGroupRequest.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** propertyUpdates **   <a name="tm-Type-ComponentUpdateRequest-propertyUpdates"></a>
An object that maps strings to the properties to set in the component type update. Each string in the mapping must be unique to this object.
Type: String to [PropertyRequest](API_PropertyRequest.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** updateType **   <a name="tm-Type-ComponentUpdateRequest-updateType"></a>
The update type of the component update request.
Type: String
Valid Values: `CREATE | UPDATE | DELETE`
Required: No

## See Also
<a name="API_ComponentUpdateRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ComponentUpdateRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ComponentUpdateRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ComponentUpdateRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
