---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/captions-mss-output-container.html
---

# Supported source captions and output captions in an MSS output container
<a name="captions-mss-output-container"></a>

To read this table, find the type of container and captions from your input. The supported caption formats for this *output *container are then shown in the last column.

<a name="table-captions-mss-output-container"></a>

- **HLS Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D
  - **Source caption format:** SCTE-20 / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D

- **MP4 Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D
  - **Source caption format:** SCTE-20 / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D

- **MXF Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D
  - **Source caption format:** Ancillary Data / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D
  - **Source caption format:** Teletext / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D

- **QuickTime Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D
  - **Source caption format:** Ancillary Data / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D

- **Raw Container**
  - **Source caption format:** SRT / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D
  - **Source caption format:** SMI / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D
  - **Source caption format:** TTML / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D
  - **Source caption format:** STL / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D
  - **Source caption format:** SCC / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D

- **RTMP Container**
  - **Source caption format:** Embedded
  - **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D

- **SDI Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D
  - **Source caption format:** Teletext / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D
  - **Source caption format:** ARIB / **Supported output captions:** None

- **MPEG2-TS Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D
  - **Source caption format:** SCTE-20 / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D
  - **Source caption format:** Teletext / **Supported output captions:** Burn-in, SMPTE-TT, TTML, EBU-TT-D
  - **Source caption format:** ARIB / **Supported output captions:** None
  - **Source caption format:** DVB-Sub / **Supported output captions:** SMPTE-TT
  - **Source caption format:** SCTE-27 / **Supported output captions:** SMPTE-TT

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
