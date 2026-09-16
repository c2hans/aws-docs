---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_DeleteMicrovmImage.html
---

# DeleteMicrovmImage
<a name="API_DeleteMicrovmImage"></a>

Deletes a MicroVM image. This operation is idempotent; deleting an image that has already been deleted succeeds without error.

## Request Syntax
<a name="API_DeleteMicrovmImage_RequestSyntax"></a>

```
DELETE /2025-09-09/microvm-images/{{imageIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteMicrovmImage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [imageIdentifier](#API_DeleteMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-DeleteMicrovmImage-request-uri-imageIdentifier"></a>
The unique identifier (ARN or ID) of the MicroVM image to delete.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_DeleteMicrovmImage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteMicrovmImage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "imageIdentifier": "string",
   "state": "string"
}
```

## Response Elements
<a name="API_DeleteMicrovmImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageIdentifier](#API_DeleteMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-DeleteMicrovmImage-response-imageIdentifier"></a>
The identifier of the deleted MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [state](#API_DeleteMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-DeleteMicrovmImage-response-state"></a>
The current state of the MicroVM image after deletion.
Type: String
Valid Values: `CREATING | CREATED | CREATE_FAILED | UPDATING | UPDATED | UPDATE_FAILED | DELETING | DELETE_FAILED | DELETED`

## Errors
<a name="API_DeleteMicrovmImage_Errors"></a>

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
<a name="API_DeleteMicrovmImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-microvms-2025-09-09/DeleteMicrovmImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-microvms-2025-09-09/DeleteMicrovmImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/DeleteMicrovmImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-microvms-2025-09-09/DeleteMicrovmImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/DeleteMicrovmImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-microvms-2025-09-09/DeleteMicrovmImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-microvms-2025-09-09/DeleteMicrovmImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-microvms-2025-09-09/DeleteMicrovmImage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-microvms-2025-09-09/DeleteMicrovmImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/DeleteMicrovmImage)
