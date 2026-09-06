---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_FirewallManagerStatement.html
---

# FirewallManagerStatement
<a name="API_FirewallManagerStatement"></a>

The processing guidance for an AWS Firewall Manager rule. This is like a regular rule [Statement](API_Statement.md), but it can only contain a single rule group reference.

## Contents
<a name="API_FirewallManagerStatement_Contents"></a>

 ** ManagedRuleGroupStatement **   <a name="WAF-Type-FirewallManagerStatement-ManagedRuleGroupStatement"></a>
A statement used by AWS Firewall Manager to run the rules that are defined in a managed rule group. This is managed by Firewall Manager for an AWS Firewall Manager AWS WAF policy.
Type: [ManagedRuleGroupStatement](API_ManagedRuleGroupStatement.md) object
Required: No

 ** RuleGroupReferenceStatement **   <a name="WAF-Type-FirewallManagerStatement-RuleGroupReferenceStatement"></a>
A statement used by AWS Firewall Manager to run the rules that are defined in a rule group. This is managed by Firewall Manager for an AWS Firewall Manager AWS WAF policy.
Type: [RuleGroupReferenceStatement](API_RuleGroupReferenceStatement.md) object
Required: No

## See Also
<a name="API_FirewallManagerStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/FirewallManagerStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/FirewallManagerStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/FirewallManagerStatement)
