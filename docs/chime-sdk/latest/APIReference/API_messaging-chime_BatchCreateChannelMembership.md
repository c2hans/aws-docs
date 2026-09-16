---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_BatchCreateChannelMembership.html
---

# BatchCreateChannelMembership
<a name="API_messaging-chime_BatchCreateChannelMembership"></a>

Adds a specified number of users and bots to a channel.

## Request Syntax
<a name="API_messaging-chime_BatchCreateChannelMembership_RequestSyntax"></a>

```
POST /channels/{{channelArn}}/memberships?operation=batch-create HTTP/1.1
x-amz-chime-bearer: {{ChimeBearer}}
Content-type: application/json

{
   "MemberArns": [ "{{string}}" ],
   "SubChannelId": "{{string}}",
   "Type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_messaging-chime_BatchCreateChannelMembership_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelArn](#API_messaging-chime_BatchCreateChannelMembership_RequestSyntax) **   <a name="chimesdk-messaging-chime_BatchCreateChannelMembership-request-uri-ChannelArn"></a>
The ARN of the channel to which you're adding users or bots.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [ChimeBearer](#API_messaging-chime_BatchCreateChannelMembership_RequestSyntax) **   <a name="chimesdk-messaging-chime_BatchCreateChannelMembership-request-ChimeBearer"></a>
The ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_messaging-chime_BatchCreateChannelMembership_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MemberArns](#API_messaging-chime_BatchCreateChannelMembership_RequestSyntax) **   <a name="chimesdk-messaging-chime_BatchCreateChannelMembership-request-MemberArns"></a>
The ARNs of the members you want to add to the channel. Only `AppInstanceUsers` and `AppInstanceBots` can be added as a channel member.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [SubChannelId](#API_messaging-chime_BatchCreateChannelMembership_RequestSyntax) **   <a name="chimesdk-messaging-chime_BatchCreateChannelMembership-request-SubChannelId"></a>
The ID of the SubChannel in the request.
Only required when creating membership in a SubChannel for a moderator in an elastic channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** [Type](#API_messaging-chime_BatchCreateChannelMembership_RequestSyntax) **   <a name="chimesdk-messaging-chime_BatchCreateChannelMembership-request-Type"></a>
The membership type of a user, `DEFAULT` or `HIDDEN`. Default members are always returned as part of `ListChannelMemberships`. Hidden members are only returned if the type filter in `ListChannelMemberships` equals `HIDDEN`. Otherwise hidden members are not returned. This is only supported by moderators.
Type: String
Valid Values: `DEFAULT | HIDDEN`
Required: No

## Response Syntax
<a name="API_messaging-chime_BatchCreateChannelMembership_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BatchChannelMemberships": {
      "ChannelArn": "string",
      "InvitedBy": {
         "Arn": "string",
         "Name": "string"
      },
      "Members": [
         {
            "Arn": "string",
            "Name": "string"
         }
      ],
      "SubChannelId": "string",
      "Type": "string"
   },
   "Errors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "MemberArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_messaging-chime_BatchCreateChannelMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BatchChannelMemberships](#API_messaging-chime_BatchCreateChannelMembership_ResponseSyntax) **   <a name="chimesdk-messaging-chime_BatchCreateChannelMembership-response-BatchChannelMemberships"></a>
The list of channel memberships in the response.
Type: [BatchChannelMemberships](API_messaging-chime_BatchChannelMemberships.md) object

 ** [Errors](#API_messaging-chime_BatchCreateChannelMembership_ResponseSyntax) **   <a name="chimesdk-messaging-chime_BatchCreateChannelMembership-response-Errors"></a>
If the action fails for one or more of the memberships in the request, a list of the memberships is returned, along with error codes and error messages.
Type: Array of [BatchCreateChannelMembershipError](API_messaging-chime_BatchCreateChannelMembershipError.md) objects

## Errors
<a name="API_messaging-chime_BatchCreateChannelMembership_Errors"></a>

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
<a name="API_messaging-chime_BatchCreateChannelMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/BatchCreateChannelMembership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/BatchCreateChannelMembership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/BatchCreateChannelMembership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/BatchCreateChannelMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/BatchCreateChannelMembership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/BatchCreateChannelMembership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/BatchCreateChannelMembership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/BatchCreateChannelMembership)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/BatchCreateChannelMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/BatchCreateChannelMembership)
