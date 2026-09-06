---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_APIKeySummary.html
---

# APIKeySummary
<a name="API_APIKeySummary"></a>

Information for a single API key.

API keys are required for the integration of the CAPTCHA API in your JavaScript client applications. The API lets you customize the placement and characteristics of the CAPTCHA puzzle for your end users. For more information about the CAPTCHA JavaScript integration, see [AWS WAF client application integration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html) in the * AWS WAF Developer Guide*.

## Contents
<a name="API_APIKeySummary_Contents"></a>

 ** APIKey **   <a name="WAF-Type-APIKeySummary-APIKey"></a>
The generated, encrypted API key. You can copy this for use in your JavaScript CAPTCHA integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** CreationTimestamp **   <a name="WAF-Type-APIKeySummary-CreationTimestamp"></a>
The date and time that the key was created.
Type: Timestamp
Required: No

 ** TokenDomains **   <a name="WAF-Type-APIKeySummary-TokenDomains"></a>
The token domains that are defined in this API key.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `^[\w\.\-/]+$`
Required: No

 ** Version **   <a name="WAF-Type-APIKeySummary-Version"></a>
Internal value used by AWS WAF to manage the key.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_APIKeySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/APIKeySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/APIKeySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/APIKeySummary)
