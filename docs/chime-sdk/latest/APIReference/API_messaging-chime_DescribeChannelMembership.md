---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelMembership.html
---

# DescribeChannelMembership
<a name="API_messaging-chime_DescribeChannelMembership"></a>

Returns the full details of a user's channel membership.

**Note**
The `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call as the value in the header.

## Request Syntax
<a name="API_messaging-chime_DescribeChannelMembership_RequestSyntax"></a>

```
GET /channels/{{channelArn}}/memberships/{{memberArn}}?sub-channel-id={{SubChannelId}} HTTP/1.1
x-amz-chime-bearer: {{ChimeBearer}}
```

## URI Request Parameters
<a name="API_messaging-chime_DescribeChannelMembership_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelArn](#API_messaging-chime_DescribeChannelMembership_RequestSyntax) **   <a name="chimesdk-messaging-chime_DescribeChannelMembership-request-uri-ChannelArn"></a>
The ARN of the channel.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [ChimeBearer](#API_messaging-chime_DescribeChannelMembership_RequestSyntax) **   <a name="chimesdk-messaging-chime_DescribeChannelMembership-request-ChimeBearer"></a>
The ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [memberArn](#API_messaging-chime_DescribeChannelMembership_RequestSyntax) **   <a name="chimesdk-messaging-chime_DescribeChannelMembership-request-uri-MemberArn"></a>
The `AppInstanceUserArn` of the member.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [SubChannelId](#API_messaging-chime_DescribeChannelMembership_RequestSyntax) **   <a name="chimesdk-messaging-chime_DescribeChannelMembership-request-uri-SubChannelId"></a>
The ID of the SubChannel in the request. The response contains an `ElasticChannelConfiguration` object.
Only required to get a user’s SubChannel membership details.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`

## Request Body
<a name="API_messaging-chime_DescribeChannelMembership_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_messaging-chime_DescribeChannelMembership_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChannelMembership": {
      "ChannelArn": "string",
      "CreatedTimestamp": number,
      "InvitedBy": {
         "Arn": "string",
         "Name": "string"
      },
      "LastUpdatedTimestamp": number,
      "Member": {
         "Arn": "string",
         "Name": "string"
      },
      "SubChannelId": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_messaging-chime_DescribeChannelMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChannelMembership](#API_messaging-chime_DescribeChannelMembership_ResponseSyntax) **   <a name="chimesdk-messaging-chime_DescribeChannelMembership-response-ChannelMembership"></a>
The details of the membership.
Type: [ChannelMembership](API_messaging-chime_ChannelMembership.md) object

## Errors
<a name="API_messaging-chime_DescribeChannelMembership_Errors"></a>

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
<a name="API_messaging-chime_DescribeChannelMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/DescribeChannelMembership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/DescribeChannelMembership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/DescribeChannelMembership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/DescribeChannelMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/DescribeChannelMembership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/DescribeChannelMembership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/DescribeChannelMembership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/DescribeChannelMembership)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/DescribeChannelMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/DescribeChannelMembership)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
