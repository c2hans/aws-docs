---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListTelemetryFields.html
---

# ListTelemetryFields
<a name="API_ListTelemetryFields"></a>

Lists fields available for telemetry queries.

Returns a list of fields included in the specified dataset, granular to telemetry type. Returned field names reflect the exact stored casing and are case-sensitive when referenced in query expressions; the query engine does not normalize identifier case.

## Request Parameters
<a name="API_ListTelemetryFields_RequestParameters"></a>

 ** dataSetName **
The name of the dataset to list fields for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** endTime **
Inclusive end of the lookback window. When omitted, the service defaults to the current time.
Type: Timestamp
Required: No

 ** nextToken **
A token to retrieve the next page of results. Reserved for future pagination; the service does not paginate at this time and returns null.
Type: String
Required: No

 ** startTime **
Inclusive start of the lookback window. When omitted, the service defaults to the configured lookback before endTime.
Type: Timestamp
Required: No

 ** telemetryType **
The type of telemetry to filter fields by.
Type: String
Valid Values: `LOGS | TRACES`
Required: No

## Response Elements
<a name="API_ListTelemetryFields_ResponseElements"></a>

The following elements are returned by the service.

 ** fields **
The list of fields available for queries.
Type: Array of [Field](API_Field.md) objects

 ** nextToken **
A token to retrieve the next page of results, or null if there are no more results.
Type: String

## Errors
<a name="API_ListTelemetryFields_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_ListTelemetryFields_Examples"></a>

### List fields for a dataset
<a name="API_ListTelemetryFields_Example_1"></a>

The following example lists the log fields available in the specified dataset. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_ListTelemetryFields_Example_1_Request"></a>

```
{
  "dataSetName": "default",
  "telemetryType": "LOGS"
}
```

#### Sample Response
<a name="API_ListTelemetryFields_Example_1_Response"></a>

```
{
  "fields": [
    {
      "name": "@timestamp"
    },
    {
      "name": "@message"
    },
    {
      "children": [
        {
          "name": "http.method"
        },
        {
          "name": "http.status_code"
        }
      ],
      "name": "attributes"
    }
  ]
}
```

## See Also
<a name="API_ListTelemetryFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/ListTelemetryFields)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/ListTelemetryFields)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/ListTelemetryFields)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/ListTelemetryFields)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/ListTelemetryFields)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/ListTelemetryFields)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/ListTelemetryFields)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/ListTelemetryFields)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/ListTelemetryFields)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/ListTelemetryFields)
