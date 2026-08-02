---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-VideoTrackSettings.html
---

# VideoTrackSettings
<a name="structures-VideoTrackSettings"></a>

Object specifying encoder-specific settings.

## Contents
<a name="structures-VideoTrackSettings-contente"></a>
+ **bf**
  + Number of consecutive bframes. Default: 0.
  + Type: Integer
  + Valid Range: Minimum value of 0.
  + Required: No
+ **bitrate**
  + Target bitrate in kilobits per second.
  + Type: Integer
  + Valid Range: Minimum value of 1.
  + Required: Yes
+ **keyint\_sec**
  + Number of seconds between keyframes. 0 indicates that the encoder should decide.
  + Type: Integer
  + Valid Range: Minimum value of 0. Maximum value of 10.
  + Required: Yes
+ **lookahead**
  + Enables lookahead. Default: `false` (disabled).
  + Type: Boolean
  + Required: No
+ **preset2**
  + The desired balance between the speed and the quality of encoding using presets specific to the GPU card manufacturer. For example, NVIDIA uses values of p1 through p7, with p1 indicating faster encoding with lower quality and p7 indicating slower encoding with higher quality.
  + Type: String
  + Required: Yes
+ **profile**
  + Profile of the codec. Not all values may be valid for each codec. For the HEVC codec, `profile` must be set to `main`.
  + Type: String
  + Valid Values: `baseline` \| `main` \| `high`
  + Required: Yes
+ **psycho\_aq**
  + Enables Psycho Visual Adaptive Quantization Tuning to increase perceived visual quality. Default: `false` (disabled).
  + Type: Boolean
  + Required: No
+ **rate\_control**
  + Rate control.
  + Type: String
  + Valid Values: `CBR`
  + Required: Yes
+ **tune**
  + Tuning parameter returned only for NVIDIA GPUs.
  + Type: String
  + Valid Values: `hq` \| `ll` \| `ul`
  + Required: No
