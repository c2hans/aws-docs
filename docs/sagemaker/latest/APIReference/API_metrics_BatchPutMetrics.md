---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_metrics_BatchPutMetrics.html
---

# BatchPutMetrics
<a name="API_metrics_BatchPutMetrics"></a>

Used to ingest training metrics into SageMaker. These metrics can be visualized in SageMaker Studio.

## Request Syntax
<a name="API_metrics_BatchPutMetrics_RequestSyntax"></a>

```
PUT /BatchPutMetrics HTTP/1.1
Content-type: application/json

{
   "MetricData": [
      {
         "MetricName": "{{string}}",
         "Step": {{number}},
         "Timestamp": {{number}},
         "Value": {{number}}
      }
   ],
   "TrialComponentName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_metrics_BatchPutMetrics_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_metrics_BatchPutMetrics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MetricData](#API_metrics_BatchPutMetrics_RequestSyntax) **   <a name="sagemaker-metrics_BatchPutMetrics-request-MetricData"></a>
A list of raw metric values to put.
Type: Array of [RawMetricData](API_metrics_RawMetricData.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [TrialComponentName](#API_metrics_BatchPutMetrics_RequestSyntax) **   <a name="sagemaker-metrics_BatchPutMetrics-request-TrialComponentName"></a>
The name of the Trial Component to associate with the metrics. The Trial Component name must be entirely lowercase.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `^[a-z0-9](-*[a-z0-9]){0,119}`
Required: Yes

## Response Syntax
<a name="API_metrics_BatchPutMetrics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Errors": [
      {
         "Code": "string",
         "MetricIndex": number
      }
   ]
}
```

## Response Elements
<a name="API_metrics_BatchPutMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_metrics_BatchPutMetrics_ResponseSyntax) **   <a name="sagemaker-metrics_BatchPutMetrics-response-Errors"></a>
Lists any errors that occur when inserting metric data.
Type: Array of [BatchPutMetricsError](API_metrics_BatchPutMetricsError.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

## Errors
<a name="API_metrics_BatchPutMetrics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_metrics_BatchPutMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-metrics-2022-09-30/BatchPutMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-metrics-2022-09-30/BatchPutMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-metrics-2022-09-30/BatchPutMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-metrics-2022-09-30/BatchPutMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-metrics-2022-09-30/BatchPutMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-metrics-2022-09-30/BatchPutMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-metrics-2022-09-30/BatchPutMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-metrics-2022-09-30/BatchPutMetrics)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-metrics-2022-09-30/BatchPutMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-metrics-2022-09-30/BatchPutMetrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
