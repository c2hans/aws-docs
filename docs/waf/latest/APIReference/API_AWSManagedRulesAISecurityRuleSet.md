---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_AWSManagedRulesAISecurityRuleSet.html
---

# AWSManagedRulesAISecurityRuleSet

Configures the use of the AI security managed rule group, `AWSManagedRulesAISecurityRuleSet`. This configuration is used in `ManagedRuleGroupConfig`.

The rule group always runs its own inspections. The configuration that you provide here determines whether the rule group also uses Amazon Bedrock Guardrails to inspect web requests, or web requests and responses.

Use of this rule group is not supported in AWS Firewall Manager.

## Contents
<a name="API_AWSManagedRulesAISecurityRuleSet_Contents"></a>

 ** BedrockGuardrails **   <a name="WAF-Type-AWSManagedRulesAISecurityRuleSet-BedrockGuardrails"></a>
Specifies whether and how the rule group uses Amazon Bedrock Guardrails.
Type: [BedrockGuardrails](API_BedrockGuardrails.md) object
Required: Yes

## See Also
<a name="API_AWSManagedRulesAISecurityRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/AWSManagedRulesAISecurityRuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/AWSManagedRulesAISecurityRuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/AWSManagedRulesAISecurityRuleSet)
