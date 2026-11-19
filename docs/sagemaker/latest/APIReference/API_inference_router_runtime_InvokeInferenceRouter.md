---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_inference_router_runtime_InvokeInferenceRouter.html
---

# InvokeInferenceRouter

Sends a real-time inference request to an inference router. In the request, you name the routing target, and the router sends the request to one of the routing target's destinations. The response includes the destination that served the request and the reason that the router chose it.

The following limits apply:
+ The maximum request payload is 6 MB. A request with a larger body fails with HTTP status code 413.
+ Your model has up to 60 seconds for each attempt, the same limit as `InvokeEndpoint`. If your account has a higher model execution timeout for `InvokeEndpoint`, it doesn't apply through an inference router. For models that take longer, use `InvokeInferenceRouterAsync`.

If a destination returns an error that the router can retry, such as a throttling error, before your model produces a response, the router retries the request once on another destination. A request that times out on a destination isn't retried. Because a request can make two attempts, set your client read timeout to at least 170 seconds.

The caller needs permission to invoke the inference router and every destination of the routing target. For information about permissions, see [Route requests across Regions with inference routers](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router.html).

## Request Syntax
<a name="API_inference_router_runtime_InvokeInferenceRouter_RequestSyntax"></a>

```
POST /inference-routers/{{InferenceRouterName}}/invocations HTTP/1.1
X-Amzn-SageMaker-Routing-Target-Name: {{RoutingTargetName}}
Content-Type: {{ContentType}}
Accept: {{Accept}}
X-Amzn-SageMaker-Inference-Id: {{InferenceId}}
X-Amzn-SageMaker-Prefix-Aware-Id: {{PrefixAwareId}}
X-Amzn-SageMaker-Custom-Attributes: {{CustomAttributes}}

{{Body}}
```

