---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_MetricFilter.html
---

# MetricFilter
<a name="API_MetricFilter"></a>

Metric filters express how CloudWatch Logs would extract metric observations from ingested log events and transform them into metric data in a CloudWatch metric.

## Contents
<a name="API_MetricFilter_Contents"></a>

 ** applyOnTransformedLogs **   <a name="CWL-Type-MetricFilter-applyOnTransformedLogs"></a>
This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see [PutTransformer](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html).
If this value is `true`, the metric filter is applied on the transformed version of the log events instead of the original ingested log events.
Type: Boolean
Required: No

 ** creationTime **   <a name="CWL-Type-MetricFilter-creationTime"></a>
The creation time of the metric filter, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** emitSystemFieldDimensions **   <a name="CWL-Type-MetricFilter-emitSystemFieldDimensions"></a>
The list of system fields that are emitted as additional dimensions in the generated metrics. Returns the `emitSystemFieldDimensions` value if it was specified when the metric filter was created.
Type: Array of strings
Required: No

 ** fieldSelectionCriteria **   <a name="CWL-Type-MetricFilter-fieldSelectionCriteria"></a>
The filter expression that specifies which log events are processed by this metric filter based on system fields. Returns the `fieldSelectionCriteria` value if it was specified when the metric filter was created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** filterName **   <a name="CWL-Type-MetricFilter-filterName"></a>
The name of the metric filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

 ** filterPattern **   <a name="CWL-Type-MetricFilter-filterPattern"></a>
A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event can contain timestamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** logGroupName **   <a name="CWL-Type-MetricFilter-logGroupName"></a>
The name of the log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** metricTransformations **   <a name="CWL-Type-MetricFilter-metricTransformations"></a>
The metric transformations.
Type: Array of [MetricTransformation](API_MetricTransformation.md) objects
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_MetricFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/MetricFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/MetricFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/MetricFilter)
