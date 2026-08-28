---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PlaybackConfiguration.html
---

# PlaybackConfiguration
<a name="API_PlaybackConfiguration"></a>

A playback configuration. For information about MediaTailor configurations, see [Working with configurations in AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html).

## Contents
<a name="API_PlaybackConfiguration_Contents"></a>

 ** AdConditioningConfiguration **   <a name="mediatailor-Type-PlaybackConfiguration-AdConditioningConfiguration"></a>
The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns, and what priority MediaTailor uses when inserting ads.
Type: [AdConditioningConfiguration](API_AdConditioningConfiguration.md) object
Required: No

 ** AdDecisionServerConfiguration **   <a name="mediatailor-Type-PlaybackConfiguration-AdDecisionServerConfiguration"></a>
Configuration parameters for customizing HTTP requests sent to the ad decision server (ADS). This allows you to specify the HTTP method, headers, request body, and compression settings for ADS requests.
Type: [AdDecisionServerConfiguration](API_AdDecisionServerConfiguration.md) object
Required: No

 ** AdDecisionServerUrl **   <a name="mediatailor-Type-PlaybackConfiguration-AdDecisionServerUrl"></a>
The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.
Type: String
Required: No

 ** AdsPersonalizationConcurrency **   <a name="mediatailor-Type-PlaybackConfiguration-AdsPersonalizationConcurrency"></a>
The concurrency settings for ad decision server interactions. These settings control how many simultaneous ADS requests MediaTailor makes per manifest request.
Type: [AdsPersonalizationConcurrency](API_AdsPersonalizationConcurrency.md) object
Required: No

 ** AdsPersonalizationTimeouts **   <a name="mediatailor-Type-PlaybackConfiguration-AdsPersonalizationTimeouts"></a>
The timeout settings for ad decision server interactions. These settings control how long MediaTailor waits for ADS responses and the total time budget for ad personalization across live, VOD, and prefetch workflows.
Type: [AdsPersonalizationTimeouts](API_AdsPersonalizationTimeouts.md) object
Required: No

 ** AvailSuppression **   <a name="mediatailor-Type-PlaybackConfiguration-AvailSuppression"></a>
The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see [Ad Suppression](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).
Type: [AvailSuppression](API_AvailSuppression.md) object
Required: No

 ** Bumper **   <a name="mediatailor-Type-PlaybackConfiguration-Bumper"></a>
The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see [Bumpers](https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html).
Type: [Bumper](API_Bumper.md) object
Required: No

 ** CdnConfiguration **   <a name="mediatailor-Type-PlaybackConfiguration-CdnConfiguration"></a>
The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.
Type: [CdnConfiguration](API_CdnConfiguration.md) object
Required: No

 ** ConfigurationAliases **   <a name="mediatailor-Type-PlaybackConfiguration-ConfigurationAliases"></a>
The player parameters and aliases used as dynamic variables during session initialization. For more information, see [Domain Variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domains.html).
Type: String to string to string map map
Required: No

 ** DashConfiguration **   <a name="mediatailor-Type-PlaybackConfiguration-DashConfiguration"></a>
The configuration for a DASH source.
Type: [DashConfiguration](API_DashConfiguration.md) object
Required: No

 ** DualStackPlaybackEndpointPrefix **   <a name="mediatailor-Type-PlaybackConfiguration-DualStackPlaybackEndpointPrefix"></a>
The dual-stack (IPv4 and IPv6) URL that your player accesses to get a manifest from AWS Elemental MediaTailor.
Type: String
Required: No

 ** DualStackSessionInitializationEndpointPrefix **   <a name="mediatailor-Type-PlaybackConfiguration-DualStackSessionInitializationEndpointPrefix"></a>
The dual-stack (IPv4 and IPv6) URL that your player uses to initialize a session that uses client-side reporting.
Type: String
Required: No

 ** FunctionMapping **   <a name="mediatailor-Type-PlaybackConfiguration-FunctionMapping"></a>
