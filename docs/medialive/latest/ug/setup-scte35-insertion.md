---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/setup-scte35-insertion.html
---

# Inserting SCTE 35 messages using the schedule
<a name="setup-scte35-insertion"></a>

Use the [channel schedule](x-actions-in-schedule-SCTE35.md) to insert SCTE 35 messages into the outptus of a MediaLive CHANNEL. For example, you can add an action in the channel schedule to insert a splice insert in the running channel at a specific time.

The main use case for this feature is to add SCTE 35 messages, when the source content doesn't already include SCTE 35 messages.

To insert SCTE 35 messages in the content, create actions in the schedule. For detailed information, see [Creating an AWS Elemental MediaLive schedule](working-with-schedule.md).

After MediaLive inserts the SCTE 35 message in the channel, MediaLive processes the message in the same way as it would process SCTE 35 messages that were in the input. You define this processing when you create the channel and configure these options:
+ Blanking
+ Blackout
+ Manifest decoration
+ Passthrough

For a summary of these options, see [Scope of processing by feature](scope-by-feature.md) and [Supported features by output type](processing-applicability-by-output-type.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
