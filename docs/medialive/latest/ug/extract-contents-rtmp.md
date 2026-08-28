---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/extract-contents-rtmp.html
---

# Identifying content in an RTMP source
<a name="extract-contents-rtmp"></a>

This procedure applies to both RTMP push and pull inputs from the internet, and to RTMP inputs from Amazon Virtual Private Cloud. The content in an RTMP input always consists of one video, one audio, and optional captions.

Obtain identifying information from the content provider.

|  Asset  |  Details  | Information to obtain |
| --- | --- | --- |
| Video | You don't need identifying information. MediaLive always extracts the single video asset. | None |
| Audio | You don't need identifying information. MediaLive always extracts the single audio asset | Obtain the numbers and languages of the tracks. For example, "track 1 is French".  |
| Captions | EmbeddedThe captions might be embedded in the video track or might be embedded in an ancillary track. | Obtain the languages in the channel numbers. For example, "channel 1 is French".  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
