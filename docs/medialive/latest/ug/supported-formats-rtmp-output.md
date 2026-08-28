---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/supported-formats-rtmp-output.html
---

# Captions formats supported in RTMP outputs
<a name="supported-formats-rtmp-output"></a>

In this table, look up your input container and captions type. Then read across to find the caption formats that are supported in MediaLive in an RTMP output, when you have this input container and captions type.

- **CDI container**
  - **Source caption input:** ARIB / **Supported output captions:** None
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEmbeddedRTMP CaptionInfo
  - **Source caption input:** Teletext / **Supported output captions:** None

- **HLS container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEmbedded<br />RTMP CaptionInfo
  - **Source caption input:** SCTE-20 / **Supported output captions:** Embedded

- **Link container**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inEmbedded<br />RTMP CaptionInfo
  - **Source caption input:** Teletext / **Supported output captions:** None

- **MP4 container**
  - **Source caption input:** Ancillary / **Supported output captions:** Burn-inEmbedded<br />RTMP CaptionInfo
  - **Source caption input:** Embedded or Embedded\+SCTE-20 / **Supported output captions:** Burn-inEmbedded<br />RTMP CaptionInfo

- **RTMP container**
  - **Source caption input:** Embedded
  - **Supported output captions:** Burn-inEmbedded<br />RTMP CaptionInfo

- **MPEG-TS container (through MediaConnect or through the RTP or SRT protocols)**
  - **Source caption input:** ARIB / **Supported output captions:** None
  - **Source caption input:** DVB-Sub / **Supported output captions:** Burn-in
  - **Source caption input:** Embedded or Embedded\+SCTE-20 / **Supported output captions:** Burn-inEmbedded<br />RTMP CaptionInfo
  - **Source caption input:** SCTE-20 / **Supported output captions:** EmbeddedRTMP CaptionInfo
  - **Source caption input:** SCTE-27 / **Supported output captions:** Burn-in
  - **Source caption input:** Teletext / **Supported output captions:** None

- **SMPTE 2110**
  - **Source caption input:** Embedded / **Supported output captions:** Burn-inRTMP CaptionInfo<br />Embedded<br />Embedded\+SCTE-20<br />SCTE-20<br />SCTE-20\+Embedded
  - **Source caption input:** Teletext / **Supported output captions:** None

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
