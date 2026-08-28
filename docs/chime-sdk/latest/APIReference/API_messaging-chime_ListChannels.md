---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannels.html
---

# ListChannels
<a name="API_messaging-chime_ListChannels"></a>

Lists all Channels created under a single Chime App as a paginated list. You can specify filters to narrow results.

**Functionality & restrictions**
+ Use privacy = `PUBLIC` to retrieve all public channels in the account.
+ Only an `AppInstanceAdmin` can set privacy = `PRIVATE` to list the private channels in an account.

**Note**
The `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call as the value in the header.

## Request Syntax
<a name="API_messaging-chime_ListChannels_RequestSyntax"></a>

```
GET /channels?app-instance-arn={{AppInstanceArn}}&max-results={{MaxResults}}&next-token={{NextToken}}&privacy={{Privacy}} HTTP/1.1
x-amz-chime-bearer: {{ChimeBearer}}
```

## URI Request Parameters
<a name="API_messaging-chime_ListChannels_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AppInstanceArn](#API_messaging-chime_ListChannels_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannels-request-uri-AppInstanceArn"></a>
The ARN of the `AppInstance`.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [ChimeBearer](#API_messaging-chime_ListChannels_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannels-request-ChimeBearer"></a>
The ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [MaxResults](#API_messaging-chime_ListChannels_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannels-request-uri-MaxResults"></a>
The maximum number of channels that you want to return.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_messaging-chime_ListChannels_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannels-request-uri-NextToken"></a>
The token passed by previous API calls until all requested channels are returned.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

 ** [Privacy](#API_messaging-chime_ListChannels_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannels-request-uri-Privacy"></a>
The privacy setting. `PUBLIC` retrieves all the public channels. `PRIVATE` retrieves private channels. Only an `AppInstanceAdmin` can retrieve private channels.
Valid Values: `PUBLIC | PRIVATE`

## Request Body
<a name="API_messaging-chime_ListChannels_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_messaging-chime_ListChannels_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Channels": [
      {
         "ChannelArn": "string",
         "LastMessageTimestamp": number,
         "Metadata": "string",
         "Mode": "string",
         "Name": "string",
         "Privacy": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_messaging-chime_ListChannels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Channels](#API_messaging-chime_ListChannels_ResponseSyntax) **   <a name="chimesdk-messaging-chime_ListChannels-response-Channels"></a>
The information about each channel.
Type: Array of [ChannelSummary](API_messaging-chime_ChannelSummary.md) objects

 ** [NextToken](#API_messaging-chime_ListChannels_ResponseSyntax) **   <a name="chimesdk-messaging-chime_ListChannels-response-NextToken"></a>
The token returned from previous API requests until the number of channels is reached.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

## Errors
<a name="API_messaging-chime_ListChannels_Errors"></a>

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
<a name="API_messaging-chime_ListChannels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/ListChannels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/ListChannels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/ListChannels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/ListChannels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/ListChannels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/ListChannels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/ListChannels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/ListChannels)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/ListChannels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/ListChannels)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
