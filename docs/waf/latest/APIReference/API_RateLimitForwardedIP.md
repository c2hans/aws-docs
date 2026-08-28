---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RateLimitForwardedIP.html
---

# RateLimitForwardedIP
<a name="API_RateLimitForwardedIP"></a>

Specifies the first IP address in an HTTP header as an aggregate key for a rate-based rule. Each distinct forwarded IP address contributes to the aggregation instance.

This setting is used only in the `RateBasedStatementCustomKey` specification of a rate-based rule statement. When you specify an IP or forwarded IP in the custom key settings, you must also specify at least one other key to use. You can aggregate on only the forwarded IP address by specifying `FORWARDED_IP` in your rate-based statement's `AggregateKeyType`.

This data type supports using the forwarded IP address in the web request aggregation for a rate-based rule, in `RateBasedStatementCustomKey`. The JSON specification for using the forwarded IP address doesn't explicitly use this data type.

JSON specification: `"ForwardedIP": {}`

When you use this specification, you must also configure the forwarded IP address in the rate-based statement's `ForwardedIPConfig`.

## Contents
<a name="API_RateLimitForwardedIP_Contents"></a>

The members of this exception structure are context-dependent.

## See Also
<a name="API_RateLimitForwardedIP_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RateLimitForwardedIP)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RateLimitForwardedIP)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RateLimitForwardedIP)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
