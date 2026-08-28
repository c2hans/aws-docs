---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/encode-rules.html
---

# Summary of encode rules for output groups
<a name="encode-rules"></a>

 This table summarizes the rules for encodes for each output group. In the first column, find the output group that you want, then read across the row.

| Type of output group | Rule for video encodes | Rule for audio encodes | Rule for captions encodes |
| --- | --- | --- | --- |
| Archive | One or more video encodes. | Zero or more audio encodes. | Zero or more captions encodes. The captions are either embedded or object-style captions. |
| CMAF Ingest | One or more video encodes. Typically, there are multiple video encodes. | Zero or more audio encodes. Typically, there are multiple audio encodes.  | Zero or more captions encodes. Typically, there are caption languages to match the audio languages. The captions are embedded or sidecar captions. |
| Frame Capture | One video encode. | Zero audio encodes. | Zero captions encodes. |
| HLS or MediaPackage | One or more video encodes. Typically, there are multiple video encodes. | Zero or more audio encodes. Typically, there are multiple audio encodes.  | Zero or more captions encodes. Typically, there are caption languages to match the audio languages. The captions are either embedded or sidecar captions. |
| Microsoft Smooth | One or more video encodes. Typically, there are multiple video encodes. | Zero or more audio encodes. Typically, there are multiple audio encodes.  | Zero or more captions encodes. Typically, there are caption languages to match the audio languages. The captions are always sidecar captions. |
| RTMP | One video encode. | Zero or one audio encodes.  | Zero or one caption encodes. The captions are either embedded or object-style captions. |
| SRT caller | One or more video encodes. | One or more audio encodes. | Zero or more captions encodes. The captions are either embedded or object-style captions. |
| UDP | One or more video encodes.  | One or more audio encodes.  | Zero or more captions encodes. The captions are either embedded or object-style captions. |

Some output groups also support audio-only outputs. See [Setting up the output](audio-only-outputs-and-outputgroups.md).

Some output groups also support outputs that contain JPEG files, to support trick play according to the Roku specification. See [Trick-play track via the Image Media Playlist specification](trick-play-roku.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
