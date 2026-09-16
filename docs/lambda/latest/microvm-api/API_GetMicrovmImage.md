---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_GetMicrovmImage.html
---

# GetMicrovmImage
<a name="API_GetMicrovmImage"></a>

Retrieves the details of a MicroVM image, including its state, versions, and configuration.

## Request Syntax
<a name="API_GetMicrovmImage_RequestSyntax"></a>

```
GET /2025-09-09/microvm-images/{{imageIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMicrovmImage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [imageIdentifier](#API_GetMicrovmImage_RequestSyntax) **   <a name="lambdamicrovm-GetMicrovmImage-request-uri-imageIdentifier"></a>
The unique identifier (ARN or ID) of the MicroVM image to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_GetMicrovmImage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMicrovmImage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "imageArn": "string",
   "latestActiveImageVersion": "string",
   "latestFailedImageVersion": "string",
   "name": "string",
   "state": "string",
   "tags": {
      "string" : "string"
   },
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetMicrovmImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImage-response-createdAt"></a>
The timestamp when the MicroVM image was created.
Type: Timestamp

 ** [imageArn](#API_GetMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImage-response-imageArn"></a>
The ARN of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [latestActiveImageVersion](#API_GetMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImage-response-latestActiveImageVersion"></a>
The latest active version of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [latestFailedImageVersion](#API_GetMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImage-response-latestFailedImageVersion"></a>
The latest failed version of the MicroVM image, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [name](#API_GetMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImage-response-name"></a>
The name of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`

 ** [state](#API_GetMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImage-response-state"></a>
The current state of the MicroVM image.
Type: String
Valid Values: `CREATING | CREATED | CREATE_FAILED | UPDATING | UPDATED | UPDATE_FAILED | DELETING | DELETE_FAILED | DELETED`

 ** [tags](#API_GetMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImage-response-tags"></a>
A set of key-value pairs that you can attach to the resource. Use tags to categorize resources for cost allocation, access control (ABAC), and organization.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

 ** [updatedAt](#API_GetMicrovmImage_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImage-response-updatedAt"></a>
The timestamp when the MicroVM image was last updated.
Type: Timestamp

## Errors
<a name="API_GetMicrovmImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetMicrovmImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-microvms-2025-09-09/GetMicrovmImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-microvms-2025-09-09/GetMicrovmImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/GetMicrovmImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-microvms-2025-09-09/GetMicrovmImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/GetMicrovmImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-microvms-2025-09-09/GetMicrovmImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-microvms-2025-09-09/GetMicrovmImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-microvms-2025-09-09/GetMicrovmImage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-microvms-2025-09-09/GetMicrovmImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/GetMicrovmImage)
