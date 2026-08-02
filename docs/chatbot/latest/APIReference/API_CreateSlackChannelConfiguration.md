---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CreateSlackChannelConfiguration.html
---

# CreateSlackChannelConfiguration
<a name="API_CreateSlackChannelConfiguration"></a>

Creates an Amazon Q Developer configuration for Slack.

## Request Syntax
<a name="API_CreateSlackChannelConfiguration_RequestSyntax"></a>

```
POST /create-slack-channel-configuration HTTP/1.1
Content-type: application/json

{
   "ConfigurationName": "{{string}}",
   "GuardrailPolicyArns": [ "{{string}}" ],
   "IamRoleArn": "{{string}}",
   "LoggingLevel": "{{string}}",
   "SlackChannelId": "{{string}}",
   "SlackChannelName": "{{string}}",
   "SlackTeamId": "{{string}}",
   "SnsTopicArns": [ "{{string}}" ],
   "Tags": [
      {
         "TagKey": "{{string}}",
         "TagValue": "{{string}}"
      }
   ],
   "UserAuthorizationRequired": {{boolean}}
}
```

## URI Request Parameters
<a name="API_CreateSlackChannelConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSlackChannelConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConfigurationName](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateSlackChannelConfiguration-request-ConfigurationName"></a>
The name of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

 ** [GuardrailPolicyArns](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateSlackChannelConfiguration-request-GuardrailPolicyArns"></a>
The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed `AdministratorAccess` policy is applied by default if this is not set.
Type: Array of strings
Length Constraints: Minimum length of 11. Maximum length of 1163.
Pattern: `(^$|(?!.*\/aws-service-role\/.*)arn:aws:iam:[A-Za-z0-9_\/.-]{0,63}:[A-Za-z0-9_\/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_\/+=,@.-]{0,1023})`
Required: No

 ** [IamRoleArn](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateSlackChannelConfiguration-request-IamRoleArn"></a>
A user-defined role that Amazon Q Developer assumes. This is not the service-linked role.
For more information, see [IAM policies for Amazon Q Developer](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** [LoggingLevel](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateSlackChannelConfiguration-request-LoggingLevel"></a>
Logging levels include `ERROR`, `INFO`, or `NONE`.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 5.
Pattern: `(ERROR|INFO|NONE)`
Required: No

 ** [SlackChannelId](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateSlackChannelConfiguration-request-SlackChannelId"></a>
The ID of the Slack channel.
To get this ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ABCBBLZZZ.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9]+`
Required: Yes

 ** [SlackChannelName](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateSlackChannelConfiguration-request-SlackChannelName"></a>
The name of the Slack channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [SlackTeamId](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateSlackChannelConfiguration-request-SlackTeamId"></a>
The ID of the Slack workspace authorized with Amazon Q Developer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9A-Z]{1,255}`
Required: Yes

 ** [SnsTopicArns](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateSlackChannelConfiguration-request-SnsTopicArns"></a>
The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to Amazon Q Developer.
Type: Array of strings
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: No

 ** [Tags](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateSlackChannelConfiguration-request-Tags"></a>
A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [UserAuthorizationRequired](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateSlackChannelConfiguration-request-UserAuthorizationRequired"></a>
Enables use of a user role requirement in your chat configuration.
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreateSlackChannelConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "ChannelConfiguration": {
      "ChatConfigurationArn": "string",
      "ConfigurationName": "string",
      "GuardrailPolicyArns": [ "string" ],
      "IamRoleArn": "string",
      "LoggingLevel": "string",
      "SlackChannelId": "string",
      "SlackChannelName": "string",
      "SlackTeamId": "string",
      "SlackTeamName": "string",
      "SnsTopicArns": [ "string" ],
      "State": "string",
      "StateReason": "string",
      "Tags": [
         {
            "TagKey": "string",
            "TagValue": "string"
         }
      ],
      "UserAuthorizationRequired": boolean
   }
}
```

## Response Elements
<a name="API_CreateSlackChannelConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [ChannelConfiguration](#API_CreateSlackChannelConfiguration_ResponseSyntax) **   <a name="qdevinchatapps-CreateSlackChannelConfiguration-response-ChannelConfiguration"></a>
The configuration for a Slack channel configured with Amazon Q Developer.
Type: [SlackChannelConfiguration](API_SlackChannelConfiguration.md) object

## Errors
<a name="API_CreateSlackChannelConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was an issue processing your request.
HTTP Status Code: 409

 ** CreateSlackChannelConfigurationException **
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
<a name="API_CreateSlackChannelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/CreateSlackChannelConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/CreateSlackChannelConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/CreateSlackChannelConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/CreateSlackChannelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/CreateSlackChannelConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/CreateSlackChannelConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/CreateSlackChannelConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/CreateSlackChannelConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/CreateSlackChannelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/CreateSlackChannelConfiguration)
