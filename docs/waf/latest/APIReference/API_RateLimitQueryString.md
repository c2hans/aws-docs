---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RateLimitQueryString.html
---

# RateLimitQueryString
<a name="API_RateLimitQueryString"></a>

Specifies the request's query string as an aggregate key for a rate-based rule. Each distinct string contributes to the aggregation instance. If you use just the query string as your custom key, then each string fully defines an aggregation instance.

## Contents
<a name="API_RateLimitQueryString_Contents"></a>

 ** TextTransformations **   <a name="WAF-Type-RateLimitQueryString-TextTransformations"></a>
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. Text transformations are used in rule match statements, to transform the `FieldToMatch` request component before inspecting it, and they're used in rate-based rule statements, to transform request components before using them as custom aggregation keys. If you specify one or more transformations to apply, AWS WAF performs all transformations on the specified content, starting from the lowest priority setting, and then uses the transformed component contents.
Type: Array of [TextTransformation](API_TextTransformation.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## See Also
<a name="API_RateLimitQueryString_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RateLimitQueryString)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RateLimitQueryString)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RateLimitQueryString)
