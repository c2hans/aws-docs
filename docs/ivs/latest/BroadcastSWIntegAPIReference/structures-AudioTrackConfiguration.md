---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-AudioTrackConfiguration.html
---

# AudioTrackConfiguration
<a name="structures-AudioTrackConfiguration"></a>

Complex type specifying an audio track configuration to be used by the encoder.

## Contents
<a name="structures-AudioTrackConfiguration-contente"></a>
+ **channels**
  + Number of audio channels.
  + Type: Integer
  + Valid Values: 2
  + Required: Yes
+ **codec**
  + Codec used for the audio encoding.
  + Type: String
  + Valid Values: `aac`
  + Required: Yes
+ **settings**
  + Audio encoder settings.
  + Type: [AudioTrackSettings](structures-AudioTrackSettings.md) object
+ **track\_id**
  + Track index as defined in the [Enhanced Audio](https://veovera.org/docs/enhanced/enhanced-rtmp-v2#enhanced-audio) section of the E-RTMP specification. Track 0 is the primary audio track and should be encoded as standard RTMP audio unless the codec being used does not allow it.
  + Type: Integer
  + Required: Yes
