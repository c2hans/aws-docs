---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallRuleGroupMetadata.html
---

# FirewallRuleGroupMetadata
<a name="API_route53resolver_FirewallRuleGroupMetadata"></a>

Minimal high-level information for a firewall rule group. The action [ListFirewallRuleGroups](API_route53resolver_ListFirewallRuleGroups.md) returns an array of these objects.

To retrieve full information for a firewall rule group, call [GetFirewallRuleGroup](API_route53resolver_GetFirewallRuleGroup.md) and [ListFirewallRules](API_route53resolver_ListFirewallRules.md).

## Contents
<a name="API_route53resolver_FirewallRuleGroupMetadata_Contents"></a>

 ** Arn **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupMetadata-Arn"></a>
The ARN (Amazon Resource Name) of the rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** CreatorRequestId **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupMetadata-CreatorRequestId"></a>
A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Id **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupMetadata-Id"></a>
The ID of the rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Name **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupMetadata-Name"></a>
The name of the rule group.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** OwnerId **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupMetadata-OwnerId"></a>
The AWS account ID for the account that created the rule group. When a rule group is shared with your account, this is the account that has shared the rule group with you.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 32.
Required: No

 ** ShareStatus **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupMetadata-ShareStatus"></a>
Whether the rule group is shared with other AWS accounts, or was shared with the current account by another AWS account. Sharing is configured through AWS Resource Access Manager (AWS RAM).
Type: String
Valid Values: `NOT_SHARED | SHARED_WITH_ME | SHARED_BY_ME`
Required: No

## See Also
<a name="API_route53resolver_FirewallRuleGroupMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/FirewallRuleGroupMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/FirewallRuleGroupMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/FirewallRuleGroupMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