## URI Request Parameters
<a name="API_inference_router_runtime_InvokeInferenceRouter_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Accept](#API_inference_router_runtime_InvokeInferenceRouter_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouter-request-Accept"></a>
The MIME type that you want for the inference response. The router passes it to the destination.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [ContentType](#API_inference_router_runtime_InvokeInferenceRouter_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouter-request-ContentType"></a>
The MIME type of the input data in the request body. The router passes it to the destination.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [CustomAttributes](#API_inference_router_runtime_InvokeInferenceRouter_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouter-request-CustomAttributes"></a>
Provides additional information about the inference request. The value is an opaque string that the router passes, unchanged, to the model container of the destination that serves the request. The value can contain up to 1,024 visible US-ASCII characters.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [InferenceId](#API_inference_router_runtime_InvokeInferenceRouter_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouter-request-InferenceId"></a>
An identifier for the inference request. The router passes it to the destination.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\S[\p{Print}]*`

 ** [InferenceRouterName](#API_inference_router_runtime_InvokeInferenceRouter_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouter-request-uri-InferenceRouterName"></a>
The name of the inference router to invoke.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** [PrefixAwareId](#API_inference_router_runtime_InvokeInferenceRouter_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouter-request-PrefixAwareId"></a>
An optional, stable identifier that serves as a routing hint for prefix-aware routing. The router passes it to the destination that serves the request. Within that destination, requests with the same prefix and the same identifier go to the same instance. If requests from different applications might have the same prompt prefix, set a different identifier for each application to differentiate their routing decisions.
Applies only to destination endpoints configured with a `RoutingStrategy` of `PREFIX_AWARE`.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\S[\p{Print}]*`

 ** [RoutingTargetName](#API_inference_router_runtime_InvokeInferenceRouter_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouter-request-RoutingTargetName"></a>
The name of the routing target in the inference router. The routing target lists the destinations that can serve the request.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

## Request Body
<a name="API_inference_router_runtime_InvokeInferenceRouter_RequestBody"></a>

The request accepts the following binary data.

 ** [Body](#API_inference_router_runtime_InvokeInferenceRouter_RequestSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouter-request-Body"></a>
The input data for the inference, in the format that your model expects. The body can't be empty.
Length Constraints: Minimum length of 0. Maximum length of 6291456.
Required: Yes

## Response Syntax
<a name="API_inference_router_runtime_InvokeInferenceRouter_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{ContentType}}
X-Amzn-SageMaker-Invoked-Routed-Resource-Arn: {{InvokedRoutedResourceArn}}
X-Amzn-SageMaker-Invoked-Routing-Reason: {{RoutingReason}}
X-Amzn-Invoked-Production-Variant: {{InvokedProductionVariant}}
X-Amzn-SageMaker-Custom-Attributes: {{CustomAttributes}}

{{Body}}
```

## Response Elements
<a name="API_inference_router_runtime_InvokeInferenceRouter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ContentType](#API_inference_router_runtime_InvokeInferenceRouter_ResponseSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouter-response-ContentType"></a>
The MIME type of the inference returned in the response body.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [CustomAttributes](#API_inference_router_runtime_InvokeInferenceRouter_ResponseSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouter-response-CustomAttributes"></a>
Provides additional information in the response about the inference. This is the value that the model container of the destination returned, unchanged.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [InvokedProductionVariant](#API_inference_router_runtime_InvokeInferenceRouter_ResponseSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouter-response-InvokedProductionVariant"></a>
The production variant of the destination endpoint that served the request.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [InvokedRoutedResourceArn](#API_inference_router_runtime_InvokeInferenceRouter_ResponseSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouter-response-InvokedRoutedResourceArn"></a>
The Amazon Resource Name (ARN) of the endpoint or inference component that served the request.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [RoutingReason](#API_inference_router_runtime_InvokeInferenceRouter_ResponseSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouter-response-RoutingReason"></a>
The reason that the router chose the destination that served the request. Possible values:
+  `local-preferred` – The destination is a healthy destination in the router's Region.
+  `capacity-available` – No destination in the router's Region could take the request, and two or more destinations in other Regions could.
+  `only-healthy` – No destination in the router's Region could take the request, and exactly one destination in another Region could.
+  `failover` – The router moved the request away from destinations in its Region because they were overloaded or returning errors. You also see this value when the router can't assess destination health, and when no destination is healthy and the router tries one anyway.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\p{ASCII}*`

The response returns the following as the HTTP body.

 ** [Body](#API_inference_router_runtime_InvokeInferenceRouter_ResponseSyntax) **   <a name="sagemaker-inference_router_runtime_InvokeInferenceRouter-response-Body"></a>
The inference that the model returned.
Length Constraints: Minimum length of 0. Maximum length of 6291456.

## Errors
<a name="API_inference_router_runtime_InvokeInferenceRouter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform this action. Check that the caller is allowed to invoke the inference router and every destination of the routing target.
 ** Message **
A message that describes the error.
HTTP Status Code: 403

 ** InternalDependencyException **
The request failed because of an error in an internal dependency. Retry the request with exponential backoff.
 ** Message **
A message that describes the error.
HTTP Status Code: 530

 ** InternalFailure **
An internal error occurred. Retry the request with exponential backoff. The AWS SDKs and the AWS CLI do this by default.
 ** Message **
A message that describes the error.
HTTP Status Code: 500

 ** ModelError **
The model in the destination that served the request returned an error. Check `OriginalStatusCode`, `OriginalMessage`, and the destination's logs in Amazon CloudWatch.
 ** LogStreamArn **
The Amazon Resource Name (ARN) of the Amazon CloudWatch log stream for the destination that served the request.
 ** Message **
A message that describes the error.
 ** OriginalMessage **
The error message that the model container returned.
 ** OriginalStatusCode **
The HTTP status code that the model container returned.
HTTP Status Code: 424

 ** ModelNotReadyException **
The destination isn't ready to serve the model, for example because an inference component has no copies. Retry the request later.
 ** Message **
A message that describes the error.
HTTP Status Code: 429

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
<a name="API_inference_router_runtime_InvokeInferenceRouter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouter)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-inference-router-runtime-2026-01-01/InvokeInferenceRouter)
