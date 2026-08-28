---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/about-color-metadata-simplified.html
---

# General information about color space
<a name="about-color-metadata-simplified"></a>

Following is some general information about how MediaLive handles color space.

**Topics**
+ [Components of color space](color-space-simplified-definitions.md)
+ [Color space standards that MediaLive supports](color-space-simplified-standards.md)

**Default behavior**

The default behavior for a channel is to pass through the color space and pass through the uncorrected color space metadata. Therefore, if you want to pass through the color space to all the outputs, you can stop reading this entire section about handling color space.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
