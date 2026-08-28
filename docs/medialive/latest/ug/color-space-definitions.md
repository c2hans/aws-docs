---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/color-space-definitions.html
---

# Definition
<a name="color-space-definitions"></a>

There are four components to color space:
+ The specific *color space* that applies to the video content. The color space specifies a range of pixel colors that can apply to the content.
+ The *color space metadata*, which identifies the color space being used. If this metadata is present, the content is said to be *marked* for a color space.
+ The *brightness function* that applies to the color space. The brightness function controls the brightness of each pixel. The brightness is also known as gamma tables, electro-optical transfer function (EOTF), and transfer function.
+ The *brightness metadata*, which identifies the brightness function being used.
+ The *display metadata * that applies to the color space. Not all standards have this metadata.

The video might use a specific *color space* and a specific *brightness function*. The video might also carry *color space metadata *that describes aspects of the color.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
