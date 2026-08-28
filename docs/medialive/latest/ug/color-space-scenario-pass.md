---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/color-space-scenario-pass.html
---

# Scenario A – Metadata is accurate
<a name="color-space-scenario-pass"></a>

During assessment of the MediaLive input, you might have determined the following:
+ The content is in one color space, the color space is supported, and the color space metadata is accurate.
+ Or different portions of the content are in different color spaces, and the color space metadata is accurate for each portion.

You have these options for handling the metadata in the output:

**Include the metadata**

Follow the procedure in [Set up inputs to correct metadata](color-space-input-setup.md), and set the key fields as follows:
+ **Color space **field – Set to **FOLLOW**
+ **Color space usage **field – MediaLive ignores this field.

During processing, MediaLive will read the metadata, in order to identify the color space.

**Remove the metadata**

You might have already decided to remove the color space metadata even though it is accurate. For example, the color space might change frequently within the input, or between one input and another. You know that there is a system downstream of MediaLive that can't handle changes in the metadata.

You can still convert or pass through the color space. It is safe to convert the color space because the metadata is reliable.

Follow the procedure in [Set up inputs to correct metadata](color-space-input-setup.md), and set the key fields as follows:
+ **Color space **field – Set to **FOLLOW**
+ **Color space usage **field – MediaLive ignores this field.

During processing, MediaLive will read the metadata, in order to identify the color space.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
