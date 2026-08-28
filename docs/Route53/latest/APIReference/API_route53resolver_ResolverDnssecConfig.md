---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverDnssecConfig.html
---

# ResolverDnssecConfig
<a name="API_route53resolver_ResolverDnssecConfig"></a>

A complex type that contains information about a configuration for DNSSEC validation.

## Contents
<a name="API_route53resolver_ResolverDnssecConfig_Contents"></a>

 ** Id **   <a name="Route53Resolver-Type-route53resolver_ResolverDnssecConfig-Id"></a>
The ID for a configuration for DNSSEC validation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** OwnerId **   <a name="Route53Resolver-Type-route53resolver_ResolverDnssecConfig-OwnerId"></a>
The owner account ID of the virtual private cloud (VPC) for a configuration for DNSSEC validation.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 32.
Required: No

 ** ResourceId **   <a name="Route53Resolver-Type-route53resolver_ResolverDnssecConfig-ResourceId"></a>
The ID of the virtual private cloud (VPC) that you're configuring the DNSSEC validation status for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ValidationStatus **   <a name="Route53Resolver-Type-route53resolver_ResolverDnssecConfig-ValidationStatus"></a>
The validation status for a DNSSEC configuration. The status can be one of the following:
+  **ENABLING:** DNSSEC validation is being enabled but is not complete.
+  **ENABLED:** DNSSEC validation is enabled.
+  **DISABLING:** DNSSEC validation is being disabled but is not complete.
+  **DISABLED** DNSSEC validation is disabled.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | UPDATING_TO_USE_LOCAL_RESOURCE_SETTING | USE_LOCAL_RESOURCE_SETTING`
Required: No

## See Also
<a name="API_route53resolver_ResolverDnssecConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ResolverDnssecConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ResolverDnssecConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ResolverDnssecConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
