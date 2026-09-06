---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_metrics_BatchPutMetricsError.html
---

# BatchPutMetricsError
<a name="API_metrics_BatchPutMetricsError"></a>

An error that occured when putting the metric data.

## Contents
<a name="API_metrics_BatchPutMetricsError_Contents"></a>

 ** Code **   <a name="sagemaker-Type-metrics_BatchPutMetricsError-Code"></a>
The error code of an error that occured when attempting to put metrics.
+  `METRIC_LIMIT_EXCEEDED`: The maximum amount of metrics per resource is exceeded.
+  `INTERNAL_ERROR`: An internal error occured.
+  `VALIDATION_ERROR`: The metric data failed validation.
+  `CONFLICT_ERROR`: Multiple requests attempted to modify the same data simultaneously.
Type: String
Valid Values: `METRIC_LIMIT_EXCEEDED | INTERNAL_ERROR | VALIDATION_ERROR | CONFLICT_ERROR`
Required: No

 ** MetricIndex **   <a name="sagemaker-Type-metrics_BatchPutMetricsError-MetricIndex"></a>
An index that corresponds to the metric in the request.
Type: Integer
Required: No

## See Also
<a name="API_metrics_BatchPutMetricsError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-metrics-2022-09-30/BatchPutMetricsError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-metrics-2022-09-30/BatchPutMetricsError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-metrics-2022-09-30/BatchPutMetricsError)
