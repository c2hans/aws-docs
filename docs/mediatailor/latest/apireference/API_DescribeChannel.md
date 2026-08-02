---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DescribeChannel.html
---

# DescribeChannel
<a name="API_DescribeChannel"></a>

Describes a channel. For information about MediaTailor channels, see [Working with channels](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html) in the *MediaTailor User Guide*.

## Request Syntax
<a name="API_DescribeChannel_RequestSyntax"></a>

```
GET /channel/{{ChannelName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeChannel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelName](#API_DescribeChannel_RequestSyntax) **   <a name="mediatailor-DescribeChannel-request-uri-ChannelName"></a>
The name of the channel.
Required: Yes

## Request Body
<a name="API_DescribeChannel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeChannel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Audiences": [ "string" ],
   "ChannelName": "string",
   "ChannelState": "string",
   "CreationTime": number,
   "FillerSlate": {
      "SourceLocationName": "string",
      "VodSourceName": "string"
   },
   "LastModifiedTime": number,
   "LogConfiguration": {
      "LogTypes": [ "string" ]
   },
   "Outputs": [
      {
         "DashPlaylistSettings": {
            "ManifestWindowSeconds": number,
            "MinBufferTimeSeconds": number,
            "MinUpdatePeriodSeconds": number,
            "SuggestedPresentationDelaySeconds": number
         },
         "DualStackPlaybackUrl": "string",
         "HlsPlaylistSettings": {
            "AdMarkupType": [ "string" ],
            "ManifestWindowSeconds": number
         },
         "ManifestName": "string",
         "PlaybackUrl": "string",
         "SourceGroup": "string"
      }
   ],
   "PlaybackMode": "string",
   "tags": {
      "string" : "string"
   },
   "Tier": "string",
   "TimeShiftConfiguration": {
      "MaxTimeDelaySeconds": number
   }
}
```

## Response Elements
<a name="API_DescribeChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DescribeChannel_ResponseSyntax) **   <a name="mediatailor-DescribeChannel-response-Arn"></a>
The ARN of the channel.
Type: String

 ** [Audiences](#API_DescribeChannel_ResponseSyntax) **   <a name="mediatailor-DescribeChannel-response-Audiences"></a>
The list of audiences defined in channel.
Type: Array of strings

 ** [ChannelName](#API_DescribeChannel_ResponseSyntax) **   <a name="mediatailor-DescribeChannel-response-ChannelName"></a>
The name of the channel.
Type: String

 ** [ChannelState](#API_DescribeChannel_ResponseSyntax) **   <a name="mediatailor-DescribeChannel-response-ChannelState"></a>
Indicates whether the channel is in a running state or not.
Type: String
Valid Values: `RUNNING | STOPPED`

 ** [CreationTime](#API_DescribeChannel_ResponseSyntax) **   <a name="mediatailor-DescribeChannel-response-CreationTime"></a>
The timestamp of when the channel was created.
Type: Timestamp

 ** [FillerSlate](#API_DescribeChannel_ResponseSyntax) **   <a name="mediatailor-DescribeChannel-response-FillerSlate"></a>
Contains information about the slate used to fill gaps between programs in the schedule.
Type: [SlateSource](API_SlateSource.md) object

 ** [LastModifiedTime](#API_DescribeChannel_ResponseSyntax) **   <a name="mediatailor-DescribeChannel-response-LastModifiedTime"></a>
The timestamp of when the channel was last modified.
Type: Timestamp

 ** [LogConfiguration](#API_DescribeChannel_ResponseSyntax) **   <a name="mediatailor-DescribeChannel-response-LogConfiguration"></a>
The log configuration for the channel.
Type: [LogConfigurationForChannel](API_LogConfigurationForChannel.md) object

 ** [Outputs](#API_DescribeChannel_ResponseSyntax) **   <a name="mediatailor-DescribeChannel-response-Outputs"></a>
The channel's output properties.
Type: Array of [ResponseOutputItem](API_ResponseOutputItem.md) objects

 ** [PlaybackMode](#API_DescribeChannel_ResponseSyntax) **   <a name="mediatailor-DescribeChannel-response-PlaybackMode"></a>
The channel's playback mode.
Type: String

 ** [tags](#API_DescribeChannel_ResponseSyntax) **   <a name="mediatailor-DescribeChannel-response-tags"></a>
The tags assigned to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

 ** [Tier](#API_DescribeChannel_ResponseSyntax) **   <a name="mediatailor-DescribeChannel-response-Tier"></a>
The channel's tier.
Type: String

 ** [TimeShiftConfiguration](#API_DescribeChannel_ResponseSyntax) **   <a name="mediatailor-DescribeChannel-response-TimeShiftConfiguration"></a>
 The time-shifted viewing configuration for the channel.
Type: [TimeShiftConfiguration](API_TimeShiftConfiguration.md) object

## Errors
<a name="API_DescribeChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/DescribeChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/DescribeChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/DescribeChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/DescribeChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/DescribeChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/DescribeChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/DescribeChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/DescribeChannel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/DescribeChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/DescribeChannel)
