---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_training_session_runtime_ExecuteSamplingOperation.html
---

# ExecuteSamplingOperation
<a name="API_training_session_runtime_ExecuteSamplingOperation"></a>

Submits an asynchronous sampling operation to generate text or compute log-probabilities from the model associated with the specified training session. The session must be in `Running` or `Blocked` state. Use `GetSamplingOperationResult` to poll for the result.

## Request Syntax
<a name="API_training_session_runtime_ExecuteSamplingOperation_RequestSyntax"></a>

```
POST /v1/training-sessions/{{trainingSessionName}}/sampling-operations HTTP/1.1
Content-type: application/json

{
   "operationConfig": { ... }
}
```

## URI Request Parameters
<a name="API_training_session_runtime_ExecuteSamplingOperation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [trainingSessionName](#API_training_session_runtime_ExecuteSamplingOperation_RequestSyntax) **   <a name="sagemaker-training_session_runtime_ExecuteSamplingOperation-request-uri-trainingSessionName"></a>
The name of the training session to sample from.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Request Body
<a name="API_training_session_runtime_ExecuteSamplingOperation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [operationConfig](#API_training_session_runtime_ExecuteSamplingOperation_RequestSyntax) **   <a name="sagemaker-training_session_runtime_ExecuteSamplingOperation-request-operationConfig"></a>
The configuration for the sample operation. Specify either a sample configuration to generate text or a computeLogprobs configuration to compute token log-probabilities.
Type: [SampleOperationConfig](API_training_session_runtime_SampleOperationConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_training_session_runtime_ExecuteSamplingOperation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "operationId": "string"
}
```

## Response Elements
<a name="API_training_session_runtime_ExecuteSamplingOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operationId](#API_training_session_runtime_ExecuteSamplingOperation_ResponseSyntax) **   <a name="sagemaker-training_session_runtime_ExecuteSamplingOperation-response-operationId"></a>
The unique identifier for the submitted sample operation. Use this identifier with `GetSamplingOperationResult` to retrieve the operation status and result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

## Errors
<a name="API_training_session_runtime_ExecuteSamplingOperation_Errors"></a>

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
<a name="API_training_session_runtime_ExecuteSamplingOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemakertrainingsessionruntime-2025-02-10/ExecuteSamplingOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemakertrainingsessionruntime-2025-02-10/ExecuteSamplingOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/ExecuteSamplingOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemakertrainingsessionruntime-2025-02-10/ExecuteSamplingOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/ExecuteSamplingOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemakertrainingsessionruntime-2025-02-10/ExecuteSamplingOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemakertrainingsessionruntime-2025-02-10/ExecuteSamplingOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemakertrainingsessionruntime-2025-02-10/ExecuteSamplingOperation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemakertrainingsessionruntime-2025-02-10/ExecuteSamplingOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/ExecuteSamplingOperation)
