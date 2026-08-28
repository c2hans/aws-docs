---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CreateMicrosoftTeamsChannelConfiguration.html
---

# CreateMicrosoftTeamsChannelConfiguration
<a name="API_CreateMicrosoftTeamsChannelConfiguration"></a>

Creates an Amazon Q Developer configuration for Microsoft Teams.

## Request Syntax
<a name="API_CreateMicrosoftTeamsChannelConfiguration_RequestSyntax"></a>

```
POST /create-ms-teams-channel-configuration HTTP/1.1
Content-type: application/json

{
   "ChannelId": "{{string}}",
   "ChannelName": "{{string}}",
   "ConfigurationName": "{{string}}",
   "GuardrailPolicyArns": [ "{{string}}" ],
   "IamRoleArn": "{{string}}",
   "LoggingLevel": "{{string}}",
   "SnsTopicArns": [ "{{string}}" ],
   "Tags": [
      {
         "TagKey": "{{string}}",
         "TagValue": "{{string}}"
      }
   ],
   "TeamId": "{{string}}",
   "TeamName": "{{string}}",
   "TenantId": "{{string}}",
   "UserAuthorizationRequired": {{boolean}}
}
```

## URI Request Parameters
<a name="API_CreateMicrosoftTeamsChannelConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMicrosoftTeamsChannelConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChannelId](#API_CreateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateMicrosoftTeamsChannelConfiguration-request-ChannelId"></a>
The ID of the Microsoft Teams channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9-_=+\/.,])*%3[aA]([a-zA-Z0-9-_=+\/.,])*%40([a-zA-Z0-9-_=+\/.,])*`
Required: Yes

 ** [ChannelName](#API_CreateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateMicrosoftTeamsChannelConfiguration-request-ChannelName"></a>
The name of the Microsoft Teams channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(.*)`
Required: No

 ** [ConfigurationName](#API_CreateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateMicrosoftTeamsChannelConfiguration-request-ConfigurationName"></a>
The name of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

 ** [GuardrailPolicyArns](#API_CreateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateMicrosoftTeamsChannelConfiguration-request-GuardrailPolicyArns"></a>
The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed `AdministratorAccess` policy is applied by default if this is not set.
Type: Array of strings
Length Constraints: Minimum length of 11. Maximum length of 1163.
Pattern: `(^$|(?!.*\/aws-service-role\/.*)arn:aws:iam:[A-Za-z0-9_\/.-]{0,63}:[A-Za-z0-9_\/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_\/+=,@.-]{0,1023})`
Required: No

 ** [IamRoleArn](#API_CreateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateMicrosoftTeamsChannelConfiguration-request-IamRoleArn"></a>
A user-defined role that Amazon Q Developer assumes. This is not the service-linked role.
For more information, see [IAM policies for Amazon Q Developer](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** [LoggingLevel](#API_CreateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateMicrosoftTeamsChannelConfiguration-request-LoggingLevel"></a>
Logging levels include `ERROR`, `INFO`, or `NONE`.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 5.
Pattern: `(ERROR|INFO|NONE)`
Required: No

 ** [SnsTopicArns](#API_CreateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateMicrosoftTeamsChannelConfiguration-request-SnsTopicArns"></a>
The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to Amazon Q Developer.
Type: Array of strings
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: No

 ** [Tags](#API_CreateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateMicrosoftTeamsChannelConfiguration-request-Tags"></a>
A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [TeamId](#API_CreateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateMicrosoftTeamsChannelConfiguration-request-TeamId"></a>
 The ID of the Microsoft Teams authorized with Amazon Q Developer.
To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the Amazon Q Developer console. Then you can copy and paste the team ID from the console. For more information, see [Step 1: Configure a Microsoft Teams client](https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}`
Required: Yes

 ** [TeamName](#API_CreateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateMicrosoftTeamsChannelConfiguration-request-TeamName"></a>
The name of the Microsoft Teams Team.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(.*)`
Required: No

 ** [TenantId](#API_CreateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateMicrosoftTeamsChannelConfiguration-request-TenantId"></a>
The ID of the Microsoft Teams tenant.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}`
Required: Yes

 ** [UserAuthorizationRequired](#API_CreateMicrosoftTeamsChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateMicrosoftTeamsChannelConfiguration-request-UserAuthorizationRequired"></a>
Enables use of a user role requirement in your chat configuration.
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreateMicrosoftTeamsChannelConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateMicrosoftTeamsChannelConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [ChannelConfiguration](#API_CreateMicrosoftTeamsChannelConfiguration_ResponseSyntax) **   <a name="qdevinchatapps-CreateMicrosoftTeamsChannelConfiguration-response-ChannelConfiguration"></a>
The configuration for a Microsoft Teams channel configured with Amazon Q Developer.
Type: [TeamsChannelConfiguration](API_TeamsChannelConfiguration.md) object

## Errors
<a name="API_CreateMicrosoftTeamsChannelConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was an issue processing your request.
HTTP Status Code: 409

 ** CreateTeamsChannelConfigurationException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

 ** InvalidParameterException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** InvalidRequestException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** LimitExceededException **
You have exceeded a service limit for Amazon Q Developer.
HTTP Status Code: 403

## See Also
<a name="API_CreateMicrosoftTeamsChannelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/CreateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/CreateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/CreateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/CreateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/CreateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/CreateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/CreateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/CreateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/CreateMicrosoftTeamsChannelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/CreateMicrosoftTeamsChannelConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
