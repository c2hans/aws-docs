---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSServiceProjectedUtilizationMetric.html
---

# ECSServiceProjectedUtilizationMetric
<a name="API_ECSServiceProjectedUtilizationMetric"></a>

 Describes the projected utilization metrics of an Amazon ECS service recommendation option.

To determine the performance difference between your current Amazon ECS service and the recommended option, compare the utilization metric data of your service against its projected utilization metric data.

## Contents
<a name="API_ECSServiceProjectedUtilizationMetric_Contents"></a>

 ** lowerBoundValue **   <a name="computeoptimizer-Type-ECSServiceProjectedUtilizationMetric-lowerBoundValue"></a>
 The lower bound values for the projected utilization metrics.
Type: Double
Required: No

 ** name **   <a name="computeoptimizer-Type-ECSServiceProjectedUtilizationMetric-name"></a>
 The name of the projected utilization metric.
The following utilization metrics are available:
+  `Cpu` — The percentage of allocated compute units that are currently in use on the service tasks.
+  `Memory` — The percentage of memory that's currently in use on the service tasks.
Type: String
Valid Values: `Cpu | Memory`
Required: No

 ** statistic **   <a name="computeoptimizer-Type-ECSServiceProjectedUtilizationMetric-statistic"></a>
The statistic of the projected utilization metric.
The Compute Optimizer API, AWS Command Line Interface (AWS CLI), and SDKs return utilization metrics using only the `Maximum` statistic, which is the highest value observed during the specified period.
The Compute Optimizer console displays graphs for some utilization metrics using the `Average` statistic, which is the value of `Sum` / `SampleCount` during the specified period. For more information, see [Viewing resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html) in the * AWS Compute Optimizer User Guide*. You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).
Type: String
Valid Values: `Maximum | Average`
Required: No

 ** upperBoundValue **   <a name="computeoptimizer-Type-ECSServiceProjectedUtilizationMetric-upperBoundValue"></a>
 The upper bound values for the projected utilization metrics.
Type: Double
Required: No

## See Also
<a name="API_ECSServiceProjectedUtilizationMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/ECSServiceProjectedUtilizationMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/ECSServiceProjectedUtilizationMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/ECSServiceProjectedUtilizationMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
