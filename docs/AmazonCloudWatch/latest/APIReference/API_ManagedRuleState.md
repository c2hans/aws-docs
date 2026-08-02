---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ManagedRuleState.html
---

# ManagedRuleState
<a name="API_ManagedRuleState"></a>

 The status of a managed Contributor Insights rule.

## Contents
<a name="API_ManagedRuleState_Contents"></a>

 ** RuleName **   <a name="ACW-Type-ManagedRuleState-RuleName"></a>
 The name of the Contributor Insights rule that contains data for the specified AWS resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x20-\x7E]+`
Required: Yes

 ** State **   <a name="ACW-Type-ManagedRuleState-State"></a>
 Indicates whether the rule is enabled or disabled.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\x20-\x7E]+`
Required: Yes

## See Also
<a name="API_ManagedRuleState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ManagedRuleState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ManagedRuleState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ManagedRuleState)
