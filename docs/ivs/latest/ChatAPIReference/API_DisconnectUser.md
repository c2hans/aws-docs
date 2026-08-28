---
source_url: https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_DisconnectUser.html
---

# DisconnectUser
<a name="API_DisconnectUser"></a>

Disconnects all connections using a specified user ID from a room. This replicates the [ DisconnectUser](https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-disconnectuser-publish.html) WebSocket operation in the Amazon IVS Chat Messaging API.

## Request Syntax
<a name="API_DisconnectUser_RequestSyntax"></a>

```
POST /DisconnectUser HTTP/1.1
Content-type: application/json

{
   "reason": "{{string}}",
   "roomIdentifier": "{{string}}",
   "userId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DisconnectUser_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DisconnectUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [reason](#API_DisconnectUser_RequestSyntax) **   <a name="ivs-DisconnectUser-request-reason"></a>
Reason for disconnecting the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [roomIdentifier](#API_DisconnectUser_RequestSyntax) **   <a name="ivs-DisconnectUser-request-roomIdentifier"></a>
Identifier of the room from which the user's clients should be disconnected. Currently this must be an ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivschat:[a-z0-9-]+:[0-9]+:room/[a-zA-Z0-9-]+`
Required: Yes

 ** [userId](#API_DisconnectUser_RequestSyntax) **   <a name="ivs-DisconnectUser-request-userId"></a>
ID of the user (connection) to disconnect from the room.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Response Syntax
<a name="API_DisconnectUser_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisconnectUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisconnectUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

HTTP Status Code: 403

 ** PendingVerification **

HTTP Status Code: 403

 ** ResourceNotFoundException **

HTTP Status Code: 404

 ** ThrottlingException **

HTTP Status Code: 429

 ** ValidationException **

HTTP Status Code: 400

## See Also
<a name="API_DisconnectUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivschat-2020-07-14/DisconnectUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivschat-2020-07-14/DisconnectUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivschat-2020-07-14/DisconnectUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivschat-2020-07-14/DisconnectUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivschat-2020-07-14/DisconnectUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivschat-2020-07-14/DisconnectUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivschat-2020-07-14/DisconnectUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivschat-2020-07-14/DisconnectUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivschat-2020-07-14/DisconnectUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivschat-2020-07-14/DisconnectUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
