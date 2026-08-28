---
source_url: https://docs.aws.amazon.com/elemental-server/latest/ug/blanking-and-pass-through-and-manifest-decoration.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Blanking and Passthrough and Manifest Decoration
<a name="blanking-and-pass-through-and-manifest-decoration"></a>

It is important to understand that the logic for blanking ad content works on the video content associated with the “ad avail event” while the logic for passthrough and manifest decoration works with the actual SCTE-35 message.

So you can blank ad avails and not pass through SCTE-35 messages or not blank ad avails and not pass through SCTE-35 messages and decorate the manifest, or any combination: the actions are independent.

The only exception to this rule is for HLS outputs: manifest decoration and passthrough are either both enabled or both disabled.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
