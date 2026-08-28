---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_RedactChannelMessage.html
---

# RedactChannelMessage
<a name="API_messaging-chime_RedactChannelMessage"></a>

Redacts message content and metadata. The message exists in the back end, but the action returns null content, and the state shows as redacted.

**Note**
The `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call as the value in the header.

## Request Syntax
<a name="API_messaging-chime_RedactChannelMessage_RequestSyntax"></a>

```
POST /channels/{{channelArn}}/messages/{messageId}?operation=redact HTTP/1.1
x-amz-chime-bearer: {{ChimeBearer}}
Content-type: application/json

{
   "SubChannelId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_messaging-chime_RedactChannelMessage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelArn](#API_messaging-chime_RedactChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_RedactChannelMessage-request-uri-ChannelArn"></a>
The ARN of the channel containing the messages that you want to redact.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [ChimeBearer](#API_messaging-chime_RedactChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_RedactChannelMessage-request-ChimeBearer"></a>
The ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [messageId](#API_messaging-chime_RedactChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_RedactChannelMessage-request-uri-MessageId"></a>
The ID of the message being redacted.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`
Required: Yes

## Request Body
<a name="API_messaging-chime_RedactChannelMessage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SubChannelId](#API_messaging-chime_RedactChannelMessage_RequestSyntax) **   <a name="chimesdk-messaging-chime_RedactChannelMessage-request-SubChannelId"></a>
The ID of the SubChannel in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

## Response Syntax
<a name="API_messaging-chime_RedactChannelMessage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChannelArn": "string",
   "MessageId": "string",
   "SubChannelId": "string"
}
```

## Response Elements
<a name="API_messaging-chime_RedactChannelMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChannelArn](#API_messaging-chime_RedactChannelMessage_ResponseSyntax) **   <a name="chimesdk-messaging-chime_RedactChannelMessage-response-ChannelArn"></a>
The ARN of the channel containing the messages that you want to redact.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [MessageId](#API_messaging-chime_RedactChannelMessage_ResponseSyntax) **   <a name="chimesdk-messaging-chime_RedactChannelMessage-response-MessageId"></a>
The ID of the message being redacted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`

 ** [SubChannelId](#API_messaging-chime_RedactChannelMessage_ResponseSyntax) **   <a name="chimesdk-messaging-chime_RedactChannelMessage-response-SubChannelId"></a>
The ID of the SubChannel in the response.
Only required when redacting messages in a SubChannel that the user belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`

## Errors
<a name="API_messaging-chime_RedactChannelMessage_Errors"></a>

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
<a name="API_messaging-chime_RedactChannelMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/RedactChannelMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/RedactChannelMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/RedactChannelMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/RedactChannelMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/RedactChannelMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/RedactChannelMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/RedactChannelMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/RedactChannelMessage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/RedactChannelMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/RedactChannelMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
