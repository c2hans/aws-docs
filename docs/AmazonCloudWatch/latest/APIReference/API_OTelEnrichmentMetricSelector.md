---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_OTelEnrichmentMetricSelector.html
---

# OTelEnrichmentMetricSelector
<a name="API_OTelEnrichmentMetricSelector"></a>

Selects the metrics in one namespace, for use in the `IncludeFilters` or `ExcludeFilters` parameter of [StartOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StartOTelEnrichment.html) or [UpdateOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateOTelEnrichment.html).

A maximum of 100 selectors is allowed across `IncludeFilters` and `ExcludeFilters` combined.

## Contents
<a name="API_OTelEnrichmentMetricSelector_Contents"></a>

 ** Namespace **   <a name="ACW-Type-OTelEnrichmentMetricSelector-Namespace"></a>
The namespace of the metrics to select. Namespaces are matched exactly and are case-sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^:].*`
Required: Yes

 ** MetricNames **   <a name="ACW-Type-OTelEnrichmentMetricSelector-MetricNames"></a>
The names of the metrics to select within the namespace. Metric names are matched exactly and are case-sensitive. If this parameter is omitted, every metric in the namespace is selected.
A maximum of 100 metric names is allowed for each selector.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_OTelEnrichmentMetricSelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/OTelEnrichmentMetricSelector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/OTelEnrichmentMetricSelector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/OTelEnrichmentMetricSelector)
