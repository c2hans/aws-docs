---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ParticipantRecordingHlsConfiguration.html
---

# ParticipantRecordingHlsConfiguration
<a name="API_ParticipantRecordingHlsConfiguration"></a>

An object representing a configuration of participant HLS recordings for individual participant recording.

## Contents
<a name="API_ParticipantRecordingHlsConfiguration_Contents"></a>

 ** targetSegmentDurationSeconds **   <a name="ivsrealtimeeapireference-Type-ParticipantRecordingHlsConfiguration-targetSegmentDurationSeconds"></a>
Defines the target duration for recorded segments generated when recording a stage participant. Segments may have durations longer than the specified value when needed to ensure each segment begins with a keyframe. Default: 6.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10.
Required: No

## See Also
<a name="API_ParticipantRecordingHlsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/ParticipantRecordingHlsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/ParticipantRecordingHlsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/ParticipantRecordingHlsConfiguration)
