---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_PipConfiguration.html
---

# PipConfiguration
<a name="API_PipConfiguration"></a>

Configuration information specific to Picture-in-Picture (PiP) layout, for [server-side composition](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/server-side-composition.html).

## Contents
<a name="API_PipConfiguration_Contents"></a>

 ** featuredParticipantAttribute **   <a name="ivsrealtimeeapireference-Type-PipConfiguration-featuredParticipantAttribute"></a>
This attribute name identifies the featured slot. A participant with this attribute set to `"true"` (as a string value) in [ParticipantTokenConfiguration](API_ParticipantTokenConfiguration.md) is placed in the featured slot. Default: `""` (no featured participant).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** gridGap **   <a name="ivsrealtimeeapireference-Type-PipConfiguration-gridGap"></a>
Specifies the spacing between participant tiles in pixels. Default: `0`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** omitStoppedVideo **   <a name="ivsrealtimeeapireference-Type-PipConfiguration-omitStoppedVideo"></a>
Determines whether to omit participants with stopped video in the composition. Default: `false`.
Type: Boolean
Required: No

 ** participantOrderAttribute **   <a name="ivsrealtimeeapireference-Type-PipConfiguration-participantOrderAttribute"></a>
Attribute name in [ParticipantTokenConfiguration](API_ParticipantTokenConfiguration.md) identifying the participant ordering key. Participants with `participantOrderAttribute` set to `""` or not specified are ordered based on their arrival time into the stage.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** pipBehavior **   <a name="ivsrealtimeeapireference-Type-PipConfiguration-pipBehavior"></a>
Defines PiP behavior when all participants have left: `STATIC` (maintains original position/size) or `DYNAMIC` (expands to full composition). Default: `STATIC`.
Type: String
Valid Values: `STATIC | DYNAMIC`
Required: No

 ** pipHeight **   <a name="ivsrealtimeeapireference-Type-PipConfiguration-pipHeight"></a>
Specifies the height of the PiP window in pixels. When this is not set explicitly, `pipHeight`’s value will be based on the size of the composition and the aspect ratio of the participant’s video.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** pipOffset **   <a name="ivsrealtimeeapireference-Type-PipConfiguration-pipOffset"></a>
Sets the PiP window’s offset position in pixels from the closest edges determined by `PipPosition`. Default: `0`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** pipParticipantAttribute **   <a name="ivsrealtimeeapireference-Type-PipConfiguration-pipParticipantAttribute"></a>
Specifies the participant for the PiP window. A participant with this attribute set to `"true"` (as a string value) in [ParticipantTokenConfiguration](API_ParticipantTokenConfiguration.md) is placed in the PiP slot. Default: `""` (no PiP participant).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** pipPosition **   <a name="ivsrealtimeeapireference-Type-PipConfiguration-pipPosition"></a>
Determines the corner position of the PiP window. Default: `BOTTOM_RIGHT`.
Type: String
Valid Values: `TOP_LEFT | TOP_RIGHT | BOTTOM_LEFT | BOTTOM_RIGHT`
Required: No

 ** pipWidth **   <a name="ivsrealtimeeapireference-Type-PipConfiguration-pipWidth"></a>
Specifies the width of the PiP window in pixels. When this is not set explicitly, `pipWidth`’s value will be based on the size of the composition and the aspect ratio of the participant’s video.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** videoFillMode **   <a name="ivsrealtimeeapireference-Type-PipConfiguration-videoFillMode"></a>
Defines how video content fits within the participant tile: `FILL` (stretched), `COVER` (cropped), or `CONTAIN` (letterboxed). Default: `COVER`.
Type: String
Valid Values: `FILL | COVER | CONTAIN`
Required: No

## See Also
<a name="API_PipConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/PipConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/PipConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/PipConfiguration)
