---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/color-space-simplified-input-output-requirements.html
---

# Output requirements
<a name="color-space-simplified-input-output-requirements"></a>

**Supported output types**

All color space types except Dolby Vision 8.1 can be set up in all MediaLive output group types.

Dolby Vision 8.1 can be set up only in the following output group types:
+ Archive
+ CMAF Ingest
+ HLS
+ UDP

**Supported output codecs**

The following table specifies the supported video codecs for the output color spaces. A value of Yes means that when the video output uses this codec, you can convert to the specified color space.

|  Output color space   | AV1 | AVC (H.264) | HEVC (H.265) |
| --- | --- | --- | --- |
| Rec. 601 | Yes | Yes | Yes |
| Rec. 709 | Yes | Yes | Yes |
| HDR10  | Yes |  | Yes |
| HLG | Yes |  | Yes |
| Dolby Vision 8.1 |  |  | Yes |

**Supported video profile for HDR10 or Dolby Vision 8.1 outputs**

For HDR10 or Dolby Vision 8.1 outputs, the video profile must include the term *10BIT*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
