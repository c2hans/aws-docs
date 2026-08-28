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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
