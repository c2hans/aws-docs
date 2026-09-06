---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RateLimitIP.html
---

# RateLimitIP
<a name="API_RateLimitIP"></a>

Specifies the IP address in the web request as an aggregate key for a rate-based rule. Each distinct IP address contributes to the aggregation instance.

This setting is used only in the `RateBasedStatementCustomKey` specification of a rate-based rule statement. To use this in the custom key settings, you must specify at least one other key to use, along with the IP address. To aggregate on only the IP address, in your rate-based statement's `AggregateKeyType`, specify `IP`.

JSON specification: `"RateLimitIP": {}`

## Contents
<a name="API_RateLimitIP_Contents"></a>

The members of this exception structure are context-dependent.

## See Also
<a name="API_RateLimitIP_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RateLimitIP)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RateLimitIP)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RateLimitIP)
