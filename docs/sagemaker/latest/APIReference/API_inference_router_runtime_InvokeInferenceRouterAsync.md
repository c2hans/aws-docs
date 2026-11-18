---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_inference_router_runtime_InvokeInferenceRouterAsync.html
---

# InvokeInferenceRouterAsync
<a name="API_inference_router_runtime_InvokeInferenceRouterAsync"></a>

Submits an asynchronous inference request to an inference router. Before you call this operation, upload the input data to Amazon S3 in the router's AWS Region. The router returns as soon as it accepts the request, and sends the request to one of the destinations of the routing target. The destination reads the input from Amazon S3, and the inference response is written to the Amazon S3 output path that the routing target specifies.

If a destination doesn't start the request within the routing target's `MaxTimeInBacklogSeconds`, the router moves the request to another destination. After your model starts processing the request, the request doesn't move. If no destination can take the request before `RequestTTLSeconds` runs out, or every destination has been tried, the router writes a failure object to the `FailureLocation` and publishes a notification to the routing target's error topic, if one is configured.

For information about the permissions that the caller and each destination need, see [Send asynchronous requests through an inference router](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-async.html).

## Request Syntax
<a name="API_inference_router_runtime_InvokeInferenceRouterAsync_RequestSyntax"></a>

```
POST /inference-routers/{{InferenceRouterName}}/async-invocations HTTP/1.1
X-Amzn-SageMaker-Routing-Target-Name: {{RoutingTargetName}}
X-Amzn-SageMaker-Content-Type: {{ContentType}}
X-Amzn-SageMaker-Accept: {{Accept}}
X-Amzn-SageMaker-Custom-Attributes: {{CustomAttributes}}
X-Amzn-SageMaker-Inference-Id: {{InferenceId}}
X-Amzn-SageMaker-InputLocation: {{InputLocation}}
X-Amzn-SageMaker-S3OutputPathExtension: {{S3OutputPathExtension}}
X-Amzn-SageMaker-Filename: {{Filename}}
X-Amzn-SageMaker-RequestTTLSeconds: {{RequestTTLSeconds}}
X-Amzn-SageMaker-InvocationTimeoutSeconds: {{InvocationTimeoutSeconds}}
```

