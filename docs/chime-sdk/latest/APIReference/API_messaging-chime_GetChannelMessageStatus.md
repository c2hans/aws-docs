---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetChannelMessageStatus.html
---

# GetChannelMessageStatus
<a name="API_messaging-chime_GetChannelMessageStatus"></a>

Gets message status for a specified `messageId`. Use this API to determine the intermediate status of messages going through channel flow processing. The API provides an alternative to retrieving message status if the event was not received because a client wasn't connected to a websocket.

Messages can have any one of these statuses.

SENT
Message processed successfully

PENDING
Ongoing processing

FAILED
Processing failed

DENIED
Message denied by the processor

**Note**
This API does not return statuses for denied messages, because we don't store them once the processor denies them.
Only the message sender can invoke this API.
The `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call as the value in the header.

## Request Syntax
<a name="API_messaging-chime_GetChannelMessageStatus_RequestSyntax"></a>

```
GET /channels/{{channelArn}}/messages/{messageId}?scope=message-status&sub-channel-id={{SubChannelId}} HTTP/1.1
x-amz-chime-bearer: {{ChimeBearer}}
```

## URI Request Parameters
<a name="API_messaging-chime_GetChannelMessageStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelArn](#API_messaging-chime_GetChannelMessageStatus_RequestSyntax) **   <a name="chimesdk-messaging-chime_GetChannelMessageStatus-request-uri-ChannelArn"></a>
The ARN of the channel
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [ChimeBearer](#API_messaging-chime_GetChannelMessageStatus_RequestSyntax) **   <a name="chimesdk-messaging-chime_GetChannelMessageStatus-request-ChimeBearer"></a>
The `AppInstanceUserArn` of the user making the API call.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [messageId](#API_messaging-chime_GetChannelMessageStatus_RequestSyntax) **   <a name="chimesdk-messaging-chime_GetChannelMessageStatus-request-uri-MessageId"></a>
The ID of the message.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`
Required: Yes

 ** [SubChannelId](#API_messaging-chime_GetChannelMessageStatus_RequestSyntax) **   <a name="chimesdk-messaging-chime_GetChannelMessageStatus-request-uri-SubChannelId"></a>
The ID of the SubChannel in the request.
Only required when getting message status in a SubChannel that the user belongs to.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`

## Request Body
<a name="API_messaging-chime_GetChannelMessageStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_messaging-chime_GetChannelMessageStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Status": {
      "Detail": "string",
      "Value": "string"
   }
}
```

## Response Elements
<a name="API_messaging-chime_GetChannelMessageStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Status](#API_messaging-chime_GetChannelMessageStatus_ResponseSyntax) **   <a name="chimesdk-messaging-chime_GetChannelMessageStatus-response-Status"></a>
The message status and details.
Type: [ChannelMessageStatusStructure](API_messaging-chime_ChannelMessageStatusStructure.md) object

## Errors
<a name="API_messaging-chime_GetChannelMessageStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

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
<a name="API_messaging-chime_GetChannelMessageStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/GetChannelMessageStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/GetChannelMessageStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/GetChannelMessageStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/GetChannelMessageStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/GetChannelMessageStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/GetChannelMessageStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/GetChannelMessageStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/GetChannelMessageStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/GetChannelMessageStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/GetChannelMessageStatus)
