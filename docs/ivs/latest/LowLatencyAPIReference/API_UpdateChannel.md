---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_UpdateChannel.html
---

# UpdateChannel
<a name="API_UpdateChannel"></a>

Updates a channel's configuration. Live channels cannot be updated. You must stop the ongoing stream, update the channel, and restart the stream for the changes to take effect.

## Request Syntax
<a name="API_UpdateChannel_RequestSyntax"></a>

```
POST /UpdateChannel HTTP/1.1
Content-type: application/json

{
   "adConfigurationArn": "{{string}}",
   "arn": "{{string}}",
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
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateChannel_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateChannel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [adConfigurationArn](#API_UpdateChannel_RequestSyntax) **   <a name="ivs-UpdateChannel-request-adConfigurationArn"></a>
ARN of the ad configuration associated with the channel.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:ad-configuration/[a-zA-Z0-9-]+$`
Required: No

 ** [arn](#API_UpdateChannel_RequestSyntax) **   <a name="ivs-UpdateChannel-request-arn"></a>
ARN of the channel to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: Yes

 ** [authorized](#API_UpdateChannel_RequestSyntax) **   <a name="ivs-UpdateChannel-request-authorized"></a>
Whether the channel is private (enabled for playback authorization).
Type: Boolean
Required: No

 ** [containerFormat](#API_UpdateChannel_RequestSyntax) **   <a name="ivs-UpdateChannel-request-containerFormat"></a>
Indicates which content-packaging format is used (MPEG-TS or fMP4). If `multitrackInputConfiguration` is specified and `enabled` is `true`, then `containerFormat` is required and must be set to `FRAGMENTED_MP4`. Otherwise, `containerFormat` may be set to `TS` or `FRAGMENTED_MP4`. Default: `TS`.
Type: String
Valid Values: `TS | FRAGMENTED_MP4`
Required: No

 ** [insecureIngest](#API_UpdateChannel_RequestSyntax) **   <a name="ivs-UpdateChannel-request-insecureIngest"></a>
Whether the channel allows insecure RTMP and SRT ingest. Default: `false`.
Type: Boolean
Required: No

 ** [latencyMode](#API_UpdateChannel_RequestSyntax) **   <a name="ivs-UpdateChannel-request-latencyMode"></a>
Channel latency mode. Use `NORMAL` to broadcast and deliver live video up to Full HD. Use `LOW` for near-real-time interaction with viewers.
Type: String
Valid Values: `NORMAL | LOW`
Required: No

 ** [multitrackInputConfiguration](#API_UpdateChannel_RequestSyntax) **   <a name="ivs-UpdateChannel-request-multitrackInputConfiguration"></a>
Object specifying multitrack input configuration. Default: no multitrack input configuration is specified.
Type: [MultitrackInputConfiguration](API_MultitrackInputConfiguration.md) object
Required: No

 ** [name](#API_UpdateChannel_RequestSyntax) **   <a name="ivs-UpdateChannel-request-name"></a>
Channel name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** [playbackRestrictionPolicyArn](#API_UpdateChannel_RequestSyntax) **   <a name="ivs-UpdateChannel-request-playbackRestrictionPolicyArn"></a>
Playback-restriction-policy ARN. A valid ARN value here both specifies the ARN and enables playback restriction. If this is set to an empty string, playback restriction policy is disabled.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:playback-restriction-policy/[a-zA-Z0-9-]+$`
Required: No

 ** [preset](#API_UpdateChannel_RequestSyntax) **   <a name="ivs-UpdateChannel-request-preset"></a>
Optional transcode preset for the channel. This is selectable only for `ADVANCED_HD` and `ADVANCED_SD` channel types. For those channel types, the default `preset` is `HIGHER_BANDWIDTH_DELIVERY`. For other channel types (`BASIC` and `STANDARD`), `preset` is the empty string (`""`).
Type: String
Valid Values: `HIGHER_BANDWIDTH_DELIVERY | CONSTRAINED_BANDWIDTH_DELIVERY`
Required: No

 ** [recordingConfigurationArn](#API_UpdateChannel_RequestSyntax) **   <a name="ivs-UpdateChannel-request-recordingConfigurationArn"></a>
Recording-configuration ARN. A valid ARN value here both specifies the ARN and enables recording. If this is set to an empty string, recording is disabled.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$`
Required: No

 ** [type](#API_UpdateChannel_RequestSyntax) **   <a name="ivs-UpdateChannel-request-type"></a>
Channel type, which determines the allowable resolution and bitrate. *If you exceed the allowable input resolution or bitrate, the stream probably will disconnect immediately.* Default: `STANDARD`. For details, see [Channel Types](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/channel-types.html).
Type: String
Valid Values: `BASIC | STANDARD | ADVANCED_SD | ADVANCED_HD`
Required: No

## Response Syntax
<a name="API_UpdateChannel_ResponseSyntax"></a>

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
   }
}
```

## Response Elements
<a name="API_UpdateChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [channel](#API_UpdateChannel_ResponseSyntax) **   <a name="ivs-UpdateChannel-response-channel"></a>
Object specifying the updated channel.
Type: [Channel](API_Channel.md) object

## Errors
<a name="API_UpdateChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** PendingVerification **
Your account is pending verification.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/UpdateChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/UpdateChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/UpdateChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/UpdateChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/UpdateChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/UpdateChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/UpdateChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/UpdateChannel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/UpdateChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/UpdateChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
