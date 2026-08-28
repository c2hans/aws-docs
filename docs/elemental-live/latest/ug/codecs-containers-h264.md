---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/codecs-containers-h264.html
---

# Video: H.264 (AVC) support
<a name="codecs-containers-h264"></a>

H.264 is supported in the following variations.

<a name="codecs-containers-h264-table"></a>

- **Input**
  - **Chroma Sampling:** 4:2:0  / **Bit Depth:** 8-bit and 10-bit / **License Requirement:** None
  - **Chroma Sampling:** 4:2:2 / **Bit Depth:** 8-bit and 10-bit / **License Requirement:** None
  - **Profile/Format:** Baseline, Main, High, High 10, High 4:2:2, High 10 Intra, High 422 Intra, AS-11/RP2027
  - **Level:** 1.0-5.2

- **Output**
  - **Chroma Sampling:** 4:2:0  / **Bit Depth:** 8-bit / **License Requirement:** None
  - **Chroma Sampling:** 4:2:0  / **Bit Depth:** 10-bit / **License Requirement:** For AVC Intra, purchase the BCE license pack.
  - **Chroma Sampling:** 4:2:2  / **Bit Depth:** 8-bit and 10-bit / **License Requirement:** For AVC Intra, purchase the BCE license pack.<br />For AVC 4:2:2, purchase the BCE license pack.

Both 4:2:0 and 4:2:2 chroma sampling are supported in raw outputs (.264, .avc, extensions) and MPEG-2 transport streams.

In all other containers, only 4:2:0 chroma sampling is supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
