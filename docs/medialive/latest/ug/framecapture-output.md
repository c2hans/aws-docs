---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/framecapture-output.html
---

# Frame capture output
<a name="framecapture-output"></a>

In a Frame capture output, MediaLive supports SCTE 35 features as follows:
+ Passthrough of the SCTE 35 messages – Not applicable.
+ Manifest decoration – Not supported because these outputs don't have manifests.
+ Blanking and blackout – Applicable. Content in the output is blanked or blacked out if the features are enabled at the channel level.

A Frame capture output doesn't support passthrough of the SCTE 35 messages. However, if blanking or blackout is enabled (at the channel level), then content that falls between the start and stop of the blackout is blanked or blacked out, even though no SCTE 35 messages are present.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
