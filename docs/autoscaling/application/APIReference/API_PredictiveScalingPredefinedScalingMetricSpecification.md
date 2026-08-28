---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingPredefinedScalingMetricSpecification.html
---

# PredictiveScalingPredefinedScalingMetricSpecification
<a name="API_PredictiveScalingPredefinedScalingMetricSpecification"></a>

 Describes a scaling metric for a predictive scaling policy.

When returned in the output of `DescribePolicies`, it indicates that a predictive scaling policy uses individually specified load and scaling metrics instead of a metric pair.

The following predefined metrics are available for predictive scaling:
+  `ECSServiceAverageCPUUtilization`
+  `ECSServiceAverageMemoryUtilization`
+  `ECSServiceCPUUtilization`
+  `ECSServiceMemoryUtilization`
+  `ECSServiceTotalCPUUtilization`
+  `ECSServiceTotalMemoryUtilization`
+  `ALBRequestCount`
+  `ALBRequestCountPerTarget`
+  `TotalALBRequestCount`

## Contents
<a name="API_PredictiveScalingPredefinedScalingMetricSpecification_Contents"></a>

 ** PredefinedMetricType **   <a name="autoscaling-Type-PredictiveScalingPredefinedScalingMetricSpecification-PredefinedMetricType"></a>
 The metric type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** ResourceLabel **   <a name="autoscaling-Type-PredictiveScalingPredefinedScalingMetricSpecification-ResourceLabel"></a>
 A label that uniquely identifies a specific target group from which to determine the average request count.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Required: No

## See Also
<a name="API_PredictiveScalingPredefinedScalingMetricSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/PredictiveScalingPredefinedScalingMetricSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/PredictiveScalingPredefinedScalingMetricSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/PredictiveScalingPredefinedScalingMetricSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
