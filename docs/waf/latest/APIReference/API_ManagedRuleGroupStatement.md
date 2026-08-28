---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ManagedRuleGroupStatement.html
---

# ManagedRuleGroupStatement
<a name="API_ManagedRuleGroupStatement"></a>

A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling [ListAvailableManagedRuleGroups](API_ListAvailableManagedRuleGroups.md).

You cannot nest a `ManagedRuleGroupStatement`, for example for use inside a `NotStatement` or `OrStatement`. You cannot use a managed rule group inside another rule group. You can only reference a managed rule group as a top-level statement within a rule that you define in a web ACL.

**Note**
You are charged additional fees when you use the AWS WAF Bot Control managed rule group `AWSManagedRulesBotControlRuleSet`, the AWS WAF Fraud Control account takeover prevention (ATP) managed rule group `AWSManagedRulesATPRuleSet`, or the AWS WAF Fraud Control account creation fraud prevention (ACFP) managed rule group `AWSManagedRulesACFPRuleSet`. For more information, see [AWS WAF Pricing](http://aws.amazon.com/waf/pricing/).

## Contents
<a name="API_ManagedRuleGroupStatement_Contents"></a>

 ** Name **   <a name="WAF-Type-ManagedRuleGroupStatement-Name"></a>
The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: Yes

 ** VendorName **   <a name="WAF-Type-ManagedRuleGroupStatement-VendorName"></a>
The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** ExcludedRules **   <a name="WAF-Type-ManagedRuleGroupStatement-ExcludedRules"></a>
Rules in the referenced rule group whose actions are set to `Count`.
Instead of this option, use `RuleActionOverrides`. It accepts any valid action setting, including `Count`.
Type: Array of [ExcludedRule](API_ExcludedRule.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** ManagedRuleGroupConfigs **   <a name="WAF-Type-ManagedRuleGroupStatement-ManagedRuleGroupConfigs"></a>
Additional information that's used by a managed rule group. Many managed rule groups don't require this.
The rule groups used for intelligent threat mitigation require additional configuration:
+ Use the `AWSManagedRulesACFPRuleSet` configuration object to configure the account creation fraud prevention managed rule group. The configuration includes the registration and sign-up pages of your application and the locations in the account creation request payload of data, such as the user email and phone number fields.
+ Use the `AWSManagedRulesAntiDDoSRuleSet` configuration object to configure the anti-DDoS managed rule group. The configuration includes the sensitivity levels to use in the rules that typically block and challenge requests that might be participating in DDoS attacks and the specification to use to indicate whether a request can handle a silent browser challenge.
+ Use the `AWSManagedRulesATPRuleSet` configuration object to configure the account takeover prevention managed rule group. The configuration includes the sign-in page of your application and the locations in the login request payload of data such as the username and password.
+ Use the `AWSManagedRulesBotControlRuleSet` configuration object to configure the protection level that you want the Bot Control rule group to use.
Type: Array of [ManagedRuleGroupConfig](API_ManagedRuleGroupConfig.md) objects
Required: No

 ** RuleActionOverrides **   <a name="WAF-Type-ManagedRuleGroupStatement-RuleActionOverrides"></a>
Action settings to use in the place of the rule actions that are configured inside the rule group. You specify one override for each rule whose action you want to change.
Verify the rule names in your overrides carefully. With managed rule groups, AWS WAF silently ignores any override that uses an invalid rule name. With customer-owned rule groups, invalid rule names in your overrides will cause web ACL updates to fail. An invalid rule name is any name that doesn't exactly match the case-sensitive name of an existing rule in the rule group.
You can use overrides for testing, for example you can override all of rule actions to `Count` and then monitor the resulting count metrics to understand how the rule group would handle your web traffic. You can also permanently override some or all actions, to modify how the rule group manages your web traffic.
Type: Array of [RuleActionOverride](API_RuleActionOverride.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** ScopeDownStatement **   <a name="WAF-Type-ManagedRuleGroupStatement-ScopeDownStatement"></a>
An optional nested statement that narrows the scope of the web requests that are evaluated by the managed rule group. Requests are only evaluated by the rule group if they match the scope-down statement. You can use any nestable [Statement](API_Statement.md) in the scope-down statement, and you can nest statements at any level, the same as you can for a rule statement.
Type: [Statement](API_Statement.md) object
Required: No

 ** Version **   <a name="WAF-Type-ManagedRuleGroupStatement-Version"></a>
The version of the managed rule group to use. If you specify this, the version setting is fixed until you change it. If you don't specify this, AWS WAF uses the vendor's default version, and then keeps the version at the vendor's default when the vendor updates the managed rule group settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[\w#:\.\-/]+$`
Required: No

## See Also
<a name="API_ManagedRuleGroupStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ManagedRuleGroupStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ManagedRuleGroupStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ManagedRuleGroupStatement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
