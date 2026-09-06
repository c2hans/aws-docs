---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CreateChimeWebhookConfiguration.html
---

# CreateChimeWebhookConfiguration
<a name="API_CreateChimeWebhookConfiguration"></a>

Creates an Amazon Q Developer configuration for Amazon Chime.

## Request Syntax
<a name="API_CreateChimeWebhookConfiguration_RequestSyntax"></a>

```
POST /create-chime-webhook-configuration HTTP/1.1
Content-type: application/json

{
   "ConfigurationName": "{{string}}",
   "IamRoleArn": "{{string}}",
   "LoggingLevel": "{{string}}",
   "SnsTopicArns": [ "{{string}}" ],
   "Tags": [
      {
         "TagKey": "{{string}}",
         "TagValue": "{{string}}"
      }
   ],
   "WebhookDescription": "{{string}}",
   "WebhookUrl": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateChimeWebhookConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateChimeWebhookConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConfigurationName](#API_CreateChimeWebhookConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateChimeWebhookConfiguration-request-ConfigurationName"></a>
The name of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

 ** [IamRoleArn](#API_CreateChimeWebhookConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateChimeWebhookConfiguration-request-IamRoleArn"></a>
A user-defined role that Amazon Q Developer assumes. This is not the service-linked role.
For more information, see [IAM policies for Amazon Q Developer](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** [LoggingLevel](#API_CreateChimeWebhookConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateChimeWebhookConfiguration-request-LoggingLevel"></a>
Logging levels include `ERROR`, `INFO`, or `NONE`.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 5.
Pattern: `(ERROR|INFO|NONE)`
Required: No

 ** [SnsTopicArns](#API_CreateChimeWebhookConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateChimeWebhookConfiguration-request-SnsTopicArns"></a>
The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to Amazon Q Developer.
Type: Array of strings
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** [Tags](#API_CreateChimeWebhookConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateChimeWebhookConfiguration-request-Tags"></a>
A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [WebhookDescription](#API_CreateChimeWebhookConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateChimeWebhookConfiguration-request-WebhookDescription"></a>
A description of the webhook. We recommend using the convention `RoomName/WebhookName`.
For more information, see [Tutorial: Get started with Amazon Chime](https://docs.aws.amazon.com/chatbot/latest/adminguide/chime-setup.html) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [WebhookUrl](#API_CreateChimeWebhookConfiguration_RequestSyntax) **   <a name="qdevinchatapps-CreateChimeWebhookConfiguration-request-WebhookUrl"></a>
The URL for the Amazon Chime webhook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `https://hooks\.chime\.aws/incomingwebhooks/[A-Za-z0-9\-]+?\?token=[A-Za-z0-9\-]+`
Required: Yes

## Response Syntax
<a name="API_CreateChimeWebhookConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "WebhookConfiguration": {
      "ChatConfigurationArn": "string",
      "ConfigurationName": "string",
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
      "WebhookDescription": "string"
   }
}
```

## Response Elements
<a name="API_CreateChimeWebhookConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [WebhookConfiguration](#API_CreateChimeWebhookConfiguration_ResponseSyntax) **   <a name="qdevinchatapps-CreateChimeWebhookConfiguration-response-WebhookConfiguration"></a>
An Amazon Chime webhook configuration.
Type: [ChimeWebhookConfiguration](API_ChimeWebhookConfiguration.md) object

## Errors
<a name="API_CreateChimeWebhookConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was an issue processing your request.
HTTP Status Code: 409

 ** CreateChimeWebhookConfigurationException **
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
<a name="API_CreateChimeWebhookConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/CreateChimeWebhookConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/CreateChimeWebhookConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/CreateChimeWebhookConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/CreateChimeWebhookConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/CreateChimeWebhookConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/CreateChimeWebhookConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/CreateChimeWebhookConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/CreateChimeWebhookConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/CreateChimeWebhookConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/CreateChimeWebhookConfiguration)
