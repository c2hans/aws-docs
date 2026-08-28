---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverRuleAssociation.html
---

# ResolverRuleAssociation
<a name="API_route53resolver_ResolverRuleAssociation"></a>

In the response to an [AssociateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverRule.html), [DisassociateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverRule.html), or [ListResolverRuleAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRuleAssociations.html) request, provides information about an association between a Resolver rule and a VPC. The association determines which DNS queries that originate in the VPC are forwarded to your network.

## Contents
<a name="API_route53resolver_ResolverRuleAssociation_Contents"></a>

 ** Id **   <a name="Route53Resolver-Type-route53resolver_ResolverRuleAssociation-Id"></a>
The ID of the association between a Resolver rule and a VPC. Resolver assigns this value when you submit an [AssociateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverRule.html) request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Name **   <a name="Route53Resolver-Type-route53resolver_ResolverRuleAssociation-Name"></a>
The name of an association between a Resolver rule and a VPC.
The name can be up to 64 characters long and can contain letters (a-z, A-Z), numbers (0-9), hyphens (-), underscores (\_), and spaces. The name cannot consist of only numbers.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** ResolverRuleId **   <a name="Route53Resolver-Type-route53resolver_ResolverRuleAssociation-ResolverRuleId"></a>
The ID of the Resolver rule that you associated with the VPC that is specified by `VPCId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Status **   <a name="Route53Resolver-Type-route53resolver_ResolverRuleAssociation-Status"></a>
A code that specifies the current status of the association between a Resolver rule and a VPC.
Type: String
Valid Values: `CREATING | COMPLETE | DELETING | FAILED | OVERRIDDEN`
Required: No

 ** StatusMessage **   <a name="Route53Resolver-Type-route53resolver_ResolverRuleAssociation-StatusMessage"></a>
A detailed description of the status of the association between a Resolver rule and a VPC.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** VPCId **   <a name="Route53Resolver-Type-route53resolver_ResolverRuleAssociation-VPCId"></a>
The ID of the VPC that you associated the Resolver rule with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_route53resolver_ResolverRuleAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ResolverRuleAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ResolverRuleAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ResolverRuleAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
