---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannel.html
---

# CreateChannel
<a name="API_messaging-chime_CreateChannel"></a>

Creates a channel to which you can add users and send messages.

 **Restriction**: You can't change a channel's privacy.

**Note**
The `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call as the value in the header.

## Request Syntax
<a name="API_messaging-chime_CreateChannel_RequestSyntax"></a>

```
POST /channels HTTP/1.1
x-amz-chime-bearer: {{ChimeBearer}}
Content-type: application/json

{
   "AppInstanceArn": "{{string}}",
   "ChannelId": "{{string}}",
   "ClientRequestToken": "{{string}}",
   "ElasticChannelConfiguration": {
      "MaximumSubChannels": {{number}},
      "MinimumMembershipPercentage": {{number}},
      "TargetMembershipsPerSubChannel": {{number}}
   },
   "ExpirationSettings": {
      "ExpirationCriterion": "{{string}}",
      "ExpirationDays": {{number}}
   },
   "MemberArns": [ "{{string}}" ],
   "Metadata": "{{string}}",
   "Mode": "{{string}}",
   "ModeratorArns": [ "{{string}}" ],
   "Name": "{{string}}",
   "Privacy": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_messaging-chime_CreateChannel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChimeBearer](#API_messaging-chime_CreateChannel_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannel-request-ChimeBearer"></a>
The ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_messaging-chime_CreateChannel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AppInstanceArn](#API_messaging-chime_CreateChannel_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannel-request-AppInstanceArn"></a>
The ARN of the channel request.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [ChannelId](#API_messaging-chime_CreateChannel_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannel-request-ChannelId"></a>
An ID for the channel being created. If you do not specify an ID, a UUID will be created for the channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9]([A-Za-z0-9\:\-\_\.\@]{0,62}[A-Za-z0-9])?`
Required: No

 ** [ClientRequestToken](#API_messaging-chime_CreateChannel_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannel-request-ClientRequestToken"></a>
The client token for the request. An `Idempotency` token.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[-_a-zA-Z0-9]*`
Required: Yes

 ** [ElasticChannelConfiguration](#API_messaging-chime_CreateChannel_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannel-request-ElasticChannelConfiguration"></a>
The attributes required to configure and create an elastic channel. An elastic channel can support a maximum of 1-million users, excluding moderators.
Type: [ElasticChannelConfiguration](API_messaging-chime_ElasticChannelConfiguration.md) object
Required: No

 ** [ExpirationSettings](#API_messaging-chime_CreateChannel_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannel-request-ExpirationSettings"></a>
Settings that control the interval after which the channel is automatically deleted.
Type: [ExpirationSettings](API_messaging-chime_ExpirationSettings.md) object
Required: No

 ** [MemberArns](#API_messaging-chime_CreateChannel_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannel-request-MemberArns"></a>
The ARNs of the channel members in the request.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** [Metadata](#API_messaging-chime_CreateChannel_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannel-request-Metadata"></a>
The metadata of the creation request. Limited to 1KB and UTF-8.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** [Mode](#API_messaging-chime_CreateChannel_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannel-request-Mode"></a>
The channel mode: `UNRESTRICTED` or `RESTRICTED`. Administrators, moderators, and channel members can add themselves and other members to unrestricted channels. Only administrators and moderators can add members to restricted channels.
Type: String
Valid Values: `UNRESTRICTED | RESTRICTED`
Required: No

 ** [ModeratorArns](#API_messaging-chime_CreateChannel_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannel-request-ModeratorArns"></a>
The ARNs of the channel moderators in the request.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** [Name](#API_messaging-chime_CreateChannel_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannel-request-Name"></a>
The name of the channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
Required: Yes

 ** [Privacy](#API_messaging-chime_CreateChannel_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannel-request-Privacy"></a>
The channel's privacy level: `PUBLIC` or `PRIVATE`. Private channels aren't discoverable by users outside the channel. Public channels are discoverable by anyone in the `AppInstance`.
Type: String
Valid Values: `PUBLIC | PRIVATE`
Required: No

 ** [Tags](#API_messaging-chime_CreateChannel_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannel-request-Tags"></a>
The tags for the creation request.
Type: Array of [Tag](API_messaging-chime_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_messaging-chime_CreateChannel_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "ChannelArn": "string"
}
```

## Response Elements
<a name="API_messaging-chime_CreateChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [ChannelArn](#API_messaging-chime_CreateChannel_ResponseSyntax) **   <a name="chimesdk-messaging-chime_CreateChannel-response-ChannelArn"></a>
The ARN of the channel.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

## Errors
<a name="API_messaging-chime_CreateChannel_Errors"></a>

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
<a name="API_messaging-chime_CreateChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/CreateChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/CreateChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/CreateChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/CreateChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/CreateChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/CreateChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/CreateChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/CreateChannel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/CreateChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/CreateChannel)
