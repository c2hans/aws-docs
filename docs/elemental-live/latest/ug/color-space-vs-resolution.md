---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-vs-resolution.html
---

# Color space versus video resolution
<a name="color-space-vs-resolution"></a>

Color space refers to the range of color. Elemental Live supports the following color spaces:
+ SDR (standard dynamic range)
+ HDR (high dynamic range)

Resolution refers to the video pixel count. Elemental Live supports the following resolutions:
+ SD (standard definition).
+ HD (high definition).
+ UHD (ultra-high definition). For UHD, Elemental Live supports resolutions up to 4K.

The following combinations of color space and resolution are typically used:
+ SDR color space can be associated with SD, HD, and UHD video.
+ HDR color space can be associated with HD or UHD video.

HDR isn't typically associated with SD content, but Elemental Live *does* support this combination.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
