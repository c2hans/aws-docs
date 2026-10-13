---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_training_session_runtime_SampleTrainingSessionWithResponseStream.html
---

# SampleTrainingSessionWithResponseStream
<a name="API_training_session_runtime_SampleTrainingSessionWithResponseStream"></a>

Streams inference responses from the model associated with the specified training session. Use this operation for real-time token-by-token generation. The service passes the request body to the model without modification.

## Request Syntax
<a name="API_training_session_runtime_SampleTrainingSessionWithResponseStream_RequestSyntax"></a>

```
POST /training-sessions/{{trainingSessionName}}/sample-with-response-stream HTTP/1.1
Content-Type: {{contentType}}
Accept: {{accept}}
X-Amzn-SageMaker-Model-Package: {{modelPackageArn}}

{{body}}
```

## URI Request Parameters
<a name="API_training_session_runtime_SampleTrainingSessionWithResponseStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accept](#API_training_session_runtime_SampleTrainingSessionWithResponseStream_RequestSyntax) **   <a name="sagemaker-training_session_runtime_SampleTrainingSessionWithResponseStream-request-accept"></a>
The desired MIME type of the inference body in the response.

 ** [contentType](#API_training_session_runtime_SampleTrainingSessionWithResponseStream_RequestSyntax) **   <a name="sagemaker-training_session_runtime_SampleTrainingSessionWithResponseStream-request-contentType"></a>
The MIME type of the input data in the request body.

 ** [modelPackageArn](#API_training_session_runtime_SampleTrainingSessionWithResponseStream_RequestSyntax) **   <a name="sagemaker-training_session_runtime_SampleTrainingSessionWithResponseStream-request-modelPackageArn"></a>
The ARN of the model package whose checkpoint to invoke.

 ** [trainingSessionName](#API_training_session_runtime_SampleTrainingSessionWithResponseStream_RequestSyntax) **   <a name="sagemaker-training_session_runtime_SampleTrainingSessionWithResponseStream-request-uri-trainingSessionName"></a>
The name of the training session whose model to invoke.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Request Body
<a name="API_training_session_runtime_SampleTrainingSessionWithResponseStream_RequestBody"></a>

The request accepts the following binary data.

 ** [body](#API_training_session_runtime_SampleTrainingSessionWithResponseStream_RequestSyntax) **   <a name="sagemaker-training_session_runtime_SampleTrainingSessionWithResponseStream-request-body"></a>
The raw inference request body.

## Response Syntax
<a name="API_training_session_runtime_SampleTrainingSessionWithResponseStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{contentType}}

{{body}}
```

## Response Elements
<a name="API_training_session_runtime_SampleTrainingSessionWithResponseStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [contentType](#API_training_session_runtime_SampleTrainingSessionWithResponseStream_ResponseSyntax) **   <a name="sagemaker-training_session_runtime_SampleTrainingSessionWithResponseStream-response-contentType"></a>
The MIME type of the streaming inference result.

The response returns the following as the HTTP body.

 ** [body](#API_training_session_runtime_SampleTrainingSessionWithResponseStream_ResponseSyntax) **   <a name="sagemaker-training_session_runtime_SampleTrainingSessionWithResponseStream-response-body"></a>
The streaming inference response from the model, delivered as a series of chunks.

## Errors
<a name="API_training_session_runtime_SampleTrainingSessionWithResponseStream_Errors"></a>

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
<a name="API_training_session_runtime_SampleTrainingSessionWithResponseStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemakertrainingsessionruntime-2025-02-10/SampleTrainingSessionWithResponseStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemakertrainingsessionruntime-2025-02-10/SampleTrainingSessionWithResponseStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/SampleTrainingSessionWithResponseStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemakertrainingsessionruntime-2025-02-10/SampleTrainingSessionWithResponseStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/SampleTrainingSessionWithResponseStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemakertrainingsessionruntime-2025-02-10/SampleTrainingSessionWithResponseStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemakertrainingsessionruntime-2025-02-10/SampleTrainingSessionWithResponseStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemakertrainingsessionruntime-2025-02-10/SampleTrainingSessionWithResponseStream)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemakertrainingsessionruntime-2025-02-10/SampleTrainingSessionWithResponseStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/SampleTrainingSessionWithResponseStream)
