---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/color-space-scenario-correct.html
---

# Scenario B – Metadata can be corrected with force
<a name="color-space-scenario-correct"></a>

During assessment of the MediaLive input, you might have determined the following:
+ The content is in one color space, and that is a supported color space.
+ The color space metadata is inaccurate. It could be any combination of inaccurate, missing, unknown, or unsupported (inaccurately marked as a color space that MediaLive doesn't support).

Note that this is the scenario that always applies if the input is from an AWS Elemental Link device.

You have this option for handling the metadata in the output:

**Correct the metadata**

You can correct the metadata. Follow the procedure in [Set up inputs to correct metadata](color-space-input-setup.md), and set the key fields as follows:
+ **Color space **field – Set to the color space that has unacceptable metadata.
+ **Color space usage **field – Set to **FORCE**

During processing, MediaLive will create metadata of the specified color space for all missing, unmarked, and unknown metadata. It will also change all existing metadata to the specified color space. (It will *force* the metadata.)

After ingest, all the content in the input will be consistently marked as one color space.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
