---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html
---

# RuleGroup
<a name="API_RuleGroup"></a>

 A rule group defines a collection of rules to inspect and control web requests that you can use in a [WebACL](API_WebACL.md). When you create a rule group, you define an immutable capacity limit. If you update a rule group, you must stay within the capacity. This allows others to reuse the rule group with confidence in its capacity requirements.

## Contents
<a name="API_RuleGroup_Contents"></a>

 ** ARN **   <a name="WAF-Type-RuleGroup-ARN"></a>
The Amazon Resource Name (ARN) of the entity.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: Yes

 ** Capacity **   <a name="WAF-Type-RuleGroup-Capacity"></a>
The web ACL capacity units (WCUs) required for this rule group.
When you create your own rule group, you define this, and you cannot change it after creation. When you add or modify the rules in a rule group, AWS WAF enforces this limit. You can check the capacity for a set of rules using [CheckCapacity](API_CheckCapacity.md).
 AWS WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. AWS WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see [AWS WAF web ACL capacity units (WCU)](https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html) in the * AWS WAF Developer Guide*.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

 ** Id **   <a name="WAF-Type-RuleGroup-Id"></a>
A unique identifier for the rule group. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: Yes

 ** Name **   <a name="WAF-Type-RuleGroup-Name"></a>
The name of the rule group. You cannot change the name of a rule group after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: Yes

 ** VisibilityConfig **   <a name="WAF-Type-RuleGroup-VisibilityConfig"></a>
Defines and enables Amazon CloudWatch metrics and web request sample collection.
Type: [VisibilityConfig](API_VisibilityConfig.md) object
Required: Yes

 ** AvailableLabels **   <a name="WAF-Type-RuleGroup-AvailableLabels"></a>
The labels that one or more rules in this rule group add to matching web requests. These labels are defined in the `RuleLabels` for a [Rule](API_Rule.md).
Type: Array of [LabelSummary](API_LabelSummary.md) objects
Required: No

 ** ConsumedLabels **   <a name="WAF-Type-RuleGroup-ConsumedLabels"></a>
The labels that one or more rules in this rule group match against in label match statements. These labels are defined in a `LabelMatchStatement` specification, in the [Statement](API_Statement.md) definition of a rule.
Type: Array of [LabelSummary](API_LabelSummary.md) objects
Required: No

 ** CustomResponseBodies **   <a name="WAF-Type-RuleGroup-CustomResponseBodies"></a>
A map of custom response keys and content bodies. When you create a rule with a block action, you can send a custom response to the web request. You define these for the rule group, and then use them in the rules that you define in the rule group.
For information about customizing web requests and responses, see [Customizing web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the * AWS WAF Developer Guide*.
For information about the limits on count and size for custom request and response settings, see [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the * AWS WAF Developer Guide*.
Type: String to [CustomResponseBody](API_CustomResponseBody.md) object map
Map Entries: Maximum number of items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^[\w\-]+$`
Required: No

 ** Description **   <a name="WAF-Type-RuleGroup-Description"></a>
A description of the rule group that helps with identification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=:#@/\-,\.][\w+=:#@/\-,\.\s]+[\w+=:#@/\-,\.]$`
Required: No

 ** LabelNamespace **   <a name="WAF-Type-RuleGroup-LabelNamespace"></a>
The label namespace prefix for this rule group. All labels added by rules in this rule group have this prefix.
+ The syntax for the label namespace prefix for your rule groups is the following:

   `awswaf:<account ID>:rulegroup:<rule group name>:`
+ When a rule with a label matches a web request, AWS WAF adds the fully qualified label to the request. A fully qualified label is made up of the label namespace from the rule group or web ACL where the rule is defined and the label from the rule, separated by a colon:

   `<label namespace>:<label from rule>`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9A-Za-z_\-:]+$`
Required: No

 ** MonetizationConfig **   <a name="WAF-Type-RuleGroup-MonetizationConfig"></a>
The monetization configuration for the rule group. Required when any rule in the rule group uses the `Monetize` action. When a rule group with a `MonetizationConfig` is used in a web ACL, the rule group's configuration applies to rules within that group unless overridden at the web ACL level.
Type: [MonetizationConfig](API_MonetizationConfig.md) object
Required: No

 ** Rules **   <a name="WAF-Type-RuleGroup-Rules"></a>
The [Rule](API_Rule.md) statements used to identify the web requests that you want to manage. Each rule includes one top-level statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.
Type: Array of [Rule](API_Rule.md) objects
Required: No

## See Also
<a name="API_RuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RuleGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RuleGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RuleGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
