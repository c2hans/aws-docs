---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ManagedRuleSetVersion.html
---

# ManagedRuleSetVersion
<a name="API_ManagedRuleSetVersion"></a>

Information for a single version of a managed rule set.

**Note**
This is intended for use only by vendors of managed rule sets. Vendors are AWS and AWS Marketplace sellers.
Vendors, you can use the managed rule set APIs to provide controlled rollout of your versioned managed rule group offerings for your customers. The APIs are `ListManagedRuleSets`, `GetManagedRuleSet`, `PutManagedRuleSetVersions`, and `UpdateManagedRuleSetVersionExpiryDate`.

## Contents
<a name="API_ManagedRuleSetVersion_Contents"></a>

 ** AssociatedRuleGroupArn **   <a name="WAF-Type-ManagedRuleSetVersion-AssociatedRuleGroupArn"></a>
The Amazon Resource Name (ARN) of the vendor rule group that's used to define the published version of your managed rule group.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** Capacity **   <a name="WAF-Type-ManagedRuleSetVersion-Capacity"></a>
The web ACL capacity units (WCUs) required for this rule group.
 AWS WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. AWS WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see [AWS WAF web ACL capacity units (WCU)](https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html) in the * AWS WAF Developer Guide*.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** ExpiryTimestamp **   <a name="WAF-Type-ManagedRuleSetVersion-ExpiryTimestamp"></a>
The time that this version is set to expire.
Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, "2016-09-27T14:50Z".
Type: Timestamp
Required: No

 ** ForecastedLifetime **   <a name="WAF-Type-ManagedRuleSetVersion-ForecastedLifetime"></a>
The amount of time you expect this version of your managed rule group to last, in days.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** LastUpdateTimestamp **   <a name="WAF-Type-ManagedRuleSetVersion-LastUpdateTimestamp"></a>
The last time that you updated this version.
Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, "2016-09-27T14:50Z".
Type: Timestamp
Required: No

 ** PublishTimestamp **   <a name="WAF-Type-ManagedRuleSetVersion-PublishTimestamp"></a>
The time that you first published this version.
Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, "2016-09-27T14:50Z".
Type: Timestamp
Required: No

## See Also
<a name="API_ManagedRuleSetVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ManagedRuleSetVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ManagedRuleSetVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ManagedRuleSetVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
