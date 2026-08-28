---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html
---

# InvokeEndpoint
<a name="API_runtime_InvokeEndpoint"></a>

After you deploy a model into production using Amazon SageMaker AI hosting services, your client applications use this API to get inferences from the model hosted at the specified endpoint.

For an overview of Amazon SageMaker AI, see [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html).

Amazon SageMaker AI strips all POST headers except those supported by the API. Amazon SageMaker AI might add additional headers. You should not rely on the behavior of headers outside those enumerated in the request syntax.

Calls to `InvokeEndpoint` are authenticated by using AWS Signature Version 4. For information, see [Authenticating Requests (AWS Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html) in the *Amazon S3 API Reference*.

A customer's model containers must respond to requests within 60 seconds. The model itself can have a maximum processing time of 60 seconds before responding to invocations. If your model is going to take 50-60 seconds of processing time, the SDK socket timeout should be set to be 70 seconds.

**Note**
Endpoints are scoped to an individual account, and are not public. The URL does not contain the account ID, but Amazon SageMaker AI determines the account ID from the authentication token that is supplied by the caller.

## Request Syntax
<a name="API_runtime_InvokeEndpoint_RequestSyntax"></a>

```
POST /endpoints/{{EndpointName}}/invocations HTTP/1.1
Content-Type: {{ContentType}}
Accept: {{Accept}}
X-Amzn-SageMaker-Custom-Attributes: {{CustomAttributes}}
X-Amzn-SageMaker-Target-Model: {{TargetModel}}
X-Amzn-SageMaker-Target-Variant: {{TargetVariant}}
X-Amzn-SageMaker-Target-Container-Hostname: {{TargetContainerHostname}}
X-Amzn-SageMaker-Inference-Id: {{InferenceId}}
X-Amzn-SageMaker-Enable-Explanations: {{EnableExplanations}}
X-Amzn-SageMaker-Inference-Component: {{InferenceComponentName}}
X-Amzn-SageMaker-Session-Id: {{SessionId}}
X-Amzn-SageMaker-Prefix-Aware-Id: {{PrefixAwareId}}

{{Body}}
```

## URI Request Parameters
<a name="API_runtime_InvokeEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Accept](#API_runtime_InvokeEndpoint_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-request-Accept"></a>
The desired MIME type of the inference response from the model container.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [ContentType](#API_runtime_InvokeEndpoint_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-request-ContentType"></a>
The MIME type of the input data in the request body.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [CustomAttributes](#API_runtime_InvokeEndpoint_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-request-CustomAttributes"></a>
Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker AI endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in [Section 3.3.6. Field Value Components](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6) of the Hypertext Transfer Protocol (HTTP/1.1).
The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with `Trace ID:` in your post-processing function.
This feature is currently supported in the AWS SDKs but not in the Amazon SageMaker AI Python SDK.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [EnableExplanations](#API_runtime_InvokeEndpoint_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-request-EnableExplanations"></a>
An optional JMESPath expression used to override the `EnableExplanations` parameter of the `ClarifyExplainerConfig` API. See the [EnableExplanations](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html#clarify-online-explainability-create-endpoint-enable) section in the developer guide for more information.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`

 ** [EndpointName](#API_runtime_InvokeEndpoint_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-request-uri-EndpointName"></a>
The name of the endpoint that you specified when you created the endpoint using the [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html) API.
Length Constraints: Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** [InferenceComponentName](#API_runtime_InvokeEndpoint_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-request-InferenceComponentName"></a>
If the endpoint hosts one or more inference components, this parameter specifies the name of inference component to invoke.
Length Constraints: Maximum length of 63.
Pattern: `^[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?$`

 ** [InferenceId](#API_runtime_InvokeEndpoint_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-request-InferenceId"></a>
If you provide a value, it is added to the captured data when you enable data capture on the endpoint. For information about data capture, see [Capture Data](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html).
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\A\S[\p{Print}]*\z`

 ** [PrefixAwareId](#API_runtime_InvokeEndpoint_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-request-PrefixAwareId"></a>
An optional, stable identifier that serves as a routing hint for prefix-aware routing. The service routes requests with the same prefix and the same identifier to the same instance. If requests from different applications might have the same prompt prefix, set a different identifier for each application to differentiate their routing decisions.
Applies only to endpoints configured with a `RoutingStrategy` of `PREFIX_AWARE`.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\A\S[\p{Print}]*\z`

 ** [SessionId](#API_runtime_InvokeEndpoint_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-request-SessionId"></a>
Creates a stateful session or identifies an existing one. You can do one of the following:
+ Create a stateful session by specifying the value `NEW_SESSION`.
+ Send your request to an existing stateful session by specifying the ID of that session.
With a stateful session, you can send multiple requests to a stateful model. When you create a session with a stateful model, the model must create the session ID and set the expiration time. The model must also provide that information in the response to your request. You can get the ID and timestamp from the `NewSessionId` response parameter. For any subsequent request where you specify that session ID, SageMaker AI routes the request to the same instance that supports the session.
Length Constraints: Maximum length of 256.
Pattern: `^(NEW_SESSION)$|^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`

 ** [TargetContainerHostname](#API_runtime_InvokeEndpoint_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-request-TargetContainerHostname"></a>
If the endpoint hosts multiple containers and is configured to use direct invocation, this parameter specifies the host name of the container to invoke.
Length Constraints: Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`

 ** [TargetModel](#API_runtime_InvokeEndpoint_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-request-TargetModel"></a>
The model to request for inference when invoking a multi-model endpoint.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\A\S[\p{Print}]*\z`

 ** [TargetVariant](#API_runtime_InvokeEndpoint_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-request-TargetVariant"></a>
Specify the production variant to send the inference request to when invoking an endpoint that is running two or more variants. Note that this parameter overrides the default behavior for the endpoint, which is to distribute the invocation traffic based on the variant weights.
For information about how to use variant targeting to perform a/b testing, see [Test models in production](https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html)
Length Constraints: Maximum length of 63.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`

## Request Body
<a name="API_runtime_InvokeEndpoint_RequestBody"></a>

The request accepts the following binary data.

 ** [Body](#API_runtime_InvokeEndpoint_RequestSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-request-Body"></a>
Provides input data, in the format specified in the `ContentType` request header. Amazon SageMaker AI passes all of the data in the body to the model.
For information about the format of the request body, see [Common Data Formats-Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html).
Length Constraints: Maximum length of 6291456.
Required: Yes

## Response Syntax
<a name="API_runtime_InvokeEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{ContentType}}
x-Amzn-Invoked-Production-Variant: {{InvokedProductionVariant}}
X-Amzn-SageMaker-Custom-Attributes: {{CustomAttributes}}
X-Amzn-SageMaker-New-Session-Id: {{NewSessionId}}
X-Amzn-SageMaker-Closed-Session-Id: {{ClosedSessionId}}

{{Body}}
```

## Response Elements
<a name="API_runtime_InvokeEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ClosedSessionId](#API_runtime_InvokeEndpoint_ResponseSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-response-ClosedSessionId"></a>
If you closed a stateful session with your request, the ID of that session.
Length Constraints: Maximum length of 256.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`

 ** [ContentType](#API_runtime_InvokeEndpoint_ResponseSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-response-ContentType"></a>
The MIME type of the inference returned from the model container.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [CustomAttributes](#API_runtime_InvokeEndpoint_ResponseSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-response-CustomAttributes"></a>
Provides additional information in the response about the inference returned by a model hosted at an Amazon SageMaker AI endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to return an ID received in the `CustomAttributes` header of a request or other metadata that a service endpoint was programmed to produce. The value must consist of no more than 1024 visible US-ASCII characters as specified in [Section 3.3.6. Field Value Components](https://tools.ietf.org/html/rfc7230#section-3.2.6) of the Hypertext Transfer Protocol (HTTP/1.1). If the customer wants the custom attribute returned, the model must set the custom attribute to be included on the way back.
The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with `Trace ID:` in your post-processing function.
This feature is currently supported in the AWS SDKs but not in the Amazon SageMaker AI Python SDK.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [InvokedProductionVariant](#API_runtime_InvokeEndpoint_ResponseSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-response-InvokedProductionVariant"></a>
Identifies the production variant that was invoked.
Length Constraints: Maximum length of 1024.
Pattern: `\p{ASCII}*`

 ** [NewSessionId](#API_runtime_InvokeEndpoint_ResponseSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-response-NewSessionId"></a>
If you created a stateful session with your request, the ID and expiration time that the model assigns to that session.
Length Constraints: Maximum length of 256.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*;\sExpires=[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$`

The response returns the following as the HTTP body.

 ** [Body](#API_runtime_InvokeEndpoint_ResponseSyntax) **   <a name="sagemaker-runtime_InvokeEndpoint-response-Body"></a>
Includes the inference provided by the model.
For information about the format of the response body, see [Common Data Formats-Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html).
If the explainer is activated, the body includes the explanations provided by the model. For more information, see the **Response section** under [Invoke the Endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-invoke-endpoint.html#clarify-online-explainability-response) in the Developer Guide.
Length Constraints: Maximum length of 6291456.

## Errors
<a name="API_runtime_InvokeEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalDependencyException **
Your request caused an exception with an internal dependency. Contact customer support.
HTTP Status Code: 530

 ** InternalFailure **
 An internal failure occurred.
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

 ** ModelNotReadyException **
Either a serverless endpoint variant's resources are still being provisioned, or a multi-model endpoint is still downloading or loading the target model. Wait and try your request again.
HTTP Status Code: 429

 ** ServiceUnavailable **
 The service is unavailable. Try your call again.
HTTP Status Code: 503

 ** ValidationError **
 Inspect your request and try again.
HTTP Status Code: 400

## Examples
<a name="API_runtime_InvokeEndpoint_Examples"></a>

### Pass a trace ID in the CustomAttribute of a request and return it in the CustomAttribute of the response.
<a name="API_runtime_InvokeEndpoint_Example_1"></a>

In this example a trace ID is passed to the service endpoint in the `CustomAttributes` header of the request and then retrieved and returned in the `CustomAttributes` header of the response.

#### Sample Request
<a name="API_runtime_InvokeEndpoint_Example_1_Request"></a>

```
import boto3

client = boto3.client('sagemaker-runtime')

custom_attributes = "c000b4f9-df62-4c85-a0bf-7c525f9104a4"  # An example of a trace ID.
endpoint_name = "..."                                       # Your endpoint name.
content_type = "..."                                        # The MIME type of the input data in the request body.
accept = "..."                                              # The desired MIME type of the inference in the response.
payload = "..."                                             # Payload for inference.
response = client.invoke_endpoint(
    EndpointName=endpoint_name,
    CustomAttributes=custom_attributes,
    ContentType=content_type,
    Accept=accept,
    Body=payload
    )

print(response['CustomAttributes'])                         # If model receives and updates the custom_attributes header
                                                            # by adding "Trace id: " in front of custom_attributes in the request,
                                                            # custom_attributes in response becomes
                                                            # "Trace ID: c000b4f9-df62-4c85-a0bf-7c525f9104a4"
```

#### Sample Response
<a name="API_runtime_InvokeEndpoint_Example_1_Response"></a>

```
Trace ID: c000b4f9-df62-4c85-a0bf-7c525f9104a4
```

## See Also
<a name="API_runtime_InvokeEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/runtime.sagemaker-2017-05-13/InvokeEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/runtime.sagemaker-2017-05-13/InvokeEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/runtime.sagemaker-2017-05-13/InvokeEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/runtime.sagemaker-2017-05-13/InvokeEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/runtime.sagemaker-2017-05-13/InvokeEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/runtime.sagemaker-2017-05-13/InvokeEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/runtime.sagemaker-2017-05-13/InvokeEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/runtime.sagemaker-2017-05-13/InvokeEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/runtime.sagemaker-2017-05-13/InvokeEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/runtime.sagemaker-2017-05-13/InvokeEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
