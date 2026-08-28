---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint DashManifestConfiguration
<a name="aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration"></a>

The DASH manifest configuration associated with the origin endpoint.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration-syntax.json"></a>

```
{
  "[AudioTimelinePattern](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-audiotimelinepattern)" : {{String}},
  "[AvailabilityStartTimeConfiguration](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-availabilitystarttimeconfiguration)" : {{DashAvailabilityStartTimeConfiguration}},
  "[BaseUrls](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-baseurls)" : {{[ DashBaseUrl, ... ]}},
  "[Compactness](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-compactness)" : {{String}},
  "[DrmSignaling](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-drmsignaling)" : {{String}},
  "[DvbSettings](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-dvbsettings)" : {{DashDvbSettings}},
  "[FilterConfiguration](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-filterconfiguration)" : {{FilterConfiguration}},
  "[ManifestName](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-manifestname)" : {{String}},
  "[ManifestWindowSeconds](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-manifestwindowseconds)" : {{Integer}},
  "[MinBufferTimeSeconds](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-minbuffertimeseconds)" : {{Integer}},
  "[MinUpdatePeriodSeconds](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-minupdateperiodseconds)" : {{Integer}},
  "[PeriodTriggers](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-periodtriggers)" : {{[ String, ... ]}},
  "[Profiles](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-profiles)" : {{[ String, ... ]}},
  "[ProgramInformation](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-programinformation)" : {{DashProgramInformation}},
  "[ScteDash](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-sctedash)" : {{ScteDash}},
  "[SegmentTemplateFormat](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-segmenttemplateformat)" : {{String}},
  "[SubtitleConfiguration](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-subtitleconfiguration)" : {{DashSubtitleConfiguration}},
  "[SuggestedPresentationDelaySeconds](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-suggestedpresentationdelayseconds)" : {{Integer}},
  "[UriPathType](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-uripathtype)" : {{String}},
  "[UtcTiming](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-utctiming)" : {{DashUtcTiming}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration-syntax.yaml"></a>

```
  [AudioTimelinePattern](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-audiotimelinepattern): {{String}}
  [AvailabilityStartTimeConfiguration](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-availabilitystarttimeconfiguration): {{
    DashAvailabilityStartTimeConfiguration}}
  [BaseUrls](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-baseurls): {{
    - DashBaseUrl}}
  [Compactness](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-compactness): {{String}}
  [DrmSignaling](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-drmsignaling): {{String}}
  [DvbSettings](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-dvbsettings): {{
    DashDvbSettings}}
  [FilterConfiguration](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-filterconfiguration): {{
    FilterConfiguration}}
  [ManifestName](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-manifestname): {{String}}
  [ManifestWindowSeconds](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-manifestwindowseconds): {{Integer}}
  [MinBufferTimeSeconds](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-minbuffertimeseconds): {{Integer}}
  [MinUpdatePeriodSeconds](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-minupdateperiodseconds): {{Integer}}
  [PeriodTriggers](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-periodtriggers): {{
    - String}}
  [Profiles](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-profiles): {{
    - String}}
  [ProgramInformation](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-programinformation): {{
    DashProgramInformation}}
  [ScteDash](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-sctedash): {{
    ScteDash}}
  [SegmentTemplateFormat](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-segmenttemplateformat): {{String}}
  [SubtitleConfiguration](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-subtitleconfiguration): {{
    DashSubtitleConfiguration}}
  [SuggestedPresentationDelaySeconds](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-suggestedpresentationdelayseconds): {{Integer}}
  [UriPathType](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-uripathtype): {{String}}
  [UtcTiming](#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-utctiming): {{
    DashUtcTiming}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration-properties"></a>

