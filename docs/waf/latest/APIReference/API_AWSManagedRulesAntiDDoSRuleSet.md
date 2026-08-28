---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_AWSManagedRulesAntiDDoSRuleSet.html
---

# AWSManagedRulesAntiDDoSRuleSet
<a name="API_AWSManagedRulesAntiDDoSRuleSet"></a>

Configures the use of the anti-DDoS managed rule group, `AWSManagedRulesAntiDDoSRuleSet`. This configuration is used in `ManagedRuleGroupConfig`.

The configuration that you provide here determines whether and how the rules in the rule group are used.

For additional information about this and the other intelligent threat mitigation rule groups, see [Intelligent threat mitigation in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections) and [AWS Managed Rules rule groups list](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list) in the * AWS WAF Developer Guide*.

## Contents
<a name="API_AWSManagedRulesAntiDDoSRuleSet_Contents"></a>

 ** ClientSideActionConfig **   <a name="WAF-Type-AWSManagedRulesAntiDDoSRuleSet-ClientSideActionConfig"></a>
Configures the request handling that's applied by the managed rule group rules `ChallengeAllDuringEvent` and `ChallengeDDoSRequests` during a distributed denial of service (DDoS) attack.
Type: [ClientSideActionConfig](API_ClientSideActionConfig.md) object
Required: Yes

 ** SensitivityToBlock **   <a name="WAF-Type-AWSManagedRulesAntiDDoSRuleSet-SensitivityToBlock"></a>
The sensitivity that the rule group rule `DDoSRequests` uses when matching against the DDoS suspicion labeling on a request. The managed rule group adds the labeling during DDoS events, before the `DDoSRequests` rule runs.
The higher the sensitivity, the more levels of labeling that the rule matches:
+ Low sensitivity is less sensitive, causing the rule to match only on the most likely participants in an attack, which are the requests with the high suspicion label `awswaf:managed:aws:anti-ddos:high-suspicion-ddos-request`.
+ Medium sensitivity causes the rule to match on the medium and high suspicion labels.
+ High sensitivity causes the rule to match on all of the suspicion labels: low, medium, and high.
Default: `LOW`
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

## See Also
<a name="API_AWSManagedRulesAntiDDoSRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/AWSManagedRulesAntiDDoSRuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/AWSManagedRulesAntiDDoSRuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/AWSManagedRulesAntiDDoSRuleSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
