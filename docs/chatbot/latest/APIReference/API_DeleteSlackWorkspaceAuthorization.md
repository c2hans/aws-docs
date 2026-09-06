---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteSlackWorkspaceAuthorization.html
---

# DeleteSlackWorkspaceAuthorization
<a name="API_DeleteSlackWorkspaceAuthorization"></a>

Deletes the Slack workspace authorization that allows channels to be configured in that workspace. This requires all configured channels in the workspace to be deleted.

## Request Syntax
<a name="API_DeleteSlackWorkspaceAuthorization_RequestSyntax"></a>

```
POST /delete-slack-workspace-authorization HTTP/1.1
Content-type: application/json

{
   "SlackTeamId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteSlackWorkspaceAuthorization_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteSlackWorkspaceAuthorization_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SlackTeamId](#API_DeleteSlackWorkspaceAuthorization_RequestSyntax) **   <a name="qdevinchatapps-DeleteSlackWorkspaceAuthorization-request-SlackTeamId"></a>
The ID of the Slack workspace authorized with Amazon Q Developer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9A-Z]{1,255}`
Required: Yes

## Response Syntax
<a name="API_DeleteSlackWorkspaceAuthorization_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteSlackWorkspaceAuthorization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteSlackWorkspaceAuthorization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DeleteSlackWorkspaceAuthorizationFault **
There was an issue deleting your Slack workspace.
HTTP Status Code: 500

 ** InvalidParameterException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

## See Also
<a name="API_DeleteSlackWorkspaceAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/DeleteSlackWorkspaceAuthorization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/DeleteSlackWorkspaceAuthorization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/DeleteSlackWorkspaceAuthorization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/DeleteSlackWorkspaceAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/DeleteSlackWorkspaceAuthorization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/DeleteSlackWorkspaceAuthorization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/DeleteSlackWorkspaceAuthorization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/DeleteSlackWorkspaceAuthorization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/DeleteSlackWorkspaceAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/DeleteSlackWorkspaceAuthorization)
