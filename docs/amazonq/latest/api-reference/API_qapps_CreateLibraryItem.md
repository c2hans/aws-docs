---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CreateLibraryItem.html
---

# CreateLibraryItem
<a name="API_qapps_CreateLibraryItem"></a>

Creates a new library item for an Amazon Q App, allowing it to be discovered and used by other allowed users.

## Request Syntax
<a name="API_qapps_CreateLibraryItem_RequestSyntax"></a>

```
POST /catalog.createItem HTTP/1.1
instance-id: {{instanceId}}
Content-type: application/json

{
   "appId": "{{string}}",
   "appVersion": {{number}},
   "categories": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_qapps_CreateLibraryItem_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_qapps_CreateLibraryItem_RequestSyntax) **   <a name="qbusiness-qapps_CreateLibraryItem-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

## Request Body
<a name="API_qapps_CreateLibraryItem_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appId](#API_qapps_CreateLibraryItem_RequestSyntax) **   <a name="qbusiness-qapps_CreateLibraryItem-request-appId"></a>
The unique identifier of the Amazon Q App to publish to the library.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** [appVersion](#API_qapps_CreateLibraryItem_RequestSyntax) **   <a name="qbusiness-qapps_CreateLibraryItem-request-appVersion"></a>
The version of the Amazon Q App to publish to the library.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** [categories](#API_qapps_CreateLibraryItem_RequestSyntax) **   <a name="qbusiness-qapps_CreateLibraryItem-request-categories"></a>
The categories to associate with the library item for easier discovery.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

## Response Syntax
<a name="API_qapps_CreateLibraryItem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "createdBy": "string",
   "isVerified": boolean,
   "libraryItemId": "string",
   "ratingCount": number,
   "status": "string",
   "updatedAt": "string",
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_qapps_CreateLibraryItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_qapps_CreateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_CreateLibraryItem-response-createdAt"></a>
The date and time the library item was created.
Type: Timestamp

 ** [createdBy](#API_qapps_CreateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_CreateLibraryItem-response-createdBy"></a>
The user who created the library item.
Type: String

 ** [isVerified](#API_qapps_CreateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_CreateLibraryItem-response-isVerified"></a>
Indicates whether the library item has been verified.
Type: Boolean

 ** [libraryItemId](#API_qapps_CreateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_CreateLibraryItem-response-libraryItemId"></a>
The unique identifier of the new library item.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`

 ** [ratingCount](#API_qapps_CreateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_CreateLibraryItem-response-ratingCount"></a>
The number of ratings the library item has received from users.
Type: Integer

 ** [status](#API_qapps_CreateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_CreateLibraryItem-response-status"></a>
The status of the new library item, such as "Published".
Type: String

 ** [updatedAt](#API_qapps_CreateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_CreateLibraryItem-response-updatedAt"></a>
The date and time the library item was last updated.
Type: Timestamp

 ** [updatedBy](#API_qapps_CreateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_CreateLibraryItem-response-updatedBy"></a>
The user who last updated the library item.
Type: String

## Errors
<a name="API_qapps_CreateLibraryItem_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The client is not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal service error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** resourceId **
The unique identifier of the resource
 ** resourceType **
The type of the resource
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The requested operation could not be completed because it would exceed the service's quota or limit.
 ** quotaCode **
The code of the quota that was exceeded
 ** resourceId **
The unique identifier of the resource
 ** resourceType **
The type of the resource
 ** serviceCode **
The code for the service where the quota was exceeded
HTTP Status Code: 402

 ** ThrottlingException **
The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.
 ** quotaCode **
The code of the quota that was exceeded
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation
 ** serviceCode **
The code for the service where the quota was exceeded
HTTP Status Code: 429

 ** UnauthorizedException **
The client is not authenticated or authorized to perform the requested operation.
HTTP Status Code: 401

 ** ValidationException **
The input failed to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_qapps_CreateLibraryItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/CreateLibraryItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/CreateLibraryItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/CreateLibraryItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/CreateLibraryItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/CreateLibraryItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/CreateLibraryItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/CreateLibraryItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/CreateLibraryItem)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/CreateLibraryItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/CreateLibraryItem)
