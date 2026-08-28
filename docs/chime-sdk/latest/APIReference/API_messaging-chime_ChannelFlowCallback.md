---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelFlowCallback.html
---

# ChannelFlowCallback
<a name="API_messaging-chime_ChannelFlowCallback"></a>

Calls back Amazon Chime SDK messaging with a processing response message. This should be invoked from the processor Lambda. This is a developer API.

You can return one of the following processing responses:
+ Update message content or metadata
+ Deny a message
+ Make no changes to the message

## Request Syntax
<a name="API_messaging-chime_ChannelFlowCallback_RequestSyntax"></a>

```
POST /channels/{channelArn}?operation=channel-flow-callback HTTP/1.1
Content-type: application/json

{
   "CallbackId": "{{string}}",
   "ChannelMessage": {
      "Content": "{{string}}",
      "ContentType": "{{string}}",
      "MessageAttributes": {
         "{{string}}" : {
            "StringValues": [ "{{string}}" ]
         }
      },
      "MessageId": "{{string}}",
      "Metadata": "{{string}}",
      "PushNotification": {
         "Body": "{{string}}",
         "Title": "{{string}}",
         "Type": "{{string}}"
      },
      "SubChannelId": "{{string}}"
   },
   "DeleteResource": {{boolean}}
}
```

## URI Request Parameters
<a name="API_messaging-chime_ChannelFlowCallback_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelArn](#API_messaging-chime_ChannelFlowCallback_RequestSyntax) **   <a name="chimesdk-messaging-chime_ChannelFlowCallback-request-uri-ChannelArn"></a>
The ARN of the channel.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_messaging-chime_ChannelFlowCallback_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CallbackId](#API_messaging-chime_ChannelFlowCallback_RequestSyntax) **   <a name="chimesdk-messaging-chime_ChannelFlowCallback-request-CallbackId"></a>
The identifier passed to the processor by the service when invoked. Use the identifier to call back the service.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.
Required: Yes

 ** [ChannelMessage](#API_messaging-chime_ChannelFlowCallback_RequestSyntax) **   <a name="chimesdk-messaging-chime_ChannelFlowCallback-request-ChannelMessage"></a>
Stores information about the processed message.
Type: [ChannelMessageCallback](API_messaging-chime_ChannelMessageCallback.md) object
Required: Yes

 ** [DeleteResource](#API_messaging-chime_ChannelFlowCallback_RequestSyntax) **   <a name="chimesdk-messaging-chime_ChannelFlowCallback-request-DeleteResource"></a>
When a processor determines that a message needs to be `DENIED`, pass this parameter with a value of true.
Type: Boolean
Required: No

## Response Syntax
<a name="API_messaging-chime_ChannelFlowCallback_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CallbackId": "string",
   "ChannelArn": "string"
}
```

## Response Elements
<a name="API_messaging-chime_ChannelFlowCallback_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CallbackId](#API_messaging-chime_ChannelFlowCallback_ResponseSyntax) **   <a name="chimesdk-messaging-chime_ChannelFlowCallback-response-CallbackId"></a>
The call back ID passed in the request.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.

 ** [ChannelArn](#API_messaging-chime_ChannelFlowCallback_ResponseSyntax) **   <a name="chimesdk-messaging-chime_ChannelFlowCallback-response-ChannelArn"></a>
The ARN of the channel.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

## Errors
<a name="API_messaging-chime_ChannelFlowCallback_Errors"></a>

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
<a name="API_messaging-chime_ChannelFlowCallback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/ChannelFlowCallback)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/ChannelFlowCallback)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/ChannelFlowCallback)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/ChannelFlowCallback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/ChannelFlowCallback)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/ChannelFlowCallback)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/ChannelFlowCallback)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/ChannelFlowCallback)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/ChannelFlowCallback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/ChannelFlowCallback)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