A map of lifecycle hook event names to function identifiers. The function mapping specifies which function MediaTailor executes at each lifecycle hook during ad insertion. Valid keys are `PRE_SESSION_INITIALIZATION` and `PRE_ADS_REQUEST`. For more information, see [Functions lifecycle hooks](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-hooks.html) in the *MediaTailor User Guide*.
Type: String to string map
Valid Keys: `PRE_SESSION_INITIALIZATION | PRE_ADS_REQUEST`
Required: No

 ** HlsConfiguration **   <a name="mediatailor-Type-PlaybackConfiguration-HlsConfiguration"></a>
The configuration for HLS content.
Type: [HlsConfiguration](API_HlsConfiguration.md) object
Required: No

 ** InsertionMode **   <a name="mediatailor-Type-PlaybackConfiguration-InsertionMode"></a>
The setting that controls whether players can use stitched or guided ad insertion. The default, `STITCHED_ONLY`, forces all player sessions to use stitched (server-side) ad insertion. Choosing `PLAYER_SELECT` allows players to select either stitched or guided ad insertion at session-initialization time. The default for players that do not specify an insertion mode is stitched.
Type: String
Valid Values: `STITCHED_ONLY | PLAYER_SELECT`
Required: No

 ** LivePreRollConfiguration **   <a name="mediatailor-Type-PlaybackConfiguration-LivePreRollConfiguration"></a>
The configuration for pre-roll ad insertion.
Type: [LivePreRollConfiguration](API_LivePreRollConfiguration.md) object
Required: No

 ** LogConfiguration **   <a name="mediatailor-Type-PlaybackConfiguration-LogConfiguration"></a>
Defines where AWS Elemental MediaTailor sends logs for the playback configuration.
Type: [LogConfiguration](API_LogConfiguration.md) object
Required: No

 ** ManifestProcessingRules **   <a name="mediatailor-Type-PlaybackConfiguration-ManifestProcessingRules"></a>
The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.
Type: [ManifestProcessingRules](API_ManifestProcessingRules.md) object
Required: No

 ** Name **   <a name="mediatailor-Type-PlaybackConfiguration-Name"></a>
The identifier for the playback configuration.
Type: String
Required: No

 ** PersonalizationThresholdSeconds **   <a name="mediatailor-Type-PlaybackConfiguration-PersonalizationThresholdSeconds"></a>
Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to *ad replacement* in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see [Ad Behavior in AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** PlaybackConfigurationArn **   <a name="mediatailor-Type-PlaybackConfiguration-PlaybackConfigurationArn"></a>
The Amazon Resource Name (ARN) for the playback configuration.
Type: String
Required: No

 ** PlaybackEndpointPrefix **   <a name="mediatailor-Type-PlaybackConfiguration-PlaybackEndpointPrefix"></a>
The URL that your player accesses to get a manifest from AWS Elemental MediaTailor.
Type: String
Required: No

 ** SessionInitializationEndpointPrefix **   <a name="mediatailor-Type-PlaybackConfiguration-SessionInitializationEndpointPrefix"></a>
The URL that your player uses to initialize a session that uses client-side reporting.
Type: String
Required: No

 ** SlateAdUrl **   <a name="mediatailor-Type-PlaybackConfiguration-SlateAdUrl"></a>
The URL for a video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID playback configurations. For VPAID, the slate is required because MediaTailor provides it in the slots designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.
Type: String
Required: No

 ** tags **   <a name="mediatailor-Type-PlaybackConfiguration-tags"></a>
The tags to assign to the playback configuration. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map
Required: No

 ** TranscodeProfileName **   <a name="mediatailor-Type-PlaybackConfiguration-TranscodeProfileName"></a>
The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.
Type: String
Required: No

 ** VideoContentSourceUrl **   <a name="mediatailor-Type-PlaybackConfiguration-VideoContentSourceUrl"></a>
The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.
Type: String
Required: No

## See Also
<a name="API_PlaybackConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/PlaybackConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/PlaybackConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/PlaybackConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
