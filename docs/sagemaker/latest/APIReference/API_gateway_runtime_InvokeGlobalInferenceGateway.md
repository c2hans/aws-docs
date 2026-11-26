---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_gateway_runtime_InvokeGlobalInferenceGateway.html
---

# InvokeGlobalInferenceGateway

Buffered (non-streaming) inference. Returns the full OpenAI completion body.

Errors carry their origin in the `Message` prefix. Every typed error's text is in the `Message` member (JSON key `Message`), and starts with one of these prefixes:

Global Inference Gateway:
The gateway rejected or failed the request itself: validation, authorization, throttling, routing (the gateway or model was not found, or no capacity is available), a gateway limit or time limit, or failing to reach the inference gateway (`Global Inference Gateway: could not reach the inference gateway: <reason>`, or `Global Inference Gateway: timed out waiting for the inference gateway`). This includes the 400 for an invalid request and the 413 for a request body that is too large.

inference gateway:
The inference gateway serving the model returned an error status. The message gives that status code and up to 256 bytes of its error message, for example `inference gateway: 503 <message>`. A `BadGatewayException` can instead read `inference gateway: response ended unexpectedly`, with no status, when the inference gateway's connection failed while it was sending the response.

inference gateway (<component>):
The same, when the inference gateway reports which of its components produced the error, for example `inference gateway (model server): 502 <message>`. The component is one of:
config
The inference gateway's configuration and proxy layer.
scheduler
The inference gateway's request scheduler.
model selector
The inference gateway's model selector.
model server
The model server.

Every error status the inference gateway returns is a typed error, chosen by that status:

400, and any other 4xx not listed here
A 400 validation error.

401, 403
 `AccessDeniedException` (403).

404
 `ResourceNotFoundException`.

408
 `GatewayTimeoutException` (504).

429
 `ThrottlingException`, with the `Retry-After` header.

502, and 500, 503 or any other 5xx not listed here
 `BadGatewayException` (502). A 5xx from the inference gateway can occur after the model started processing the request, so it is not modeled as retryable, and the gateway may already have tried another inference gateway.

504
 `GatewayTimeoutException`.

**Important**
This error is not modeled as retryable, but the standard retry modes of AWS SDKs retry 5xx status codes. Each retry runs the inference again.

## Request Syntax
<a name="API_gateway_runtime_InvokeGlobalInferenceGateway_RequestSyntax"></a>

```
POST /global-inference-gateway/{{GatewayId}}/invocations HTTP/1.1
Accept: {{Accept}}
Content-Type: {{ContentType}}
X-Amzn-SageMaker-Customer-Identity-Token: {{CustomerIdentityToken}}

{{Body}}
```

