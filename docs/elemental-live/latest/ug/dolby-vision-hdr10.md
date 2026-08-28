---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/dolby-vision-hdr10.html
---

# Dolby Vision color space
<a name="dolby-vision-hdr10"></a>

The information for handling video that is in the Dolby Vision color space has changed. AWS Elemental Live no longer requires source video to contain the RPUs that are used to produce some of the color space metadata. Now, Elemental Live produces the metadata without relying on external RPUs.

In addition, the information for Dolby Vision has been integrated into the standard section on color space, [Working with color space](hdr-working-with.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
