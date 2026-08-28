---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteFirewallRuleEntry.html
---

# DeleteFirewallRuleEntry
<a name="API_route53resolver_DeleteFirewallRuleEntry"></a>

The details for deleting a single firewall rule in a batch operation.

## Contents
<a name="API_route53resolver_DeleteFirewallRuleEntry_Contents"></a>

 ** FirewallRuleGroupId **   <a name="Route53Resolver-Type-route53resolver_DeleteFirewallRuleEntry-FirewallRuleGroupId"></a>
The unique identifier of the firewall rule group for the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** FirewallDomainListId **   <a name="Route53Resolver-Type-route53resolver_DeleteFirewallRuleEntry-FirewallDomainListId"></a>
The ID of the domain list that's used in the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** FirewallThreatProtectionId **   <a name="Route53Resolver-Type-route53resolver_DeleteFirewallRuleEntry-FirewallThreatProtectionId"></a>
The ID of the DNS Firewall Advanced rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Qtype **   <a name="Route53Resolver-Type-route53resolver_DeleteFirewallRuleEntry-Qtype"></a>
The DNS query type that the rule evaluates.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Required: No

## See Also
<a name="API_route53resolver_DeleteFirewallRuleEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/DeleteFirewallRuleEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/DeleteFirewallRuleEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/DeleteFirewallRuleEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
