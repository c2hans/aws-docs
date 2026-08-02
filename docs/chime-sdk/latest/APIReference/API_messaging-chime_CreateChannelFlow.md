---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelFlow.html
---

# CreateChannelFlow
<a name="API_messaging-chime_CreateChannelFlow"></a>

Creates a channel flow, a container for processors. Processors are AWS Lambda functions that perform actions on chat messages, such as stripping out profanity. You can associate channel flows with channels, and the processors in the channel flow then take action on all messages sent to that channel. This is a developer API.

Channel flows process the following items:

1. New and updated messages

1. Persistent and non-persistent messages

1. The Standard message type

**Note**
Channel flows don't process Control or System messages. For more information about the message types provided by Chime SDK messaging, refer to [Message types](https://docs.aws.amazon.com/chime-sdk/latest/dg/using-the-messaging-sdk.html#msg-types) in the *Amazon Chime developer guide*.

## Request Syntax
<a name="API_messaging-chime_CreateChannelFlow_RequestSyntax"></a>

```
POST /channel-flows HTTP/1.1
Content-type: application/json

{
   "AppInstanceArn": "{{string}}",
   "ClientRequestToken": "{{string}}",
   "Name": "{{string}}",
   "Processors": [
      {
         "Configuration": {
            "Lambda": {
               "InvocationType": "{{string}}",
               "ResourceArn": "{{string}}"
            }
         },
         "ExecutionOrder": {{number}},
         "FallbackAction": "{{string}}",
         "Name": "{{string}}"
      }
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_messaging-chime_CreateChannelFlow_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_messaging-chime_CreateChannelFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AppInstanceArn](#API_messaging-chime_CreateChannelFlow_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelFlow-request-AppInstanceArn"></a>
The ARN of the channel flow request.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [ClientRequestToken](#API_messaging-chime_CreateChannelFlow_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelFlow-request-ClientRequestToken"></a>
The client token for the request. An Idempotency token.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[-_a-zA-Z0-9]*`
Required: Yes

 ** [Name](#API_messaging-chime_CreateChannelFlow_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelFlow-request-Name"></a>
The name of the channel flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
Required: Yes

 ** [Processors](#API_messaging-chime_CreateChannelFlow_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelFlow-request-Processors"></a>
Information about the processor Lambda functions.
Type: Array of [Processor](API_messaging-chime_Processor.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: Yes

 ** [Tags](#API_messaging-chime_CreateChannelFlow_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelFlow-request-Tags"></a>
The tags for the creation request.
Type: Array of [Tag](API_messaging-chime_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_messaging-chime_CreateChannelFlow_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "ChannelFlowArn": "string"
}
```

## Response Elements
<a name="API_messaging-chime_CreateChannelFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [ChannelFlowArn](#API_messaging-chime_CreateChannelFlow_ResponseSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelFlow-response-ChannelFlowArn"></a>
The ARN of the channel flow.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

## Errors
<a name="API_messaging-chime_CreateChannelFlow_Errors"></a>

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

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
HTTP Status Code: 400

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
<a name="API_messaging-chime_CreateChannelFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/CreateChannelFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/CreateChannelFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/CreateChannelFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/CreateChannelFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/CreateChannelFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/CreateChannelFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/CreateChannelFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/CreateChannelFlow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/CreateChannelFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/CreateChannelFlow)
