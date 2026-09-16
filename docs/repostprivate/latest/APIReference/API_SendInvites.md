---
source_url: https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_SendInvites.html
---

# SendInvites
<a name="API_SendInvites"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AWS re:Post Private. After June 30, 2027, you will no longer be able to access the re:Post Private console or re:Post Private resources. For more information, see [AWS re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html).

Sends an invitation email to selected users and groups.

## Request Syntax
<a name="API_SendInvites_RequestSyntax"></a>

```
POST /spaces/{{spaceId}}/invite HTTP/1.1
Content-type: application/json

{
   "accessorIds": [ "{{string}}" ],
   "body": "{{string}}",
   "title": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendInvites_RequestParameters"></a>

The request uses the following URI parameters.

 ** [spaceId](#API_SendInvites_RequestSyntax) **   <a name="repostprivate-SendInvites-request-uri-spaceId"></a>
The ID of the private re:Post.
Required: Yes

## Request Body
<a name="API_SendInvites_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accessorIds](#API_SendInvites_RequestSyntax) **   <a name="repostprivate-SendInvites-request-accessorIds"></a>
The array of identifiers for the users and groups.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: Yes

 ** [body](#API_SendInvites_RequestSyntax) **   <a name="repostprivate-SendInvites-request-body"></a>
The body of the invite.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 600.
Required: Yes

 ** [title](#API_SendInvites_RequestSyntax) **   <a name="repostprivate-SendInvites-request-title"></a>
The title of the invite.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

## Response Syntax
<a name="API_SendInvites_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_SendInvites_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SendInvites_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** quotaCode **
The code to identify the quota.
 ** retryAfterSeconds **
 Advice to clients on when the call can be safely retried.
 ** serviceCode **
The code to identify the service.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The field that caused the error, if applicable.
 ** reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_SendInvites_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/repostspace-2022-05-13/SendInvites)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/repostspace-2022-05-13/SendInvites)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/repostspace-2022-05-13/SendInvites)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/repostspace-2022-05-13/SendInvites)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/repostspace-2022-05-13/SendInvites)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/repostspace-2022-05-13/SendInvites)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/repostspace-2022-05-13/SendInvites)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/repostspace-2022-05-13/SendInvites)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/repostspace-2022-05-13/SendInvites)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/repostspace-2022-05-13/SendInvites)
