---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_Relationship.html
---

# Relationship
<a name="API_Relationship"></a>

An object that specifies a relationship with another component type.

## Contents
<a name="API_Relationship_Contents"></a>

 ** relationshipType **   <a name="tm-Type-Relationship-relationshipType"></a>
The type of the relationship.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

 ** targetComponentTypeId **   <a name="tm-Type-Relationship-targetComponentTypeId"></a>
The ID of the target component type associated with this relationship.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`
Required: No

## See Also
<a name="API_Relationship_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/Relationship)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/Relationship)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/Relationship)
