---
source_url: https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_BatchRemoveChannelRoleFromAccessors.html
---

# BatchRemoveChannelRoleFromAccessors
<a name="API_BatchRemoveChannelRoleFromAccessors"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AWS re:Post Private. After June 30, 2027, you will no longer be able to access the re:Post Private console or re:Post Private resources. For more information, see [AWS re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html).

Remove a role from multiple users or groups in a private re:Post channel.

## Request Syntax
<a name="API_BatchRemoveChannelRoleFromAccessors_RequestSyntax"></a>

```
PATCH /spaces/{{spaceId}}/channels/{{channelId}}/roles HTTP/1.1
Content-type: application/json

{
   "accessorIds": [ "{{string}}" ],
   "channelRole": "{{string}}"
}
```

## URI Request Parameters
<a name="API_BatchRemoveChannelRoleFromAccessors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelId](#API_BatchRemoveChannelRoleFromAccessors_RequestSyntax) **   <a name="repostprivate-BatchRemoveChannelRoleFromAccessors-request-uri-channelId"></a>
The unique ID of the private re:Post channel.
Length Constraints: Fixed length of 24.
Required: Yes

 ** [spaceId](#API_BatchRemoveChannelRoleFromAccessors_RequestSyntax) **   <a name="repostprivate-BatchRemoveChannelRoleFromAccessors-request-uri-spaceId"></a>
The unique ID of the private re:Post.
Required: Yes

## Request Body
<a name="API_BatchRemoveChannelRoleFromAccessors_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accessorIds](#API_BatchRemoveChannelRoleFromAccessors_RequestSyntax) **   <a name="repostprivate-BatchRemoveChannelRoleFromAccessors-request-accessorIds"></a>
The users or groups identifiers to remove the role from.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: Yes

 ** [channelRole](#API_BatchRemoveChannelRoleFromAccessors_RequestSyntax) **   <a name="repostprivate-BatchRemoveChannelRoleFromAccessors-request-channelRole"></a>
The channel role to remove from the users or groups.
Type: String
Valid Values: `ASKER | EXPERT | MODERATOR | SUPPORTREQUESTOR`
Required: Yes

## Response Syntax
<a name="API_BatchRemoveChannelRoleFromAccessors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "accessorId": "string",
         "error": number,
         "message": "string"
      }
   ],
   "removedAccessorIds": [ "string" ]
}
```

## Response Elements
<a name="API_BatchRemoveChannelRoleFromAccessors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchRemoveChannelRoleFromAccessors_ResponseSyntax) **   <a name="repostprivate-BatchRemoveChannelRoleFromAccessors-response-errors"></a>
An array of errors that occurred when roles were removed.
Type: Array of [BatchError](API_BatchError.md) objects

 ** [removedAccessorIds](#API_BatchRemoveChannelRoleFromAccessors_ResponseSyntax) **   <a name="repostprivate-BatchRemoveChannelRoleFromAccessors-response-removedAccessorIds"></a>
An array of successfully updated identifiers.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.

## Errors
<a name="API_BatchRemoveChannelRoleFromAccessors_Errors"></a>

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
<a name="API_BatchRemoveChannelRoleFromAccessors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/repostspace-2022-05-13/BatchRemoveChannelRoleFromAccessors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/repostspace-2022-05-13/BatchRemoveChannelRoleFromAccessors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/repostspace-2022-05-13/BatchRemoveChannelRoleFromAccessors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/repostspace-2022-05-13/BatchRemoveChannelRoleFromAccessors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/repostspace-2022-05-13/BatchRemoveChannelRoleFromAccessors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/repostspace-2022-05-13/BatchRemoveChannelRoleFromAccessors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/repostspace-2022-05-13/BatchRemoveChannelRoleFromAccessors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/repostspace-2022-05-13/BatchRemoveChannelRoleFromAccessors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/repostspace-2022-05-13/BatchRemoveChannelRoleFromAccessors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/repostspace-2022-05-13/BatchRemoveChannelRoleFromAccessors)
