---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RuleGroupSourceStatelessRuleDefinition.html
---

# RuleGroupSourceStatelessRuleDefinition
<a name="API_RuleGroupSourceStatelessRuleDefinition"></a>

The definition of the stateless rule.

## Contents
<a name="API_RuleGroupSourceStatelessRuleDefinition_Contents"></a>

 ** Actions **   <a name="securityhub-Type-RuleGroupSourceStatelessRuleDefinition-Actions"></a>
The actions to take on a packet that matches one of the stateless rule definition's match attributes. You must specify a standard action (`aws:pass`, `aws:drop`, or `aws:forward_to_sfe`). You can then add custom actions.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** MatchAttributes **   <a name="securityhub-Type-RuleGroupSourceStatelessRuleDefinition-MatchAttributes"></a>
The criteria for Network Firewall to use to inspect an individual packet in a stateless rule inspection.
Type: [RuleGroupSourceStatelessRuleMatchAttributes](API_RuleGroupSourceStatelessRuleMatchAttributes.md) object
Required: No

## See Also
<a name="API_RuleGroupSourceStatelessRuleDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RuleGroupSourceStatelessRuleDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RuleGroupSourceStatelessRuleDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RuleGroupSourceStatelessRuleDefinition)
