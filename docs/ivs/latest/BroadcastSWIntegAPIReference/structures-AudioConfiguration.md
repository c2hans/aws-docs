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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
