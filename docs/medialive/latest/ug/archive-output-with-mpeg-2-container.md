---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/archive-output-with-mpeg-2-container.html
---

# Archive output with MPEG-2 container
<a name="archive-output-with-mpeg-2-container"></a>

In an Archive output (a transport stream in an MPEG-2 container), MediaLive supports SCTE 35 features as follows:
+ Passthrough of the SCTE 35 messages – Supported.
+ Manifest decoration – Not supported because these outputs don't have manifests.
+ Blanking and blackout – Applicable. Content in the output is blanked or blacked out if the features are enabled at the channel level.

Be careful of setting up so that you have removed messages from the input (passthrough disabled) and you have not enabled blanking and blackout. In this case, the video content that was marked by messages (in the input) will not be marked (in the output).
+ If you have the rights to that video content, there is no problem setting up this way.
+ If you don't have the rights, then the only way to find that content will be to look for the IDR i-frames that identify where the SCTE 35 message used to be.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
