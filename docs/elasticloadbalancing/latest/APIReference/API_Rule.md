---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_Rule.html
---

# Rule
<a name="API_Rule"></a>

Information about a rule.

## Contents
<a name="API_Rule_Contents"></a>

 ** Actions.member.N **
The actions. Each rule must include exactly one of the following types of actions: `forward`, `redirect`, or `fixed-response`, and it must be the last action to be performed.
Type: Array of [Action](API_Action.md) objects
Required: No

 ** Conditions.member.N **
The conditions. Each rule can include zero or one of the following conditions: `http-request-method`, `host-header`, `path-pattern`, and `source-ip`, and zero or more of the following conditions: `http-header` and `query-string`.
Type: Array of [RuleCondition](API_RuleCondition.md) objects
Required: No

 ** IsDefault **
Indicates whether this is the default rule.
Type: Boolean
Required: No

 ** Priority **
The priority.
Type: String
Required: No

 ** RuleArn **
The Amazon Resource Name (ARN) of the rule.
Type: String
Required: No

 ** Transforms.member.N **
The transforms for the rule.
Type: Array of [RuleTransform](API_RuleTransform.md) objects
Required: No

## See Also
<a name="API_Rule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/Rule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/Rule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/Rule)
