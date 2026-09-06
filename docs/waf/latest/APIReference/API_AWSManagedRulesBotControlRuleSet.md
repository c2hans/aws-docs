---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_AWSManagedRulesBotControlRuleSet.html
---

# AWSManagedRulesBotControlRuleSet
<a name="API_AWSManagedRulesBotControlRuleSet"></a>

Details for your use of the Bot Control managed rule group, `AWSManagedRulesBotControlRuleSet`. This configuration is used in `ManagedRuleGroupConfig`.

For additional information about this and the other intelligent threat mitigation rule groups, see [Intelligent threat mitigation in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections) and [AWS Managed Rules rule groups list](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list) in the * AWS WAF Developer Guide*.

## Contents
<a name="API_AWSManagedRulesBotControlRuleSet_Contents"></a>

 ** InspectionLevel **   <a name="WAF-Type-AWSManagedRulesBotControlRuleSet-InspectionLevel"></a>
The inspection level to use for the Bot Control rule group. The common level is the least expensive. The targeted level includes all common level rules and adds rules with more advanced inspection criteria. For details, see [AWS WAF Bot Control rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html) in the * AWS WAF Developer Guide*.
Type: String
Valid Values: `COMMON | TARGETED`
Required: Yes

 ** EnableMachineLearning **   <a name="WAF-Type-AWSManagedRulesBotControlRuleSet-EnableMachineLearning"></a>
Applies only to the targeted inspection level.
Determines whether to use machine learning (ML) to analyze your web traffic for bot-related activity. Machine learning is required for the Bot Control rules `TGT_ML_CoordinatedActivityLow` and `TGT_ML_CoordinatedActivityMedium`, which inspect for anomalous behavior that might indicate distributed, coordinated bot activity.
For more information about this choice, see the listing for these rules in the table at [Bot Control rules listing](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html#aws-managed-rule-groups-bot-rules) in the * AWS WAF Developer Guide*.
Default: `TRUE`
Type: Boolean
Required: No

## See Also
<a name="API_AWSManagedRulesBotControlRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/AWSManagedRulesBotControlRuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/AWSManagedRulesBotControlRuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/AWSManagedRulesBotControlRuleSet)
