---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PutChannelMembershipPreferences.html
---

# PutChannelMembershipPreferences
<a name="API_messaging-chime_PutChannelMembershipPreferences"></a>

Sets the membership preferences of an `AppInstanceUser` or `AppInstanceBot` for the specified channel. The user or bot must be a member of the channel. Only the user or bot who owns the membership can set preferences. Users or bots in the `AppInstanceAdmin` and channel moderator roles can't set preferences for other users. Banned users or bots can't set membership preferences for the channel from which they are banned.

**Note**
The x-amz-chime-bearer request header is mandatory. Use the ARN of an `AppInstanceUser` or `AppInstanceBot` that makes the API call as the value in the header.

## Request Syntax
<a name="API_messaging-chime_PutChannelMembershipPreferences_RequestSyntax"></a>

```
PUT /channels/{{channelArn}}/memberships/{{memberArn}}/preferences HTTP/1.1
x-amz-chime-bearer: {{ChimeBearer}}
Content-type: application/json

{
   "Preferences": {
      "PushNotifications": {
         "AllowNotifications": "{{string}}",
         "FilterRule": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_messaging-chime_PutChannelMembershipPreferences_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelArn](#API_messaging-chime_PutChannelMembershipPreferences_RequestSyntax) **   <a name="chimesdk-messaging-chime_PutChannelMembershipPreferences-request-uri-ChannelArn"></a>
The ARN of the channel.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [ChimeBearer](#API_messaging-chime_PutChannelMembershipPreferences_RequestSyntax) **   <a name="chimesdk-messaging-chime_PutChannelMembershipPreferences-request-ChimeBearer"></a>
The ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [memberArn](#API_messaging-chime_PutChannelMembershipPreferences_RequestSyntax) **   <a name="chimesdk-messaging-chime_PutChannelMembershipPreferences-request-uri-MemberArn"></a>
The ARN of the member setting the preferences.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_messaging-chime_PutChannelMembershipPreferences_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Preferences](#API_messaging-chime_PutChannelMembershipPreferences_RequestSyntax) **   <a name="chimesdk-messaging-chime_PutChannelMembershipPreferences-request-Preferences"></a>
The channel membership preferences of an `AppInstanceUser` .
Type: [ChannelMembershipPreferences](API_messaging-chime_ChannelMembershipPreferences.md) object
Required: Yes

## Response Syntax
<a name="API_messaging-chime_PutChannelMembershipPreferences_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChannelArn": "string",
   "Member": {
      "Arn": "string",
      "Name": "string"
   },
   "Preferences": {
      "PushNotifications": {
         "AllowNotifications": "string",
         "FilterRule": "string"
      }
   }
}
```

## Response Elements
<a name="API_messaging-chime_PutChannelMembershipPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChannelArn](#API_messaging-chime_PutChannelMembershipPreferences_ResponseSyntax) **   <a name="chimesdk-messaging-chime_PutChannelMembershipPreferences-response-ChannelArn"></a>
The ARN of the channel.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [Member](#API_messaging-chime_PutChannelMembershipPreferences_ResponseSyntax) **   <a name="chimesdk-messaging-chime_PutChannelMembershipPreferences-response-Member"></a>
The details of a user.
Type: [Identity](API_messaging-chime_Identity.md) object

 ** [Preferences](#API_messaging-chime_PutChannelMembershipPreferences_ResponseSyntax) **   <a name="chimesdk-messaging-chime_PutChannelMembershipPreferences-response-Preferences"></a>
The ARN and metadata of the member being added.
Type: [ChannelMembershipPreferences](API_messaging-chime_ChannelMembershipPreferences.md) object

## Errors
<a name="API_messaging-chime_PutChannelMembershipPreferences_Errors"></a>

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
<a name="API_messaging-chime_PutChannelMembershipPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/PutChannelMembershipPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/PutChannelMembershipPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/PutChannelMembershipPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/PutChannelMembershipPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/PutChannelMembershipPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/PutChannelMembershipPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/PutChannelMembershipPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/PutChannelMembershipPreferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/PutChannelMembershipPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/PutChannelMembershipPreferences)
