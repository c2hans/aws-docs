---
source_url: https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ScalingPolicy.html
---

# ScalingPolicy
<a name="API_ScalingPolicy"></a>

Represents a scaling policy.

## Contents
<a name="API_ScalingPolicy_Contents"></a>

 ** PolicyName **   <a name="autoscaling-Type-ScalingPolicy-PolicyName"></a>
The name of the scaling policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\p{Print}+`
Required: Yes

 ** PolicyType **   <a name="autoscaling-Type-ScalingPolicy-PolicyType"></a>
The type of scaling policy.
Type: String
Valid Values: `TargetTrackingScaling`
Required: Yes

 ** TargetTrackingConfiguration **   <a name="autoscaling-Type-ScalingPolicy-TargetTrackingConfiguration"></a>
The target tracking scaling policy. Includes support for predefined or customized metrics.
Type: [TargetTrackingConfiguration](API_TargetTrackingConfiguration.md) object
Required: No

## See Also
<a name="API_ScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-plans-2018-01-06/ScalingPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-plans-2018-01-06/ScalingPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-plans-2018-01-06/ScalingPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
