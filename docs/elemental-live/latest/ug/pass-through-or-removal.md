---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/pass-through-or-removal.html
---

# Passthrough or removal of SCTE messages
<a name="pass-through-or-removal"></a>

SCTE-35 messages from the input can be passed through (included) in the data stream for the following outputs.
+ Archive outputs with MPEG-2 as the container: You specify whether to pass through at the output level.
+ HLS: You specify whether to pass through at the output group level: passthrough or removal applies globally to all outputs in the output group.
+ UDP/TS: You specify whether to pass through at the output level: for each individual output in the output group.

SCTE-104 messages are handled for each output as follows:
+ If you choose to pass through the SCTE-35, then all SCTE-104 messages are converted to SCTE-35 messages (of the same message type) and included in the data stream.
+ If you choose to remove the SCTE-35 messages, the SCTE-104 messages are also removed.

**Topics**
+ [Archive procedure](pass-through-or-removal-archive.md)
+ [Apple HLS passthrough procedure](pass-through-or-removal-apple-hls.md)
+ [UDP/TS procedure](pass-through-or-removal-udp-ts.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
