---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-convert-e.html
---

# Converting other color spaces to Dolby Vision 5.0 or 8.1
<a name="color-space-convert-e"></a>

You shouldn't convert non-HDR10 video to Dolby Vision. For example, you shouldn't convert SDR 601 to Dolby Vision. Converting a non-HDR10 video to Dolby Vision doesn't comply with the usage intended by Dolby Vision. After conversion of the color space, the color map of the video will be completely wrong.

The only color space that you should convert to Dolby Vision is HDR10.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
