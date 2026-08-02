---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_SubscriptionInfo.html
---

# SubscriptionInfo
<a name="API_route53resolver_SubscriptionInfo"></a>

Identifies the AWS Marketplace product that backs a partner-managed rule type. Returned as part of [FirewallRuleTypeDefinition](API_route53resolver_FirewallRuleTypeDefinition.md) when the rule type variant requires an active customer subscription to the named product.

## Contents
<a name="API_route53resolver_SubscriptionInfo_Contents"></a>

 ** ProductId **   <a name="Route53Resolver-Type-route53resolver_SubscriptionInfo-ProductId"></a>
The AWS Marketplace product identifier of the partner threat-protection product. Use this value to verify or manage the calling account's subscription in AWS Marketplace.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** VendorName **   <a name="Route53Resolver-Type-route53resolver_SubscriptionInfo-VendorName"></a>
The name of the AWS Marketplace seller (vendor) that publishes the partner threat-protection product (for example, `Palo Alto Networks`).
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_route53resolver_SubscriptionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/SubscriptionInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/SubscriptionInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/SubscriptionInfo)
