---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/captions-hls-output-container.html
---

# Supported source captions and output captions in an HLS output container
<a name="captions-hls-output-container"></a>

To read this table, find the type of container and captions from your input. The supported captions formats for this *output *container are then shown in the last column.

<a name="table-captions-hls-output-container"></a>

- **HLS Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, Embedded, Web-VTT
  - **Source caption format:** SCTE-20 / **Supported output captions:** Burn-in, Embedded, Web-VTT

- **MP4 Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, Embedded, Web-VTT
  - **Source caption format:** SCTE-20 / **Supported output captions:** Burn-in, Embedded, Web-VTT

- **MXF Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, Embedded, Web-VTT
  - **Source caption format:** Ancillary Data / **Supported output captions:** Burn-in, Embedded, Web-VTT
  - **Source caption format:** Teletext / **Supported output captions:** None

- **QuickTime Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, Embedded, Web-VTT
  - **Source caption format:** Ancillary Data / **Supported output captions:** Burn-in, Embedded, Web-VTT

- **Raw Container**
  - **Source caption format:** SRT / **Supported output captions:** Burn-in, Web-VTT
  - **Source caption format:** SMI / **Supported output captions:** Burn-in, Web-VTT
  - **Source caption format:** TTML / **Supported output captions:** Burn-in, Web-VTT
  - **Source caption format:** STL / **Supported output captions:** Burn-in, Web-VTT
  - **Source caption format:** SCC / **Supported output captions:** Burn-in, Embedded, Web-VTT

- **RTMP Container**
  - **Source caption format:** Embedded
  - **Supported output captions:** Burn-in, Embedded, Web-VTT

- **SDI Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, Embedded, Web-VTT
  - **Source caption format:** Teletext / **Supported output captions:** Burn-in, Web-VTT
  - **Source caption format:** ARIB / **Supported output captions:** None

- **MPEG2-TS Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, Embedded, Web-VTT
  - **Source caption format:** SCTE-20 / **Supported output captions:** Burn-in, Embedded, Web-VTT
  - **Source caption format:** Teletext / **Supported output captions:** Burn-in, Web-VTT
  - **Source caption format:** ARIB / **Supported output captions:** None
  - **Source caption format:** DVB-Sub / **Supported output captions:** Burn-in, Web-VTT
  - **Source caption format:** SCTE-27 / **Supported output captions:** Burn-in, Web-VTT

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
