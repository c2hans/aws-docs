---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetDashManifestConfiguration.html
---

# GetDashManifestConfiguration
<a name="API_GetDashManifestConfiguration"></a>

Retrieve the DASH manifest configuration.

## Contents
<a name="API_GetDashManifestConfiguration_Contents"></a>

 ** ManifestName **   <a name="mediapackage-Type-GetDashManifestConfiguration-ManifestName"></a>
A short string that's appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default manifest name, index.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** Url **   <a name="mediapackage-Type-GetDashManifestConfiguration-Url"></a>
The egress domain URL for stream delivery from MediaPackage.
Type: String
Required: Yes

 ** AudioTimelinePattern **   <a name="mediapackage-Type-GetDashManifestConfiguration-AudioTimelinePattern"></a>
How MediaPackage represents the audio timeline in the DASH manifest, using DASH Segment Duration Patternization for audio adaptation sets. `PATTERNED` indicates that MediaPackage uses a pattern-based segment template for audio, reducing manifest size. `NONE` indicates that the manifest contains an explicit timeline for each audio segment.
Type: String
Valid Values: `NONE | PATTERNED`
Required: No

 ** AvailabilityStartTimeConfiguration **   <a name="mediapackage-Type-GetDashManifestConfiguration-AvailabilityStartTimeConfiguration"></a>
The configuration for the DASH `availabilityStartTime` attribute of the Media Presentation Description (MPD).
Type: [DashAvailabilityStartTimeConfiguration](API_DashAvailabilityStartTimeConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** BaseUrls **   <a name="mediapackage-Type-GetDashManifestConfiguration-BaseUrls"></a>
The base URL to use for retrieving segments.
Type: Array of [DashBaseUrl](API_DashBaseUrl.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** Compactness **   <a name="mediapackage-Type-GetDashManifestConfiguration-Compactness"></a>
The layout of the DASH manifest that MediaPackage produces. `STANDARD` indicates a default manifest, which is compacted. `NONE` indicates a full manifest.
Type: String
Valid Values: `STANDARD | NONE`
Required: No

 ** DrmSignaling **   <a name="mediapackage-Type-GetDashManifestConfiguration-DrmSignaling"></a>
Determines how the DASH manifest signals the DRM content.
Type: String
Valid Values: `INDIVIDUAL | REFERENCED`
Required: No

 ** DvbSettings **   <a name="mediapackage-Type-GetDashManifestConfiguration-DvbSettings"></a>
For endpoints that use the DVB-DASH profile only. The font download and error reporting information that you want MediaPackage to pass through to the manifest.
Type: [DashDvbSettings](API_DashDvbSettings.md) object
Required: No

 ** FilterConfiguration **   <a name="mediapackage-Type-GetDashManifestConfiguration-FilterConfiguration"></a>
Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.
Type: [FilterConfiguration](API_FilterConfiguration.md) object
Required: No

 ** ManifestWindowSeconds **   <a name="mediapackage-Type-GetDashManifestConfiguration-ManifestWindowSeconds"></a>
The total duration (in seconds) of the manifest's content.
Type: Integer
Required: No

 ** MinBufferTimeSeconds **   <a name="mediapackage-Type-GetDashManifestConfiguration-MinBufferTimeSeconds"></a>
Minimum amount of content (in seconds) that a player must keep available in the buffer.
Type: Integer
Required: No

 ** MinUpdatePeriodSeconds **   <a name="mediapackage-Type-GetDashManifestConfiguration-MinUpdatePeriodSeconds"></a>
Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest.
Type: Integer
Required: No

 ** PeriodTriggers **   <a name="mediapackage-Type-GetDashManifestConfiguration-PeriodTriggers"></a>
A list of triggers that controls when AWS Elemental MediaPackage separates the MPEG-DASH manifest into multiple periods. Leave this value empty to indicate that the manifest is contained all in one period. For more information about periods in the DASH manifest, see [Multi-period DASH in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/userguide/multi-period.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Valid Values: `AVAILS | DRM_KEY_ROTATION | SOURCE_CHANGES | SOURCE_DISRUPTIONS | NONE`
Required: No

 ** Profiles **   <a name="mediapackage-Type-GetDashManifestConfiguration-Profiles"></a>
The profile that the output is compliant with.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Valid Values: `DVB_DASH`
Required: No

 ** ProgramInformation **   <a name="mediapackage-Type-GetDashManifestConfiguration-ProgramInformation"></a>
Details about the content that you want MediaPackage to pass through in the manifest to the playback device.
Type: [DashProgramInformation](API_DashProgramInformation.md) object
Required: No

 ** ScteDash **   <a name="mediapackage-Type-GetDashManifestConfiguration-ScteDash"></a>
The SCTE configuration.
Type: [ScteDash](API_ScteDash.md) object
Required: No

 ** SegmentTemplateFormat **   <a name="mediapackage-Type-GetDashManifestConfiguration-SegmentTemplateFormat"></a>
Determines the type of variable used in the `media` URL of the `SegmentTemplate` tag in the manifest. Also specifies if segment timeline information is included in `SegmentTimeline` or `SegmentTemplate`.
Value description:
+  `NUMBER_WITH_TIMELINE` - The `$Number$` variable is used in the `media` URL. The value of this variable is the sequential number of the segment. A full `SegmentTimeline` object is presented in each `SegmentTemplate`.
Type: String
Valid Values: `NUMBER_WITH_TIMELINE`
Required: No

 ** SubtitleConfiguration **   <a name="mediapackage-Type-GetDashManifestConfiguration-SubtitleConfiguration"></a>
The configuration for DASH subtitles.
Type: [DashSubtitleConfiguration](API_DashSubtitleConfiguration.md) object
Required: No

 ** SuggestedPresentationDelaySeconds **   <a name="mediapackage-Type-GetDashManifestConfiguration-SuggestedPresentationDelaySeconds"></a>
The amount of time (in seconds) that the player should be from the end of the manifest.
Type: Integer
Required: No

 ** UriPathType **   <a name="mediapackage-Type-GetDashManifestConfiguration-UriPathType"></a>
The type of path used in manifest URIs. `LEAF` indicates leaf-relative paths. `ROOT` indicates root-relative paths that include the full path from root.
Type: String
Valid Values: `LEAF | ROOT`
Required: No

 ** UtcTiming **   <a name="mediapackage-Type-GetDashManifestConfiguration-UtcTiming"></a>
Determines the type of UTC timing included in the DASH Media Presentation Description (MPD).
Type: [DashUtcTiming](API_DashUtcTiming.md) object
Required: No

## See Also
<a name="API_GetDashManifestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/GetDashManifestConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/GetDashManifestConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/GetDashManifestConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
