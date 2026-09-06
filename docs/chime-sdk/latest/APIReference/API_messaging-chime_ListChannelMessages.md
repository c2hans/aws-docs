---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMessages.html
---

# ListChannelMessages
<a name="API_messaging-chime_ListChannelMessages"></a>

List all the messages in a channel. Returns a paginated list of `ChannelMessages`. By default, sorted by creation timestamp in descending order.

**Note**
Redacted messages appear in the results as empty, since they are only redacted, not deleted. Deleted messages do not appear in the results. This action always returns the latest version of an edited message.
Also, the `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call as the value in the header.

## Request Syntax
<a name="API_messaging-chime_ListChannelMessages_RequestSyntax"></a>

```
GET /channels/{{channelArn}}/messages?max-results={{MaxResults}}&next-token={{NextToken}}&not-after={{NotAfter}}&not-before={{NotBefore}}&sort-order={{SortOrder}}&sub-channel-id={{SubChannelId}} HTTP/1.1
x-amz-chime-bearer: {{ChimeBearer}}
```

## URI Request Parameters
<a name="API_messaging-chime_ListChannelMessages_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelArn](#API_messaging-chime_ListChannelMessages_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMessages-request-uri-ChannelArn"></a>
The ARN of the channel.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [ChimeBearer](#API_messaging-chime_ListChannelMessages_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMessages-request-ChimeBearer"></a>
The ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [MaxResults](#API_messaging-chime_ListChannelMessages_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMessages-request-uri-MaxResults"></a>
The maximum number of messages that you want returned.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_messaging-chime_ListChannelMessages_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMessages-request-uri-NextToken"></a>
The token passed by previous API calls until all requested messages are returned.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

 ** [NotAfter](#API_messaging-chime_ListChannelMessages_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMessages-request-uri-NotAfter"></a>
The final or ending time stamp for your requested messages.

 ** [NotBefore](#API_messaging-chime_ListChannelMessages_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMessages-request-uri-NotBefore"></a>
The initial or starting time stamp for your requested messages.

 ** [SortOrder](#API_messaging-chime_ListChannelMessages_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMessages-request-uri-SortOrder"></a>
The order in which you want messages sorted. Default is Descending, based on time created.
Valid Values: `ASCENDING | DESCENDING`

 ** [SubChannelId](#API_messaging-chime_ListChannelMessages_RequestSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMessages-request-uri-SubChannelId"></a>
The ID of the SubChannel in the request.
Only required when listing the messages in a SubChannel that the user belongs to.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`

## Request Body
<a name="API_messaging-chime_ListChannelMessages_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_messaging-chime_ListChannelMessages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChannelArn": "string",
   "ChannelMessages": [
      {
         "Content": "string",
         "ContentType": "string",
         "CreatedTimestamp": number,
         "LastEditedTimestamp": number,
         "LastUpdatedTimestamp": number,
         "MessageAttributes": {
            "string" : {
               "StringValues": [ "string" ]
            }
         },
         "MessageId": "string",
         "Metadata": "string",
         "Redacted": boolean,
         "Sender": {
            "Arn": "string",
            "Name": "string"
         },
         "Status": {
            "Detail": "string",
            "Value": "string"
         },
         "Target": [
            {
               "MemberArn": "string"
            }
         ],
         "Type": "string"
      }
   ],
   "NextToken": "string",
   "SubChannelId": "string"
}
```

## Response Elements
<a name="API_messaging-chime_ListChannelMessages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChannelArn](#API_messaging-chime_ListChannelMessages_ResponseSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMessages-response-ChannelArn"></a>
The ARN of the channel containing the requested messages.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [ChannelMessages](#API_messaging-chime_ListChannelMessages_ResponseSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMessages-response-ChannelMessages"></a>
The information about, and content of, each requested message.
Type: Array of [ChannelMessageSummary](API_messaging-chime_ChannelMessageSummary.md) objects

 ** [NextToken](#API_messaging-chime_ListChannelMessages_ResponseSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMessages-response-NextToken"></a>
The token passed by previous API calls until all requested messages are returned.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

 ** [SubChannelId](#API_messaging-chime_ListChannelMessages_ResponseSyntax) **   <a name="chimesdk-messaging-chime_ListChannelMessages-response-SubChannelId"></a>
The ID of the SubChannel in the response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`

## Errors
<a name="API_messaging-chime_ListChannelMessages_Errors"></a>

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
<a name="API_messaging-chime_ListChannelMessages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/ListChannelMessages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/ListChannelMessages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/ListChannelMessages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/ListChannelMessages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/ListChannelMessages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/ListChannelMessages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/ListChannelMessages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/ListChannelMessages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/ListChannelMessages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/ListChannelMessages)
