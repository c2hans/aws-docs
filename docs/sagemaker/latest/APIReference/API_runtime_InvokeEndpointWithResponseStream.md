---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpointWithResponseStream.html
---

# InvokeEndpointWithResponseStream
<a name="API_runtime_InvokeEndpointWithResponseStream"></a>

Invokes a model at the specified endpoint to return the inference response as a stream. The inference stream provides the response payload incrementally as a series of parts. Before you can get an inference stream, you must have access to a model that's deployed using Amazon SageMaker AI hosting services, and the container for that model must support inference streaming.

For more information that can help you use this API, see the following sections in the *Amazon SageMaker AI Developer Guide*:
+ For information about how to add streaming support to a model, see [How Containers Serve Requests](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-code-how-containe-serves-requests).
+ For information about how to process the streaming response, see [Invoke real-time endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-test-endpoints.html).

Before you can use this operation, your IAM permissions must allow the `sagemaker:InvokeEndpoint` action. For more information about Amazon SageMaker AI actions for IAM policies, see [Actions, resources, and condition keys for Amazon SageMaker AI](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsagemaker.html) in the *IAM Service Authorization Reference*.

Amazon SageMaker AI strips all POST headers except those supported by the API. Amazon SageMaker AI might add additional headers. You should not rely on the behavior of headers outside those enumerated in the request syntax.

