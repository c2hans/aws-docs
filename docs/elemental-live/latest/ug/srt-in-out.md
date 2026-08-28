---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/srt-in-out.html
---

# Working with SRT
<a name="srt-in-out"></a>

Elemental Live supports both inputs and outputs that use the SRT (secure reliable transport) protocol.

Elemental Live can ingest a transport stream (TS) that is sent from an SRT caller. In this scenario, the upstream system initiates the handshake that precedes transmission. AWS Elemental Live is the SRT listener that accepts or rejects the handshake. The transport stream source can be encrypted with AES.

To work with SRT inputs, see [Ingesting SRT content](input-srt.md). To work with SRT outputs, see [Delivering TS using the SRT protocol](output-srt.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
