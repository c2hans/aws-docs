---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredictiveScalingCustomizedScalingMetric.html
---

# PredictiveScalingCustomizedScalingMetric
<a name="API_PredictiveScalingCustomizedScalingMetric"></a>

Describes a custom scaling metric for a predictive scaling policy.

## Contents
<a name="API_PredictiveScalingCustomizedScalingMetric_Contents"></a>

 ** MetricDataQueries.member.N **
One or more metric data queries to provide the data points for a scaling metric. Use multiple metric data queries only if you are performing a math expression on returned data.
Type: Array of [MetricDataQuery](API_MetricDataQuery.md) objects
Required: Yes

## See Also
<a name="API_PredictiveScalingCustomizedScalingMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/PredictiveScalingCustomizedScalingMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/PredictiveScalingCustomizedScalingMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/PredictiveScalingCustomizedScalingMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
