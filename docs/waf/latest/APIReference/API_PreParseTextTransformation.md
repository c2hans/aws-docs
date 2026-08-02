---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_PreParseTextTransformation.html
---

# PreParseTextTransformation
<a name="API_PreParseTextTransformation"></a>

A pre-parse text transformation that normalizes the raw query string before AWS WAF parses it into individual query arguments. Pre-parse text transformations are only supported when `FieldToMatch` is `SingleQueryArgument` or `AllQueryArguments`.

## Contents
<a name="API_PreParseTextTransformation_Contents"></a>

 ** Priority **   <a name="WAF-Type-PreParseTextTransformation-Priority"></a>
Sets the relative processing order for the pre-parse text transformations that you define. AWS WAF processes all transformations, from lowest priority value to highest, before inspecting the transformed content.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** Type **   <a name="WAF-Type-PreParseTextTransformation-Type"></a>
The type of pre-parse text transformation to apply to the raw query string.
Type: String
Valid Values: `NONE | URL_DECODE | URL_DECODE_UNI | COMBINE_DUPLICATE_QUERY_ARGS_BY_COMMA | REPLACE_SEMICOLONS_WITH_AMPERSANDS`
Required: Yes

## See Also
<a name="API_PreParseTextTransformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/PreParseTextTransformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/PreParseTextTransformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/PreParseTextTransformation)
