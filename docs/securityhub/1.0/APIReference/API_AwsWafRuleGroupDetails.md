---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafRuleGroupDetails.html
---

# AwsWafRuleGroupDetails
<a name="API_AwsWafRuleGroupDetails"></a>

Provides information about an AWS WAF rule group. A rule group is a collection of rules for inspecting and controlling web requests.

## Contents
<a name="API_AwsWafRuleGroupDetails_Contents"></a>

 ** MetricName **   <a name="securityhub-Type-AwsWafRuleGroupDetails-MetricName"></a>
The name of the metrics for this rule group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsWafRuleGroupDetails-Name"></a>
The name of the rule group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleGroupId **   <a name="securityhub-Type-AwsWafRuleGroupDetails-RuleGroupId"></a>
The ID of the rule group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Rules **   <a name="securityhub-Type-AwsWafRuleGroupDetails-Rules"></a>
Provides information about the rules attached to the rule group. These rules identify the web requests that you want to allow, block, or count.
Type: Array of [AwsWafRuleGroupRulesDetails](API_AwsWafRuleGroupRulesDetails.md) objects
Required: No

## See Also
<a name="API_AwsWafRuleGroupDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafRuleGroupDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafRuleGroupDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafRuleGroupDetails)
