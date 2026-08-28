---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/supported-containers-inputs.html
---

# Rules for extracting captions from sources
<a name="supported-containers-inputs"></a>

To use captions in a source, Elemental Live must be able to extract the captions. The rules are as follows:
+ Elemental Live can always extract sidecar captions from the source, so long as Elemental Live supports the captions format.
+ Elemental Live can always support captions from a streaming source, so long as Elemental Live supports the captions format and the input type.
+ Elemental Live can't necessarily extract captions from a file source. Even if Elemental Live supports the captions format, it can extract the captions only from specific container types. See the table that follows.

| Container in file input | Elemental Live can extract captions from the container? |
| --- | --- |
| Adobe Flash |   |
| Audio Video Interleave (AVI) |   |
| HLS | Yes |
| Matroska |   |
| MP4 | Yes |
| MPEG Transport Stream (TS) | Yes |
| MPEG-1 System Stream |   |
| MXF | Yes |
| No container | Yes |
| QuickTime | Yes |
| WAV | Yes  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
