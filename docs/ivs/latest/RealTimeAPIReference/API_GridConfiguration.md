---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GridConfiguration.html
---

# GridConfiguration
<a name="API_GridConfiguration"></a>

Configuration information specific to Grid layout, for server-side composition. See "Layouts" in [Server-Side Composition](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/server-side-composition.html).

## Contents
<a name="API_GridConfiguration_Contents"></a>

 ** featuredParticipantAttribute **   <a name="ivsrealtimeeapireference-Type-GridConfiguration-featuredParticipantAttribute"></a>
This attribute name identifies the featured slot. A participant with this attribute set to `"true"` (as a string value) in [ParticipantTokenConfiguration](API_ParticipantTokenConfiguration.md) is placed in the featured slot. Default: `""` (no featured participant).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** gridGap **   <a name="ivsrealtimeeapireference-Type-GridConfiguration-gridGap"></a>
Specifies the spacing between participant tiles in pixels. Default: `2`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** omitStoppedVideo **   <a name="ivsrealtimeeapireference-Type-GridConfiguration-omitStoppedVideo"></a>
Determines whether to omit participants with stopped video in the composition. Default: `false`.
Type: Boolean
Required: No

 ** participantOrderAttribute **   <a name="ivsrealtimeeapireference-Type-GridConfiguration-participantOrderAttribute"></a>
Attribute name in [ParticipantTokenConfiguration](API_ParticipantTokenConfiguration.md) identifying the participant ordering key. Participants with `participantOrderAttribute` set to `""` or not specified are ordered based on their arrival time into the stage.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** videoAspectRatio **   <a name="ivsrealtimeeapireference-Type-GridConfiguration-videoAspectRatio"></a>
Sets the non-featured participant display mode, to control the aspect ratio of video tiles. `VIDEO` is 16:9, `SQUARE` is 1:1, and `PORTRAIT` is 3:4. Default: `VIDEO`.
Type: String
Valid Values: `AUTO | VIDEO | SQUARE | PORTRAIT`
Required: No

 ** videoFillMode **   <a name="ivsrealtimeeapireference-Type-GridConfiguration-videoFillMode"></a>
Defines how video content fits within the participant tile: `FILL` (stretched), `COVER` (cropped), or `CONTAIN` (letterboxed). When not set, `videoFillMode` defaults to `COVER` fill mode for participants in the grid and to `CONTAIN` fill mode for featured participants.
Type: String
Valid Values: `FILL | COVER | CONTAIN`
Required: No

## See Also
<a name="API_GridConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/GridConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/GridConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/GridConfiguration)
