---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-convert-b.html
---

# Converting one HDR color space to another
<a name="color-space-convert-b"></a>

You can convert video between the HDR10 color space and the HLG color space, in either direction. In this case, Elemental Live makes the following changes:
+ It changes the pixel values, if necessary, to fit the colors into the different color space.
+ It changes the color space metadata to identify the new color space.
+ It applies the new brightness function to the video.
+ If converting to HDR10, it calculates display metadata for the video.

After the conversion, the video complies completely with the new color space. The color will be slightly different, but probably not more or less rich. The color will match the new brightness function.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
