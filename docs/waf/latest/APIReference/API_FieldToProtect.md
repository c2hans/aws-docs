---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToProtect.html
---

# FieldToProtect
<a name="API_FieldToProtect"></a>

Specifies a field type and keys to protect in stored web request data. This is part of the data protection configuration for a web ACL.

## Contents
<a name="API_FieldToProtect_Contents"></a>

 ** FieldType **   <a name="WAF-Type-FieldToProtect-FieldType"></a>
Specifies the web request component type to protect.
Type: String
Valid Values: `SINGLE_HEADER | SINGLE_COOKIE | SINGLE_QUERY_ARGUMENT | QUERY_STRING | BODY`
Required: Yes

 ** FieldKeys **   <a name="WAF-Type-FieldToProtect-FieldKeys"></a>
Specifies the keys to protect for the specified field type. If you don't specify any key, then all keys for the field type are protected.
Type: Array of strings
Array Members: Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_FieldToProtect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/FieldToProtect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/FieldToProtect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/FieldToProtect)
