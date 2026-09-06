---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_UtilizationPreference.html
---

# UtilizationPreference
<a name="API_UtilizationPreference"></a>

 The preference to control the resource’s CPU utilization threshold, CPU utilization headroom, and memory utilization headroom.

**Note**
This preference is only available for the Amazon EC2 instance resource type.

## Contents
<a name="API_UtilizationPreference_Contents"></a>

 ** metricName **   <a name="computeoptimizer-Type-UtilizationPreference-metricName"></a>
 The name of the resource utilization metric name to customize.
Type: String
Valid Values: `CpuUtilization | MemoryUtilization`
Required: No

 ** metricParameters **   <a name="computeoptimizer-Type-UtilizationPreference-metricParameters"></a>
 The parameters to set when customizing the resource utilization thresholds.
Type: [CustomizableMetricParameters](API_CustomizableMetricParameters.md) object
Required: No

## See Also
<a name="API_UtilizationPreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/UtilizationPreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/UtilizationPreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/UtilizationPreference)
