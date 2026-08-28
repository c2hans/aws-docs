---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_TargetTrackingScalingPolicy.html
---

# TargetTrackingScalingPolicy
<a name="API_TargetTrackingScalingPolicy"></a>

A scaling policy for the capacity provider that automatically adjusts capacity to maintain a target value for a specific metric.

## Contents
<a name="API_TargetTrackingScalingPolicy_Contents"></a>

 ** PredefinedMetricType **   <a name="lambda-Type-TargetTrackingScalingPolicy-PredefinedMetricType"></a>
The predefined metric type to track for scaling decisions.
Type: String
Valid Values: `LambdaCapacityProviderAverageCPUUtilization`
Required: Yes

 ** TargetValue **   <a name="lambda-Type-TargetTrackingScalingPolicy-TargetValue"></a>
The target value for the metric that the scaling policy attempts to maintain through scaling actions.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 100.0.
Required: Yes

## See Also
<a name="API_TargetTrackingScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/TargetTrackingScalingPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/TargetTrackingScalingPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/TargetTrackingScalingPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
