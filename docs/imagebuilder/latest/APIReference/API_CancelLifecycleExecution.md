---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CancelLifecycleExecution.html
---

# CancelLifecycleExecution
<a name="API_CancelLifecycleExecution"></a>

Cancel a specific image lifecycle policy runtime instance.

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
Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
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
The unique identifier for the image lifecycle runtime instance that was canceled.
Type: String
Pattern: `^lce-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

## Errors
<a name="API_CancelLifecycleExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** IdempotentParameterMismatchException **
You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.
HTTP Status Code: 400

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

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
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/CancelLifecycleExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/CancelLifecycleExecution)
