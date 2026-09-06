---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateLibraryItem.html
---

# UpdateLibraryItem
<a name="API_qapps_UpdateLibraryItem"></a>

Updates the library item for an Amazon Q App.

## Request Syntax
<a name="API_qapps_UpdateLibraryItem_RequestSyntax"></a>

```
POST /catalog.updateItem HTTP/1.1
instance-id: {{instanceId}}
Content-type: application/json

{
   "categories": [ "{{string}}" ],
   "libraryItemId": "{{string}}",
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_qapps_UpdateLibraryItem_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_qapps_UpdateLibraryItem_RequestSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

## Request Body
<a name="API_qapps_UpdateLibraryItem_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [categories](#API_qapps_UpdateLibraryItem_RequestSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-request-categories"></a>
The new categories to associate with the library item.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: No

 ** [libraryItemId](#API_qapps_UpdateLibraryItem_RequestSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-request-libraryItemId"></a>
The unique identifier of the library item to update.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** [status](#API_qapps_UpdateLibraryItem_RequestSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-request-status"></a>
The new status to set for the library item, such as "Published" or "Hidden".
Type: String
Valid Values: `PUBLISHED | DISABLED`
Required: No

## Response Syntax
<a name="API_qapps_UpdateLibraryItem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appId": "string",
   "appVersion": number,
   "categories": [
      {
         "appCount": number,
         "color": "string",
         "id": "string",
         "title": "string"
      }
   ],
   "createdAt": "string",
   "createdBy": "string",
   "isRatedByUser": boolean,
   "isVerified": boolean,
   "libraryItemId": "string",
   "ratingCount": number,
   "status": "string",
   "updatedAt": "string",
   "updatedBy": "string",
   "userCount": number
}
```

## Response Elements
<a name="API_qapps_UpdateLibraryItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appId](#API_qapps_UpdateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-response-appId"></a>
The unique identifier of the Q App associated with the library item.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`

 ** [appVersion](#API_qapps_UpdateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-response-appVersion"></a>
The version of the Q App associated with the library item.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.

 ** [categories](#API_qapps_UpdateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-response-categories"></a>
The categories associated with the updated library item.
Type: Array of [Category](API_qapps_Category.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.

 ** [createdAt](#API_qapps_UpdateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-response-createdAt"></a>
The date and time the library item was originally created.
Type: Timestamp

 ** [createdBy](#API_qapps_UpdateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-response-createdBy"></a>
The user who originally created the library item.
Type: String

 ** [isRatedByUser](#API_qapps_UpdateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-response-isRatedByUser"></a>
Whether the current user has rated the library item.
Type: Boolean

 ** [isVerified](#API_qapps_UpdateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-response-isVerified"></a>
Indicates whether the library item has been verified.
Type: Boolean

 ** [libraryItemId](#API_qapps_UpdateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-response-libraryItemId"></a>
The unique identifier of the updated library item.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`

 ** [ratingCount](#API_qapps_UpdateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-response-ratingCount"></a>
The number of ratings the library item has received.
Type: Integer

 ** [status](#API_qapps_UpdateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-response-status"></a>
The new status of the updated library item.
Type: String

 ** [updatedAt](#API_qapps_UpdateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-response-updatedAt"></a>
The date and time the library item was last updated.
Type: Timestamp

 ** [updatedBy](#API_qapps_UpdateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-response-updatedBy"></a>
The user who last updated the library item.
Type: String

 ** [userCount](#API_qapps_UpdateLibraryItem_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateLibraryItem-response-userCount"></a>
The number of users who have the associated Q App.
Type: Integer

## Errors
<a name="API_qapps_UpdateLibraryItem_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The client is not authorized to perform the requested operation.
HTTP Status Code: 403

 ** ConflictException **
The requested operation could not be completed due to a conflict with the current state of the resource.
 ** resourceId **
The unique identifier of the resource
 ** resourceType **
The type of the resource
HTTP Status Code: 409

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
<a name="API_qapps_UpdateLibraryItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/UpdateLibraryItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/UpdateLibraryItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/UpdateLibraryItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/UpdateLibraryItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/UpdateLibraryItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/UpdateLibraryItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/UpdateLibraryItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/UpdateLibraryItem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/UpdateLibraryItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/UpdateLibraryItem)
