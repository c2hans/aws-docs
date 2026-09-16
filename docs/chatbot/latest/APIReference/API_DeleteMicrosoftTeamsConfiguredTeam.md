---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteMicrosoftTeamsConfiguredTeam.html
---

# DeleteMicrosoftTeamsConfiguredTeam
<a name="API_DeleteMicrosoftTeamsConfiguredTeam"></a>

Deletes the Microsoft Teams team authorization allowing for channels to be configured in that Microsoft Teams team. Note that the Microsoft Teams team must have no channels configured to remove it.

## Request Syntax
<a name="API_DeleteMicrosoftTeamsConfiguredTeam_RequestSyntax"></a>

```
POST /delete-ms-teams-configured-teams HTTP/1.1
Content-type: application/json

{
   "TeamId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteMicrosoftTeamsConfiguredTeam_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteMicrosoftTeamsConfiguredTeam_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TeamId](#API_DeleteMicrosoftTeamsConfiguredTeam_RequestSyntax) **   <a name="qdevinchatapps-DeleteMicrosoftTeamsConfiguredTeam-request-TeamId"></a>
The ID of the Microsoft Teams team authorized with Amazon Q Developer.
To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the Amazon Q Developer in chat applications console. Then you can copy and paste the team ID from the console. For more information, see [Step 1: Configure a Microsoft Teams client](https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}`
Required: Yes

## Response Syntax
<a name="API_DeleteMicrosoftTeamsConfiguredTeam_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteMicrosoftTeamsConfiguredTeam_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteMicrosoftTeamsConfiguredTeam_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DeleteTeamsConfiguredTeamException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

 ** InvalidParameterException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

## See Also
<a name="API_DeleteMicrosoftTeamsConfiguredTeam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/DeleteMicrosoftTeamsConfiguredTeam)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/DeleteMicrosoftTeamsConfiguredTeam)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/DeleteMicrosoftTeamsConfiguredTeam)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/DeleteMicrosoftTeamsConfiguredTeam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/DeleteMicrosoftTeamsConfiguredTeam)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/DeleteMicrosoftTeamsConfiguredTeam)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/DeleteMicrosoftTeamsConfiguredTeam)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/DeleteMicrosoftTeamsConfiguredTeam)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/DeleteMicrosoftTeamsConfiguredTeam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/DeleteMicrosoftTeamsConfiguredTeam)
