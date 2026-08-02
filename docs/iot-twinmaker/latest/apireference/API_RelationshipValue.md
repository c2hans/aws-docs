---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_RelationshipValue.html
---

# RelationshipValue
<a name="API_RelationshipValue"></a>

A value that associates a component and an entity.

## Contents
<a name="API_RelationshipValue_Contents"></a>

 ** targetComponentName **   <a name="tm-Type-RelationshipValue-targetComponentName"></a>
The name of the target component associated with the relationship value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** targetEntityId **   <a name="tm-Type-RelationshipValue-targetEntityId"></a>
The ID of the target entity associated with this relationship value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
Required: No

## See Also
<a name="API_RelationshipValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/RelationshipValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/RelationshipValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/RelationshipValue)
