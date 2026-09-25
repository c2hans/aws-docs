---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetTelemetryQueryResults.html
---

# GetTelemetryQueryResults
<a name="API_GetTelemetryQueryResults"></a>

Returns the results for the specified query.

## Request Parameters
<a name="API_GetTelemetryQueryResults_RequestParameters"></a>

 ** maxResults **
The maximum number of result rows to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** nextToken **
A token to retrieve the next page of results.
Type: String
Required: No

 ** queryId **
The unique ID of the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

## Response Elements
<a name="API_GetTelemetryQueryResults_ResponseElements"></a>

The following elements are returned by the service.

 ** nextToken **
A token to retrieve the next page of results, or null if there are no more results.
Type: String

 ** rows **
The result rows returned by the query.
Type: Array of string to string maps

 ** statistics **
Statistics about the query execution.
Type: [QueryStatistics](API_QueryStatistics.md) object

 ** status **
The current execution status of the query.
Type: String
Valid Values: `Running | Failed | Complete | Cancelled`

## Errors
<a name="API_GetTelemetryQueryResults_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** errorCode **
The error code associated with the internal error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** errorCode **
The error code associated with the failure.
 ** resourceId **
The identifier of the resource that could not be found. Not always present.
 ** resourceType **
The type of the resource that could not be found. Not always present.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled due to exceeding the allowed request rate.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request. Not always present.
HTTP Status Code: 429

 ** ValidationException **
A parameter is specified incorrectly.
 ** errorCode **
The error code associated with the validation failure.
HTTP Status Code: 400

## Examples
<a name="API_GetTelemetryQueryResults_Examples"></a>

### Get telemetry query results
<a name="API_GetTelemetryQueryResults_Example_1"></a>

The following example retrieves a page of results for a completed query, along with execution statistics. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_GetTelemetryQueryResults_Example_1_Request"></a>

```
{
  "maxResults": 100,
  "queryId": "3b2a1c0d-7e6f-4a5b-8c9d-0e1f2a3b4c5d"
}
```

#### Sample Response
<a name="API_GetTelemetryQueryResults_Example_1_Response"></a>

```
{
  "rows": [
    {
      "error_count": "42",
      "service.name": "checkout-service"
    },
    {
      "error_count": "7",
      "service.name": "payments-service"
    }
  ],
  "statistics": {
    "bytesScanned": 1048576.0,
    "partialResults": {
      "partialResultsDetected": false
    },
    "percentComplete": 100,
    "recordsMatched": 49,
    "recordsScanned": 20000
  },
  "status": "Complete"
}
```

## See Also
<a name="API_GetTelemetryQueryResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/GetTelemetryQueryResults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/GetTelemetryQueryResults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/GetTelemetryQueryResults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/GetTelemetryQueryResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/GetTelemetryQueryResults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/GetTelemetryQueryResults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/GetTelemetryQueryResults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/GetTelemetryQueryResults)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/GetTelemetryQueryResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/GetTelemetryQueryResults)
