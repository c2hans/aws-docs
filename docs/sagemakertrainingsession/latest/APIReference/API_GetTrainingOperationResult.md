---
source_url: https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_GetTrainingOperationResult.html
---

# GetTrainingOperationResult
<a name="API_GetTrainingOperationResult"></a>

Retrieves the current status and result of a previously submitted training operation. Poll this operation until the status reaches a terminal state (Completed, Failed, or Skipped).

## Request Syntax
<a name="API_GetTrainingOperationResult_RequestSyntax"></a>

```
GET /v1/training-sessions/{{trainingSessionName}}/operations/{{operationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTrainingOperationResult_RequestParameters"></a>

The request uses the following URI parameters.

 ** [operationId](#API_GetTrainingOperationResult_RequestSyntax) **   <a name="sagemakertrainingsession-GetTrainingOperationResult-request-uri-operationId"></a>
The unique identifier of the operation to retrieve, returned by `ExecuteTrainingOperation`.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [trainingSessionName](#API_GetTrainingOperationResult_RequestSyntax) **   <a name="sagemakertrainingsession-GetTrainingOperationResult-request-uri-trainingSessionName"></a>
The name of the training session that owns the operation.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Request Body
<a name="API_GetTrainingOperationResult_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTrainingOperationResult_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errorDetails": "string",
   "operationResult": { ... },
   "status": "string",
   "tokenUsage": {
      "trainingTokens": number
   }
}
```

## Response Elements
<a name="API_GetTrainingOperationResult_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errorDetails](#API_GetTrainingOperationResult_ResponseSyntax) **   <a name="sagemakertrainingsession-GetTrainingOperationResult-response-errorDetails"></a>
A message describing why the operation failed. The service populates this field only when the status is `Failed`.
Type: String

 ** [operationResult](#API_GetTrainingOperationResult_ResponseSyntax) **   <a name="sagemakertrainingsession-GetTrainingOperationResult-response-operationResult"></a>
The result payload of the operation. The service populates this field only when the status is `Completed`. The populated member of the union corresponds to the operation type that was submitted.
Type: [OperationResult](API_OperationResult.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_GetTrainingOperationResult_ResponseSyntax) **   <a name="sagemakertrainingsession-GetTrainingOperationResult-response-status"></a>
The current status of the operation. Possible values are `Pending`, `InProgress`, `Completed`, `Failed`, or `Skipped`.
Type: String
Valid Values: `Pending | InProgress | Completed | Failed | Skipped`

 ** [tokenUsage](#API_GetTrainingOperationResult_ResponseSyntax) **   <a name="sagemakertrainingsession-GetTrainingOperationResult-response-tokenUsage"></a>
The token usage statistics for metering purposes. The service populates this field for forward and forwardBackward operations upon completion.
Type: [TrainingTokenUsage](API_TrainingTokenUsage.md) object

## Errors
<a name="API_GetTrainingOperationResult_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetTrainingOperationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemakertrainingsessionruntime-2025-02-10/GetTrainingOperationResult)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemakertrainingsessionruntime-2025-02-10/GetTrainingOperationResult)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/GetTrainingOperationResult)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemakertrainingsessionruntime-2025-02-10/GetTrainingOperationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/GetTrainingOperationResult)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemakertrainingsessionruntime-2025-02-10/GetTrainingOperationResult)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemakertrainingsessionruntime-2025-02-10/GetTrainingOperationResult)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemakertrainingsessionruntime-2025-02-10/GetTrainingOperationResult)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemakertrainingsessionruntime-2025-02-10/GetTrainingOperationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/GetTrainingOperationResult)
