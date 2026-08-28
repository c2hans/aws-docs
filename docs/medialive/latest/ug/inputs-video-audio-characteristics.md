---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/inputs-video-audio-characteristics.html
---

# Characteristics for video and audio sources
<a name="inputs-video-audio-characteristics"></a>

**Orientation**

MediaLive supports any aspect ratio — landscape or portrait.

**Input frame rate**

MediaLive only supports constant frame rate (CFR) inputs. It does not support variable frame rates (VFR).

**Other characteristics**

| Container | Video characteristics | Audio characteristics |
| --- | --- | --- |
| CDI—MediaLive only supports these characteristics for CDI inputs. |  +  Uncompressed YCbCr 4:2:2 8-bit <br />+  Uncompressed YCbCr 4:2:2 10-bit   |  +  24-bit Big-Endian PCM <br />+  Mono (1.0), Dual mono (2.0), Stereo (2.0), 5.1, 7.1 <br />+  222, SGRP <br />+  48kHz, 96 kHz   |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