## URI Request Parameters
<a name="API_inference_router_runtime_InvokeInferenceRouterAsync_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Accept](#API_inference_router_runtime_InvokeInferenceRouterAsync_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouterAsync-request-Accept"></a>
The MIME type that you want for the inference response. The router passes it to the destination.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [ContentType](#API_inference_router_runtime_InvokeInferenceRouterAsync_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouterAsync-request-ContentType"></a>
The MIME type of the input data in Amazon S3. The router passes it to the destination.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [CustomAttributes](#API_inference_router_runtime_InvokeInferenceRouterAsync_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouterAsync-request-CustomAttributes"></a>
Provides additional information about the inference request. The value is an opaque string that the router passes, unchanged, to the model container of the destination that serves the request. The value can contain up to 1,024 visible US-ASCII characters.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [Filename](#API_inference_router_runtime_InvokeInferenceRouterAsync_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouterAsync-request-Filename"></a>
The file name of the inference response stored in Amazon S3. If you don't provide one, SageMaker AI generates one.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!.*\..*\.)[a-zA-Z0-9][a-zA-Z0-9-_\.]*`

 ** [InferenceId](#API_inference_router_runtime_InvokeInferenceRouterAsync_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouterAsync-request-InferenceId"></a>
An identifier for the inference request. If you don't provide one, SageMaker AI generates one and returns it in the response.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\S[\p{Print}]*`

 ** [InferenceRouterName](#API_inference_router_runtime_InvokeInferenceRouterAsync_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouterAsync-request-uri-InferenceRouterName"></a>
The name of the inference router to invoke.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** [InputLocation](#API_inference_router_runtime_InvokeInferenceRouterAsync_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouterAsync-request-InputLocation"></a>
The Amazon S3 URI of the object that contains the input data for the inference. The bucket must be in the inference router's AWS Region and owned by the router's account. The destination endpoint's execution role reads the object, and the destination's asynchronous inference limits apply to it.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** [InvocationTimeoutSeconds](#API_inference_router_runtime_InvokeInferenceRouterAsync_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouterAsync-request-InvocationTimeoutSeconds"></a>
The maximum time, in seconds, that a destination can spend processing the request before the request is marked as expired. The default is 900 seconds (15 minutes).
Valid Range: Minimum value of 1. Maximum value of 3600.

 ** [RequestTTLSeconds](#API_inference_router_runtime_InvokeInferenceRouterAsync_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouterAsync-request-RequestTTLSeconds"></a>
The time to live of the request, in seconds, measured from when the router accepts it. If no destination starts the request in this time, the request fails. The default is 21,600 seconds (6 hours).
Valid Range: Minimum value of 60. Maximum value of 21600.

 ** [RoutingTargetName](#API_inference_router_runtime_InvokeInferenceRouterAsync_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouterAsync-request-RoutingTargetName"></a>
The name of the routing target in the inference router. The routing target must be configured for asynchronous inference.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** [S3OutputPathExtension](#API_inference_router_runtime_InvokeInferenceRouterAsync_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouterAsync-request-S3OutputPathExtension"></a>
The path extension that is appended to the routing target's Amazon S3 output path where the inference response is stored.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(?!s3:|https:)[a-zA-Z0-9!_.*'()/-]+`

## Request Body
<a name="API_inference_router_runtime_InvokeInferenceRouterAsync_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_inference_router_runtime_InvokeInferenceRouterAsync_ResponseSyntax"></a>

```
HTTP/1.1 202
X-Amzn-SageMaker-OutputLocation: {{OutputLocation}}
X-Amzn-SageMaker-FailureLocation: {{FailureLocation}}
Content-type: application/json

{
   "InferenceId": "string"
}
```

## Response Elements
<a name="API_inference_router_runtime_InvokeInferenceRouterAsync_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The response returns the following HTTP headers.

 ** [FailureLocation](#API_inference_router_runtime_InvokeInferenceRouterAsync_ResponseSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouterAsync-response-FailureLocation"></a>
The Amazon S3 URI where the failure details are written if the inference fails.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [OutputLocation](#API_inference_router_runtime_InvokeInferenceRouterAsync_ResponseSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouterAsync-response-OutputLocation"></a>
The Amazon S3 URI where the inference response is written. The location doesn't change if the router moves the request to another destination.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\p{ASCII}*`

The following data is returned in JSON format by the service.

 ** [InferenceId](#API_inference_router_runtime_InvokeInferenceRouterAsync_ResponseSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouterAsync-response-InferenceId"></a>
The identifier for the inference request. This is the `InferenceId` that you provided, or the one that SageMaker AI generated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\p{ASCII}*`

## Errors
<a name="API_inference_router_runtime_InvokeInferenceRouterAsync_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform this action. Check that the caller is allowed to invoke the inference router and every destination of the routing target.
 ** Message **
A message that describes the error.
HTTP Status Code: 403

 ** InternalFailure **
An internal error occurred. Retry the request with exponential backoff. The AWS SDKs and the AWS CLI do this by default.
 ** Message **
A message that describes the error.
HTTP Status Code: 500

 ** RequestTimeoutException **
The inference router didn't receive the complete request within 300 seconds of accepting it, for example because of a very slow upload. Retry the request.
 ** Message **
A message that describes the error.
HTTP Status Code: 408

 ** ServiceUnavailableException **
The service is temporarily unavailable. For example, no destination of the routing target could serve the request, or a destination didn't respond. Retry the request with exponential backoff. The AWS SDKs and the AWS CLI do this by default.
 ** Message **
A message that describes the error.
HTTP Status Code: 503

 ** ThrottlingException **
The request was denied because you exceeded the request rate for the inference router, or because a destination throttled the request. Retry the request with exponential backoff.
 ** Message **
A message that describes the error.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the inference router name, the routing target name, and the request parameters, and then try again.
 ** Message **
A message that describes the error.
HTTP Status Code: 400

## See Also
<a name="API_inference_router_runtime_InvokeInferenceRouterAsync_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouterAsync)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouterAsync)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouterAsync)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouterAsync)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouterAsync)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouterAsync)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouterAsync)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouterAsync)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouterAsync)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouterAsync)
