---
source_url: https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_GetChannel.html
---

# GetChannel
<a name="API_GetChannel"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AWS re:Post Private. After June 30, 2027, you will no longer be able to access the re:Post Private console or re:Post Private resources. For more information, see [AWS re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html).

Displays information about a channel in a private re:Post.

## Request Syntax
<a name="API_GetChannel_RequestSyntax"></a>

```
GET /spaces/{{spaceId}}/channels/{{channelId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetChannel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelId](#API_GetChannel_RequestSyntax) **   <a name="repostprivate-GetChannel-request-uri-channelId"></a>
The unique ID of the private re:Post channel.
Length Constraints: Fixed length of 24.
Required: Yes

 ** [spaceId](#API_GetChannel_RequestSyntax) **   <a name="repostprivate-GetChannel-request-uri-spaceId"></a>
The unique ID of the private re:Post.
Required: Yes

## Request Body
<a name="API_GetChannel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetChannel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "channelDescription": "string",
   "channelId": "string",
   "channelName": "string",
   "channelRoles": {
      "string" : [ "string" ]
   },
   "channelStatus": "string",
   "createDateTime": "string",
   "deleteDateTime": "string",
   "spaceId": "string"
}
```

## Response Elements
<a name="API_GetChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [channelDescription](#API_GetChannel_ResponseSyntax) **   <a name="repostprivate-GetChannel-response-channelDescription"></a>
A description for the channel. This is used only to help you identify this channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [channelId](#API_GetChannel_ResponseSyntax) **   <a name="repostprivate-GetChannel-response-channelId"></a>
The unique ID of the private re:Post channel.
Type: String
Length Constraints: Fixed length of 24.

 ** [channelName](#API_GetChannel_ResponseSyntax) **   <a name="repostprivate-GetChannel-response-channelName"></a>
The name for the channel. This must be unique per private re:Post.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [channelRoles](#API_GetChannel_ResponseSyntax) **   <a name="repostprivate-GetChannel-response-channelRoles"></a>
The channel roles associated to the users and groups of the channel.
Type: String to array of strings map
Valid Values: `ASKER | EXPERT | MODERATOR | SUPPORTREQUESTOR`

 ** [channelStatus](#API_GetChannel_ResponseSyntax) **   <a name="repostprivate-GetChannel-response-channelStatus"></a>
The status pf the channel.
Type: String
Valid Values: `CREATED | CREATING | CREATE_FAILED | DELETED | DELETING | DELETE_FAILED`

 ** [createDateTime](#API_GetChannel_ResponseSyntax) **   <a name="repostprivate-GetChannel-response-createDateTime"></a>
The date when the channel was created.
Type: Timestamp

 ** [deleteDateTime](#API_GetChannel_ResponseSyntax) **   <a name="repostprivate-GetChannel-response-deleteDateTime"></a>
The date when the channel was deleted.
Type: Timestamp

 ** [spaceId](#API_GetChannel_ResponseSyntax) **   <a name="repostprivate-GetChannel-response-spaceId"></a>
The unique ID of the private re:Post.
Type: String

## Errors
<a name="API_GetChannel_Errors"></a>

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
<a name="API_GetChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/repostspace-2022-05-13/GetChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/repostspace-2022-05-13/GetChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/repostspace-2022-05-13/GetChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/repostspace-2022-05-13/GetChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/repostspace-2022-05-13/GetChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/repostspace-2022-05-13/GetChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/repostspace-2022-05-13/GetChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/repostspace-2022-05-13/GetChannel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/repostspace-2022-05-13/GetChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/repostspace-2022-05-13/GetChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS re:Post Private. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query repostprivate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
