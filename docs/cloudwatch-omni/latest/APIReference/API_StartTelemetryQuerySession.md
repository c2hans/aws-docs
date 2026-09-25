---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_StartTelemetryQuerySession.html
---

# StartTelemetryQuerySession
<a name="API_StartTelemetryQuerySession"></a>

Starts a new telemetry query session.

A session provides a logical grouping for one or more telemetry queries. The returned session ID is required when starting queries via StartTelemetryQuery.

## Request Parameters
<a name="API_StartTelemetryQuerySession_RequestParameters"></a>

 ** sessionName **
A human-readable name for the session. Names under `/aws/` are reserved for service integrations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([a-zA-Z0-9_-]+|/aws/[a-zA-Z0-9_-]+(/[a-zA-Z0-9_-]+)?)`
Required: No

## Response Elements
<a name="API_StartTelemetryQuerySession_ResponseElements"></a>

The following element is returned by the service.

 ** sessionId **
The unique ID of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`

## Errors
<a name="API_StartTelemetryQuerySession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The operation could not be completed because of a conflict with the current state of the resource.
 ** conflictType **
The type of conflict that caused the request to fail. Not always present.
 ** errorCode **
The error code associated with the conflict. Not always present.
 ** message **
A human-readable description of the conflict.
 ** resourceId **
The identifier of the resource that is in conflict. Not always present.
 ** resourceType **
The type of the resource that is in conflict. Not always present.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** errorCode **
The error code associated with the internal error.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
A service quota was exceeded.
HTTP Status Code: 402

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
<a name="API_StartTelemetryQuerySession_Examples"></a>

### Start a telemetry query session
<a name="API_StartTelemetryQuerySession_Example_1"></a>

The following example starts a session for grouping telemetry queries and returns its session ID. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_StartTelemetryQuerySession_Example_1_Request"></a>

```
{
  "sessionName": "prod-latency-investigation"
}
```

#### Sample Response
<a name="API_StartTelemetryQuerySession_Example_1_Response"></a>

```
{
  "sessionId": "9f8c7d6e-5b4a-4c3d-9e2f-1a0b2c3d4e5f"
}
```

## See Also
<a name="API_StartTelemetryQuerySession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/StartTelemetryQuerySession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/StartTelemetryQuerySession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/StartTelemetryQuerySession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/StartTelemetryQuerySession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/StartTelemetryQuerySession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/StartTelemetryQuerySession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/StartTelemetryQuerySession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/StartTelemetryQuerySession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/StartTelemetryQuerySession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/StartTelemetryQuerySession)
