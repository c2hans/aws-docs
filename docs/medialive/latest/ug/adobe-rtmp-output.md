---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/adobe-rtmp-output.html
---

# RTMP output
<a name="adobe-rtmp-output"></a>

In an RTMP output, MediaLive supports SCTE 35 features as follows:
+ Passthrough of the SCTE 35 messages – Not applicable.
+ Manifest decoration – Not supported.
+ Blanking and blackout – Applicable. Content in the output is blanked or blacked out if the features are enabled at the channel level.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
