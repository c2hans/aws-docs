---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleActionOverride.html
---

# RuleActionOverride
<a name="API_RuleActionOverride"></a>

Action setting to use in the place of a rule action that is configured inside the rule group. You specify one override for each rule whose action you want to change.

**Note**
Verify the rule names in your overrides carefully. With managed rule groups, AWS WAF silently ignores any override that uses an invalid rule name. With customer-owned rule groups, invalid rule names in your overrides will cause web ACL updates to fail. An invalid rule name is any name that doesn't exactly match the case-sensitive name of an existing rule in the rule group.

You can use overrides for testing, for example you can override all of rule actions to `Count` and then monitor the resulting count metrics to understand how the rule group would handle your web traffic. You can also permanently override some or all actions, to modify how the rule group manages your web traffic.

## Contents
<a name="API_RuleActionOverride_Contents"></a>

 ** ActionToUse **   <a name="WAF-Type-RuleActionOverride-ActionToUse"></a>
The override action to use, in place of the configured action of the rule in the rule group.
Type: [RuleAction](API_RuleAction.md) object
Required: Yes

 ** Name **   <a name="WAF-Type-RuleActionOverride-Name"></a>
The name of the rule to override.
Verify the rule names in your overrides carefully. With managed rule groups, AWS WAF silently ignores any override that uses an invalid rule name. With customer-owned rule groups, invalid rule names in your overrides will cause web ACL updates to fail. An invalid rule name is any name that doesn't exactly match the case-sensitive name of an existing rule in the rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: Yes

## See Also
<a name="API_RuleActionOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RuleActionOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RuleActionOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RuleActionOverride)
