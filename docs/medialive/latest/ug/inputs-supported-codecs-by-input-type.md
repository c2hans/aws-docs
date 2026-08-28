---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/inputs-supported-codecs-by-input-type.html
---

# Supported codecs by input type
<a name="inputs-supported-codecs-by-input-type"></a>

The following table lists the video and audio codecs that each type of MediaLive input type supports.

| Media type | Video codecs | Audio codecs |
| --- | --- | --- |
| CDISee [Characteristics for video and audio sources](inputs-video-audio-characteristics.md) for more information. | Uncompressed video | Dolby E wrapped in PCMPCM |
| HLSSee [HLS inputs](#hls-inputs-anchor), after this table. | H.264 (AVC) | AAC<br />Dolby Digital<br />Dolby Digital Plus |
| Link HD | Any codec that is included in a Link container is always supported by MediaLive. | Up to 8 channels of PCM audio when using HDMI or SDI input |
| Link UHD | Any codec that is included in a Link container is always supported by MediaLive. | Up to 8 channels of PCM audio when using HDMI inputUp to 16 channels of PCM audio when using SDI input<br />Dolby Digital<br />Dolby Digital Plus |
| MediaConnect | H.264 (AVC)<br />H.265 (HEVC)<br />MPEG-2 | AAC<br />Dolby Digital<br />Dolby E wrapped in PCM<br />Dolby Digital Plus<br />MPEG Audio<br />PCM |
| MP4 | H.264 (AVC)H.265 (HEVC)<br />MPEG-2 | AACDolby E wrapped in PCM |
| RTMP | H.264 (AVC) | AAC |
| RTP | H.264 (AVC)<br />H.265 (HEVC)<br />MPEG-2 | AAC<br />Dolby Digital<br />Dolby E wrapped in PCM<br />Dolby Digital Plus<br />MPEG Audio<br />PCM |
| SMPTE 2110 stream | Uncompressed | Dolby DigitalDolby Digital Plus<br />PCM |
| SRT caller | H.264 (AVC)<br />H.265 (HEVC)<br />MPEG-2 | AAC<br />Dolby Digital<br />Dolby E wrapped in PCM<br />Dolby Digital Plus<br />MPEG Audio<br />PCM |
| SRT Listener | H.264 (AVC)<br />H.265 (HEVC)<br />MPEG-2 | AAC<br />Dolby Digital<br />Dolby E wrapped in PCM<br />Dolby Digital Plus<br />MPEG Audio<br />PCM |
| Transport Stream (TS) file | H.264 (AVC)<br />H.265 (HEVC)<br />MPEG-2 | AAC<br />Dolby Digital<br />Dolby E wrapped in PCM<br />Dolby Digital Plus<br />MPEG Audio<br />PCM |

**HLS inputs**

The audio and video assets can be multiplexed in a single stream. Or the audio can be in a separate audio rendition group. If you are using audio in a rendition group, the group can be selected by using the **Group ID** and **Name** that is in the **\#EXT-X-MEDIA** tag.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
