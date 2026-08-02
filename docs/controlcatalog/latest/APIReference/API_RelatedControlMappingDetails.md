---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_RelatedControlMappingDetails.html
---

# RelatedControlMappingDetails
<a name="API_RelatedControlMappingDetails"></a>

A structure that describes a control's relationship status with other controls.

## Contents
<a name="API_RelatedControlMappingDetails_Contents"></a>

 ** RelationType **   <a name="controlcatalog-Type-RelatedControlMappingDetails-RelationType"></a>
Returns an enumerated value that represents the relationship between two or more controls.
Type: String
Valid Values: `COMPLEMENTARY | ALTERNATIVE | MUTUALLY_EXCLUSIVE`
Required: Yes

 ** ControlArn **   <a name="controlcatalog-Type-RelatedControlMappingDetails-ControlArn"></a>
The unique identifier of a control.
Type: String
Length Constraints: Minimum length of 34. Maximum length of 2048.
Pattern: `arn:(aws(?:[-a-z]*)?):(controlcatalog|controltower):[a-zA-Z0-9-]*::control/[0-9a-zA-Z_\-]+`
Required: No

## See Also
<a name="API_RelatedControlMappingDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/RelatedControlMappingDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/RelatedControlMappingDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/RelatedControlMappingDetails)
