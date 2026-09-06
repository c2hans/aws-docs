---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CompositeComponentRequest.html
---

# CompositeComponentRequest
<a name="API_CompositeComponentRequest"></a>

An object that sets information about the composite component update request.

## Contents
<a name="API_CompositeComponentRequest_Contents"></a>

 ** description **   <a name="tm-Type-CompositeComponentRequest-description"></a>
The description of the component type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** properties **   <a name="tm-Type-CompositeComponentRequest-properties"></a>
This is an object that maps strings to the properties to set in the component type. Each string in the mapping must be unique to this object.
Type: String to [PropertyRequest](API_PropertyRequest.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** propertyGroups **   <a name="tm-Type-CompositeComponentRequest-propertyGroups"></a>
The property groups.
Type: String to [ComponentPropertyGroupRequest](API_ComponentPropertyGroupRequest.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

## See Also
<a name="API_CompositeComponentRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/CompositeComponentRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/CompositeComponentRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/CompositeComponentRequest)
