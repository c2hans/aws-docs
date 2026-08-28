---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html
---

# Rule
<a name="API_Rule"></a>

A single rule, which you can use in a [WebACL](API_WebACL.md) or [RuleGroup](API_RuleGroup.md) to identify web requests that you want to manage in some way. Each rule includes one top-level [Statement](API_Statement.md) that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.

## Contents
<a name="API_Rule_Contents"></a>

 ** Name **   <a name="WAF-Type-Rule-Name"></a>
The name of the rule.
If you change the name of a `Rule` after you create it and you want the rule's metric name to reflect the change, update the metric name in the rule's `VisibilityConfig` settings. AWS WAF doesn't automatically update the metric name when you update the rule name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: Yes

 ** Priority **   <a name="WAF-Type-Rule-Priority"></a>
If you define more than one `Rule` in a `WebACL`, AWS WAF evaluates each request against the `Rules` in order based on the value of `Priority`. AWS WAF processes rules with lower priority first. The priorities don't need to be consecutive, but they must all be different.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** Statement **   <a name="WAF-Type-Rule-Statement"></a>
The AWS WAF processing statement for the rule, for example [ByteMatchStatement](API_ByteMatchStatement.md) or [SizeConstraintStatement](API_SizeConstraintStatement.md).
Type: [Statement](API_Statement.md) object
Required: Yes

 ** VisibilityConfig **   <a name="WAF-Type-Rule-VisibilityConfig"></a>
Defines and enables Amazon CloudWatch metrics and web request sample collection.
If you change the name of a `Rule` after you create it and you want the rule's metric name to reflect the change, update the metric name as well. AWS WAF doesn't automatically update the metric name.
Type: [VisibilityConfig](API_VisibilityConfig.md) object
Required: Yes

 ** Action **   <a name="WAF-Type-Rule-Action"></a>
The action that AWS WAF should take on a web request when it matches the rule statement. Settings at the web ACL level can override the rule action setting.
This is used only for rules whose statements do not reference a rule group. Rule statements that reference a rule group include `RuleGroupReferenceStatement` and `ManagedRuleGroupStatement`.
You must specify either this `Action` setting or the rule `OverrideAction` setting, but not both:
+ If the rule statement does not reference a rule group, use this rule action setting and not the rule override action setting.
+ If the rule statement references a rule group, use the override action setting and not this action setting.
Type: [RuleAction](API_RuleAction.md) object
Required: No

 ** CaptchaConfig **   <a name="WAF-Type-Rule-CaptchaConfig"></a>
Specifies how AWS WAF should handle `CAPTCHA` evaluations. If you don't specify this, AWS WAF uses the `CAPTCHA` configuration that's defined for the web ACL.
Type: [CaptchaConfig](API_CaptchaConfig.md) object
Required: No

 ** ChallengeConfig **   <a name="WAF-Type-Rule-ChallengeConfig"></a>
Specifies how AWS WAF should handle `Challenge` evaluations. If you don't specify this, AWS WAF uses the challenge configuration that's defined for the web ACL.
Type: [ChallengeConfig](API_ChallengeConfig.md) object
Required: No

 ** OverrideAction **   <a name="WAF-Type-Rule-OverrideAction"></a>
The action to use in the place of the action that results from the rule group evaluation. Set the override action to none to leave the result of the rule group alone. Set it to count to override the result to count only.
You can only use this for rule statements that reference a rule group, like `RuleGroupReferenceStatement` and `ManagedRuleGroupStatement`.
This option is usually set to none. It does not affect how the rules in the rule group are evaluated. If you want the rules in the rule group to only count matches, do not use this and instead use the rule action override option, with `Count` action, in your rule group reference statement settings.
Type: [OverrideAction](API_OverrideAction.md) object
Required: No

 ** RuleLabels **   <a name="WAF-Type-Rule-RuleLabels"></a>
Labels to apply to web requests that match the rule match statement. AWS WAF applies fully qualified labels to matching web requests. A fully qualified label is the concatenation of a label namespace and a rule label. The rule's rule group or web ACL defines the label namespace.
Any rule that isn't a rule group reference statement or managed rule group statement can add labels to matching web requests.
Rules that run after this rule in the web ACL can match against these labels using a `LabelMatchStatement`.
For each label, provide a case-sensitive string containing optional namespaces and a label name, according to the following guidelines:
+ Separate each component of the label with a colon.
+ Each namespace or name can have up to 128 characters.
+ You can specify up to 5 namespaces in a label.
+ Don't use the following reserved words in your label specification: `aws`, `waf`, `managed`, `rulegroup`, `webacl`, `regexpatternset`, or `ipset`.
For example, `myLabelName` or `nameSpace1:nameSpace2:myLabelName`.
Type: Array of [Label](API_Label.md) objects
Required: No

## See Also
<a name="API_Rule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/Rule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/Rule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/Rule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
