---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Metric.html
---

# Metric
<a name="API_Metric"></a>

The representation of a metric.

## Contents
<a name="API_Metric_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MetricQuery **
The query to retrieve metric data points.
Type: [MetricQuery](API_MetricQuery.md) object
Required: No

 ** Name **
The name of a metric.
Type: String
Required: No

 ** References.member.N **
A list of metric references (thresholds).
Type: Array of [MetricReference](API_MetricReference.md) objects
Required: No

 ** StatisticsDetails **
The details of different statistics for a metric. The description might contain markdown.
Type: String
Required: No

## See Also
<a name="API_Metric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/Metric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/Metric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/Metric)
