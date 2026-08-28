---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/video-characteristics-resolution.html
---

# Resolutions supported in video outputs in MediaLive
<a name="video-characteristics-resolution"></a>

In the following table, each row defines the video resolutions that apply to the terms SD, HD, and UHD. The table also specifies the resolutions that are supported with each codec.

| Resolution | Definition | Supported in AV1 outputs | Supported in AVC outputs | Supported in HEVC outputs | Supported in MPEG-2 codec |
| --- | --- | --- | --- | --- | --- |
| SD | Vertical resolution under 720 | Yes | Yes | Yes | Yes |
| HD | Vertical resolution over 720, up to and including 1080 | Yes | Yes | Yes |  |
| UHD or 4K | Vertical resolution over 1080, up to and including 2160  |  | Yes | Yes |  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
