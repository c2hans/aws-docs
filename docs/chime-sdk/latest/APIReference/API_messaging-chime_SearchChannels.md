---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SearchChannels.html
---

# SearchChannels
<a name="API_messaging-chime_SearchChannels"></a>

Allows the `ChimeBearer` to search channels by channel members. Users or bots can search across the channels that they belong to. Users in the `AppInstanceAdmin` role can search across all channels.

The `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call as the value in the header.

**Note**
This operation isn't supported for `AppInstanceUsers` with a large number of memberships.

## Request Syntax
<a name="API_messaging-chime_SearchChannels_RequestSyntax"></a>

```
POST /channels?operation=search&max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
x-amz-chime-bearer: {{ChimeBearer}}
Content-type: application/json

{
   "Fields": [
      {
         "Key": "{{string}}",
         "Operator": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ]
}
```

## URI Request Parameters
<a name="API_messaging-chime_SearchChannels_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChimeBearer](#API_messaging-chime_SearchChannels_RequestSyntax) **   <a name="chimesdk-messaging-chime_SearchChannels-request-ChimeBearer"></a>
The `AppInstanceUserArn` of the user making the API call.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [MaxResults](#API_messaging-chime_SearchChannels_RequestSyntax) **   <a name="chimesdk-messaging-chime_SearchChannels-request-uri-MaxResults"></a>
The maximum number of channels that you want returned.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_messaging-chime_SearchChannels_RequestSyntax) **   <a name="chimesdk-messaging-chime_SearchChannels-request-uri-NextToken"></a>
The token returned from previous API requests until the number of channels is reached.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

## Request Body
<a name="API_messaging-chime_SearchChannels_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Fields](#API_messaging-chime_SearchChannels_RequestSyntax) **   <a name="chimesdk-messaging-chime_SearchChannels-request-Fields"></a>
A list of the `Field` objects in the channel being searched.
Type: Array of [SearchField](API_messaging-chime_SearchField.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

## Response Syntax
<a name="API_messaging-chime_SearchChannels_ResponseSyntax"></a>

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
<a name="API_messaging-chime_SearchChannels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Channels](#API_messaging-chime_SearchChannels_ResponseSyntax) **   <a name="chimesdk-messaging-chime_SearchChannels-response-Channels"></a>
A list of the channels in the request.
Type: Array of [ChannelSummary](API_messaging-chime_ChannelSummary.md) objects

 ** [NextToken](#API_messaging-chime_SearchChannels_ResponseSyntax) **   <a name="chimesdk-messaging-chime_SearchChannels-response-NextToken"></a>
The token returned from previous API responses until the number of channels is reached.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

## Errors
<a name="API_messaging-chime_SearchChannels_Errors"></a>

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
<a name="API_messaging-chime_SearchChannels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/SearchChannels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/SearchChannels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/SearchChannels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/SearchChannels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/SearchChannels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/SearchChannels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/SearchChannels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/SearchChannels)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/SearchChannels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/SearchChannels)
