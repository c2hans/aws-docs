---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediatailor-playbackconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration
<a name="aws-resource-mediatailor-playbackconfiguration"></a>

Adds a new playback configuration to AWS Elemental MediaTailor.

## Syntax
<a name="aws-resource-mediatailor-playbackconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediatailor-playbackconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::MediaTailor::PlaybackConfiguration",
  "Properties" : {
      "[AdConditioningConfiguration](#cfn-mediatailor-playbackconfiguration-adconditioningconfiguration)" : {{AdConditioningConfiguration}},
      "[AdDecisionServerConfiguration](#cfn-mediatailor-playbackconfiguration-addecisionserverconfiguration)" : {{AdDecisionServerConfiguration}},
      "[AdDecisionServerUrl](#cfn-mediatailor-playbackconfiguration-addecisionserverurl)" : {{String}},
      "[AdsPersonalizationConcurrency](#cfn-mediatailor-playbackconfiguration-adspersonalizationconcurrency)" : {{AdsPersonalizationConcurrency}},
      "[AdsPersonalizationTimeouts](#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts)" : {{AdsPersonalizationTimeouts}},
      "[AvailSuppression](#cfn-mediatailor-playbackconfiguration-availsuppression)" : {{AvailSuppression}},
      "[Bumper](#cfn-mediatailor-playbackconfiguration-bumper)" : {{Bumper}},
      "[CdnConfiguration](#cfn-mediatailor-playbackconfiguration-cdnconfiguration)" : {{CdnConfiguration}},
      "[ConfigurationAliases](#cfn-mediatailor-playbackconfiguration-configurationaliases)" : {{{{{Key}}: {{Value}}, ...}}},
      "[DashConfiguration](#cfn-mediatailor-playbackconfiguration-dashconfiguration)" : {{DashConfiguration}},
      "[FunctionMapping](#cfn-mediatailor-playbackconfiguration-functionmapping)" : {{{{{Key}}: {{Value}}, ...}}},
      "[HlsConfiguration](#cfn-mediatailor-playbackconfiguration-hlsconfiguration)" : {{HlsConfiguration}},
      "[InsertionMode](#cfn-mediatailor-playbackconfiguration-insertionmode)" : {{String}},
      "[LivePreRollConfiguration](#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration)" : {{LivePreRollConfiguration}},
      "[LogConfiguration](#cfn-mediatailor-playbackconfiguration-logconfiguration)" : {{LogConfiguration}},
      "[ManifestProcessingRules](#cfn-mediatailor-playbackconfiguration-manifestprocessingrules)" : {{ManifestProcessingRules}},
      "[Name](#cfn-mediatailor-playbackconfiguration-name)" : {{String}},
      "[PersonalizationThresholdSeconds](#cfn-mediatailor-playbackconfiguration-personalizationthresholdseconds)" : {{Integer}},
      "[SlateAdUrl](#cfn-mediatailor-playbackconfiguration-slateadurl)" : {{String}},
      "[Tags](#cfn-mediatailor-playbackconfiguration-tags)" : {{[ Tag, ... ]}},
      "[TranscodeProfileName](#cfn-mediatailor-playbackconfiguration-transcodeprofilename)" : {{String}},
      "[VideoContentSourceUrl](#cfn-mediatailor-playbackconfiguration-videocontentsourceurl)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-mediatailor-playbackconfiguration-syntax.yaml"></a>

```
Type: AWS::MediaTailor::PlaybackConfiguration
Properties:
  [AdConditioningConfiguration](#cfn-mediatailor-playbackconfiguration-adconditioningconfiguration): {{
    AdConditioningConfiguration}}
  [AdDecisionServerConfiguration](#cfn-mediatailor-playbackconfiguration-addecisionserverconfiguration): {{
    AdDecisionServerConfiguration}}
  [AdDecisionServerUrl](#cfn-mediatailor-playbackconfiguration-addecisionserverurl): {{String}}
  [AdsPersonalizationConcurrency](#cfn-mediatailor-playbackconfiguration-adspersonalizationconcurrency): {{
    AdsPersonalizationConcurrency}}
  [AdsPersonalizationTimeouts](#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts): {{
    AdsPersonalizationTimeouts}}
  [AvailSuppression](#cfn-mediatailor-playbackconfiguration-availsuppression): {{
    AvailSuppression}}
  [Bumper](#cfn-mediatailor-playbackconfiguration-bumper): {{
    Bumper}}
  [CdnConfiguration](#cfn-mediatailor-playbackconfiguration-cdnconfiguration): {{
    CdnConfiguration}}
  [ConfigurationAliases](#cfn-mediatailor-playbackconfiguration-configurationaliases): {{
    {{Key}}: {{Value}}}}
  [DashConfiguration](#cfn-mediatailor-playbackconfiguration-dashconfiguration): {{
    DashConfiguration}}
  [FunctionMapping](#cfn-mediatailor-playbackconfiguration-functionmapping): {{
    {{Key}}: {{Value}}}}
  [HlsConfiguration](#cfn-mediatailor-playbackconfiguration-hlsconfiguration): {{
    HlsConfiguration}}
  [InsertionMode](#cfn-mediatailor-playbackconfiguration-insertionmode): {{String}}
  [LivePreRollConfiguration](#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration): {{
    LivePreRollConfiguration}}
  [LogConfiguration](#cfn-mediatailor-playbackconfiguration-logconfiguration): {{
    LogConfiguration}}
  [ManifestProcessingRules](#cfn-mediatailor-playbackconfiguration-manifestprocessingrules): {{
    ManifestProcessingRules}}
  [Name](#cfn-mediatailor-playbackconfiguration-name): {{String}}
  [PersonalizationThresholdSeconds](#cfn-mediatailor-playbackconfiguration-personalizationthresholdseconds): {{Integer}}
  [SlateAdUrl](#cfn-mediatailor-playbackconfiguration-slateadurl): {{String}}
  [Tags](#cfn-mediatailor-playbackconfiguration-tags): {{
    - Tag}}
  [TranscodeProfileName](#cfn-mediatailor-playbackconfiguration-transcodeprofilename): {{String}}
  [VideoContentSourceUrl](#cfn-mediatailor-playbackconfiguration-videocontentsourceurl): {{String}}
```

## Properties
<a name="aws-resource-mediatailor-playbackconfiguration-properties"></a>

`AdConditioningConfiguration`  <a name="cfn-mediatailor-playbackconfiguration-adconditioningconfiguration"></a>
The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns, and what priority MediaTailor uses when inserting ads.
*Required*: No
*Type*: [AdConditioningConfiguration](aws-properties-mediatailor-playbackconfiguration-adconditioningconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdDecisionServerConfiguration`  <a name="cfn-mediatailor-playbackconfiguration-addecisionserverconfiguration"></a>
Configuration parameters for customizing HTTP requests sent to the ad decision server (ADS). This allows you to specify the HTTP method, headers, request body, and compression settings for ADS requests.
*Required*: No
*Type*: [AdDecisionServerConfiguration](aws-properties-mediatailor-playbackconfiguration-addecisionserverconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdDecisionServerUrl`  <a name="cfn-mediatailor-playbackconfiguration-addecisionserverurl"></a>
The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdsPersonalizationConcurrency`  <a name="cfn-mediatailor-playbackconfiguration-adspersonalizationconcurrency"></a>
The concurrency settings for ad decision server interactions. These settings control how many simultaneous ADS requests MediaTailor makes per manifest request.
*Required*: No
*Type*: [AdsPersonalizationConcurrency](aws-properties-mediatailor-playbackconfiguration-adspersonalizationconcurrency.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdsPersonalizationTimeouts`  <a name="cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts"></a>
The timeout settings for ad decision server interactions. These settings control how long MediaTailor waits for ADS responses and the total time budget for ad personalization across live, VOD, and prefetch workflows.
*Required*: No
*Type*: [AdsPersonalizationTimeouts](aws-properties-mediatailor-playbackconfiguration-adspersonalizationtimeouts.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AvailSuppression`  <a name="cfn-mediatailor-playbackconfiguration-availsuppression"></a>
The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see [Ad Suppression](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).
*Required*: No
*Type*: [AvailSuppression](aws-properties-mediatailor-playbackconfiguration-availsuppression.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Bumper`  <a name="cfn-mediatailor-playbackconfiguration-bumper"></a>
The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see [Bumpers](https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html).
*Required*: No
*Type*: [Bumper](aws-properties-mediatailor-playbackconfiguration-bumper.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CdnConfiguration`  <a name="cfn-mediatailor-playbackconfiguration-cdnconfiguration"></a>
The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.
*Required*: No
*Type*: [CdnConfiguration](aws-properties-mediatailor-playbackconfiguration-cdnconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigurationAliases`  <a name="cfn-mediatailor-playbackconfiguration-configurationaliases"></a>
The player parameters and aliases used as dynamic variables during session initialization. For more information, see [Domain Variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domain.html).
*Required*: No
*Type*: Object
*Pattern*: `player_params\.\w+\Z`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DashConfiguration`  <a name="cfn-mediatailor-playbackconfiguration-dashconfiguration"></a>
The configuration for a DASH source.
*Required*: No
*Type*: [DashConfiguration](aws-properties-mediatailor-playbackconfiguration-dashconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionMapping`  <a name="cfn-mediatailor-playbackconfiguration-functionmapping"></a>
A map of lifecycle hook event names to function identifiers. The function mapping specifies which function MediaTailor executes at each lifecycle hook during ad insertion. Valid keys are `PRE_SESSION_INITIALIZATION` and `PRE_ADS_REQUEST`. For more information, see [Functions lifecycle hooks](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-hooks.html) in the *MediaTailor User Guide*.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HlsConfiguration`  <a name="cfn-mediatailor-playbackconfiguration-hlsconfiguration"></a>
The configuration for HLS content.
*Required*: No
*Type*: [HlsConfiguration](aws-properties-mediatailor-playbackconfiguration-hlsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InsertionMode`  <a name="cfn-mediatailor-playbackconfiguration-insertionmode"></a>
The setting that controls whether players can use stitched or guided ad insertion. The default, `STITCHED_ONLY`, forces all player sessions to use stitched (server-side) ad insertion. Choosing `PLAYER_SELECT` allows players to select either stitched or guided ad insertion at session-initialization time. The default for players that do not specify an insertion mode is stitched.
*Required*: No
*Type*: String
*Allowed values*: `STITCHED_ONLY | PLAYER_SELECT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LivePreRollConfiguration`  <a name="cfn-mediatailor-playbackconfiguration-liveprerollconfiguration"></a>
The configuration for pre-roll ad insertion.
*Required*: No
*Type*: [LivePreRollConfiguration](aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogConfiguration`  <a name="cfn-mediatailor-playbackconfiguration-logconfiguration"></a>
Defines where AWS Elemental MediaTailor sends logs for the playback configuration.
*Required*: No
*Type*: [LogConfiguration](aws-properties-mediatailor-playbackconfiguration-logconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestProcessingRules`  <a name="cfn-mediatailor-playbackconfiguration-manifestprocessingrules"></a>
The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.
*Required*: No
*Type*: [ManifestProcessingRules](aws-properties-mediatailor-playbackconfiguration-manifestprocessingrules.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-mediatailor-playbackconfiguration-name"></a>
The identifier for the playback configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PersonalizationThresholdSeconds`  <a name="cfn-mediatailor-playbackconfiguration-personalizationthresholdseconds"></a>
Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to *ad replacement* in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see [Ad Behavior in AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlateAdUrl`  <a name="cfn-mediatailor-playbackconfiguration-slateadurl"></a>
The URL for a video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID playback configurations. For VPAID, the slate is required because MediaTailor provides it in the slots designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-mediatailor-playbackconfiguration-tags"></a>
The tags to assign to the playback configuration. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-mediatailor-playbackconfiguration-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TranscodeProfileName`  <a name="cfn-mediatailor-playbackconfiguration-transcodeprofilename"></a>
The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VideoContentSourceUrl`  <a name="cfn-mediatailor-playbackconfiguration-videocontentsourceurl"></a>
The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediatailor-playbackconfiguration-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-mediatailor-playbackconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-mediatailor-playbackconfiguration-return-values-fn--getatt-fn--getatt"></a>

`DashConfiguration.ManifestEndpointPrefix`  <a name="DashConfiguration.ManifestEndpointPrefix-fn::getatt"></a>
The URL generated by MediaTailor to initiate a playback session. The session uses server-side reporting. This setting is ignored in PUT operations.

`HlsConfiguration.ManifestEndpointPrefix`  <a name="HlsConfiguration.ManifestEndpointPrefix-fn::getatt"></a>
The URL that is used to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.

`PlaybackConfigurationArn`  <a name="PlaybackConfigurationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the playback configuration.

`PlaybackEndpointPrefix`  <a name="PlaybackEndpointPrefix-fn::getatt"></a>
The URL that the player accesses to get a manifest from MediaTailor. This session will use server-side reporting.

`SessionInitializationEndpointPrefix`  <a name="SessionInitializationEndpointPrefix-fn::getatt"></a>
The URL that the player uses to initialize a session that uses client-side reporting.
