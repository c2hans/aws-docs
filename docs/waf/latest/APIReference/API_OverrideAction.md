---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_OverrideAction.html
---

# OverrideAction
<a name="API_OverrideAction"></a>

The action to use in the place of the action that results from the rule group evaluation. Set the override action to none to leave the result of the rule group alone. Set it to count to override the result to count only.

You can only use this for rule statements that reference a rule group, like `RuleGroupReferenceStatement` and `ManagedRuleGroupStatement`.

**Note**
This option is usually set to none. It does not affect how the rules in the rule group are evaluated. If you want the rules in the rule group to only count matches, do not use this and instead use the rule action override option, with `Count` action, in your rule group reference statement settings.

## Contents
<a name="API_OverrideAction_Contents"></a>

 ** Count **   <a name="WAF-Type-OverrideAction-Count"></a>
Override the rule group evaluation result to count only.
This option is usually set to none. It does not affect how the rules in the rule group are evaluated. If you want the rules in the rule group to only count matches, do not use this and instead use the rule action override option, with `Count` action, in your rule group reference statement settings.
Type: [CountAction](API_CountAction.md) object
Required: No

 ** None **   <a name="WAF-Type-OverrideAction-None"></a>
Don't override the rule group evaluation result. This is the most common setting.
Type: [NoneAction](API_NoneAction.md) object
Required: No

## See Also
<a name="API_OverrideAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/OverrideAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/OverrideAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/OverrideAction)
