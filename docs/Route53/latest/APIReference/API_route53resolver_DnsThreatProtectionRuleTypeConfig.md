---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DnsThreatProtectionRuleTypeConfig.html
---

# DnsThreatProtectionRuleTypeConfig
<a name="API_route53resolver_DnsThreatProtectionRuleTypeConfig"></a>

The configuration for a DNS threat protection rule type within the rule type framework.

## Contents
<a name="API_route53resolver_DnsThreatProtectionRuleTypeConfig_Contents"></a>

 ** ConfidenceThreshold **   <a name="Route53Resolver-Type-route53resolver_DnsThreatProtectionRuleTypeConfig-ConfidenceThreshold"></a>
The confidence threshold for DNS Firewall Advanced. You must provide this value when you create or update a DNS Firewall Advanced rule. The confidence level values mean:
+  `LOW`: Provides the highest detection rate for threats, but also increases false positives.
+  `MEDIUM`: Provides a balance between detecting threats and false positives.
+  `HIGH`: Detects only the most well corroborated threats with a low rate of false positives.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: Yes

 ** Value **   <a name="Route53Resolver-Type-route53resolver_DnsThreatProtectionRuleTypeConfig-Value"></a>
The type of DNS threat protection. Valid values are:
+  `DGA`: Domain generation algorithms detection. DGAs are used by attackers to generate a large number of domains to launch malware attacks.
+  `DNS_TUNNELING`: DNS tunneling detection. DNS tunneling is used by attackers to exfiltrate data from the client by using the DNS tunnel without making a network connection to the client.
+  `DICTIONARY_DGA`: Dictionary-based domain generation algorithms detection. Dictionary DGAs use wordlists to generate domains that appear more legitimate, making them harder to detect than traditional DGAs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_route53resolver_DnsThreatProtectionRuleTypeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/DnsThreatProtectionRuleTypeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/DnsThreatProtectionRuleTypeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/DnsThreatProtectionRuleTypeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