Calls to `InvokeEndpointWithResponseStream` are authenticated by using AWS Signature Version 4. For information, see [Authenticating Requests (AWS Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html) in the *Amazon S3 API Reference*.

## Request Syntax
<a name="API_runtime_InvokeEndpointWithResponseStream_RequestSyntax"></a>

```
POST /endpoints/{{EndpointName}}/invocations-response-stream HTTP/1.1
Content-Type: {{ContentType}}
X-Amzn-SageMaker-Accept: {{Accept}}
X-Amzn-SageMaker-Custom-Attributes: {{CustomAttributes}}
X-Amzn-SageMaker-Target-Variant: {{TargetVariant}}
X-Amzn-SageMaker-Target-Container-Hostname: {{TargetContainerHostname}}
X-Amzn-SageMaker-Inference-Id: {{InferenceId}}
X-Amzn-SageMaker-Inference-Component: {{InferenceComponentName}}
X-Amzn-SageMaker-Session-Id: {{SessionId}}

{{Body}}
```

## URI Request Parameters
<a name="API_runtime_InvokeEndpointWithResponseStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Accept](#API_runtime_InvokeEndpointWithResponseStream_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-request-Accept"></a>
The desired MIME type of the inference response from the model container.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [ContentType](#API_runtime_InvokeEndpointWithResponseStream_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-request-ContentType"></a>
The MIME type of the input data in the request body.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [CustomAttributes](#API_runtime_InvokeEndpointWithResponseStream_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-request-CustomAttributes"></a>
Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker AI endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in [Section 3.3.6. Field Value Components](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6) of the Hypertext Transfer Protocol (HTTP/1.1).
The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with `Trace ID:` in your post-processing function.
This feature is currently supported in the AWS SDKs but not in the Amazon SageMaker AI Python SDK.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [EndpointName](#API_runtime_InvokeEndpointWithResponseStream_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-request-uri-EndpointName"></a>
The name of the endpoint that you specified when you created the endpoint using the [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html) API.
Length Constraints: Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** [InferenceComponentName](#API_runtime_InvokeEndpointWithResponseStream_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-request-InferenceComponentName"></a>
If the endpoint hosts one or more inference components, this parameter specifies the name of inference component to invoke for a streaming response.
Length Constraints: Maximum length of 63.
Pattern: `^[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?$`

 ** [InferenceId](#API_runtime_InvokeEndpointWithResponseStream_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-request-InferenceId"></a>
An identifier that you assign to your request.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\A\S[\p{Print}]*\z`

 ** [SessionId](#API_runtime_InvokeEndpointWithResponseStream_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-request-SessionId"></a>
The ID of a stateful session to handle your request.
You can't create a stateful session by using the `InvokeEndpointWithResponseStream` action. Instead, you can create one by using the ` InvokeEndpoint ` action. In your request, you specify `NEW_SESSION` for the `SessionId` request parameter. The response to that request provides the session ID for the `NewSessionId` response parameter.
Length Constraints: Maximum length of 256.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`

 ** [TargetContainerHostname](#API_runtime_InvokeEndpointWithResponseStream_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-request-TargetContainerHostname"></a>
If the endpoint hosts multiple containers and is configured to use direct invocation, this parameter specifies the host name of the container to invoke.
Length Constraints: Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`

 ** [TargetVariant](#API_runtime_InvokeEndpointWithResponseStream_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-request-TargetVariant"></a>
Specify the production variant to send the inference request to when invoking an endpoint that is running two or more variants. Note that this parameter overrides the default behavior for the endpoint, which is to distribute the invocation traffic based on the variant weights.
For information about how to use variant targeting to perform a/b testing, see [Test models in production](https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html)
Length Constraints: Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`

## Request Body
<a name="API_runtime_InvokeEndpointWithResponseStream_RequestBody"></a>

The request accepts the following binary data.

 ** [Body](#API_runtime_InvokeEndpointWithResponseStream_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-request-Body"></a>
Provides input data, in the format specified in the `ContentType` request header. Amazon SageMaker AI passes all of the data in the body to the model.
For information about the format of the request body, see [Common Data Formats-Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html).
Length Constraints: Maximum length of 6291456.
Required: Yes

## Response Syntax
<a name="API_runtime_InvokeEndpointWithResponseStream_ResponseSyntax"></a>

```
HTTP/1.1 200
X-Amzn-SageMaker-Content-Type: {{ContentType}}
x-Amzn-Invoked-Production-Variant: {{InvokedProductionVariant}}
X-Amzn-SageMaker-Custom-Attributes: {{CustomAttributes}}
Content-type: application/json

{
   "InternalStreamFailure": {
   },
   "ModelStreamError": {
   },
   "PayloadPart": {
      "Bytes": blob
   }
}
```

## Response Elements
<a name="API_runtime_InvokeEndpointWithResponseStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ContentType](#API_runtime_InvokeEndpointWithResponseStream_ResponseSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-response-ContentType"></a>
The MIME type of the inference returned from the model container.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [CustomAttributes](#API_runtime_InvokeEndpointWithResponseStream_ResponseSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-response-CustomAttributes"></a>
Provides additional information in the response about the inference returned by a model hosted at an Amazon SageMaker AI endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to return an ID received in the `CustomAttributes` header of a request or other metadata that a service endpoint was programmed to produce. The value must consist of no more than 1024 visible US-ASCII characters as specified in [Section 3.3.6. Field Value Components](https://tools.ietf.org/html/rfc7230#section-3.2.6) of the Hypertext Transfer Protocol (HTTP/1.1). If the customer wants the custom attribute returned, the model must set the custom attribute to be included on the way back.
The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with `Trace ID:` in your post-processing function.
This feature is currently supported in the AWS SDKs but not in the Amazon SageMaker AI Python SDK.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [InvokedProductionVariant](#API_runtime_InvokeEndpointWithResponseStream_ResponseSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-response-InvokedProductionVariant"></a>
Identifies the production variant that was invoked.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

The following data is returned in JSON format by the service.

 ** [InternalStreamFailure](#API_runtime_InvokeEndpointWithResponseStream_ResponseSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-response-InternalStreamFailure"></a>
The stream processing failed because of an unknown error, exception or failure. Try your request again.
Type: Exception
HTTP Status Code:

 ** [ModelStreamError](#API_runtime_InvokeEndpointWithResponseStream_ResponseSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-response-ModelStreamError"></a>
 An error occurred while streaming the response body. This error can have the following error codes:
ModelInvocationTimeExceeded
The model failed to finish sending the response within the timeout period allowed by Amazon SageMaker AI.
StreamBroken
The Transmission Control Protocol (TCP) connection between the client and the model was reset or closed.
Type: Exception
HTTP Status Code:

 ** [PayloadPart](#API_runtime_InvokeEndpointWithResponseStream_ResponseSyntax) **   <a name="sagemaker-runtime_InvokeEndpointWithResponseStream-response-PayloadPart"></a>
A wrapper for pieces of the payload that's returned in response to a streaming inference request. A streaming inference response consists of one or more payload parts.
Type: [PayloadPart](API_runtime_PayloadPart.md) object

## Errors
<a name="API_runtime_InvokeEndpointWithResponseStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailure **
 An internal failure occurred.
HTTP Status Code: 500

 ** InternalStreamFailure **
The stream processing failed because of an unknown error, exception or failure. Try your request again.
HTTP Status Code: 500

 ** ModelError **
 Model (owned by the customer in the container) returned 4xx or 5xx error code.
 ** LogStreamArn **
 The Amazon Resource Name (ARN) of the log stream.
 ** OriginalMessage **
 Original message.
 ** OriginalStatusCode **
 Original status code.
HTTP Status Code: 424

 ** ModelStreamError **
 An error occurred while streaming the response body. This error can have the following error codes:
ModelInvocationTimeExceeded
The model failed to finish sending the response within the timeout period allowed by Amazon SageMaker AI.
StreamBroken
The Transmission Control Protocol (TCP) connection between the client and the model was reset or closed.
 ** ErrorCode **
This error can have the following error codes:
ModelInvocationTimeExceeded
The model failed to finish sending the response within the timeout period allowed by Amazon SageMaker AI.
StreamBroken
The Transmission Control Protocol (TCP) connection between the client and the model was reset or closed.
HTTP Status Code: 400

 ** ServiceUnavailable **
 The service is unavailable. Try your call again.
HTTP Status Code: 503

 ** ValidationError **
 Inspect your request and try again.
HTTP Status Code: 400

## See Also
<a name="API_runtime_InvokeEndpointWithResponseStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/runtime.sagemaker-2017-05-13/InvokeEndpointWithResponseStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/runtime.sagemaker-2017-05-13/InvokeEndpointWithResponseStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/runtime.sagemaker-2017-05-13/InvokeEndpointWithResponseStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/runtime.sagemaker-2017-05-13/InvokeEndpointWithResponseStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/runtime.sagemaker-2017-05-13/InvokeEndpointWithResponseStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/runtime.sagemaker-2017-05-13/InvokeEndpointWithResponseStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/runtime.sagemaker-2017-05-13/InvokeEndpointWithResponseStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/runtime.sagemaker-2017-05-13/InvokeEndpointWithResponseStream)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/runtime.sagemaker-2017-05-13/InvokeEndpointWithResponseStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/runtime.sagemaker-2017-05-13/InvokeEndpointWithResponseStream)
