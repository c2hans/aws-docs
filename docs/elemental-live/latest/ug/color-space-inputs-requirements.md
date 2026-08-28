---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-inputs-requirements.html
---

# Requirements for inputs
<a name="color-space-inputs-requirements"></a>

**Supported input types**

AWS Elemental Live can work with the color space in all [supported input types](ref-inputs-and-codecs.md).

**Input requirements for producing Dolby Vision outputs**

There are specific requirements for a source that you plan to convert to Dolby Vision. These requirements are stipulated by Dolby Vision, and relate to the minimal video quality required to produce Dolby Vision outputs that meet the Dolby Vision standard::
+ The video source must be HD or 4K resolution. In other words, the source must be 1080p or better.
+ The video source must be in the HDR10 color space.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
