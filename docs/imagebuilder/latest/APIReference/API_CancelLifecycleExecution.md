---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CancelLifecycleExecution.html
---

# CancelLifecycleExecution
<a name="API_CancelLifecycleExecution"></a>

Cancels a lifecycle execution – a single run of lifecycle actions that a lifecycle policy or a [StartResourceStateUpdate](API_StartResourceStateUpdate.md) request started. You can only cancel an execution that hasn't reached a terminal state. Cancellation is asynchronous and doesn't undo completed lifecycle actions.

## Request Syntax
<a name="API_CancelLifecycleExecution_RequestSyntax"></a>

```
PUT /CancelLifecycleExecution HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "lifecycleExecutionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CancelLifecycleExecution_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CancelLifecycleExecution_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CancelLifecycleExecution_RequestSyntax) **   <a name="imagebuilder-CancelLifecycleExecution-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [lifecycleExecutionId](#API_CancelLifecycleExecution_RequestSyntax) **   <a name="imagebuilder-CancelLifecycleExecution-request-lifecycleExecutionId"></a>
Identifies the specific runtime instance of the image lifecycle to cancel.
Type: String
Pattern: `^lce-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_CancelLifecycleExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "lifecycleExecutionId": "string"
}
```

## Response Elements
<a name="API_CancelLifecycleExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lifecycleExecutionId](#API_CancelLifecycleExecution_ResponseSyntax) **   <a name="imagebuilder-CancelLifecycleExecution-response-lifecycleExecutionId"></a>
The unique identifier of the lifecycle execution that the cancellation request applies to. The cancellation completes asynchronously.
Type: String
Pattern: `^lce-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

## Errors
<a name="API_CancelLifecycleExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** IdempotentParameterMismatchException **
You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_CancelLifecycleExecution_Examples"></a>

### Cancel a lifecycle execution
<a name="API_CancelLifecycleExecution_Example_1"></a>

The following example cancels the scheduled resource state update associated with the specified lifecycle execution ID before it runs.

#### Sample Request
<a name="API_CancelLifecycleExecution_Example_1_Request"></a>

```
PUT /CancelLifecycleExecution HTTP/1.1
Content-type: application/json

{
    "lifecycleExecutionId": "lce-401aefc3-a829-46f6-8fc2-91497988a503",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE97531"
}
```

#### Sample Response
<a name="API_CancelLifecycleExecution_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "lifecycleExecutionId": "lce-401aefc3-a829-46f6-8fc2-91497988a503"
}
```

## See Also
<a name="API_CancelLifecycleExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/CancelLifecycleExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/CancelLifecycleExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/CancelLifecycleExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/CancelLifecycleExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/CancelLifecycleExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/CancelLifecycleExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/CancelLifecycleExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/CancelLifecycleExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/CancelLifecycleExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/CancelLifecycleExecution)
