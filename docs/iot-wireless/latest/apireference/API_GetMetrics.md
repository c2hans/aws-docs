---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetMetrics.html
---

# GetMetrics
<a name="API_GetMetrics"></a>

Get the summary metrics for this AWS account.

## Request Syntax
<a name="API_GetMetrics_RequestSyntax"></a>

```
POST /metrics HTTP/1.1
Content-type: application/json

{
   "SummaryMetricQueries": [
      {
         "AggregationPeriod": "{{string}}",
         "Dimensions": [
            {
               "name": "{{string}}",
               "value": "{{string}}"
            }
         ],
         "EndTimestamp": {{number}},
         "MetricName": "{{string}}",
         "QueryId": "{{string}}",
         "StartTimestamp": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_GetMetrics_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetMetrics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SummaryMetricQueries](#API_GetMetrics_RequestSyntax) **   <a name="iotwireless-GetMetrics-request-SummaryMetricQueries"></a>
The list of queries to retrieve the summary metrics.
Type: Array of [SummaryMetricQuery](API_SummaryMetricQuery.md) objects
Required: No

## Response Syntax
<a name="API_GetMetrics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "SummaryMetricQueryResults": [
      {
         "AggregationPeriod": "string",
         "Dimensions": [
            {
               "name": "string",
               "value": "string"
            }
         ],
         "EndTimestamp": number,
         "Error": "string",
         "MetricName": "string",
         "QueryId": "string",
         "QueryStatus": "string",
         "StartTimestamp": number,
         "Timestamps": [ number ],
         "Unit": "string",
         "Values": [
            {
               "Avg": number,
               "Max": number,
               "Min": number,
               "P90": number,
               "Std": number,
               "Sum": number
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SummaryMetricQueryResults](#API_GetMetrics_ResponseSyntax) **   <a name="iotwireless-GetMetrics-response-SummaryMetricQueryResults"></a>
The list of summary metrics that were retrieved.
Type: Array of [SummaryMetricQueryResult](API_SummaryMetricQueryResult.md) objects

## Errors
<a name="API_GetMetrics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Adding, updating, or deleting the resource can cause an inconsistent state.
 ** ResourceId **
Id of the resource in the conflicting operation.
 ** ResourceType **
Type of the resource in the conflicting operation.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource does not exist.
 ** ResourceId **
Id of the not found resource.
 ** ResourceType **
Type of the font found resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_GetMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetMetrics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetMetrics)
