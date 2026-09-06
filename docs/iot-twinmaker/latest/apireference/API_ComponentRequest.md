---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ComponentRequest.html
---

# ComponentRequest
<a name="API_ComponentRequest"></a>

An object that sets information about a component type create or update request.

## Contents
<a name="API_ComponentRequest_Contents"></a>

 ** componentTypeId **   <a name="tm-Type-ComponentRequest-componentTypeId"></a>
The ID of the component type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`
Required: No

 ** description **   <a name="tm-Type-ComponentRequest-description"></a>
The description of the component request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** properties **   <a name="tm-Type-ComponentRequest-properties"></a>
An object that maps strings to the properties to set in the component type. Each string in the mapping must be unique to this object.
Type: String to [PropertyRequest](API_PropertyRequest.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** propertyGroups **   <a name="tm-Type-ComponentRequest-propertyGroups"></a>
The property groups.
Type: String to [ComponentPropertyGroupRequest](API_ComponentPropertyGroupRequest.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

## See Also
<a name="API_ComponentRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ComponentRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ComponentRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ComponentRequest)
