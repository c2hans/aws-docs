---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_EntityPropertyReference.html
---

# EntityPropertyReference
<a name="API_EntityPropertyReference"></a>

An object that uniquely identifies an entity property.

## Contents
<a name="API_EntityPropertyReference_Contents"></a>

 ** propertyName **   <a name="tm-Type-EntityPropertyReference-propertyName"></a>
The name of the property.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\-0-9]+`
Required: Yes

 ** componentName **   <a name="tm-Type-EntityPropertyReference-componentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** componentPath **   <a name="tm-Type-EntityPropertyReference-componentPath"></a>
This string specifies the path to the composite component, starting from the top-level component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z_\-0-9/]+`
Required: No

 ** entityId **   <a name="tm-Type-EntityPropertyReference-entityId"></a>
The ID of the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
Required: No

 ** externalIdProperty **   <a name="tm-Type-EntityPropertyReference-externalIdProperty"></a>
A mapping of external IDs to property names. External IDs uniquely identify properties from external data stores.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `.*`
Required: No

## See Also
<a name="API_EntityPropertyReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/EntityPropertyReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/EntityPropertyReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/EntityPropertyReference)
