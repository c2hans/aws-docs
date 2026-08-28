---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PutPlaybackConfiguration.html
---

# PutPlaybackConfiguration
<a name="API_PutPlaybackConfiguration"></a>

Creates a playback configuration. For information about MediaTailor configurations, see [Working with configurations in AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html).

## Request Syntax
<a name="API_PutPlaybackConfiguration_RequestSyntax"></a>

```
PUT /playbackConfiguration HTTP/1.1
Content-type: application/json

{
   "AdConditioningConfiguration": {
      "StreamingMediaFileConditioning": "{{string}}"
   },
   "AdDecisionServerConfiguration": {
      "HttpRequest": {
         "Body": "{{string}}",
         "CompressRequest": "{{string}}",
         "Headers": {
            "{{string}}" : "{{string}}"
         },
         "Method": "{{string}}"
      },
      "VastResponse": {
         "AdSequencingMode": "{{string}}"
      }
   },
   "AdDecisionServerUrl": "{{string}}",
   "AdsPersonalizationConcurrency": {
      "EnableVodVastParallelization": {{boolean}},
      "MaxConcurrentAdsRequests": {{number}}
   },
   "AdsPersonalizationTimeouts": {
      "AdsRequestTimeoutMilliseconds": {{number}},
      "LiveMaximumAdsPersonalizationTimeMilliseconds": {{number}},
      "PrefetchAdsRequestTimeoutMilliseconds": {{number}},
      "PrefetchMaximumAdsPersonalizationTimeMilliseconds": {{number}},
      "VodMaximumAdsPersonalizationTimeMilliseconds": {{number}}
   },
   "AvailSuppression": {
      "FillPolicy": "{{string}}",
      "Mode": "{{string}}",
      "Value": "{{string}}"
   },
   "Bumper": {
      "EndUrl": "{{string}}",
      "StartUrl": "{{string}}"
   },
   "CdnConfiguration": {
      "AdSegmentUrlPrefix": "{{string}}",
      "ContentSegmentUrlPrefix": "{{string}}"
   },
   "ConfigurationAliases": {
      "{{string}}" : {
         "{{string}}" : "{{string}}"
      }
   },
   "DashConfiguration": {
      "MpdLocation": "{{string}}",
      "OriginManifestType": "{{string}}"
   },
   "FunctionMapping": {
      "{{string}}" : "{{string}}"
   },
   "InsertionMode": "{{string}}",
   "LivePreRollConfiguration": {
      "AdDecisionServerConfiguration": {
         "VastResponse": {
            "AdSequencingMode": "{{string}}"
         }
      },
      "AdDecisionServerUrl": "{{string}}",
      "MaxDurationSeconds": {{number}}
   },
   "ManifestProcessingRules": {
      "AdMarkerPassthrough": {
         "Enabled": {{boolean}}
      }
   },
   "Name": "{{string}}",
   "PersonalizationThresholdSeconds": {{number}},
   "SlateAdUrl": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "TranscodeProfileName": "{{string}}",
   "VideoContentSourceUrl": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutPlaybackConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutPlaybackConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AdConditioningConfiguration](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-AdConditioningConfiguration"></a>
The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns, and what priority MediaTailor uses when inserting ads.
Type: [AdConditioningConfiguration](API_AdConditioningConfiguration.md) object
Required: No

 ** [AdDecisionServerConfiguration](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-AdDecisionServerConfiguration"></a>
The configuration for customizing HTTP requests to the ad decision server (ADS). This includes settings for request method, headers, body content, and compression options.
Type: [AdDecisionServerConfiguration](API_AdDecisionServerConfiguration.md) object
Required: No

 ** [AdDecisionServerUrl](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-AdDecisionServerUrl"></a>
The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.
Type: String
Required: No

 ** [AdsPersonalizationConcurrency](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-AdsPersonalizationConcurrency"></a>
The concurrency settings for ad decision server interactions. These settings control how many simultaneous ADS requests MediaTailor makes per manifest request.
Type: [AdsPersonalizationConcurrency](API_AdsPersonalizationConcurrency.md) object
Required: No

 ** [AdsPersonalizationTimeouts](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-AdsPersonalizationTimeouts"></a>
The timeout settings for ad decision server interactions. These settings control how long MediaTailor waits for ADS responses and the total time budget for ad personalization across live, VOD, and prefetch workflows.
Type: [AdsPersonalizationTimeouts](API_AdsPersonalizationTimeouts.md) object
Required: No

 ** [AvailSuppression](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-AvailSuppression"></a>
The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see [Ad Suppression](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).
Type: [AvailSuppression](API_AvailSuppression.md) object
Required: No

 ** [Bumper](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-Bumper"></a>
The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see [Bumpers](https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html).
Type: [Bumper](API_Bumper.md) object
Required: No

 ** [CdnConfiguration](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-CdnConfiguration"></a>
The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.
Type: [CdnConfiguration](API_CdnConfiguration.md) object
Required: No

 ** [ConfigurationAliases](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-ConfigurationAliases"></a>
The player parameters and aliases used as dynamic variables during session initialization. For more information, see [Domain Variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domains.html).
Type: String to string to string map map
Required: No

 ** [DashConfiguration](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-DashConfiguration"></a>
The configuration for DASH content.
Type: [DashConfigurationForPut](API_DashConfigurationForPut.md) object
Required: No

 ** [FunctionMapping](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-FunctionMapping"></a>
A map of lifecycle hook event names to function identifiers. The function mapping specifies which function MediaTailor executes at each lifecycle hook during ad insertion. Valid keys are `PRE_SESSION_INITIALIZATION` and `PRE_ADS_REQUEST`. For more information, see [Functions lifecycle hooks](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-hooks.html) in the *MediaTailor User Guide*.
Type: String to string map
Valid Keys: `PRE_SESSION_INITIALIZATION | PRE_ADS_REQUEST`
Required: No

 ** [InsertionMode](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-InsertionMode"></a>
The setting that controls whether players can use stitched or guided ad insertion. The default, `STITCHED_ONLY`, forces all player sessions to use stitched (server-side) ad insertion. Choosing `PLAYER_SELECT` allows players to select either stitched or guided ad insertion at session-initialization time. The default for players that do not specify an insertion mode is stitched.
Type: String
Valid Values: `STITCHED_ONLY | PLAYER_SELECT`
Required: No

 ** [LivePreRollConfiguration](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-LivePreRollConfiguration"></a>
The configuration for pre-roll ad insertion.
Type: [LivePreRollConfiguration](API_LivePreRollConfiguration.md) object
Required: No

 ** [ManifestProcessingRules](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-ManifestProcessingRules"></a>
The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.
Type: [ManifestProcessingRules](API_ManifestProcessingRules.md) object
Required: No

 ** [Name](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-Name"></a>
The identifier for the playback configuration.
Type: String
Required: Yes

 ** [PersonalizationThresholdSeconds](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-PersonalizationThresholdSeconds"></a>
Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to *ad replacement* in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see [Ad Behavior in AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [SlateAdUrl](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-SlateAdUrl"></a>
The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.
Type: String
Required: No

 ** [tags](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-tags"></a>
The tags to assign to the playback configuration. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map
Required: No

 ** [TranscodeProfileName](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-TranscodeProfileName"></a>
The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.
Type: String
Required: No

 ** [VideoContentSourceUrl](#API_PutPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-request-VideoContentSourceUrl"></a>
The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.
Type: String
Required: No

## Response Syntax
<a name="API_PutPlaybackConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AdConditioningConfiguration": {
      "StreamingMediaFileConditioning": "string"
   },
   "AdDecisionServerConfiguration": {
      "HttpRequest": {
         "Body": "string",
         "CompressRequest": "string",
         "Headers": {
            "string" : "string"
         },
         "Method": "string"
      },
      "VastResponse": {
         "AdSequencingMode": "string"
      }
   },
   "AdDecisionServerUrl": "string",
   "AdsPersonalizationConcurrency": {
      "EnableVodVastParallelization": boolean,
      "MaxConcurrentAdsRequests": number
   },
   "AdsPersonalizationTimeouts": {
      "AdsRequestTimeoutMilliseconds": number,
      "LiveMaximumAdsPersonalizationTimeMilliseconds": number,
      "PrefetchAdsRequestTimeoutMilliseconds": number,
      "PrefetchMaximumAdsPersonalizationTimeMilliseconds": number,
      "VodMaximumAdsPersonalizationTimeMilliseconds": number
   },
   "AvailSuppression": {
      "FillPolicy": "string",
      "Mode": "string",
      "Value": "string"
   },
   "Bumper": {
      "EndUrl": "string",
      "StartUrl": "string"
   },
   "CdnConfiguration": {
      "AdSegmentUrlPrefix": "string",
      "ContentSegmentUrlPrefix": "string"
   },
   "ConfigurationAliases": {
      "string" : {
         "string" : "string"
      }
   },
   "DashConfiguration": {
      "DualStackManifestEndpointPrefix": "string",
      "ManifestEndpointPrefix": "string",
      "MpdLocation": "string",
      "OriginManifestType": "string"
   },
   "DualStackPlaybackEndpointPrefix": "string",
   "DualStackSessionInitializationEndpointPrefix": "string",
   "FunctionMapping": {
      "string" : "string"
   },
   "HlsConfiguration": {
      "DualStackManifestEndpointPrefix": "string",
      "ManifestEndpointPrefix": "string"
   },
   "InsertionMode": "string",
   "LivePreRollConfiguration": {
      "AdDecisionServerConfiguration": {
         "VastResponse": {
            "AdSequencingMode": "string"
         }
      },
      "AdDecisionServerUrl": "string",
      "MaxDurationSeconds": number
   },
   "LogConfiguration": {
      "AdsInteractionLog": {
         "ExcludeEventTypes": [ "string" ],
         "PublishOptInEventTypes": [ "string" ]
      },
      "EnabledLoggingStrategies": [ "string" ],
      "ManifestServiceInteractionLog": {
         "ExcludeEventTypes": [ "string" ],
         "PublishOptInEventTypes": [ "string" ]
      },
      "PercentEnabled": number
   },
   "ManifestProcessingRules": {
      "AdMarkerPassthrough": {
         "Enabled": boolean
      }
   },
   "Name": "string",
   "PersonalizationThresholdSeconds": number,
   "PlaybackConfigurationArn": "string",
   "PlaybackEndpointPrefix": "string",
   "SessionInitializationEndpointPrefix": "string",
   "SlateAdUrl": "string",
   "tags": {
      "string" : "string"
   },
   "TranscodeProfileName": "string",
   "VideoContentSourceUrl": "string"
}
```

