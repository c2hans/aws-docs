---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallConfig.html
---

# FirewallConfig
<a name="API_route53resolver_FirewallConfig"></a>

Configuration of the firewall behavior provided by DNS Firewall for a single VPC from Amazon Virtual Private Cloud (Amazon VPC).

## Contents
<a name="API_route53resolver_FirewallConfig_Contents"></a>

 ** FirewallFailOpen **   <a name="Route53Resolver-Type-route53resolver_FirewallConfig-FirewallFailOpen"></a>
Determines how DNS Firewall operates during failures, for example when all traffic that is sent to DNS Firewall fails to receive a reply.
+ By default, fail open is disabled, which means the failure mode is closed. This approach favors security over availability. DNS Firewall returns a failure error when it is unable to properly evaluate a query.
+ If you enable this option, the failure mode is open. This approach favors availability over security. DNS Firewall allows queries to proceed if it is unable to properly evaluate them.
This behavior is only enforced for VPCs that have at least one DNS Firewall rule group association.
Type: String
Valid Values: `ENABLED | DISABLED | USE_LOCAL_RESOURCE_SETTING`
Required: No

 ** Id **   <a name="Route53Resolver-Type-route53resolver_FirewallConfig-Id"></a>
The ID of the firewall configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** OwnerId **   <a name="Route53Resolver-Type-route53resolver_FirewallConfig-OwnerId"></a>
The AWS account ID of the owner of the VPC that this firewall configuration applies to.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 32.
Required: No

 ** ResourceId **   <a name="Route53Resolver-Type-route53resolver_FirewallConfig-ResourceId"></a>
The ID of the VPC that this firewall configuration applies to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_route53resolver_FirewallConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/FirewallConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/FirewallConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/FirewallConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
