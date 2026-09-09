---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ResourceMetricSelection.html
---

# ResourceMetricSelection
<a name="API_ResourceMetricSelection"></a>

Specifies which metrics Amazon CloudWatch collects for a resource metrics configuration. Include this in a [CreateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_CreateResourceMetricsConfiguration.html) or [UpdateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateResourceMetricsConfiguration.html) request to limit collection to a specific set of metrics. If you omit metric selections, Amazon CloudWatch collects all available detailed metrics for the resource.

## Contents
<a name="API_ResourceMetricSelection_Contents"></a>

 ** IncludeMetrics **   <a name="ACW-Type-ResourceMetricSelection-IncludeMetrics"></a>
The names of the metrics to collect for the resource. Amazon CloudWatch collects only the metrics that you list here.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_ResourceMetricSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ResourceMetricSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ResourceMetricSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ResourceMetricSelection)
