---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallRuleGroupAssociation.html
---

# FirewallRuleGroupAssociation
<a name="API_route53resolver_FirewallRuleGroupAssociation"></a>

An association between a firewall rule group and a VPC, which enables DNS filtering for the VPC.

## Contents
<a name="API_route53resolver_FirewallRuleGroupAssociation_Contents"></a>

 ** Arn **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupAssociation-Arn"></a>
The Amazon Resource Name (ARN) of the firewall rule group association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** CreationTime **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupAssociation-CreationTime"></a>
The date and time that the association was created, in Unix time format and Coordinated Universal Time (UTC).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 40.
Required: No

 ** CreatorRequestId **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupAssociation-CreatorRequestId"></a>
A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** FirewallRuleGroupId **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupAssociation-FirewallRuleGroupId"></a>
The unique identifier of the firewall rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Id **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupAssociation-Id"></a>
The identifier for the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ManagedOwnerName **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupAssociation-ManagedOwnerName"></a>
The owner of the association, used only for associations that are not managed by you. If you use AWS Firewall Manager to manage your DNS Firewalls, then this reports Firewall Manager as the managed owner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** ModificationTime **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupAssociation-ModificationTime"></a>
The date and time that the association was last modified, in Unix time format and Coordinated Universal Time (UTC).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 40.
Required: No

 ** MutationProtection **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupAssociation-MutationProtection"></a>
If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** Name **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupAssociation-Name"></a>
The name of the association.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** Priority **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupAssociation-Priority"></a>
The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC. DNS Firewall filters VPC traffic starting from rule group with the lowest numeric priority setting.
Type: Integer
Required: No

 ** Status **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupAssociation-Status"></a>
The current status of the association.
Type: String
Valid Values: `COMPLETE | DELETING | UPDATING`
Required: No

 ** StatusMessage **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupAssociation-StatusMessage"></a>
Additional information about the status of the response, if available.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** VpcId **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleGroupAssociation-VpcId"></a>
The unique identifier of the VPC that is associated with the rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_route53resolver_FirewallRuleGroupAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/FirewallRuleGroupAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/FirewallRuleGroupAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/FirewallRuleGroupAssociation)
