---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ListLibraryItems.html
---

# ListLibraryItems
<a name="API_qapps_ListLibraryItems"></a>

Lists the library items for Amazon Q Apps that are published and available for users in your AWS account.

## Request Syntax
<a name="API_qapps_ListLibraryItems_RequestSyntax"></a>

```
GET /catalog.list?categoryId={{categoryId}}&limit={{limit}}&nextToken={{nextToken}} HTTP/1.1
instance-id: {{instanceId}}
```

## URI Request Parameters
<a name="API_qapps_ListLibraryItems_RequestParameters"></a>

The request uses the following URI parameters.

 ** [categoryId](#API_qapps_ListLibraryItems_RequestSyntax) **   <a name="qbusiness-qapps_ListLibraryItems-request-uri-categoryId"></a>
Optional category to filter the library items by.
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`

 ** [instanceId](#API_qapps_ListLibraryItems_RequestSyntax) **   <a name="qbusiness-qapps_ListLibraryItems-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

 ** [limit](#API_qapps_ListLibraryItems_RequestSyntax) **   <a name="qbusiness-qapps_ListLibraryItems-request-uri-limit"></a>
The maximum number of library items to return in the response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_qapps_ListLibraryItems_RequestSyntax) **   <a name="qbusiness-qapps_ListLibraryItems-request-uri-nextToken"></a>
The token to request the next page of results.
Length Constraints: Minimum length of 0. Maximum length of 300.

## Request Body
<a name="API_qapps_ListLibraryItems_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_qapps_ListLibraryItems_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "libraryItems": [
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_qapps_ListLibraryItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [libraryItems](#API_qapps_ListLibraryItems_ResponseSyntax) **   <a name="qbusiness-qapps_ListLibraryItems-response-libraryItems"></a>
The list of library items meeting the request criteria.
Type: Array of [LibraryItemMember](API_qapps_LibraryItemMember.md) objects

 ** [nextToken](#API_qapps_ListLibraryItems_ResponseSyntax) **   <a name="qbusiness-qapps_ListLibraryItems-response-nextToken"></a>
The token to use to request the next page of results.
Type: String

## Errors
<a name="API_qapps_ListLibraryItems_Errors"></a>

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
<a name="API_qapps_ListLibraryItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/ListLibraryItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/ListLibraryItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/ListLibraryItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/ListLibraryItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/ListLibraryItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/ListLibraryItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/ListLibraryItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/ListLibraryItems)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/ListLibraryItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/ListLibraryItems)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
