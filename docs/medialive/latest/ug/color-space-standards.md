---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/color-space-standards.html
---

# Supported color space standards
<a name="color-space-standards"></a>

Each color space standard follows a specific standard for the color space, and specific standards for the three sets of color data.

To read this table, find a color space in the first column, then read across to identify the standards for the color space and the three sets of color data.

|  MediaLive term for the color space   |  Complies with this color space standard   |  Complies with this brightness function standard   |  Complies with this standard for display metadata   |
| --- | --- | --- | --- |
| Rec. 601 or Rec. 601  | Rec. 601  | BT.1886  | Not applicable. This color space doesn't include display metadata. |
| Rec. 709 or Rec. 709  | Rec. 709  | BT.1886  | Not applicable. This color space doesn't include display metadata. |
| HDR10  | Rec. 2020 | SMPTE ST 2084 (PQ)  | SMPTE ST 2086  |
| HLG or HLG 2020  | Rec. 2020 | HLG rec. 2020  | Not applicable. This color space doesn't include display metadata. |
| Dolby Vision 8.1 | Rec. 2020 | SMPTE ST 2084 (PQ) | Proprietary Dolby Vision 8.1 metadata (RPU), on a per-frame basis, and SMPTE ST 2086 on a per-stream basis. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
