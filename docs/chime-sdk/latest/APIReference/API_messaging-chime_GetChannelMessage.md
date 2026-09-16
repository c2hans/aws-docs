---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetChannelMessage.html
---

# GetChannelMessage
<a name="API_messaging-chime_GetChannelMessage"></a>

Gets the full details of a channel message.

**Note**
The `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call as the value in the header.

## Request Syntax
<a name="API_messaging-chime_GetChannelMessage_RequestSyntax"></a>

```
GET /channels/{{channelArn}}/messages/{{messageId}}?sub-channel-id={{SubChannelId}} HTTP/1.1
x-amz-chime-bearer: {{ChimeBearer}}
```

## URI Request Parameters
<a name="API_messaging-chime_GetChannelMessage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelArn](#API_messaging-chime_GetChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_GetChannelMessage-request-uri-ChannelArn"></a>
The ARN of the channel.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [ChimeBearer](#API_messaging-chime_GetChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_GetChannelMessage-request-ChimeBearer"></a>
The ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [messageId](#API_messaging-chime_GetChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_GetChannelMessage-request-uri-MessageId"></a>
The ID of the message.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`
Required: Yes

 ** [SubChannelId](#API_messaging-chime_GetChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_GetChannelMessage-request-uri-SubChannelId"></a>
The ID of the SubChannel in the request.
Only required when getting messages in a SubChannel that the user belongs to.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`

## Request Body
<a name="API_messaging-chime_GetChannelMessage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_messaging-chime_GetChannelMessage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChannelMessage": {
      "ChannelArn": "string",
      "Content": "string",
      "ContentType": "string",
      "CreatedTimestamp": number,
      "LastEditedTimestamp": number,
      "LastUpdatedTimestamp": number,
      "MessageAttributes": {
         "string" : {
            "StringValues": [ "string" ]
         }
      },
      "MessageId": "string",
      "Metadata": "string",
      "Persistence": "string",
      "Redacted": boolean,
      "Sender": {
         "Arn": "string",
         "Name": "string"
      },
      "Status": {
         "Detail": "string",
         "Value": "string"
      },
      "SubChannelId": "string",
      "Target": [
         {
            "MemberArn": "string"
         }
      ],
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_messaging-chime_GetChannelMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChannelMessage](#API_messaging-chime_GetChannelMessage_ResponseSyntax) **   <a name="chimesdk-messaging-chime_GetChannelMessage-response-ChannelMessage"></a>
The details of and content in the message.
Type: [ChannelMessage](API_messaging-chime_ChannelMessage.md) object

## Errors
<a name="API_messaging-chime_GetChannelMessage_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

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
<a name="API_messaging-chime_GetChannelMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/GetChannelMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/GetChannelMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/GetChannelMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/GetChannelMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/GetChannelMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/GetChannelMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/GetChannelMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/GetChannelMessage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/GetChannelMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/GetChannelMessage)