## URI Request Parameters
<a name="API_gateway_runtime_InvokeGlobalInferenceGateway_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Accept](#API_gateway_runtime_InvokeGlobalInferenceGateway_RequestSyntax) **   <a name="sagemaker-gateway_runtime_InvokeGlobalInferenceGateway-request-Accept"></a>
The MIME type you want for the response. It is passed to the model server.

 ** [ContentType](#API_gateway_runtime_InvokeGlobalInferenceGateway_RequestSyntax) **   <a name="sagemaker-gateway_runtime_InvokeGlobalInferenceGateway-request-ContentType"></a>
The MIME type of the request body. Pass `application/json` (parameters such as `charset=utf-8` are allowed): the body is one OpenAI JSON object. The Global Inference Gateway rejects other content types with a 415 error.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [CustomerIdentityToken](#API_gateway_runtime_InvokeGlobalInferenceGateway_RequestSyntax) **   <a name="sagemaker-gateway_runtime_InvokeGlobalInferenceGateway-request-CustomerIdentityToken"></a>
Per-caller customer identity token (a JWT), forwarded unchanged to the inference gateway, which validates it. The gateway does not use it to authorize the request. Include it in the Signature Version 4 signed headers so it cannot be altered in transit. Redacted from logs, metrics and traces.

 ** [GatewayId](#API_gateway_runtime_InvokeGlobalInferenceGateway_RequestSyntax) **   <a name="sagemaker-gateway_runtime_InvokeGlobalInferenceGateway-request-uri-GatewayId"></a>
The ID of the Global Inference Gateway to invoke. IAM policies refer to the gateway by its ARN, `arn:<partition>:sagemaker:<region>:<account>:global-inference-gateway/<id>`.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_gateway_runtime_InvokeGlobalInferenceGateway_RequestBody"></a>

The request accepts the following binary data.

 ** [Body](#API_gateway_runtime_InvokeGlobalInferenceGateway_RequestSyntax) **   <a name="sagemaker-gateway_runtime_InvokeGlobalInferenceGateway-request-Body"></a>
The inference request body: one OpenAI JSON object, at most 10 MiB. Its content is passed to the model server unchanged, except that the request is always sent with `"stream": false`: this operation returns one JSON document, so a `"stream": true` in the body is overridden. Use `InvokeGlobalInferenceGatewayWithResponseStream` to stream.
A body that is not one JSON object, or that repeats the top-level `model` key with different values, is rejected with a 400 validation error. A body larger than 10 MiB is rejected with `PayloadTooLargeException` (413). The gateway reads only `model` and `stream`, and does not store the body.
Length Constraints: Minimum length of 0. Maximum length of 10485760.
Required: Yes

## Response Syntax
<a name="API_gateway_runtime_InvokeGlobalInferenceGateway_ResponseSyntax"></a>

```
HTTP/1.1 200

{{Body}}
```

## Response Elements
<a name="API_gateway_runtime_InvokeGlobalInferenceGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following as the HTTP body.

 ** [Body](#API_gateway_runtime_InvokeGlobalInferenceGateway_ResponseSyntax) **   <a name="sagemaker-gateway_runtime_InvokeGlobalInferenceGateway-response-Body"></a>
The model server's OpenAI completion JSON, returned unchanged. A response larger than 10 MiB fails with `BadGatewayException` (502).
Length Constraints: Minimum length of 0. Maximum length of 10485760.

## Errors
<a name="API_gateway_runtime_InvokeGlobalInferenceGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to invoke this gateway. Invoking requires the `sagemaker:InvokeGlobalInferenceGateway` permission, or `sagemaker:InvokeGlobalInferenceGatewayWithResponseStream` for the streaming operation, on the gateway ARN.
A message starting `inference gateway` means the inference gateway serving the model refused the request with a 401 or 403, for example for its customer identity token. Its status code is in the message (the response status is 403), and up to 256 bytes of its error message are quoted.
 ** Message **
A description of the error. It starts with a prefix such as `Global Inference Gateway: ` or `inference gateway: ` that says where the error came from.
HTTP Status Code: 403

 ** BadGatewayException **
The gateway could not get a usable response from the inference gateway. The `Message` prefix says why:
Global Inference Gateway: could not reach the inference gateway: <reason>
The request could not be sent, or the connection closed before a response arrived. For example, the connection failed, or the inference gateway closed it after reading the request.
Global Inference Gateway: timed out waiting for the inference gateway
The inference gateway stopped sending partway through the response body and the gateway's read timeout expired. The same text on a `GatewayTimeoutException` means no response arrived at all.
Any other Global Inference Gateway: message
The gateway ended a response before it was complete, for example because it exceeded the 10 MiB limit of the buffered operation, the request exceeded its maximum duration, or the inference gateway was taken out of service.
inference gateway: <status> <message>
The inference gateway serving the model returned a 502, 500, 503 or another 5xx error. Its status code is in the message (the response status is 502), and up to 256 bytes of its error message are quoted.
inference gateway: response ended unexpectedly
The inference gateway's connection failed while it was sending the response.
The inference gateway names a component in the prefix when it reports one: `inference gateway (<component>): `, where the component is `config` (the inference gateway's configuration and proxy layer), `scheduler` (its request scheduler), `model selector` (its model selector) or `model server` (the model server).
A 502 can mean the inference already ran, and the gateway may already have tried another inference gateway.
This error is not modeled as retryable, but the standard retry modes of AWS SDKs retry 5xx status codes. Each retry runs the inference again.
 ** Message **
A description of the error. It starts with a prefix such as `Global Inference Gateway: ` or `inference gateway: ` that says where the error came from.
HTTP Status Code: 502

 ** GatewayTimeoutException **
The inference gateway did not respond in time. The `Message` prefix says whose time limit expired:
Global Inference Gateway: timed out waiting for the inference gateway
The gateway's limit on the wait for the first part of the response.
inference gateway: <status> <message>
The inference gateway serving the model returned a 504, or a 408 because it timed out waiting for the request to arrive. Its status code is in the message (the response status is 504), and up to 256 bytes of its error message are quoted.
The inference gateway names a component in the prefix when it reports one: `inference gateway (<component>): `, where the component is `config` (the inference gateway's configuration and proxy layer), `scheduler` (its request scheduler), `model selector` (its model selector) or `model server` (the model server).
A timeout does not prove the inference did not run, and the gateway may already have tried another inference gateway.
This error is not modeled as retryable, but the standard retry modes of AWS SDKs retry 5xx status codes. Each retry runs the inference again.
 ** Message **
A description of the error. It starts with a prefix such as `Global Inference Gateway: ` or `inference gateway: ` that says where the error came from.
HTTP Status Code: 504

 ** InternalServerException **
An unexpected internal failure occurred.
The gateway returns this error before the request reaches a model, so retrying it does not run the inference again. AWS SDKs retry this error automatically.
 ** Message **
A description of the error. It starts with `Global Inference Gateway: `, because the Global Inference Gateway returns this error itself.
HTTP Status Code: 500

 ** PayloadTooLargeException **
The request body exceeds the 10 MiB limit. Reduce the size of the payload and send the request again.
 ** Message **
A description of the error. It starts with `Global Inference Gateway: `, because the Global Inference Gateway returns this error itself.
HTTP Status Code: 413

 ** ResourceNotFoundException **
No gateway with this ID exists in this account and Region, or no target of the gateway serves the model named in the request body. A model that is served but has no available target right now returns `ServiceUnavailableException` instead.
A message starting `inference gateway` means the inference gateway serving the model returned a 404; up to 256 bytes of its error message are quoted.
 ** Message **
A description of the error. It starts with a prefix such as `Global Inference Gateway: ` or `inference gateway: ` that says where the error came from.
 ** ResourceId **
The ID of the resource that was not found: the gateway ID, or the model name.
 ** ResourceType **
The kind of resource that was not found: the gateway, or the model.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unable to serve the request, for example because no capacity is available for the requested model. The request was not dispatched for inference.
A 503 returned by the inference gateway serving the model after dispatch is reported as `BadGatewayException`, with the 503 in its `Message`, not as this error.
The gateway returns this error before the request reaches a model, so retrying it does not run the inference again. AWS SDKs retry this error automatically.
 ** Message **
A description of the error. It starts with `Global Inference Gateway: `, because the Global Inference Gateway returns this error itself.
HTTP Status Code: 503

 ** ThrottlingException **
The request was throttled before it was dispatched for inference. Retry the request with backoff, after the `Retry-After` seconds when the response carries one.
A message starting `inference gateway` means the last inference gateway tried for the model returned a 429. The gateway may have tried others first, and they may have failed for other reasons. Up to 256 bytes of its error message are quoted.
The gateway returns this error before the request reaches a model, so retrying it does not run the inference again. AWS SDKs retry this error automatically.
 ** Message **
A description of the error. It starts with a prefix such as `Global Inference Gateway: ` or `inference gateway: ` that says where the error came from.
HTTP Status Code: 429

## See Also
<a name="API_gateway_runtime_InvokeGlobalInferenceGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-gateway-runtime-2026-10-01/InvokeGlobalInferenceGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-gateway-runtime-2026-10-01/InvokeGlobalInferenceGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-gateway-runtime-2026-10-01/InvokeGlobalInferenceGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-gateway-runtime-2026-10-01/InvokeGlobalInferenceGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-gateway-runtime-2026-10-01/InvokeGlobalInferenceGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-gateway-runtime-2026-10-01/InvokeGlobalInferenceGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-gateway-runtime-2026-10-01/InvokeGlobalInferenceGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-gateway-runtime-2026-10-01/InvokeGlobalInferenceGateway)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-gateway-runtime-2026-10-01/InvokeGlobalInferenceGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-gateway-runtime-2026-10-01/InvokeGlobalInferenceGateway)
