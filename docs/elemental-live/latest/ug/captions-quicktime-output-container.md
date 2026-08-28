---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/captions-quicktime-output-container.html
---

# Supported source captions and output captions in a QuickTime output container
<a name="captions-quicktime-output-container"></a>

To read this table, find the type of container and captions from your input. The supported caption formats for this *output *container are then shown in the last column.

<a name="table-captions-quicktime-output-container"></a>

- **HLS Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, Embedded, Embedded\+Ancillary
  - **Source caption format:** SCTE-20 / **Supported output captions:** Burn-in, Embedded, Embedded\+Ancillary

- **MP4 Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, Embedded, Embedded\+Ancillary
  - **Source caption format:** SCTE-20 / **Supported output captions:** Burn-in, Embedded, Embedded\+Ancillary

- **MXF Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, Embedded, Embedded\+Ancillary
  - **Source caption format:** Ancillary Data / **Supported output captions:** Burn-in, Embedded, Embedded\+Ancillary
  - **Source caption format:** Teletext / **Supported output captions:** Burn-in

- **QuickTime Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, Embedded, Embedded\+Ancillary
  - **Source caption format:** Ancillary Data / **Supported output captions:** Burn-in, Embedded, Embedded\+Ancillary

- **Raw Container**
  - **Source caption format:** SRT / **Supported output captions:** Burn-in
  - **Source caption format:** SMI / **Supported output captions:** Burn-in
  - **Source caption format:** TTML / **Supported output captions:** Burn-in
  - **Source caption format:** STL / **Supported output captions:** Burn-in
  - **Source caption format:** SCC / **Supported output captions:** Burn-in, Embedded, Embedded\+Ancillary

- **RTMP Container**
  - **Source caption format:** Embedded
  - **Supported output captions:** Burn-in, Embedded, Embedded\+Ancillary

- **SDI Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, Embedded, Embedded\+Ancillary
  - **Source caption format:** Teletext / **Supported output captions:** Burn-in
  - **Source caption format:** ARIB / **Supported output captions:** None

- **MPEG2-TS Container**
  - **Source caption format:** Embedded / **Supported output captions:** Burn-in, Embedded, Embedded\+Ancillary
  - **Source caption format:** SCTE-20 / **Supported output captions:** Burn-in, Embedded, Embedded\+Ancillary
  - **Source caption format:** Teletext / **Supported output captions:** Burn-in
  - **Source caption format:** ARIB / **Supported output captions:** None
  - **Source caption format:** DVB-Sub / **Supported output captions:** Burn-in
  - **Source caption format:** SCTE-27 / **Supported output captions:** Burn-in

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
