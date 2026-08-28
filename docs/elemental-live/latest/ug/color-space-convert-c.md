---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-convert-c.html
---

# Converting an HDR color space to SDR
<a name="color-space-convert-c"></a>

You can convert HDR10 or HLG video to an SDR color space. In this case, Elemental Live makes the following changes:
+ It changes the pixel values, if necessary, to fit the colors into the smaller color space.
+ It changes the color space metadata to identify the new color space.
+ It applies the new brightness function to the video.
+ It removes any display metadata because the SDR color spaces don't include display metadata.

After the conversion, the video complies completely with the new color space. The color will be less rich. The color will match the new brightness function.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
