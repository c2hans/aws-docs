---
source_url: https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_UpdateChannel.html
---

# UpdateChannel
<a name="API_UpdateChannel"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AWS re:Post Private. After June 30, 2027, you will no longer be able to access the re:Post Private console or re:Post Private resources. For more information, see [AWS re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html).

Modifies an existing channel.

## Request Syntax
<a name="API_UpdateChannel_RequestSyntax"></a>

```
PUT /spaces/{{spaceId}}/channels/{{channelId}} HTTP/1.1
Content-type: application/json

{
   "channelDescription": "{{string}}",
   "channelName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateChannel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelId](#API_UpdateChannel_RequestSyntax) **   <a name="repostprivate-UpdateChannel-request-uri-channelId"></a>
The unique ID of the private re:Post channel.
Length Constraints: Fixed length of 24.
Required: Yes

 ** [spaceId](#API_UpdateChannel_RequestSyntax) **   <a name="repostprivate-UpdateChannel-request-uri-spaceId"></a>
The unique ID of the private re:Post.
Required: Yes

## Request Body
<a name="API_UpdateChannel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelDescription](#API_UpdateChannel_RequestSyntax) **   <a name="repostprivate-UpdateChannel-request-channelDescription"></a>
A description for the channel. This is used only to help you identify this channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [channelName](#API_UpdateChannel_RequestSyntax) **   <a name="repostprivate-UpdateChannel-request-channelName"></a>
The name for the channel. This must be unique per private re:Post.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_UpdateChannel_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 409

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
<a name="API_UpdateChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/repostspace-2022-05-13/UpdateChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/repostspace-2022-05-13/UpdateChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/repostspace-2022-05-13/UpdateChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/repostspace-2022-05-13/UpdateChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/repostspace-2022-05-13/UpdateChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/repostspace-2022-05-13/UpdateChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/repostspace-2022-05-13/UpdateChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/repostspace-2022-05-13/UpdateChannel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/repostspace-2022-05-13/UpdateChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/repostspace-2022-05-13/UpdateChannel)
