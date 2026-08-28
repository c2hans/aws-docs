---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/apple-hls-output.html
---

# Apple HLS output
<a name="apple-hls-output"></a>

Apple HLS output supports both passthrough of the SCTE-35 messages and manifest decoration. In fact, with HLS outputs, passthrough and manifest decoration are either both enabled or both disabled. Therefore, workable options are:

| SCTE-35 passthrough | Insertion of SCTE-35 messages | Manifest decoration | Blanking and blackout | Effect |
| --- | --- | --- | --- | --- |
| Enabled | Yes or No | Enabled | Yes or No | Turns on passthrough of SCTE-35 messages and manifest decoration. In this case, you could also insert more SCTE-35 message if desired. You could also implement blanking and blackout. |
| Disabled | No | Disabled | No | Turns off passthrough in order to remove SCTE-35 messages from the video stream. Turns off manifest decoration. Do not insert extra messages: they simply get stripped from the output. Do not implement blanking or blackout. <br />Choose this option only if, in a downstream system, you do not want to replace video that was originally marked by cues.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
