---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ApiPattern.html
---

# ApiPattern

An API endpoint pattern that an API security event involves.

## Contents
<a name="API_ApiPattern_Contents"></a>

 ** Domains **   <a name="WAF-Type-ApiPattern-Domains"></a>
The domains that the API pattern was observed on. For example, `api.example.com`.
Type: Array of strings
Array Members: Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Method **   <a name="WAF-Type-ApiPattern-Method"></a>
The HTTP method of the API pattern. For example, `GET` or `POST`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Required: No

 ** PathPattern **   <a name="WAF-Type-ApiPattern-PathPattern"></a>
The normalized URI path of the API pattern. Templated path segments are shown in braces. For example, `/api/v1/accounts/{id}`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Port **   <a name="WAF-Type-ApiPattern-Port"></a>
The port of the API pattern. For example, `443`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

## See Also
<a name="API_ApiPattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ApiPattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ApiPattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ApiPattern)
