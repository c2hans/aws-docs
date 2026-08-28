---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/extract-contents-mp4.html
---

# Identifying content in an MP4 source
<a name="extract-contents-mp4"></a>

The content in an MP4 source always consists of one video track, one or more audio tracks, and optional captions.

Obtain identifying information from the content provider.

|  Asset  |  Details  | Information to obtain |
| --- | --- | --- |
| Video | You don't need identifying information. MediaLive always extracts the single video asset. | None |
| Audio | The source might include multiple audio tracks, typically, one for each language.  | Obtain the track numbers or three-character language codes of the languages that you want. |
| Captions | EmbeddedThe captions might be embedded in the video track or might be embedded in an ancillary track. | Obtain the languages in the channel numbers. For example, "channel 1 is French".  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
