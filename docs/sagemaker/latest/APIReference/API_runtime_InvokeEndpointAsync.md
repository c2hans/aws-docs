---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpointAsync.html
---

# InvokeEndpointAsync
<a name="API_runtime_InvokeEndpointAsync"></a>

After you deploy a model into production using Amazon SageMaker AI hosting services, your client applications use this API to get inferences from the model hosted at the specified endpoint in an asynchronous manner.

Inference requests sent to this API are enqueued for asynchronous processing. The processing of the inference request may or may not complete before you receive a response from this API. The response from this API will not contain the result of the inference request but contain information about where you can locate it.

Amazon SageMaker AI strips all POST headers except those supported by the API. Amazon SageMaker AI might add additional headers. You should not rely on the behavior of headers outside those enumerated in the request syntax.

Calls to `InvokeEndpointAsync` are authenticated by using AWS Signature Version 4. For information, see [Authenticating Requests (AWS Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html) in the *Amazon S3 API Reference*.

## Request Syntax
<a name="API_runtime_InvokeEndpointAsync_RequestSyntax"></a>

```
POST /endpoints/{{EndpointName}}/async-invocations HTTP/1.1
X-Amzn-SageMaker-Content-Type: {{ContentType}}
X-Amzn-SageMaker-Accept: {{Accept}}
X-Amzn-SageMaker-Custom-Attributes: {{CustomAttributes}}
X-Amzn-SageMaker-Inference-Id: {{InferenceId}}
X-Amzn-SageMaker-InputLocation: {{InputLocation}}
X-Amzn-SageMaker-S3OutputPathExtension: {{S3OutputPathExtension}}
X-Amzn-SageMaker-Filename: {{Filename}}
X-Amzn-SageMaker-RequestTTLSeconds: {{RequestTTLSeconds}}
X-Amzn-SageMaker-InvocationTimeoutSeconds: {{InvocationTimeoutSeconds}}

{{Body}}
```

## URI Request Parameters
<a name="API_runtime_InvokeEndpointAsync_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Accept](#API_runtime_InvokeEndpointAsync_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointAsync-request-Accept"></a>
The desired MIME type of the inference response from the model container.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [ContentType](#API_runtime_InvokeEndpointAsync_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointAsync-request-ContentType"></a>
The MIME type of the input data in the request body.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [CustomAttributes](#API_runtime_InvokeEndpointAsync_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointAsync-request-CustomAttributes"></a>
Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker AI endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in [Section 3.3.6. Field Value Components](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6) of the Hypertext Transfer Protocol (HTTP/1.1).
The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with `Trace ID:` in your post-processing function.
This feature is currently supported in the AWS SDKs but not in the Amazon SageMaker AI Python SDK.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [EndpointName](#API_runtime_InvokeEndpointAsync_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointAsync-request-uri-EndpointName"></a>
The name of the endpoint that you specified when you created the endpoint using the [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html) API.
Length Constraints: Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** [Filename](#API_runtime_InvokeEndpointAsync_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointAsync-request-Filename"></a>
The filename for the inference response payload stored in Amazon S3. If not specified, Amazon SageMaker AI generates a filename based on the inference ID.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^(?!.*\..*\.)[a-zA-Z0-9][a-zA-Z0-9-_\.]*$`

 ** [InferenceId](#API_runtime_InvokeEndpointAsync_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointAsync-request-InferenceId"></a>
The identifier for the inference request. Amazon SageMaker AI will generate an identifier for you if none is specified.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\A\S[\p{Print}]*\z`

 ** [InputLocation](#API_runtime_InvokeEndpointAsync_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointAsync-request-InputLocation"></a>
The Amazon S3 URI where the inference request payload is stored.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(https|s3)://([^/]+)/?(.*)$`

 ** [InvocationTimeoutSeconds](#API_runtime_InvokeEndpointAsync_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointAsync-request-InvocationTimeoutSeconds"></a>
Maximum amount of time in seconds a request can be processed before it is marked as expired. The default is 15 minutes, or 900 seconds.
Valid Range: Minimum value of 1. Maximum value of 3600.

 ** [RequestTTLSeconds](#API_runtime_InvokeEndpointAsync_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointAsync-request-RequestTTLSeconds"></a>
Maximum age in seconds a request can be in the queue before it is marked as expired. The default is 6 hours, or 21,600 seconds.
Valid Range: Minimum value of 60. Maximum value of 21600.

 ** [S3OutputPathExtension](#API_runtime_InvokeEndpointAsync_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointAsync-request-S3OutputPathExtension"></a>
The path extension that is appended to the Amazon S3 output path where the inference response payload is stored.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^(?!s3:|https:)[a-zA-Z0-9!_.*'()/-]+$`

## Request Body
<a name="API_runtime_InvokeEndpointAsync_RequestBody"></a>

The request accepts the following binary data.

 ** [Body](#API_runtime_InvokeEndpointAsync_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpointAsync-request-Body"></a>
Provides inline input data for the inference request, in the format specified in the `ContentType` request header. Use this parameter to send the request payload directly in the API call instead of uploading it to Amazon S3 and referencing it with `InputLocation`. The inline payload can be up to 128,000 bytes.
 `Body` and `InputLocation` are mutually exclusive. Provide exactly one of them.
For information about the format of the request body, see [Common Data Formats-Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html).
Length Constraints: Maximum length of 128000.

## Response Syntax
<a name="API_runtime_InvokeEndpointAsync_ResponseSyntax"></a>

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
<a name="API_runtime_InvokeEndpointAsync_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The response returns the following HTTP headers.

 ** [FailureLocation](#API_runtime_InvokeEndpointAsync_ResponseSyntax) **   <a name="sagemaker-runtime_InvokeEndpointAsync-response-FailureLocation"></a>
The Amazon S3 URI where the inference failure response payload is stored.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [OutputLocation](#API_runtime_InvokeEndpointAsync_ResponseSyntax) **   <a name="sagemaker-runtime_InvokeEndpointAsync-response-OutputLocation"></a>
The Amazon S3 URI where the inference response payload is stored.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

The following data is returned in JSON format by the service.

 ** [InferenceId](#API_runtime_InvokeEndpointAsync_ResponseSyntax) **   <a name="sagemaker-runtime_InvokeEndpointAsync-response-InferenceId"></a>
Identifier for an inference request. This will be the same as the `InferenceId` specified in the input. Amazon SageMaker AI will generate an identifier for you if you do not specify one.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

## Errors
<a name="API_runtime_InvokeEndpointAsync_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailure **
 An internal failure occurred.
HTTP Status Code: 500

 ** ServiceUnavailable **
 The service is unavailable. Try your call again.
HTTP Status Code: 503

 ** ValidationError **
 Inspect your request and try again.
HTTP Status Code: 400

## See Also
<a name="API_runtime_InvokeEndpointAsync_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/runtime.sagemaker-2017-05-13/InvokeEndpointAsync)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/runtime.sagemaker-2017-05-13/InvokeEndpointAsync)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/runtime.sagemaker-2017-05-13/InvokeEndpointAsync)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/runtime.sagemaker-2017-05-13/InvokeEndpointAsync)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/runtime.sagemaker-2017-05-13/InvokeEndpointAsync)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/runtime.sagemaker-2017-05-13/InvokeEndpointAsync)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/runtime.sagemaker-2017-05-13/InvokeEndpointAsync)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/runtime.sagemaker-2017-05-13/InvokeEndpointAsync)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/runtime.sagemaker-2017-05-13/InvokeEndpointAsync)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/runtime.sagemaker-2017-05-13/InvokeEndpointAsync)
