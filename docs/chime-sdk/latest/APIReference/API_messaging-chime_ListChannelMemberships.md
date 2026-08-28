---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMemberships.html
---

# ListChannelMemberships
<a name="API_messaging-chime_ListChannelMemberships"></a>

Lists all channel memberships in a channel.

**Note**
The `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call as the value in the header.

If you want to list the channels to which a specific app instance user belongs, see the [ListChannelMembershipsForAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMembershipsForAppInstanceUser.html) API.

## Request Syntax
<a name="API_messaging-chime_ListChannelMemberships_RequestSyntax"></a>

```
GET /channels/{{channelArn}}/memberships?max-results={{MaxResults}}&next-token={{NextToken}}&sub-channel-id={{SubChannelId}}&type={{Type}} HTTP/1.1
x-amz-chime-bearer: {{ChimeBearer}}
```

## URI Request Parameters
<a name="API_messaging-chime_ListChannelMemberships_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelArn](#API_messaging-chime_ListChannelMemberships_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMemberships-request-uri-ChannelArn"></a>
The maximum number of channel memberships that you want returned.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [ChimeBearer](#API_messaging-chime_ListChannelMemberships_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMemberships-request-ChimeBearer"></a>
The ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [MaxResults](#API_messaging-chime_ListChannelMemberships_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMemberships-request-uri-MaxResults"></a>
The maximum number of channel memberships that you want returned.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_messaging-chime_ListChannelMemberships_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMemberships-request-uri-NextToken"></a>
The token passed by previous API calls until all requested channel memberships are returned.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

 ** [SubChannelId](#API_messaging-chime_ListChannelMemberships_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMemberships-request-uri-SubChannelId"></a>
The ID of the SubChannel in the request.
Only required when listing a user's memberships in a particular sub-channel of an elastic channel.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`

 ** [Type](#API_messaging-chime_ListChannelMemberships_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMemberships-request-uri-Type"></a>
The membership type of a user, `DEFAULT` or `HIDDEN`. Default members are returned as part of `ListChannelMemberships` if no type is specified. Hidden members are only returned if the type filter in `ListChannelMemberships` equals `HIDDEN`.
Valid Values: `DEFAULT | HIDDEN`

## Request Body
<a name="API_messaging-chime_ListChannelMemberships_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_messaging-chime_ListChannelMemberships_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChannelArn": "string",
   "ChannelMemberships": [
      {
         "Member": {
            "Arn": "string",
            "Name": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_messaging-chime_ListChannelMemberships_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChannelArn](#API_messaging-chime_ListChannelMemberships_ResponseSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMemberships-response-ChannelArn"></a>
The ARN of the channel.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [ChannelMemberships](#API_messaging-chime_ListChannelMemberships_ResponseSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMemberships-response-ChannelMemberships"></a>
The information for the requested channel memberships.
Type: Array of [ChannelMembershipSummary](API_messaging-chime_ChannelMembershipSummary.md) objects

 ** [NextToken](#API_messaging-chime_ListChannelMemberships_ResponseSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMemberships-response-NextToken"></a>
The token passed by previous API calls until all requested channel memberships are returned.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

## Errors
<a name="API_messaging-chime_ListChannelMemberships_Errors"></a>

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
<a name="API_messaging-chime_ListChannelMemberships_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/ListChannelMemberships)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/ListChannelMemberships)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/ListChannelMemberships)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/ListChannelMemberships)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/ListChannelMemberships)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/ListChannelMemberships)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/ListChannelMemberships)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/ListChannelMemberships)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/ListChannelMemberships)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/ListChannelMemberships)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
