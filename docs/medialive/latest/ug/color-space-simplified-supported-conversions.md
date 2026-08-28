---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/color-space-simplified-supported-conversions.html
---

# Supported types of conversion in MediaLive
<a name="color-space-simplified-supported-conversions"></a>

You can configure a channel to use the standard MediaLive color corrector when converting the color space. Or you can use a [3D LUTs color corrector file](color-space-process-with-lut.md) that you provide.

The following table shows which conversions MediaLive supports. Read across each row.

|  From any of these color spaces in the source  |  To this color space in the output  | Supported? |
| --- | --- | --- |
| Rec. 709, HLG, HDR10  | Rec. 601 | Yes |
| Rec. 601, HLG, HDR10 | Rec. 709 | Yes |
| Rec. 601, Rec. 709, HLG | HDR10 | Yes |
| Rec. 601, Rec. 709, HDR10 | HLG | Yes |
| Rec. 601, Rec. 709, HLG, HDR10 | Dolby Vision 8.1 | Yes |
| Dolby Vision 8.1 | Any color space supported by MediaLive | Not supported |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
