---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/hls-output.html
---

# HLS output
<a name="hls-output"></a>

In an HLS output (a transport stream), MediaLive supports SCTE 35 features as follows:
+ Passthrough of the SCTE 35 messages – Supported.
+ Manifest decoration – Supported.
+ Blanking and blackout – Applicable. Content in the output is blanked or blacked out if the features are enabled at the channel level.

MediaLive supports the following combinations of passthrough and manifest decoration:
+ Passthrough enabled, decoration enabled.
+ Passthrough disabled, decoration enabled.
+ Passthrough disabled, decoration disabled. Be careful of setting up with this combination but leaving blanking and blackout disabled. In this case, the video content that was marked by messages (in the input) are not marked (in the output). In addition, the manifests don't have information for identifying that video content.
  + If you have the rights to that video content, there is no problem setting up this way.
  + If you don't have the rights, the only way to find that content is to look for the IDR i-frames that identify where the SCTE 35 message used to be.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
