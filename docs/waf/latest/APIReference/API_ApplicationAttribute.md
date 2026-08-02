---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ApplicationAttribute.html
---

# ApplicationAttribute
<a name="API_ApplicationAttribute"></a>

Application details defined during the web ACL creation process. Application attributes help AWS WAF give recommendations for protection packs.

## Contents
<a name="API_ApplicationAttribute_Contents"></a>

 ** Name **   <a name="WAF-Type-ApplicationAttribute-Name"></a>
Specifies the attribute name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[\w\-]+$`
Required: No

 ** Values **   <a name="WAF-Type-ApplicationAttribute-Values"></a>
Specifies the attribute value.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_ApplicationAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ApplicationAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ApplicationAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ApplicationAttribute)
