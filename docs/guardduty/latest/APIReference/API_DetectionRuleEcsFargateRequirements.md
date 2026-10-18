---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectionRuleEcsFargateRequirements.html
---

# DetectionRuleEcsFargateRequirements
<a name="API_DetectionRuleEcsFargateRequirements"></a>

The requirements for running a Runtime Monitoring custom detection rule on Amazon ECS with the Fargate launch type.

## Contents
<a name="API_DetectionRuleEcsFargateRequirements_Contents"></a>

 ** minAgentVersion **   <a name="guardduty-Type-DetectionRuleEcsFargateRequirements-minAgentVersion"></a>
The minimum GuardDuty agent version required to run the rule on Amazon ECS with the Fargate launch type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9]+(\.[0-9]+){1,3}`
Required: No

## See Also
<a name="API_DetectionRuleEcsFargateRequirements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DetectionRuleEcsFargateRequirements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DetectionRuleEcsFargateRequirements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DetectionRuleEcsFargateRequirements)
