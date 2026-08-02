---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TemplateAttributes.html
---

# TemplateAttributes
<a name="API_TemplateAttributes"></a>

Information about the template attributes.

## Contents
<a name="API_TemplateAttributes_Contents"></a>

 ** CustomAttributes **   <a name="connect-Type-TemplateAttributes-CustomAttributes"></a>
An object that specifies the custom attributes values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32767.
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Required: No

 ** CustomerProfileAttributes **   <a name="connect-Type-TemplateAttributes-CustomerProfileAttributes"></a>
An object that specifies the customer profile attributes values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template.
Type: String
Required: No

## See Also
<a name="API_TemplateAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TemplateAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TemplateAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TemplateAttributes)
