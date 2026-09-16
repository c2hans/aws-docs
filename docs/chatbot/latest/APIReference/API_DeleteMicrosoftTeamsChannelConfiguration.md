---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteMicrosoftTeamsChannelConfiguration.html
---

# DeleteMicrosoftTeamsChannelConfiguration
<a name="API_DeleteMicrosoftTeamsChannelConfiguration"></a>

Deletes a Microsoft Teams channel configuration for Amazon Q Developer.

## Request Syntax
<a name="API_DeleteMicrosoftTeamsChannelConfiguration_RequestSyntax"></a>

```
POST /delete-ms-teams-channel-configuration HTTP/1.1
Content-type: application/json

{
   "ChatConfigurationArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteMicrosoftTeamsChannelConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteMicrosoftTeamsChannelConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChatConfigurationArn](#API_DeleteMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-DeleteMicrosoftTeamsChannelConfiguration-request-ChatConfigurationArn"></a>
The Amazon Resource Name (ARN) of the MicrosoftTeamsChannelConfiguration associated with the user identity to delete.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 1169.
Pattern: `arn:aws:(wheatley|chatbot):[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

## Response Syntax
<a name="API_DeleteMicrosoftTeamsChannelConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteMicrosoftTeamsChannelConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteMicrosoftTeamsChannelConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DeleteTeamsChannelConfigurationException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

 ** InvalidParameterException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** InvalidRequestException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** ResourceNotFoundException **
We were unable to find the resource for your request
HTTP Status Code: 404

## See Also
<a name="API_DeleteMicrosoftTeamsChannelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/DeleteMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/DeleteMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/DeleteMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/DeleteMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/DeleteMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/DeleteMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/DeleteMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/DeleteMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/DeleteMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/DeleteMicrosoftTeamsChannelConfiguration)
