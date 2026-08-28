---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteMicrosoftTeamsUserIdentity.html
---

# DeleteMicrosoftTeamsUserIdentity
<a name="API_DeleteMicrosoftTeamsUserIdentity"></a>

Identifes a user level permission for a channel configuration.

## Request Syntax
<a name="API_DeleteMicrosoftTeamsUserIdentity_RequestSyntax"></a>

```
POST /delete-ms-teams-user-identity HTTP/1.1
Content-type: application/json

{
   "ChatConfigurationArn": "{{string}}",
   "UserId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteMicrosoftTeamsUserIdentity_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteMicrosoftTeamsUserIdentity_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChatConfigurationArn](#API_DeleteMicrosoftTeamsUserIdentity_RequestSyntax) **   <a name="qdevinchatapps-DeleteMicrosoftTeamsUserIdentity-request-ChatConfigurationArn"></a>
The ARN of the MicrosoftTeamsChannelConfiguration associated with the user identity to delete.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 1169.
Pattern: `arn:aws:(wheatley|chatbot):[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** [UserId](#API_DeleteMicrosoftTeamsUserIdentity_RequestSyntax) **   <a name="qdevinchatapps-DeleteMicrosoftTeamsUserIdentity-request-UserId"></a>
The Microsoft Teams user ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}`
Required: Yes

## Response Syntax
<a name="API_DeleteMicrosoftTeamsUserIdentity_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteMicrosoftTeamsUserIdentity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteMicrosoftTeamsUserIdentity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DeleteMicrosoftTeamsUserIdentityException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

 ** InvalidParameterException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** ResourceNotFoundException **
We were unable to find the resource for your request
HTTP Status Code: 404

## See Also
<a name="API_DeleteMicrosoftTeamsUserIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/DeleteMicrosoftTeamsUserIdentity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/DeleteMicrosoftTeamsUserIdentity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/DeleteMicrosoftTeamsUserIdentity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/DeleteMicrosoftTeamsUserIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/DeleteMicrosoftTeamsUserIdentity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/DeleteMicrosoftTeamsUserIdentity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/DeleteMicrosoftTeamsUserIdentity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/DeleteMicrosoftTeamsUserIdentity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/DeleteMicrosoftTeamsUserIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/DeleteMicrosoftTeamsUserIdentity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
