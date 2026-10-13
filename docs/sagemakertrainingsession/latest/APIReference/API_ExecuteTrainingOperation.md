---
source_url: https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_ExecuteTrainingOperation.html
---

# ExecuteTrainingOperation
<a name="API_ExecuteTrainingOperation"></a>

Submits an asynchronous training operation to the specified training session. The service executes operations in sequence number order. The session must be in `Running` or `Blocked` state. Use `GetTrainingOperationResult` to poll for the result. Supported operation types: `forward`, `forwardBackward`, `optimizerStep`, `saveWeights`, `saveState`, and `loadState`.

## Request Syntax
<a name="API_ExecuteTrainingOperation_RequestSyntax"></a>

```
POST /v1/training-sessions/{{trainingSessionName}}/operations HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "operationConfig": { ... },
   "sequenceNumber": {{number}}
}
```

## URI Request Parameters
<a name="API_ExecuteTrainingOperation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [trainingSessionName](#API_ExecuteTrainingOperation_RequestSyntax) **   <a name="sagemakertrainingsession-ExecuteTrainingOperation-request-uri-trainingSessionName"></a>
The name of the training session to submit the operation to.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Request Body
<a name="API_ExecuteTrainingOperation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_ExecuteTrainingOperation_RequestSyntax) **   <a name="sagemakertrainingsession-ExecuteTrainingOperation-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service ignores the request but does not return an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [operationConfig](#API_ExecuteTrainingOperation_RequestSyntax) **   <a name="sagemakertrainingsession-ExecuteTrainingOperation-request-operationConfig"></a>
The configuration that specifies the type and parameters of the training operation. Exactly one member of the union must be set.
Type: [OperationConfig](API_OperationConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [sequenceNumber](#API_ExecuteTrainingOperation_RequestSyntax) **   <a name="sagemakertrainingsession-ExecuteTrainingOperation-request-sequenceNumber"></a>
The monotonically increasing sequence number that determines execution order. The training session processes operations strictly in sequence number order. If a gap exists, the session blocks until the missing operation arrives or times out. Must be at least 1.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

## Response Syntax
<a name="API_ExecuteTrainingOperation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "operationId": "string"
}
```

## Response Elements
<a name="API_ExecuteTrainingOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operationId](#API_ExecuteTrainingOperation_ResponseSyntax) **   <a name="sagemakertrainingsession-ExecuteTrainingOperation-response-operationId"></a>
The unique identifier for the submitted operation. Use this identifier with `GetTrainingOperationResult` to retrieve the operation status and result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

## Errors
<a name="API_ExecuteTrainingOperation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The training session is in a state that cannot accept new operations. The session must be in `Running` or `Blocked` state to accept requests.
HTTP Status Code: 409

 ** InternalServerException **
An internal service error occurred. Retry the request using exponential backoff.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified training session or operation does not exist, or the operation does not belong to the specified training session.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled. Retry the request after a brief wait using exponential backoff.
HTTP Status Code: 429

 ** ValidationException **
The request is not valid. Check the request syntax and parameters. Examples include invalid sequence numbers, malformed client tokens, missing required fields, or invalid operation configuration.
HTTP Status Code: 400

## See Also
<a name="API_ExecuteTrainingOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemakertrainingsessionruntime-2025-02-10/ExecuteTrainingOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemakertrainingsessionruntime-2025-02-10/ExecuteTrainingOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/ExecuteTrainingOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemakertrainingsessionruntime-2025-02-10/ExecuteTrainingOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/ExecuteTrainingOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemakertrainingsessionruntime-2025-02-10/ExecuteTrainingOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemakertrainingsessionruntime-2025-02-10/ExecuteTrainingOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemakertrainingsessionruntime-2025-02-10/ExecuteTrainingOperation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemakertrainingsessionruntime-2025-02-10/ExecuteTrainingOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/ExecuteTrainingOperation)
