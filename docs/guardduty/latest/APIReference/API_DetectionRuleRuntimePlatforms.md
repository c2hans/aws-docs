---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectionRuleRuntimePlatforms.html
---

# DetectionRuleRuntimePlatforms
<a name="API_DetectionRuleRuntimePlatforms"></a>

The platforms on which a Runtime Monitoring custom detection rule can run. A member's presence is the support statement: when present, the rule runs on that platform and `minAgentVersion` is the minimum GuardDuty agent version required there. When absent, the rule cannot run on that platform at any agent version.

## Contents
<a name="API_DetectionRuleRuntimePlatforms_Contents"></a>

 ** ec2 **   <a name="guardduty-Type-DetectionRuleRuntimePlatforms-ec2"></a>
The requirements for running the rule on Amazon EC2.
Type: [DetectionRuleEc2Requirements](API_DetectionRuleEc2Requirements.md) object
Required: No

 ** ecsFargate **   <a name="guardduty-Type-DetectionRuleRuntimePlatforms-ecsFargate"></a>
The requirements for running the rule on Amazon ECS with the Fargate launch type.
Type: [DetectionRuleEcsFargateRequirements](API_DetectionRuleEcsFargateRequirements.md) object
Required: No

 ** eks **   <a name="guardduty-Type-DetectionRuleRuntimePlatforms-eks"></a>
The requirements for running the rule on Amazon EKS.
Type: [DetectionRuleEksRequirements](API_DetectionRuleEksRequirements.md) object
Required: No

## See Also
<a name="API_DetectionRuleRuntimePlatforms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DetectionRuleRuntimePlatforms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DetectionRuleRuntimePlatforms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DetectionRuleRuntimePlatforms)
