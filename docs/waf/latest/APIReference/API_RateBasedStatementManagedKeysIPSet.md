---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedStatementManagedKeysIPSet.html
---

# RateBasedStatementManagedKeysIPSet
<a name="API_RateBasedStatementManagedKeysIPSet"></a>

The set of IP addresses that are currently blocked for a [RateBasedStatement](API_RateBasedStatement.md). This is only available for rate-based rules that aggregate on just the IP address, with the `AggregateKeyType` set to `IP` or `FORWARDED_IP`.

A rate-based rule applies its rule action to requests from IP addresses that are in the rule's managed keys list and that match the rule's scope-down statement. When a rule has no scope-down statement, it applies the action to all requests from the IP addresses that are in the list. The rule applies its rule action to rate limit the matching requests. The action is usually Block but it can be any valid rule action except for Allow.

The maximum number of IP addresses that can be rate limited by a single rate-based rule instance is 10,000. If more than 10,000 addresses exceed the rate limit, AWS WAF limits those with the highest rates.

## Contents
<a name="API_RateBasedStatementManagedKeysIPSet_Contents"></a>

 ** Addresses **   <a name="WAF-Type-RateBasedStatementManagedKeysIPSet-Addresses"></a>
The IP addresses that are currently blocked.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `.*\S.*`
Required: No

 ** IPAddressVersion **   <a name="WAF-Type-RateBasedStatementManagedKeysIPSet-IPAddressVersion"></a>
The version of the IP addresses, either `IPV4` or `IPV6`.
Type: String
Valid Values: `IPV4 | IPV6`
Required: No

## See Also
<a name="API_RateBasedStatementManagedKeysIPSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RateBasedStatementManagedKeysIPSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RateBasedStatementManagedKeysIPSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RateBasedStatementManagedKeysIPSet)
