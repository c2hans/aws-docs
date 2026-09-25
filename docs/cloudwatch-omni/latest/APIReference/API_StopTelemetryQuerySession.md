---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_StopTelemetryQuerySession.html
---

# StopTelemetryQuerySession
<a name="API_StopTelemetryQuerySession"></a>

Stops a telemetry query session.

Terminates the specified session. After a session is stopped it cannot be reused.

## Request Parameters
<a name="API_StopTelemetryQuerySession_RequestParameters"></a>

 ** sessionId **
The unique ID of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

## Errors
<a name="API_StopTelemetryQuerySession_Errors"></a>

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
<a name="API_StopTelemetryQuerySession_Examples"></a>

### Stop a telemetry query session
<a name="API_StopTelemetryQuerySession_Example_1"></a>

The following example terminates the specified session. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_StopTelemetryQuerySession_Example_1_Request"></a>

```
{
  "sessionId": "9f8c7d6e-5b4a-4c3d-9e2f-1a0b2c3d4e5f"
}
```

#### Sample Response
<a name="API_StopTelemetryQuerySession_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_StopTelemetryQuerySession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/StopTelemetryQuerySession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/StopTelemetryQuerySession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/StopTelemetryQuerySession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/StopTelemetryQuerySession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/StopTelemetryQuerySession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/StopTelemetryQuerySession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/StopTelemetryQuerySession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/StopTelemetryQuerySession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/StopTelemetryQuerySession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/StopTelemetryQuerySession)
