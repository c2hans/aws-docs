---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UpdateMicrosoftTeamsChannelConfiguration.html
---

# UpdateMicrosoftTeamsChannelConfiguration
<a name="API_UpdateMicrosoftTeamsChannelConfiguration"></a>

Updates an Microsoft Teams channel configuration.

## Request Syntax
<a name="API_UpdateMicrosoftTeamsChannelConfiguration_RequestSyntax"></a>

```
POST /update-ms-teams-channel-configuration HTTP/1.1
Content-type: application/json

{
   "ChannelId": "{{string}}",
   "ChannelName": "{{string}}",
   "ChatConfigurationArn": "{{string}}",
   "GuardrailPolicyArns": [ "{{string}}" ],
   "IamRoleArn": "{{string}}",
   "LoggingLevel": "{{string}}",
   "SnsTopicArns": [ "{{string}}" ],
   "UserAuthorizationRequired": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateMicrosoftTeamsChannelConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateMicrosoftTeamsChannelConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChannelId](#API_UpdateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-UpdateMicrosoftTeamsChannelConfiguration-request-ChannelId"></a>
The ID of the Microsoft Teams channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9-_=+\/.,])*%3[aA]([a-zA-Z0-9-_=+\/.,])*%40([a-zA-Z0-9-_=+\/.,])*`
Required: Yes

 ** [ChannelName](#API_UpdateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-UpdateMicrosoftTeamsChannelConfiguration-request-ChannelName"></a>
The name of the Microsoft Teams channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(.*)`
Required: No

 ** [ChatConfigurationArn](#API_UpdateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-UpdateMicrosoftTeamsChannelConfiguration-request-ChatConfigurationArn"></a>
The Amazon Resource Name (ARN) of the TeamsChannelConfiguration to update.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 1169.
Pattern: `arn:aws:(wheatley|chatbot):[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** [GuardrailPolicyArns](#API_UpdateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-UpdateMicrosoftTeamsChannelConfiguration-request-GuardrailPolicyArns"></a>
The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed `AdministratorAccess` policy is applied by default if this is not set.
Type: Array of strings
Length Constraints: Minimum length of 11. Maximum length of 1163.
Pattern: `(^$|(?!.*\/aws-service-role\/.*)arn:aws:iam:[A-Za-z0-9_\/.-]{0,63}:[A-Za-z0-9_\/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_\/+=,@.-]{0,1023})`
Required: No

 ** [IamRoleArn](#API_UpdateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-UpdateMicrosoftTeamsChannelConfiguration-request-IamRoleArn"></a>
A user-defined role that Amazon Q Developer assumes. This is not the service-linked role.
For more information, see [IAM policies for Amazon Q Developer](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: No

 ** [LoggingLevel](#API_UpdateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-UpdateMicrosoftTeamsChannelConfiguration-request-LoggingLevel"></a>
Logging levels include `ERROR`, `INFO`, or `NONE`.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 5.
Pattern: `(ERROR|INFO|NONE)`
Required: No

 ** [SnsTopicArns](#API_UpdateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-UpdateMicrosoftTeamsChannelConfiguration-request-SnsTopicArns"></a>
The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to Amazon Q Developer.
Type: Array of strings
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: No

 ** [UserAuthorizationRequired](#API_UpdateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-UpdateMicrosoftTeamsChannelConfiguration-request-UserAuthorizationRequired"></a>
Enables use of a user role requirement in your chat configuration.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateMicrosoftTeamsChannelConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChannelConfiguration": {
      "ChannelId": "string",
      "ChannelName": "string",
      "ChatConfigurationArn": "string",
      "ConfigurationName": "string",
      "GuardrailPolicyArns": [ "string" ],
      "IamRoleArn": "string",
      "LoggingLevel": "string",
      "SnsTopicArns": [ "string" ],
      "State": "string",
      "StateReason": "string",
      "Tags": [
         {
            "TagKey": "string",
            "TagValue": "string"
         }
      ],
      "TeamId": "string",
      "TeamName": "string",
      "TenantId": "string",
      "UserAuthorizationRequired": boolean
   }
}
```

## Response Elements
<a name="API_UpdateMicrosoftTeamsChannelConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChannelConfiguration](#API_UpdateMicrosoftTeamsChannelConfiguration_ResponseSyntax) **   <a name="qdevinchatapps-UpdateMicrosoftTeamsChannelConfiguration-response-ChannelConfiguration"></a>
The configuration for a Microsoft Teams channel configured with Amazon Q Developer.
Type: [TeamsChannelConfiguration](API_TeamsChannelConfiguration.md) object

## Errors
<a name="API_UpdateMicrosoftTeamsChannelConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** InvalidRequestException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** ResourceNotFoundException **
We were unable to find the resource for your request
HTTP Status Code: 404

 ** UpdateTeamsChannelConfigurationException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

## See Also
<a name="API_UpdateMicrosoftTeamsChannelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/UpdateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/UpdateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/UpdateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/UpdateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/UpdateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/UpdateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/UpdateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/UpdateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/UpdateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/UpdateMicrosoftTeamsChannelConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
