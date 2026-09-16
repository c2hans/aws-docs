---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_metrics_BatchGetMetrics.html
---

# BatchGetMetrics
<a name="API_metrics_BatchGetMetrics"></a>

Used to retrieve training metrics from SageMaker.

## Request Syntax
<a name="API_metrics_BatchGetMetrics_RequestSyntax"></a>

```
POST /BatchGetMetrics HTTP/1.1
Content-type: application/json

{
   "MetricQueries": [
      {
         "End": {{number}},
         "MetricName": "{{string}}",
         "MetricStat": "{{string}}",
         "Period": "{{string}}",
         "ResourceArn": "{{string}}",
         "Start": {{number}},
         "XAxisType": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_metrics_BatchGetMetrics_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_metrics_BatchGetMetrics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MetricQueries](#API_metrics_BatchGetMetrics_RequestSyntax) **   <a name="sagemaker-metrics_BatchGetMetrics-request-MetricQueries"></a>
Queries made to retrieve training metrics from SageMaker.
Type: Array of [MetricQuery](API_metrics_MetricQuery.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_metrics_BatchGetMetrics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MetricQueryResults": [
      {
         "Message": "string",
         "MetricValues": [ number ],
         "Status": "string",
         "XAxisValues": [ number ]
      }
   ]
}
```

## Response Elements
<a name="API_metrics_BatchGetMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MetricQueryResults](#API_metrics_BatchGetMetrics_ResponseSyntax) **   <a name="sagemaker-metrics_BatchGetMetrics-response-MetricQueryResults"></a>
The results of a query to retrieve training metrics from SageMaker.
Type: Array of [MetricQueryResult](API_metrics_MetricQueryResult.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

## Errors
<a name="API_metrics_BatchGetMetrics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_metrics_BatchGetMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-metrics-2022-09-30/BatchGetMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-metrics-2022-09-30/BatchGetMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-metrics-2022-09-30/BatchGetMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-metrics-2022-09-30/BatchGetMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-metrics-2022-09-30/BatchGetMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-metrics-2022-09-30/BatchGetMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-metrics-2022-09-30/BatchGetMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-metrics-2022-09-30/BatchGetMetrics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-metrics-2022-09-30/BatchGetMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-metrics-2022-09-30/BatchGetMetrics)
