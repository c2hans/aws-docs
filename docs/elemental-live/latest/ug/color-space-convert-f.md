---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-convert-f.html
---

# Converting one SDR color space to another
<a name="color-space-convert-f"></a>

You can convert an SDR color space to another SDR color space. In this case, Elemental Live makes the following changes:
+ It changes pixels to values that represent the same color as the original values. The video now fits in the larger color space.
+ It changes the color space metadata to identify the new color space.
+ It applies the same brightness function to the video, because all the SDR color spaces use the same function.

After the conversion, the video complies completely with the new color space.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
