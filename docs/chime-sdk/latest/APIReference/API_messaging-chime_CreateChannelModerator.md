---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelModerator.html
---

# CreateChannelModerator
<a name="API_messaging-chime_CreateChannelModerator"></a>

Creates a new `ChannelModerator`. A channel moderator can:
+ Add and remove other members of the channel.
+ Add and remove other moderators of the channel.
+ Add and remove user bans for the channel.
+ Redact messages in the channel.
+ List messages in the channel.

**Note**
The `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUser` or `AppInstanceBot`of the user that makes the API call as the value in the header.

## Request Syntax
<a name="API_messaging-chime_CreateChannelModerator_RequestSyntax"></a>

```
POST /channels/{{channelArn}}/moderators HTTP/1.1
x-amz-chime-bearer: {{ChimeBearer}}
Content-type: application/json

{
   "ChannelModeratorArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_messaging-chime_CreateChannelModerator_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelArn](#API_messaging-chime_CreateChannelModerator_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelModerator-request-uri-ChannelArn"></a>
The ARN of the channel.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [ChimeBearer](#API_messaging-chime_CreateChannelModerator_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelModerator-request-ChimeBearer"></a>
The ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_messaging-chime_CreateChannelModerator_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChannelModeratorArn](#API_messaging-chime_CreateChannelModerator_RequestSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelModerator-request-ChannelModeratorArn"></a>
The `AppInstanceUserArn` of the moderator.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Response Syntax
<a name="API_messaging-chime_CreateChannelModerator_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "ChannelArn": "string",
   "ChannelModerator": {
      "Arn": "string",
      "Name": "string"
   }
}
```

## Response Elements
<a name="API_messaging-chime_CreateChannelModerator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [ChannelArn](#API_messaging-chime_CreateChannelModerator_ResponseSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelModerator-response-ChannelArn"></a>
The ARN of the channel.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [ChannelModerator](#API_messaging-chime_CreateChannelModerator_ResponseSyntax) **   <a name="chimesdk-messaging-chime_CreateChannelModerator-response-ChannelModerator"></a>
The ARNs of the channel and the moderator.
Type: [Identity](API_messaging-chime_Identity.md) object

## Errors
<a name="API_messaging-chime_CreateChannelModerator_Errors"></a>

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
<a name="API_messaging-chime_CreateChannelModerator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/CreateChannelModerator)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/CreateChannelModerator)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/CreateChannelModerator)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/CreateChannelModerator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/CreateChannelModerator)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/CreateChannelModerator)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/CreateChannelModerator)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/CreateChannelModerator)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/CreateChannelModerator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/CreateChannelModerator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
