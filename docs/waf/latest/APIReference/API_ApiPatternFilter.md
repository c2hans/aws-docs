---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ApiPatternFilter.html
---

# ApiPatternFilter

An API pattern to filter events by, used in [ListEvents](API_ListEvents.md) and [ListEventsByWebACL](API_ListEventsByWebACL.md).

## Contents
<a name="API_ApiPatternFilter_Contents"></a>

 ** Domains **   <a name="WAF-Type-ApiPatternFilter-Domains"></a>
The domains that you want the filter to match. You can specify up to 10 domains.
Type: Array of strings
Array Members: Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Method **   <a name="WAF-Type-ApiPatternFilter-Method"></a>
The HTTP method that you want the filter to match. For example, `GET` or `POST`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Required: No

 ** PathPattern **   <a name="WAF-Type-ApiPatternFilter-PathPattern"></a>
The normalized URI path that you want the filter to match. For example, `/api/v1/accounts/{id}`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Port **   <a name="WAF-Type-ApiPatternFilter-Port"></a>
The port that you want the filter to match. For example, `443`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

## See Also
<a name="API_ApiPatternFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ApiPatternFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ApiPatternFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ApiPatternFilter)