`AudioTimelinePattern`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-audiotimelinepattern"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `NONE | PATTERNED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AvailabilityStartTimeConfiguration`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-availabilitystarttimeconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [DashAvailabilityStartTimeConfiguration](aws-properties-mediapackagev2-originendpoint-dashavailabilitystarttimeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BaseUrls`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-baseurls"></a>
The base URLs to use for retrieving segments.
*Required*: No
*Type*: Array of [DashBaseUrl](aws-properties-mediapackagev2-originendpoint-dashbaseurl.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Compactness`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-compactness"></a>
The layout of the DASH manifest that MediaPackage produces. `STANDARD` indicates a default manifest, which is compacted. `NONE` indicates a full manifest.
For information about compactness, see [DASH manifest compactness](https://docs.aws.amazon.com/mediapackage/latest/userguide/compacted.html) in the *AWS Elemental MediaPackage v2 User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `STANDARD | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DrmSignaling`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-drmsignaling"></a>
Determines how the DASH manifest signals the DRM content.
*Required*: No
*Type*: String
*Allowed values*: `INDIVIDUAL | REFERENCED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DvbSettings`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-dvbsettings"></a>
For endpoints that use the DVB-DASH profile only. The font download and error reporting information that you want MediaPackage to pass through to the manifest.
*Required*: No
*Type*: [DashDvbSettings](aws-properties-mediapackagev2-originendpoint-dashdvbsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterConfiguration`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-filterconfiguration"></a>
Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.
*Required*: No
*Type*: [FilterConfiguration](aws-properties-mediapackagev2-originendpoint-filterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestName`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-manifestname"></a>
A short string that's appended to the endpoint URL. The child manifest name creates a unique path to this endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestWindowSeconds`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-manifestwindowseconds"></a>
The total duration (in seconds) of the manifest's content.
*Required*: No
*Type*: Integer
*Minimum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinBufferTimeSeconds`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-minbuffertimeseconds"></a>
Minimum amount of content (in seconds) that a player must keep available in the buffer.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinUpdatePeriodSeconds`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-minupdateperiodseconds"></a>
Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PeriodTriggers`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-periodtriggers"></a>
A list of triggers that controls when AWS Elemental MediaPackage separates the MPEG-DASH manifest into multiple periods. Type `ADS` to indicate that AWS Elemental MediaPackage must create periods in the output manifest that correspond to SCTE-35 ad markers in the input source. Leave this value empty to indicate that the manifest is contained all in one period. For more information about periods in the DASH manifest, see [Multi-period DASH in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/userguide/multi-period.html).
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Profiles`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-profiles"></a>
The profile that the output is compliant with.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProgramInformation`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-programinformation"></a>
Details about the content that you want MediaPackage to pass through in the manifest to the playback device.
*Required*: No
*Type*: [DashProgramInformation](aws-properties-mediapackagev2-originendpoint-dashprograminformation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScteDash`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-sctedash"></a>
The SCTE configuration.
*Required*: No
*Type*: [ScteDash](aws-properties-mediapackagev2-originendpoint-sctedash.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentTemplateFormat`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-segmenttemplateformat"></a>
Determines the type of variable used in the `media` URL of the `SegmentTemplate` tag in the manifest. Also specifies if segment timeline information is included in `SegmentTimeline` or `SegmentTemplate`.
Value description:
+ `NUMBER_WITH_TIMELINE` - The `$Number$` variable is used in the `media` URL. The value of this variable is the sequential number of the segment. A full `SegmentTimeline` object is presented in each `SegmentTemplate`.
*Required*: No
*Type*: String
*Allowed values*: `NUMBER_WITH_TIMELINE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubtitleConfiguration`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-subtitleconfiguration"></a>
The configuration for DASH subtitles.
*Required*: No
*Type*: [DashSubtitleConfiguration](aws-properties-mediapackagev2-originendpoint-dashsubtitleconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuggestedPresentationDelaySeconds`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-suggestedpresentationdelayseconds"></a>
The amount of time (in seconds) that the player should be from the end of the manifest.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UriPathType`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-uripathtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `LEAF | ROOT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UtcTiming`  <a name="cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-utctiming"></a>
Determines the type of UTC timing included in the DASH Media Presentation Description (MPD).
*Required*: No
*Type*: [DashUtcTiming](aws-properties-mediapackagev2-originendpoint-dashutctiming.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
