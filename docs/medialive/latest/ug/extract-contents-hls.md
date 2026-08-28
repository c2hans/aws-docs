---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/extract-contents-hls.html
---

# Identifying content in an HLS source
<a name="extract-contents-hls"></a>

The content in an HLS container is always a transport stream (TS) that contains only one video rendition (program).

Obtain identifying information from the content provider.

|  Asset  |  Details  | Information to obtain |
| --- | --- | --- |
| Video | You don't need identifying information. MediaLive always extracts the single video asset. |  |
| Audio | The source might include multiple audio PIDs. | Obtain the PIDs or three-character language codes of the languages that you want. We recommend that you obtain the PIDs for the audio assets. They are a more reliable way of identifying an audio asset.  |
| Captions | Embedded | Obtain the languages in the channel numbers. For example, "channel 1 is French" |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
