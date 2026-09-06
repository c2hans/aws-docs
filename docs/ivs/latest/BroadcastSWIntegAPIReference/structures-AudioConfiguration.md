---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-AudioConfiguration.html
---

# AudioConfiguration
<a name="structures-AudioConfiguration"></a>

Complex type specifying the stream’s audio configuration to be used by the encoder.

## Contents
<a name="structures-AudioConfiguration-contents"></a>
+ **live**
  + Audio-track configurations for the live stream.
  + Type: Array of [AudioTrackConfiguration](structures-AudioTrackConfiguration.md) objects
  + Required: Yes
+ **vod**
  + Audio-track configurations for video on demand. Returned only when audio-track configurations are requested for video on demand, by setting `vod_track_audio` to `true` in [PreferencesDescription](structures-PreferencesDescription.md).
  + Type: Array of [AudioTrackConfiguration](structures-AudioTrackConfiguration.md) objects
  + Required: No
