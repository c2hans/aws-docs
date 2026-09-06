---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchCreateFirewallRuleOutputItem.html
---

# BatchCreateFirewallRuleOutputItem
<a name="API_route53globalresolver_BatchCreateFirewallRuleOutputItem"></a>

Information about the result of creating a DNS Firewall rule in a batch operation.

## Contents
<a name="API_route53globalresolver_BatchCreateFirewallRuleOutputItem_Contents"></a>

 ** code **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleOutputItem-code"></a>
The HTTP response code for the batch operation result.
Type: Integer
Required: Yes

 ** firewallRule **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleOutputItem-firewallRule"></a>
The firewall rule that was created in the batch operation.
Type: [BatchCreateFirewallRuleResult](API_route53globalresolver_BatchCreateFirewallRuleResult.md) object
Required: Yes

 ** message **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchCreateFirewallRuleOutputItem-message"></a>
A message describing the result of the batch operation, including error details if applicable.
Type: String
Required: No

## See Also
<a name="API_route53globalresolver_BatchCreateFirewallRuleOutputItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/BatchCreateFirewallRuleOutputItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/BatchCreateFirewallRuleOutputItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/BatchCreateFirewallRuleOutputItem)
