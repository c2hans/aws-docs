---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/outputs-supported-codecs.html
---

# Supported codecs by output type
<a name="outputs-supported-codecs"></a>

The following table lists the video and audio codecs that each type of MediaLive output container (output group) supports.

| Container (output group) | Video codecs | Audio codecs |
| --- | --- | --- |
| Archive | H.264 (AVC)H.265 (HEVC) | AAC<br />Dolby Digital (AC3)<br />Dolby Digital Plus (EAC3)<br />Dolby Digital Plus with Atmos<br />MPEG-1 Layer II (MP2) |
| CMAF Ingest | AV1H.265 (AVC)<br />H.265 (HEVC) | AAC<br />Dolby Digital (AC3)<br />Dolby Digital Plus (EAC3)<br />Dolby Digital Plus with Atmos |
| Frame Capture | JPEG | None. A Frame capture output doesn't include audio. |
| HLS with a standard container | H.264 (AVC)H.265 (HEVC) | AAC<br />Dolby Digital (AC3)<br />Dolby Digital Plus (EAC3)<br />Dolby Digital Plus with Atmos |
| HLS with an fMP4 container | H.264 (AVC)<br />H.265 (HEVC) | AAC<br />Dolby Digital (AC3)<br />Dolby Digital Plus (EAC3)<br />Dolby Digital Plus with Atmos |
| MediaPackage | H.264 (AVC)<br />H.265 (HEVC) | AAC<br />Dolby Digital (AC3)<br />Dolby Digital Plus (EAC3)<br />Dolby Digital Plus with Atmos |
| MediaConnect Router | AV1<br />H.264 (AVC)<br />H.265 (HEVC)<br />MPEG-2 | AAC<br />Dolby Digital (AC3)<br />Dolby Digital Plus (EAC3)<br />Dolby Digital Plus with Atmos<br />MPEG-1 Layer II (MP2) |
| Microsoft Smooth | H.264 (AVC)<br />H.265 (HEVC) | AAC<br />Dolby Digital (AC3)<br />Dolby Digital Plus (EAC3) |
| Multiplex | H.264 (AVC)<br />H.265 (HEVC)<br />MPEG-2 | AAC<br />Dolby Digital (AC3)<br />Dolby Digital Plus (EAC3)<br />Dolby Digital Plus with Atmos |
| RTMP or RTMPS | H.264 (AVC) | AAC |
| SRT | H.264 (AVC)<br />H.265 (HEVC) | AAC<br />Dolby Digital (AC3)<br />Dolby Digital Plus (EAC3)<br />Dolby Digital Plus with Atmos<br />MPEG-1 Layer II (MP2) |
| UDP | H.264 (AVC)<br />H.265 (HEVC) | AAC<br />Dolby Digital (AC3)<br />Dolby Digital Plus (EAC3)<br />Dolby Digital Plus with Atmos<br />MPEG-1 Layer II (MP2) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
