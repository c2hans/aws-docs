---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallRuleGroup.html
---

# FirewallRuleGroup
<a name="API_route53resolver_FirewallRuleGroup"></a>

High-level information for a firewall rule group. A firewall rule group is a collection of rules that DNS Firewall uses to filter DNS network traffic for a VPC. To retrieve the rules for the rule group, call [ListFirewallRules](API_route53resolver_ListFirewallRules.md).

## Contents
<a name="API_route53resolver_FirewallRuleGroup_Contents"></a>

 ** Arn **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroup-Arn"></a>
The ARN (Amazon Resource Name) of the rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** CreationTime **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroup-CreationTime"></a>
The date and time that the rule group was created, in Unix time format and Coordinated Universal Time (UTC).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 40.
Required: No

 ** CreatorRequestId **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroup-CreatorRequestId"></a>
A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Id **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroup-Id"></a>
The ID of the rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ModificationTime **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroup-ModificationTime"></a>
The date and time that the rule group was last modified, in Unix time format and Coordinated Universal Time (UTC).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 40.
Required: No

 ** Name **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroup-Name"></a>
The name of the rule group.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** OwnerId **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroup-OwnerId"></a>
The AWS account ID for the account that created the rule group. When a rule group is shared with your account, this is the account that has shared the rule group with you.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 32.
Required: No

 ** RuleCount **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroup-RuleCount"></a>
The number of rules in the rule group.
Type: Integer
Required: No

 ** ShareStatus **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroup-ShareStatus"></a>
Whether the rule group is shared with other AWS accounts, or was shared with the current account by another AWS account. Sharing is configured through AWS Resource Access Manager (AWS RAM).
Type: String
Valid Values: `NOT_SHARED | SHARED_WITH_ME | SHARED_BY_ME`
Required: No

 ** Status **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroup-Status"></a>
The status of the domain list.
Type: String
Valid Values: `COMPLETE | DELETING | UPDATING`
Required: No

 ** StatusMessage **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroup-StatusMessage"></a>
Additional information about the status of the rule group, if available.
Type: String
Length Constraints: Maximum length of 255.
Required: No

## See Also
<a name="API_route53resolver_FirewallRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/FirewallRuleGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/FirewallRuleGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/FirewallRuleGroup)
