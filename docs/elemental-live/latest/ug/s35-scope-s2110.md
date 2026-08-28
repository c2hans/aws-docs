---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/s35-scope-s2110.html
---

# SMPTE 2110 output
<a name="s35-scope-s2110"></a>

SMPTE 2110 output supports passthrough of the SCTE-35 messages. Therefore, workable options are:

| SCTE-35 passthrough | Insertion of SCTE-35 messages | Manifest decoration | Blanking and blackout | Effect |
| --- | --- | --- | --- | --- |
| Enabled | Yes or No | Not applicable | Yes or No | Turns on passthrough of SCTE-35 messages. In this case, you could also insert more SCTE-35 messages if desired. Elemental Live converts all these SCTE-35 messages to SCTE-104 messages in the ancillary data stream in the output.You could also implement blanking and blackout. |
| Disabled | No | Not applicable | No | Doesn't include SCTE-104 messages in the output.<br />Do not insert extra messages: they are simply get stripped out of the output. Do not implement blanking or blackout.<br />Choose this option only if, in a downstream system, you do not want to replace video that was originally marked by cues.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
