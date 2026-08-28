---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/captions-mpeg2-ts-file-mpeg2-udp-streaming-output-container.html
---

# Supported source captions and output captions in MPEG2-TS or MPEG2-UDP
<a name="captions-mpeg2-ts-file-mpeg2-udp-streaming-output-container"></a>

The table provides information about captions in an MPEG2-TS file output container or MPEG2-UDP streaming output container.

To read this table, find the type of container and captions from your input. The supported caption formats for this *output *container are then shown in the last column.

<a name="table-captions-mpeg2-ts-file-mpeg2-udp-streaming-output-container"></a>

- **HLS Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, DVB-Sub, Embedded, Embedded\+SCTE-20, SCTE-20\+Embedded
  - **Source caption format:** SCTE-20 / **Supported output captions:** Burn-in, DVB-Sub, Embedded, Embedded\+SCTE-20, SCTE-20\+Embedded

- **MP4 Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, DVB-Sub, Embedded, Embedded\+SCTE-20, SCTE-20\+Embedded
  - **Source caption format:** SCTE-20 / **Supported output captions:** Burn-in, DVB-Sub, Embedded, Embedded\+SCTE-20, SCTE-20\+Embedded

- **MXF Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, DVB-Sub, Embedded, Embedded\+SCTE-20, SCTE-20\+Embedded
  - **Source caption format:** Ancillary Data / **Supported output captions:** Burn-in, DVB-Sub, Embedded, Embedded\+SCTE-20, SCTE-20\+Embedded
  - **Source caption format:** Teletext / **Supported output captions:** Burn-in, DVB-Sub, Teletext

- **QuickTime Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, DVB-Sub, Embedded, Embedded\+SCTE-20, SCTE-20\+Embedded
  - **Source caption format:** Ancillary Data / **Supported output captions:** Burn-in, DVB-Sub, Embedded, Embedded\+SCTE-20, SCTE-20\+Embedded

- **Raw Container**
  - **Source caption format:** SRT / **Supported output captions:** Burn-in, DVB-Sub
  - **Source caption format:** SMI / **Supported output captions:** Burn-in, DVB-Sub
  - **Source caption format:** TTML / **Supported output captions:** Burn-in, DVB-Sub
  - **Source caption format:** STL / **Supported output captions:** Burn-in, DVB-Sub
  - **Source caption format:** SCC / **Supported output captions:** Burn-in, DVB-Sub, Embedded, Embedded\+SCTE-20, SCTE-20\+Embedded

- **RTMP Container**
  - **Source caption format:** Embedded
  - **Supported output captions:** Burn-in, DVB-Sub, Embedded, Embedded\+SCTE-20, SCTE-20\+Embedded

- **SDI Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, DVB-Sub, Embedded, Embedded\+SCTE-20, SCTE-20\+Embedded
  - **Source caption format:** Teletext / **Supported output captions:** Burn-in, DVB-Sub, Teletext
  - **Source caption format:** ARIB / **Supported output captions:** ARIB

- **MPEG2-TS Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, DVB-Sub, Embedded, Embedded\+SCTE-20, SCTE-20\+Embedded
  - **Source caption format:** SCTE-20 / **Supported output captions:** Burn-in, DVB-Sub, Embedded, Embedded\+SCTE-20, SCTE-20\+Embedded
  - **Source caption format:** Teletext / **Supported output captions:** Burn-in, DVB-Sub, Teletext
  - **Source caption format:** ARIB / **Supported output captions:** ARIB
  - **Source caption format:** DVB-Sub / **Supported output captions:** Burn-in, DVB-Sub
  - **Source caption format:** SCTE-27 / **Supported output captions:** Burn-in, DVB-Sub

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
