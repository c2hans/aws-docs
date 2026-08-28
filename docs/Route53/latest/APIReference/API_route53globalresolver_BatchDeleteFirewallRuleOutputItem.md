---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchDeleteFirewallRuleOutputItem.html
---

# BatchDeleteFirewallRuleOutputItem
<a name="API_route53globalresolver_BatchDeleteFirewallRuleOutputItem"></a>

The result of deleting a firewall rule in a batch operation.

## Contents
<a name="API_route53globalresolver_BatchDeleteFirewallRuleOutputItem_Contents"></a>

 ** code **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchDeleteFirewallRuleOutputItem-code"></a>
The response code for the delete operation.
Type: Integer
Required: Yes

 ** firewallRule **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchDeleteFirewallRuleOutputItem-firewallRule"></a>
The firewall rule that was deleted in the batch operation.
Type: [BatchDeleteFirewallRuleResult](API_route53globalresolver_BatchDeleteFirewallRuleResult.md) object
Required: Yes

 ** message **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchDeleteFirewallRuleOutputItem-message"></a>
The response message for the delete operation.
Type: String
Required: No

## See Also
<a name="API_route53globalresolver_BatchDeleteFirewallRuleOutputItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/BatchDeleteFirewallRuleOutputItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/BatchDeleteFirewallRuleOutputItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/BatchDeleteFirewallRuleOutputItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
