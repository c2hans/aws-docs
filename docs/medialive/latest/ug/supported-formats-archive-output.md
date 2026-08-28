---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/supported-formats-archive-output.html
---

# Captions formats supported in Archive outputs
<a name="supported-formats-archive-output"></a>

In this table, look up your input container and captions type. Then read across to find the caption formats that are supported in MediaLive in an Archive (MPEG-TS file) output, when you have this input container and captions type.

- **CDI container**
  - **Source caption input:** ARIB / **Supported output captions:** ARIB
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inDVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20
  - **Source caption input:** Teletext / **Supported output captions:** DVB-Sub<br />Teletext

- **HLS container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inDVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded
  - **Source caption input:** SCTE-20 / **Supported output captions:** Burn-inDVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded

- **Link container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inDVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded
  - **Source caption input:** Teletext / **Supported output captions:** DVB-Sub<br />Teletext

- **MP4 container**
  - **Source caption input:** Ancillary / **Supported output captions:** Burn-inDVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded
  - **Source caption input:** Embedded or Embedded\+SCTE-20 / **Supported output captions:** Burn-inDVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded

- **RTMP container**
  - **Source caption input:** Embedded
  - **Supported output captions:** Burn-inDVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded

- **MPEG-TS container (through MediaConnect or through the RTP or SRT protocols)**
  - **Source caption input:** ARIB / **Supported output captions:** ARIB
  - **Source caption input:** DVB-Sub / **Supported output captions:** Burn-inDVB-Sub
  - **Source caption input:** Embedded or Embedded\+SCTE-20 / **Supported output captions:** Burn-inDVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded
  - **Source caption input:** SCTE-20 / **Supported output captions:** Burn-inDVB-Sub<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded
  - **Source caption input:** SCTE-27 / **Supported output captions:** None
  - **Source caption input:** Teletext / **Supported output captions:** DVB-Sub<br />Teletext

- **SMPTE 2110**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEmbedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded
  - **Source caption input:** Teletext / **Supported output captions:** Burnin

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
