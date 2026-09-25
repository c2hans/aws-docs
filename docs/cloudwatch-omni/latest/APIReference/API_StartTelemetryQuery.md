---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_StartTelemetryQuery.html
---

# StartTelemetryQuery
<a name="API_StartTelemetryQuery"></a>

Starts a telemetry query within a session.

Submits the provided query string for execution in the specified session. Use GetTelemetryQueryResults to poll for results and check query status.

## Request Parameters
<a name="API_StartTelemetryQuery_RequestParameters"></a>

 ** queryString **
The query string to execute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64000.
Required: Yes

 ** sessionId **
The unique ID of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

## Response Elements
<a name="API_StartTelemetryQuery_ResponseElements"></a>

The following elements are returned by the service.

 ** queryId **
The unique ID of the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`

 ** sessionId **
The unique ID of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`

## Errors
<a name="API_StartTelemetryQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

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
<a name="API_StartTelemetryQuery_Examples"></a>

### Start a telemetry query
<a name="API_StartTelemetryQuery_Example_1"></a>

The following example submits a SQL query within a session and returns the query ID used to poll for results. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_StartTelemetryQuery_Example_1_Request"></a>

```
{
  "queryString": "SELECT `@timestamp`, `@message` FROM "logs.default" WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1 HOUR' AND NOW() ORDER BY `@timestamp` DESC LIMIT 100",
  "sessionId": "9f8c7d6e-5b4a-4c3d-9e2f-1a0b2c3d4e5f"
}
```

#### Sample Response
<a name="API_StartTelemetryQuery_Example_1_Response"></a>

```
{
  "queryId": "3b2a1c0d-7e6f-4a5b-8c9d-0e1f2a3b4c5d",
  "sessionId": "9f8c7d6e-5b4a-4c3d-9e2f-1a0b2c3d4e5f"
}
```

## See Also
<a name="API_StartTelemetryQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/StartTelemetryQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/StartTelemetryQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/StartTelemetryQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/StartTelemetryQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/StartTelemetryQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/StartTelemetryQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/StartTelemetryQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/StartTelemetryQuery)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/StartTelemetryQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/StartTelemetryQuery)
