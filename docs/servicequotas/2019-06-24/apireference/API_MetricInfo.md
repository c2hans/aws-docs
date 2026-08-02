---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_MetricInfo.html
---

# MetricInfo
<a name="API_MetricInfo"></a>

Information about the CloudWatch metric that reflects quota usage.

## Contents
<a name="API_MetricInfo_Contents"></a>

 ** MetricDimensions **   <a name="servicequotas-Type-MetricInfo-MetricDimensions"></a>
The metric dimension. This is a name/value pair that is part of the identity of a metric.
Type: String to string map
Map Entries: Maximum number of 10 items.
Required: No

 ** MetricName **   <a name="servicequotas-Type-MetricInfo-MetricName"></a>
The name of the metric.
Type: String
Required: No

 ** MetricNamespace **   <a name="servicequotas-Type-MetricInfo-MetricNamespace"></a>
The namespace of the metric.
Type: String
Required: No

 ** MetricStatisticRecommendation **   <a name="servicequotas-Type-MetricInfo-MetricStatisticRecommendation"></a>
The metric statistic that we recommend you use when determining quota usage.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(Sum|Maximum)`
Required: No

## See Also
<a name="API_MetricInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/MetricInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/MetricInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/MetricInfo)
