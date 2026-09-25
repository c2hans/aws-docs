---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListTelemetryQuerySessions.html
---

# ListTelemetryQuerySessions
<a name="API_ListTelemetryQuerySessions"></a>

Lists telemetry query sessions.

Returns a list of telemetry query sessions owned by the caller.

## Request Parameters
<a name="API_ListTelemetryQuerySessions_RequestParameters"></a>

 ** maxResults **
The maximum number of sessions to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** nextToken **
A token to retrieve the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_ListTelemetryQuerySessions_ResponseElements"></a>

The following elements are returned by the service.

 ** nextToken **
A token to retrieve the next page of results, or null if there are no more results.
Type: String

 ** sessions **
The list of session summaries.
Type: Array of [SessionSummary](API_SessionSummary.md) objects

## Errors
<a name="API_ListTelemetryQuerySessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** errorCode **
The error code associated with the internal error.
HTTP Status Code: 500

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
<a name="API_ListTelemetryQuerySessions_Examples"></a>

### List telemetry query sessions
<a name="API_ListTelemetryQuerySessions_Example_1"></a>

The following example lists the query sessions owned by the caller. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_ListTelemetryQuerySessions_Example_1_Request"></a>

```
{
  "maxResults": 10
}
```

#### Sample Response
<a name="API_ListTelemetryQuerySessions_Example_1_Response"></a>

```
{
  "nextToken": "eyJvZmZzZXQiOjEwfQ==",
  "sessions": [
    {
      "createdAt": "2026-09-16T00:00:00Z",
      "lastActivityAt": "2026-09-16T00:05:00Z",
      "sessionId": "9f8c7d6e-5b4a-4c3d-9e2f-1a0b2c3d4e5f",
      "sessionName": "prod-latency-investigation"
    }
  ]
}
```

## See Also
<a name="API_ListTelemetryQuerySessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/ListTelemetryQuerySessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/ListTelemetryQuerySessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/ListTelemetryQuerySessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/ListTelemetryQuerySessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/ListTelemetryQuerySessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/ListTelemetryQuerySessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/ListTelemetryQuerySessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/ListTelemetryQuerySessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/ListTelemetryQuerySessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/ListTelemetryQuerySessions)
