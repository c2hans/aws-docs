---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSServiceProjectedMetric.html
---

# ECSServiceProjectedMetric
<a name="API_ECSServiceProjectedMetric"></a>

 Describes the projected metrics of an Amazon ECS service recommendation option.

To determine the performance difference between your current Amazon ECS service and the recommended option, compare the metric data of your service against its projected metric data.

## Contents
<a name="API_ECSServiceProjectedMetric_Contents"></a>

 ** lowerBoundValues **   <a name="computeoptimizer-Type-ECSServiceProjectedMetric-lowerBoundValues"></a>
 The lower bound values for the projected metric.
Type: Array of doubles
Required: No

 ** name **   <a name="computeoptimizer-Type-ECSServiceProjectedMetric-name"></a>
 The name of the projected metric.
The following metrics are available:
+  `Cpu` — The percentage of allocated compute units that are currently in use on the service tasks.
+  `Memory` — The percentage of memory that's currently in use on the service tasks.
Type: String
Valid Values: `Cpu | Memory`
Required: No

 ** timestamps **   <a name="computeoptimizer-Type-ECSServiceProjectedMetric-timestamps"></a>
 The timestamps of the projected metric.
Type: Array of timestamps
Required: No

 ** upperBoundValues **   <a name="computeoptimizer-Type-ECSServiceProjectedMetric-upperBoundValues"></a>
 The upper bound values for the projected metric.
Type: Array of doubles
Required: No

## See Also
<a name="API_ECSServiceProjectedMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/ECSServiceProjectedMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/ECSServiceProjectedMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/ECSServiceProjectedMetric)
