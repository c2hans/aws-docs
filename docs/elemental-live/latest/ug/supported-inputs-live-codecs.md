---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/supported-inputs-live-codecs.html
---

# Supported codecs
<a name="supported-inputs-live-codecs"></a>

This table specifies the codecs that are supported for each input media type that Elemental Live supports.

|  Media Type   |  Video Codecs   |  Audio Codecs   |
| --- | --- | --- |
| HLS  | H.264<br />H.265  | AAC  |
| MPTS  | H.264<br />H.265<br />MPEG-2  | AAC<br />Dolby Digital<br />Dolby Digital Plus<br />Dolby Digital Plus with Atmos<br />MPEG-1, layer II<br />PCM  |
| RTMP  | H.264  | AAC  |
| RTSP | H.264<br />H.265 | AAC |
| Transport stream  | H.264<br />H.265<br />J2K (only in a TS that is compliant with TR-01)<br />MPEG-2  | AAC<br />Dolby Digital<br />Dolby Digital Plus<br />Dolby Digital Plus with Atmos<br />MPEG-1, layer II<br />PCM  |
| SDI  | Uncompressed  | Dolby Digital<br />Dolby Digital Plus<br />Dolby Digital Plus with Atmos<br />Dolby E frames carried in PCM streams tagged with SMPTE-337<br />PCM  |
| HDMI  | Uncompressed  | Dolby Digital<br />Dolby Digital Plus<br />Dolby Digital Plus with Atmos<br />Dolby E frames carried in PCM streams tagged with SMPTE-337<br />PCM  |
| SDI Quad-compliant SDI 2SI-compliant SDI  | Uncompressed  | Dolby Digital<br />Dolby Digital Plus<br />Dolby Digital Plus with Atmos<br />Dolby E frames carried in PCM streams tagged with SMPTE-337<br />PCM  |
| Uncompressed SMPTE 2110  | Uncompressed<br />JPEG XS (starting with version 2.21.3)  | Dolby Digital<br />Dolby Digital Plus<br />PCM  |
| Uncompressed SMPTE 2022-6  | Uncompressed  | Dolby Digital<br />Dolby Digital Plus<br />Dolby Digital Plus with Atmos<br />PCM  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