## Response Elements
<a name="API_PutPlaybackConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdConditioningConfiguration](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-AdConditioningConfiguration"></a>
The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns, and what priority MediaTailor uses when inserting ads.
Type: [AdConditioningConfiguration](API_AdConditioningConfiguration.md) object

 ** [AdDecisionServerConfiguration](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-AdDecisionServerConfiguration"></a>
The configuration for customizing HTTP requests to the ad decision server (ADS). This includes settings for request method, headers, body content, and compression options.
Type: [AdDecisionServerConfiguration](API_AdDecisionServerConfiguration.md) object

 ** [AdDecisionServerUrl](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-AdDecisionServerUrl"></a>
The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.
Type: String

 ** [AdsPersonalizationConcurrency](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-AdsPersonalizationConcurrency"></a>
The concurrency settings for ad decision server interactions. These settings control how many simultaneous ADS requests MediaTailor makes per manifest request.
Type: [AdsPersonalizationConcurrency](API_AdsPersonalizationConcurrency.md) object

 ** [AdsPersonalizationTimeouts](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-AdsPersonalizationTimeouts"></a>
The timeout settings for ad decision server interactions. These settings control how long MediaTailor waits for ADS responses and the total time budget for ad personalization across live, VOD, and prefetch workflows.
Type: [AdsPersonalizationTimeouts](API_AdsPersonalizationTimeouts.md) object

 ** [AvailSuppression](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-AvailSuppression"></a>
The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see [Ad Suppression](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).
Type: [AvailSuppression](API_AvailSuppression.md) object

 ** [Bumper](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-Bumper"></a>
The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see [Bumpers](https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html).
Type: [Bumper](API_Bumper.md) object

 ** [CdnConfiguration](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-CdnConfiguration"></a>
The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.
Type: [CdnConfiguration](API_CdnConfiguration.md) object

 ** [ConfigurationAliases](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-ConfigurationAliases"></a>
The player parameters and aliases used as dynamic variables during session initialization. For more information, see [Domain Variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domains.html).
Type: String to string to string map map

 ** [DashConfiguration](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-DashConfiguration"></a>
The configuration for DASH content.
Type: [DashConfiguration](API_DashConfiguration.md) object

 ** [DualStackPlaybackEndpointPrefix](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-DualStackPlaybackEndpointPrefix"></a>
The dual-stack (IPv4 and IPv6) playback endpoint prefix associated with the playback configuration.
Type: String

 ** [DualStackSessionInitializationEndpointPrefix](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-DualStackSessionInitializationEndpointPrefix"></a>
The dual-stack (IPv4 and IPv6) session initialization endpoint prefix associated with the playback configuration.
Type: String

 ** [FunctionMapping](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-FunctionMapping"></a>
A map of lifecycle hook event names to function identifiers. The function mapping specifies which function MediaTailor executes at each lifecycle hook during ad insertion. Valid keys are `PRE_SESSION_INITIALIZATION` and `PRE_ADS_REQUEST`. For more information, see [Functions lifecycle hooks](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-hooks.html) in the *MediaTailor User Guide*.
Type: String to string map
Valid Keys: `PRE_SESSION_INITIALIZATION | PRE_ADS_REQUEST`

 ** [HlsConfiguration](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-HlsConfiguration"></a>
The configuration for HLS content.
Type: [HlsConfiguration](API_HlsConfiguration.md) object

 ** [InsertionMode](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-InsertionMode"></a>
The setting that controls whether players can use stitched or guided ad insertion. The default, `STITCHED_ONLY`, forces all player sessions to use stitched (server-side) ad insertion. Choosing `PLAYER_SELECT` allows players to select either stitched or guided ad insertion at session-initialization time. The default for players that do not specify an insertion mode is stitched.
Type: String
Valid Values: `STITCHED_ONLY | PLAYER_SELECT`

 ** [LivePreRollConfiguration](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-LivePreRollConfiguration"></a>
The configuration for pre-roll ad insertion.
Type: [LivePreRollConfiguration](API_LivePreRollConfiguration.md) object

 ** [LogConfiguration](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-LogConfiguration"></a>
The configuration that defines where AWS Elemental MediaTailor sends logs for the playback configuration.
Type: [LogConfiguration](API_LogConfiguration.md) object

 ** [ManifestProcessingRules](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-ManifestProcessingRules"></a>
The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.
Type: [ManifestProcessingRules](API_ManifestProcessingRules.md) object

 ** [Name](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-Name"></a>
The identifier for the playback configuration.
Type: String

 ** [PersonalizationThresholdSeconds](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-PersonalizationThresholdSeconds"></a>
Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to *ad replacement* in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see [Ad Behavior in AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).
Type: Integer
Valid Range: Minimum value of 1.

 ** [PlaybackConfigurationArn](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-PlaybackConfigurationArn"></a>
The Amazon Resource Name (ARN) associated with the playback configuration.
Type: String

 ** [PlaybackEndpointPrefix](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-PlaybackEndpointPrefix"></a>
The playback endpoint prefix associated with the playback configuration.
Type: String

 ** [SessionInitializationEndpointPrefix](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-SessionInitializationEndpointPrefix"></a>
The session initialization endpoint prefix associated with the playback configuration.
Type: String

 ** [SlateAdUrl](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-SlateAdUrl"></a>
The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.
Type: String

 ** [tags](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-tags"></a>
The tags to assign to the playback configuration. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

 ** [TranscodeProfileName](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-TranscodeProfileName"></a>
The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.
Type: String

 ** [VideoContentSourceUrl](#API_PutPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-PutPlaybackConfiguration-response-VideoContentSourceUrl"></a>
The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.
Type: String

## Errors
<a name="API_PutPlaybackConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_PutPlaybackConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/PutPlaybackConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/PutPlaybackConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/PutPlaybackConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/PutPlaybackConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/PutPlaybackConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/PutPlaybackConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/PutPlaybackConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/PutPlaybackConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/PutPlaybackConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/PutPlaybackConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
