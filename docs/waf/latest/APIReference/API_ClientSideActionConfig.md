---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ClientSideActionConfig.html
---

# ClientSideActionConfig
<a name="API_ClientSideActionConfig"></a>

This is part of the configuration for the managed rules `AWSManagedRulesAntiDDoSRuleSet` in `ManagedRuleGroupConfig`.

## Contents
<a name="API_ClientSideActionConfig_Contents"></a>

 ** Challenge **   <a name="WAF-Type-ClientSideActionConfig-Challenge"></a>
Configuration for the use of the `AWSManagedRulesAntiDDoSRuleSet` rules `ChallengeAllDuringEvent` and `ChallengeDDoSRequests`.
This setting isn't related to the configuration of the `Challenge` action itself. It only configures the use of the two anti-DDoS rules named here.
You can enable or disable the use of these rules, and you can configure how to use them when they are enabled.
Type: [ClientSideAction](API_ClientSideAction.md) object
Required: Yes

## See Also
<a name="API_ClientSideActionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ClientSideActionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ClientSideActionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ClientSideActionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
