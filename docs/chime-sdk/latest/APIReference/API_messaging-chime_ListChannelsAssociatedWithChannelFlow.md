---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelsAssociatedWithChannelFlow.html
---

# ListChannelsAssociatedWithChannelFlow
<a name="API_messaging-chime_ListChannelsAssociatedWithChannelFlow"></a>

Lists all channels associated with a specified channel flow. You can associate a channel flow with multiple channels, but you can only associate a channel with one channel flow. This is a developer API.

## Request Syntax
<a name="API_messaging-chime_ListChannelsAssociatedWithChannelFlow_RequestSyntax"></a>

```
GET /channels?scope=channel-flow-associations&channel-flow-arn={{ChannelFlowArn}}&max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_messaging-chime_ListChannelsAssociatedWithChannelFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelFlowArn](#API_messaging-chime_ListChannelsAssociatedWithChannelFlow_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelsAssociatedWithChannelFlow-request-uri-ChannelFlowArn"></a>
The ARN of the channel flow.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [MaxResults](#API_messaging-chime_ListChannelsAssociatedWithChannelFlow_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelsAssociatedWithChannelFlow-request-uri-MaxResults"></a>
The maximum number of channels that you want to return.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_messaging-chime_ListChannelsAssociatedWithChannelFlow_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelsAssociatedWithChannelFlow-request-uri-NextToken"></a>
The token passed by previous API calls until all requested channels are returned.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

## Request Body
<a name="API_messaging-chime_ListChannelsAssociatedWithChannelFlow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_messaging-chime_ListChannelsAssociatedWithChannelFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Channels": [
      {
         "ChannelArn": "string",
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
<a name="API_messaging-chime_ListChannelsAssociatedWithChannelFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Channels](#API_messaging-chime_ListChannelsAssociatedWithChannelFlow_ResponseSyntax) **   <a name="chimesdk-messaging-chime_ListChannelsAssociatedWithChannelFlow-response-Channels"></a>
The information about each channel.
Type: Array of [ChannelAssociatedWithFlowSummary](API_messaging-chime_ChannelAssociatedWithFlowSummary.md) objects

 ** [NextToken](#API_messaging-chime_ListChannelsAssociatedWithChannelFlow_ResponseSyntax) **   <a name="chimesdk-messaging-chime_ListChannelsAssociatedWithChannelFlow-response-NextToken"></a>
The token passed by previous API calls until all requested channels are returned.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

## Errors
<a name="API_messaging-chime_ListChannelsAssociatedWithChannelFlow_Errors"></a>

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
<a name="API_messaging-chime_ListChannelsAssociatedWithChannelFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/ListChannelsAssociatedWithChannelFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/ListChannelsAssociatedWithChannelFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/ListChannelsAssociatedWithChannelFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/ListChannelsAssociatedWithChannelFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/ListChannelsAssociatedWithChannelFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/ListChannelsAssociatedWithChannelFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/ListChannelsAssociatedWithChannelFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/ListChannelsAssociatedWithChannelFlow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/ListChannelsAssociatedWithChannelFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/ListChannelsAssociatedWithChannelFlow)
