---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_TerminateMicrovm.html
---

# TerminateMicrovm
<a name="API_TerminateMicrovm"></a>

Terminates a MicroVM. This operation is idempotent; terminating a MicroVM that has already been terminated succeeds without error.

## Request Syntax
<a name="API_TerminateMicrovm_RequestSyntax"></a>

```
DELETE /2025-09-09/microvms/{{microvmIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_TerminateMicrovm_RequestParameters"></a>

The request uses the following URI parameters.

 ** [microvmIdentifier](#API_TerminateMicrovm_RequestSyntax) **   <a name="lambdamicrovm-TerminateMicrovm-request-uri-microvmIdentifier"></a>
The ID of the MicroVM to terminate.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_TerminateMicrovm_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_TerminateMicrovm_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_TerminateMicrovm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TerminateMicrovm_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of the resource that caused the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An internal server error occurred. Retry the request later.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling. Retry the request later.
 ** quotaCode **
The quota code of the throttled service quota.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The service code of the throttled service quota.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_TerminateMicrovm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-microvms-2025-09-09/TerminateMicrovm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-microvms-2025-09-09/TerminateMicrovm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/TerminateMicrovm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-microvms-2025-09-09/TerminateMicrovm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/TerminateMicrovm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-microvms-2025-09-09/TerminateMicrovm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-microvms-2025-09-09/TerminateMicrovm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-microvms-2025-09-09/TerminateMicrovm)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-microvms-2025-09-09/TerminateMicrovm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/TerminateMicrovm)
