---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SendChannelMessage.html
---

# SendChannelMessage
<a name="API_messaging-chime_SendChannelMessage"></a>

Sends a message to a particular channel that the member is a part of.

**Note**
The `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call as the value in the header.
Also, `STANDARD` messages can be up to 4KB in size and contain metadata. Metadata is arbitrary, and you can use it in a variety of ways, such as containing a link to an attachment.
 `CONTROL` messages are limited to 30 bytes and do not contain metadata.

## Request Syntax
<a name="API_messaging-chime_SendChannelMessage_RequestSyntax"></a>

```
POST /channels/{{channelArn}}/messages HTTP/1.1
x-amz-chime-bearer: {{ChimeBearer}}
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "Content": "{{string}}",
   "ContentType": "{{string}}",
   "MessageAttributes": {
      "{{string}}" : {
         "StringValues": [ "{{string}}" ]
      }
   },
   "Metadata": "{{string}}",
   "Persistence": "{{string}}",
   "PushNotification": {
      "Body": "{{string}}",
      "Title": "{{string}}",
      "Type": "{{string}}"
   },
   "SubChannelId": "{{string}}",
   "Target": [
      {
         "MemberArn": "{{string}}"
      }
   ],
   "Type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_messaging-chime_SendChannelMessage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelArn](#API_messaging-chime_SendChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-request-uri-ChannelArn"></a>
The ARN of the channel.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [ChimeBearer](#API_messaging-chime_SendChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-request-ChimeBearer"></a>
The ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_messaging-chime_SendChannelMessage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_messaging-chime_SendChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-request-ClientRequestToken"></a>
The `Idempotency` token for each client request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[-_a-zA-Z0-9]*`
Required: Yes

 ** [Content](#API_messaging-chime_SendChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-request-Content"></a>
The content of the channel message.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\s\S]*`
Required: Yes

 ** [ContentType](#API_messaging-chime_SendChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-request-ContentType"></a>
The content type of the channel message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 45.
Pattern: `[\s\S]*`
Required: No

 ** [MessageAttributes](#API_messaging-chime_SendChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-request-MessageAttributes"></a>
The attributes for the message, used for message filtering along with a `FilterRule` defined in the `PushNotificationPreferences`.
Type: String to [MessageAttributeValue](API_messaging-chime_MessageAttributeValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[\s\S]*`
Required: No

 ** [Metadata](#API_messaging-chime_SendChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-request-Metadata"></a>
The optional metadata for each message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** [Persistence](#API_messaging-chime_SendChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-request-Persistence"></a>
Boolean that controls whether the message is persisted on the back end. Required.
Type: String
Valid Values: `PERSISTENT | NON_PERSISTENT`
Required: Yes

 ** [PushNotification](#API_messaging-chime_SendChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-request-PushNotification"></a>
The push notification configuration of the message.
Type: [PushNotificationConfiguration](API_messaging-chime_PushNotificationConfiguration.md) object
Required: No

 ** [SubChannelId](#API_messaging-chime_SendChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-request-SubChannelId"></a>
The ID of the SubChannel in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** [Target](#API_messaging-chime_SendChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-request-Target"></a>
The target of a message. Must be a member of the channel, such as another user, a bot, or the sender. Only the target and the sender can view targeted messages. Only users who can see targeted messages can take actions on them. However, administrators can delete targeted messages that they can’t see.
Type: Array of [Target](API_messaging-chime_Target.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [Type](#API_messaging-chime_SendChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-request-Type"></a>
The type of message, `STANDARD` or `CONTROL`.
 `STANDARD` messages can be up to 4KB in size and contain metadata. Metadata is arbitrary, and you can use it in a variety of ways, such as containing a link to an attachment.
 `CONTROL` messages are limited to 30 bytes and do not contain metadata.
Type: String
Valid Values: `STANDARD | CONTROL`
Required: Yes

## Response Syntax
<a name="API_messaging-chime_SendChannelMessage_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "ChannelArn": "string",
   "MessageId": "string",
   "Status": {
      "Detail": "string",
      "Value": "string"
   },
   "SubChannelId": "string"
}
```

## Response Elements
<a name="API_messaging-chime_SendChannelMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [ChannelArn](#API_messaging-chime_SendChannelMessage_ResponseSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-response-ChannelArn"></a>
The ARN of the channel.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [MessageId](#API_messaging-chime_SendChannelMessage_ResponseSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-response-MessageId"></a>
The ID string assigned to each message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`

 ** [Status](#API_messaging-chime_SendChannelMessage_ResponseSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-response-Status"></a>
The status of the channel message.
Type: [ChannelMessageStatusStructure](API_messaging-chime_ChannelMessageStatusStructure.md) object

 ** [SubChannelId](#API_messaging-chime_SendChannelMessage_ResponseSyntax) **   <a name="chimesdk-messaging-chime_SendChannelMessage-response-SubChannelId"></a>
The ID of the SubChannel in the response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`

## Errors
<a name="API_messaging-chime_SendChannelMessage_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

## See Also
<a name="API_messaging-chime_SendChannelMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/SendChannelMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/SendChannelMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/SendChannelMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/SendChannelMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/SendChannelMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/SendChannelMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/SendChannelMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/SendChannelMessage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/SendChannelMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/SendChannelMessage)
