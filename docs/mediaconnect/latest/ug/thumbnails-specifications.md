---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/thumbnails-specifications.html
---

# Requirements for thumbnails
<a name="thumbnails-specifications"></a>

## Requirements for the video source
<a name="thumbnails-source-video-requirements"></a>

For MediaConnect to successfully generate thumbnails, make sure that the video source meets the following requirements.

- **Maximum 4K UHD at 60 FPS (2160p60)**
  - **Video codec:** AVC (H.264) / **Scan type:** Progressive or interlaced / **Profile and format:** Baseline, Main, High, High 10, High 422, High 10 Intra, High 422 Intra / **Level:** 1.0-5.2 / **Chroma sampling:** 4:2:0, 4:2:2 / **Bit depth:** 8 bit/10 bit
  - **Video codec:** HEVC (H.265) / **Scan type:** Progressive only / **Profile and format:** Main, Main 10, Main 422 10 / **Level:** 1.0-5.2 / **Chroma sampling:** 4:2:0, 4:2:2 / **Bit depth:** 8 bit/10 bit
  - **Video codec:** MPEG-2 (H.262) / **Scan type:** Progressive or interlaced / **Profile and format:** Simple, Main, 422 / **Level:** Low, Main, High1440, High / **Chroma sampling:** 4:2:0, 4:2:2 / **Bit depth:** 8 bit/10 bit

## Requirements for the flow
<a name="thumbnails-flow-requirements"></a>

To successfully generate thumbnails, make sure that your flow meets the following requirements.

| Characteristic of the flow | Requirement |
| --- | --- |
| Type of flows that support thumbnails | Any type of flow except CDI flows. |
| Maximum number of outputs that can be attached to the flow | 10If the flow exceeds this limit, then MediaConnect won't generate any thumbnails for this flow. |
| Maximum bitrate for all the outputs that are attached to the flow | 400 MbpsIf the flow exceeds this limit, then MediaConnect won't generate any thumbnails for this flow. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
