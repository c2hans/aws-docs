---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_Rule.html
---

# Rule
<a name="API_Rule"></a>

A rule contains conditions, "unless conditions" and actions. For each envelope recipient of an email, if all conditions match and none of the "unless conditions" match, then all of the actions are executed sequentially. If no conditions are provided, the rule always applies and the actions are implicitly executed. If only "unless conditions" are provided, the rule applies if the email does not match the evaluation of the "unless conditions".

## Contents
<a name="API_Rule_Contents"></a>

 ** Actions **   <a name="sesmailmanager-Type-Rule-Actions"></a>
The list of actions to execute when the conditions match the incoming email, and none of the "unless conditions" match.
Type: Array of [RuleAction](API_RuleAction.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** Conditions **   <a name="sesmailmanager-Type-Rule-Conditions"></a>
The conditions of this rule. All conditions must match the email for the actions to be executed. An empty list of conditions means that all emails match, but are still subject to any "unless conditions"
Type: Array of [RuleCondition](API_RuleCondition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** Name **   <a name="sesmailmanager-Type-Rule-Name"></a>
The user-friendly name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** Unless **   <a name="sesmailmanager-Type-Rule-Unless"></a>
The "unless conditions" of this rule. None of the conditions can match the email for the actions to be executed. If any of these conditions do match the email, then the actions are not executed.
Type: Array of [RuleCondition](API_RuleCondition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_Rule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/Rule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/Rule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/Rule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
