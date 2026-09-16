---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateChannel.html
---

# CreateChannel
<a name="API_CreateChannel"></a>

Creates a new channel and an associated stream key to start streaming.

## Request Syntax
<a name="API_CreateChannel_RequestSyntax"></a>

```
POST /CreateChannel HTTP/1.1
Content-type: application/json

{
   "adConfigurationArn": "{{string}}",
   "authorized": {{boolean}},
   "containerFormat": "{{string}}",
   "insecureIngest": {{boolean}},
   "latencyMode": "{{string}}",
   "multitrackInputConfiguration": {
      "enabled": {{boolean}},
      "maximumResolution": "{{string}}",
      "policy": "{{string}}"
   },
   "name": "{{string}}",
   "playbackRestrictionPolicyArn": "{{string}}",
   "preset": "{{string}}",
   "recordingConfigurationArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateChannel_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateChannel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [adConfigurationArn](#API_CreateChannel_RequestSyntax) **   <a name="ivs-CreateChannel-request-adConfigurationArn"></a>
ARN of the ad configuration associated with the channel.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:ad-configuration/[a-zA-Z0-9-]+$`
Required: No

 ** [authorized](#API_CreateChannel_RequestSyntax) **   <a name="ivs-CreateChannel-request-authorized"></a>
Whether the channel is private (enabled for playback authorization). Default: `false`.
Type: Boolean
Required: No

 ** [containerFormat](#API_CreateChannel_RequestSyntax) **   <a name="ivs-CreateChannel-request-containerFormat"></a>
Indicates which content-packaging format is used (MPEG-TS or fMP4). If `multitrackInputConfiguration` is specified and `enabled` is `true`, then `containerFormat` is required and must be set to `FRAGMENTED_MP4`. Otherwise, `containerFormat` may be set to `TS` or `FRAGMENTED_MP4`. Default: `TS`.
Type: String
Valid Values: `TS | FRAGMENTED_MP4`
Required: No

 ** [insecureIngest](#API_CreateChannel_RequestSyntax) **   <a name="ivs-CreateChannel-request-insecureIngest"></a>
Whether the channel allows insecure RTMP and SRT ingest. Default: `false`.
Type: Boolean
Required: No

 ** [latencyMode](#API_CreateChannel_RequestSyntax) **   <a name="ivs-CreateChannel-request-latencyMode"></a>
Channel latency mode. Use `NORMAL` to broadcast and deliver live video up to Full HD. Use `LOW` for near-real-time interaction with viewers. Default: `LOW`.
Type: String
Valid Values: `NORMAL | LOW`
Required: No

 ** [multitrackInputConfiguration](#API_CreateChannel_RequestSyntax) **   <a name="ivs-CreateChannel-request-multitrackInputConfiguration"></a>
Object specifying multitrack input configuration. Default: no multitrack input configuration is specified.
Type: [MultitrackInputConfiguration](API_MultitrackInputConfiguration.md) object
Required: No

 ** [name](#API_CreateChannel_RequestSyntax) **   <a name="ivs-CreateChannel-request-name"></a>
Channel name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** [playbackRestrictionPolicyArn](#API_CreateChannel_RequestSyntax) **   <a name="ivs-CreateChannel-request-playbackRestrictionPolicyArn"></a>
Playback-restriction-policy ARN. A valid ARN value here both specifies the ARN and enables playback restriction. Default: "" (empty string, no playback restriction policy is applied).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:playback-restriction-policy/[a-zA-Z0-9-]+$`
Required: No

 ** [preset](#API_CreateChannel_RequestSyntax) **   <a name="ivs-CreateChannel-request-preset"></a>
Optional transcode preset for the channel. This is selectable only for `ADVANCED_HD` and `ADVANCED_SD` channel types. For those channel types, the default `preset` is `HIGHER_BANDWIDTH_DELIVERY`. For other channel types (`BASIC` and `STANDARD`), `preset` is the empty string (`""`).
Type: String
Valid Values: `HIGHER_BANDWIDTH_DELIVERY | CONSTRAINED_BANDWIDTH_DELIVERY`
Required: No

 ** [recordingConfigurationArn](#API_CreateChannel_RequestSyntax) **   <a name="ivs-CreateChannel-request-recordingConfigurationArn"></a>
Recording-configuration ARN. A valid ARN value here both specifies the ARN and enables recording. Default: "" (empty string, recording is disabled).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$`
Required: No

 ** [tags](#API_CreateChannel_RequestSyntax) **   <a name="ivs-CreateChannel-request-tags"></a>
Array of 1-50 maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

 ** [type](#API_CreateChannel_RequestSyntax) **   <a name="ivs-CreateChannel-request-type"></a>
Channel type, which determines the allowable resolution and bitrate. *If you exceed the allowable input resolution or bitrate, the stream probably will disconnect immediately.* Default: `STANDARD`. For details, see [Channel Types](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/channel-types.html).
Type: String
Valid Values: `BASIC | STANDARD | ADVANCED_SD | ADVANCED_HD`
Required: No

## Response Syntax
<a name="API_CreateChannel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "channel": {
      "adConfigurationArn": "string",
      "arn": "string",
      "authorized": boolean,
      "containerFormat": "string",
      "ingestEndpoint": "string",
      "insecureIngest": boolean,
      "latencyMode": "string",
      "multitrackInputConfiguration": {
         "enabled": boolean,
         "maximumResolution": "string",
         "policy": "string"
      },
      "name": "string",
      "playbackRestrictionPolicyArn": "string",
      "playbackUrl": "string",
      "preset": "string",
      "recordingConfigurationArn": "string",
      "srt": {
         "endpoint": "string",
         "passphrase": "string"
      },
      "tags": {
         "string" : "string"
      },
      "type": "string"
   },
   "streamKey": {
      "arn": "string",
      "channelArn": "string",
      "tags": {
         "string" : "string"
      },
      "value": "string"
   }
}
```

## Response Elements
<a name="API_CreateChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [channel](#API_CreateChannel_ResponseSyntax) **   <a name="ivs-CreateChannel-response-channel"></a>

Type: [Channel](API_Channel.md) object

 ** [streamKey](#API_CreateChannel_ResponseSyntax) **   <a name="ivs-CreateChannel-response-streamKey"></a>

Type: [StreamKey](API_StreamKey.md) object

## Errors
<a name="API_CreateChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** PendingVerification **
Your account is pending verification.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/CreateChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/CreateChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/CreateChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/CreateChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/CreateChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/CreateChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/CreateChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/CreateChannel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/CreateChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/CreateChannel)
