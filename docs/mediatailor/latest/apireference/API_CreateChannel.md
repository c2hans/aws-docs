---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_CreateChannel.html
---

# CreateChannel
<a name="API_CreateChannel"></a>

Creates a channel. For information about MediaTailor channels, see [Working with channels](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html) in the *MediaTailor User Guide*.

## Request Syntax
<a name="API_CreateChannel_RequestSyntax"></a>

```
POST /channel/{{ChannelName}} HTTP/1.1
Content-type: application/json

{
   "Audiences": [ "{{string}}" ],
   "FillerSlate": {
      "SourceLocationName": "{{string}}",
      "VodSourceName": "{{string}}"
   },
   "Outputs": [
      {
         "DashPlaylistSettings": {
            "ManifestWindowSeconds": {{number}},
            "MinBufferTimeSeconds": {{number}},
            "MinUpdatePeriodSeconds": {{number}},
            "SuggestedPresentationDelaySeconds": {{number}}
         },
         "HlsPlaylistSettings": {
            "AdMarkupType": [ "{{string}}" ],
            "ManifestWindowSeconds": {{number}}
         },
         "ManifestName": "{{string}}",
         "SourceGroup": "{{string}}"
      }
   ],
   "PlaybackMode": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "Tier": "{{string}}",
   "TimeShiftConfiguration": {
      "MaxTimeDelaySeconds": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_CreateChannel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelName](#API_CreateChannel_RequestSyntax) **   <a name="mediatailor-CreateChannel-request-uri-ChannelName"></a>
The name of the channel.
Required: Yes

## Request Body
<a name="API_CreateChannel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Audiences](#API_CreateChannel_RequestSyntax) **   <a name="mediatailor-CreateChannel-request-Audiences"></a>
The list of audiences defined in channel.
Type: Array of strings
Required: No

 ** [FillerSlate](#API_CreateChannel_RequestSyntax) **   <a name="mediatailor-CreateChannel-request-FillerSlate"></a>
The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the `LINEAR` `PlaybackMode`. MediaTailor doesn't support filler slate for channels using the `LOOP` `PlaybackMode`.
Type: [SlateSource](API_SlateSource.md) object
Required: No

 ** [Outputs](#API_CreateChannel_RequestSyntax) **   <a name="mediatailor-CreateChannel-request-Outputs"></a>
The channel's output properties.
Type: Array of [RequestOutputItem](API_RequestOutputItem.md) objects
Required: Yes

 ** [PlaybackMode](#API_CreateChannel_RequestSyntax) **   <a name="mediatailor-CreateChannel-request-PlaybackMode"></a>
The type of playback mode to use for this channel.
 `LINEAR` - The programs in the schedule play once back-to-back in the schedule.
 `LOOP` - The programs in the schedule play back-to-back in an endless loop. When the last program in the schedule stops playing, playback loops back to the first program in the schedule.
Type: String
Valid Values: `LOOP | LINEAR`
Required: Yes

 ** [tags](#API_CreateChannel_RequestSyntax) **   <a name="mediatailor-CreateChannel-request-tags"></a>
The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map
Required: No

 ** [Tier](#API_CreateChannel_RequestSyntax) **   <a name="mediatailor-CreateChannel-request-Tier"></a>
The tier of the channel.
Type: String
Valid Values: `BASIC | STANDARD`
Required: No

 ** [TimeShiftConfiguration](#API_CreateChannel_RequestSyntax) **   <a name="mediatailor-CreateChannel-request-TimeShiftConfiguration"></a>
 The time-shifted viewing configuration you want to associate to the channel.
Type: [TimeShiftConfiguration](API_TimeShiftConfiguration.md) object
Required: No

## Response Syntax
<a name="API_CreateChannel_ResponseSyntax"></a>

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
<a name="API_CreateChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateChannel_ResponseSyntax) **   <a name="mediatailor-CreateChannel-response-Arn"></a>
The Amazon Resource Name (ARN) to assign to the channel.
Type: String

 ** [Audiences](#API_CreateChannel_ResponseSyntax) **   <a name="mediatailor-CreateChannel-response-Audiences"></a>
The list of audiences defined in channel.
Type: Array of strings

 ** [ChannelName](#API_CreateChannel_ResponseSyntax) **   <a name="mediatailor-CreateChannel-response-ChannelName"></a>
The name to assign to the channel.
Type: String

 ** [ChannelState](#API_CreateChannel_ResponseSyntax) **   <a name="mediatailor-CreateChannel-response-ChannelState"></a>
Indicates whether the channel is in a running state or not.
Type: String
Valid Values: `RUNNING | STOPPED`

 ** [CreationTime](#API_CreateChannel_ResponseSyntax) **   <a name="mediatailor-CreateChannel-response-CreationTime"></a>
The timestamp of when the channel was created.
Type: Timestamp

 ** [FillerSlate](#API_CreateChannel_ResponseSyntax) **   <a name="mediatailor-CreateChannel-response-FillerSlate"></a>
Contains information about the slate used to fill gaps between programs in the schedule.
Type: [SlateSource](API_SlateSource.md) object

 ** [LastModifiedTime](#API_CreateChannel_ResponseSyntax) **   <a name="mediatailor-CreateChannel-response-LastModifiedTime"></a>
The timestamp of when the channel was last modified.
Type: Timestamp

 ** [Outputs](#API_CreateChannel_ResponseSyntax) **   <a name="mediatailor-CreateChannel-response-Outputs"></a>
The output properties to assign to the channel.
Type: Array of [ResponseOutputItem](API_ResponseOutputItem.md) objects

 ** [PlaybackMode](#API_CreateChannel_ResponseSyntax) **   <a name="mediatailor-CreateChannel-response-PlaybackMode"></a>
The playback mode to assign to the channel.
Type: String

 ** [tags](#API_CreateChannel_ResponseSyntax) **   <a name="mediatailor-CreateChannel-response-tags"></a>
The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

 ** [Tier](#API_CreateChannel_ResponseSyntax) **   <a name="mediatailor-CreateChannel-response-Tier"></a>
The tier of the channel.
Type: String

 ** [TimeShiftConfiguration](#API_CreateChannel_ResponseSyntax) **   <a name="mediatailor-CreateChannel-response-TimeShiftConfiguration"></a>
 The time-shifted viewing configuration assigned to the channel.
Type: [TimeShiftConfiguration](API_TimeShiftConfiguration.md) object

## Errors
<a name="API_CreateChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/CreateChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/CreateChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/CreateChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/CreateChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/CreateChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/CreateChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/CreateChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/CreateChannel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/CreateChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/CreateChannel)
