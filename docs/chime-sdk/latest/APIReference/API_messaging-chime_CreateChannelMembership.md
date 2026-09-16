---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelMembership.html
---

# CreateChannelMembership
<a name="API_messaging-chime_CreateChannelMembership"></a>

Adds a member to a channel. The `InvitedBy` field in `ChannelMembership` is derived from the request header. A channel member can:
+ List messages
+ Send messages
+ Receive messages
+ Edit their own messages
+ Leave the channel

Privacy settings impact this action as follows:
+ Public Channels: You do not need to be a member to list messages, but you must be a member to send messages.
+ Private Channels: You must be a member to list or send messages.

**Note**
The `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUserArn` or `AppInstanceBot` that makes the API call as the value in the header.

## Request Syntax
<a name="API_messaging-chime_CreateChannelMembership_RequestSyntax"></a>

```
POST /channels/{{channelArn}}/memberships HTTP/1.1
x-amz-chime-bearer: {{ChimeBearer}}
Content-type: application/json

{
   "MemberArn": "{{string}}",
   "SubChannelId": "{{string}}",
   "Type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_messaging-chime_CreateChannelMembership_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelArn](#API_messaging-chime_CreateChannelMembership_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelMembership-request-uri-ChannelArn"></a>
The ARN of the channel to which you're adding users.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [ChimeBearer](#API_messaging-chime_CreateChannelMembership_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelMembership-request-ChimeBearer"></a>
The ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_messaging-chime_CreateChannelMembership_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MemberArn](#API_messaging-chime_CreateChannelMembership_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelMembership-request-MemberArn"></a>
The `AppInstanceUserArn` of the member you want to add to the channel.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [SubChannelId](#API_messaging-chime_CreateChannelMembership_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelMembership-request-SubChannelId"></a>
The ID of the SubChannel in the request.
Only required when creating membership in a SubChannel for a moderator in an elastic channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** [Type](#API_messaging-chime_CreateChannelMembership_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelMembership-request-Type"></a>
The membership type of a user, `DEFAULT` or `HIDDEN`. Default members are always returned as part of `ListChannelMemberships`. Hidden members are only returned if the type filter in `ListChannelMemberships` equals `HIDDEN`. Otherwise hidden members are not returned. This is only supported by moderators.
Type: String
Valid Values: `DEFAULT | HIDDEN`
Required: Yes

## Response Syntax
<a name="API_messaging-chime_CreateChannelMembership_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "ChannelArn": "string",
   "Member": {
      "Arn": "string",
      "Name": "string"
   },
   "SubChannelId": "string"
}
```

## Response Elements
<a name="API_messaging-chime_CreateChannelMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [ChannelArn](#API_messaging-chime_CreateChannelMembership_ResponseSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelMembership-response-ChannelArn"></a>
The ARN of the channel.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [Member](#API_messaging-chime_CreateChannelMembership_ResponseSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelMembership-response-Member"></a>
The ARN and metadata of the member being added.
Type: [Identity](API_messaging-chime_Identity.md) object

 ** [SubChannelId](#API_messaging-chime_CreateChannelMembership_ResponseSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelMembership-response-SubChannelId"></a>
The ID of the SubChannel in the response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`

## Errors
<a name="API_messaging-chime_CreateChannelMembership_Errors"></a>

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

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

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
<a name="API_messaging-chime_CreateChannelMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/CreateChannelMembership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/CreateChannelMembership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/CreateChannelMembership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/CreateChannelMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/CreateChannelMembership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/CreateChannelMembership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/CreateChannelMembership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/CreateChannelMembership)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/CreateChannelMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/CreateChannelMembership)
