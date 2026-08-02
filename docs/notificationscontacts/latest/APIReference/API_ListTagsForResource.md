---
source_url: https://docs.aws.amazon.com/notificationscontacts/latest/APIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Lists all of the tags associated with the Amazon Resource Name (ARN) that you specify. The resource can be a user, server, or role.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
GET /tags/{{arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_ListTagsForResource_RequestSyntax) **   <a name="notificationscontacts-ListTagsForResource-request-uri-arn"></a>
The ARN you specified to list the tags of.
Pattern: `arn:[a-z-]{3,10}:notifications-contacts::[0-9]{12}:emailcontact/[a-z0-9]{27}`
Required: Yes

## Request Body
<a name="API_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="notificationscontacts-ListTagsForResource-response-tags"></a>
Key-value pairs that are assigned to a resource, usually for the purpose of grouping and searching for items. Tags are metadata that you define.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Your request references a resource which does not exist.
 ** resourceId **
The ID of the resource that wasn't found.
 ** resourceType **
The type of resource that wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service being throttled.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The list of input fields that are invalid.
 ** reason **
The reason why your input is considered invalid.
HTTP Status Code: 400

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notificationscontacts-2018-05-10/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notificationscontacts-2018-05-10/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notificationscontacts-2018-05-10/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notificationscontacts-2018-05-10/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notificationscontacts-2018-05-10/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notificationscontacts-2018-05-10/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notificationscontacts-2018-05-10/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notificationscontacts-2018-05-10/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notificationscontacts-2018-05-10/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notificationscontacts-2018-05-10/ListTagsForResource)
