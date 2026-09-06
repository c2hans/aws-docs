---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UpdateChimeWebhookConfiguration.html
---

# UpdateChimeWebhookConfiguration
<a name="API_UpdateChimeWebhookConfiguration"></a>

Updates a Amazon Chime webhook configuration.

## Request Syntax
<a name="API_UpdateChimeWebhookConfiguration_RequestSyntax"></a>

```
POST /update-chime-webhook-configuration HTTP/1.1
Content-type: application/json

{
   "ChatConfigurationArn": "{{string}}",
   "IamRoleArn": "{{string}}",
   "LoggingLevel": "{{string}}",
   "SnsTopicArns": [ "{{string}}" ],
   "WebhookDescription": "{{string}}",
   "WebhookUrl": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateChimeWebhookConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateChimeWebhookConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChatConfigurationArn](#API_UpdateChimeWebhookConfiguration_RequestSyntax) **   <a name="qdevinchatapps-UpdateChimeWebhookConfiguration-request-ChatConfigurationArn"></a>
The Amazon Resource Name (ARN) of the ChimeWebhookConfiguration to update.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 1169.
Pattern: `arn:aws:(wheatley|chatbot):[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** [IamRoleArn](#API_UpdateChimeWebhookConfiguration_RequestSyntax) **   <a name="qdevinchatapps-UpdateChimeWebhookConfiguration-request-IamRoleArn"></a>
A user-defined role that Amazon Q Developer assumes. This is not the service-linked role.
For more information, see [IAM policies for Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: No

 ** [LoggingLevel](#API_UpdateChimeWebhookConfiguration_RequestSyntax) **   <a name="qdevinchatapps-UpdateChimeWebhookConfiguration-request-LoggingLevel"></a>
Logging levels include `ERROR`, `INFO`, or `NONE`.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 5.
Pattern: `(ERROR|INFO|NONE)`
Required: No

 ** [SnsTopicArns](#API_UpdateChimeWebhookConfiguration_RequestSyntax) **   <a name="qdevinchatapps-UpdateChimeWebhookConfiguration-request-SnsTopicArns"></a>
The ARNs of the SNS topics that deliver notifications to Amazon Q Developer.
Type: Array of strings
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: No

 ** [WebhookDescription](#API_UpdateChimeWebhookConfiguration_RequestSyntax) **   <a name="qdevinchatapps-UpdateChimeWebhookConfiguration-request-WebhookDescription"></a>
A description of the webhook. We recommend using the convention `RoomName/WebhookName`.
For more information, see [Tutorial: Get started with Amazon Chime](https://docs.aws.amazon.com/chatbot/latest/adminguide/chime-setup.html) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [WebhookUrl](#API_UpdateChimeWebhookConfiguration_RequestSyntax) **   <a name="qdevinchatapps-UpdateChimeWebhookConfiguration-request-WebhookUrl"></a>
The URL for the Amazon Chime webhook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `https://hooks\.chime\.aws/incomingwebhooks/[A-Za-z0-9\-]+?\?token=[A-Za-z0-9\-]+`
Required: No

## Response Syntax
<a name="API_UpdateChimeWebhookConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateChimeWebhookConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WebhookConfiguration](#API_UpdateChimeWebhookConfiguration_ResponseSyntax) **   <a name="qdevinchatapps-UpdateChimeWebhookConfiguration-response-WebhookConfiguration"></a>
A Amazon Chime webhook configuration.
Type: [ChimeWebhookConfiguration](API_ChimeWebhookConfiguration.md) object

## Errors
<a name="API_UpdateChimeWebhookConfiguration_Errors"></a>

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

 ** UpdateChimeWebhookConfigurationException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

## See Also
<a name="API_UpdateChimeWebhookConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/UpdateChimeWebhookConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/UpdateChimeWebhookConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/UpdateChimeWebhookConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/UpdateChimeWebhookConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/UpdateChimeWebhookConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/UpdateChimeWebhookConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/UpdateChimeWebhookConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/UpdateChimeWebhookConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/UpdateChimeWebhookConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/UpdateChimeWebhookConfiguration)
