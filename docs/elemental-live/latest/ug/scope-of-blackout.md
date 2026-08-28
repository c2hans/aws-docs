---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/scope-of-blackout.html
---

# Scope of blackout of SCTE-35 messages
<a name="scope-of-blackout"></a>

All SCTE-35 messages that are “Other type” are blanked out as follows:

| SCTE-35 segmentation type | Blanking |
| --- | --- |
| Programs | Always |
| Chapters | Always |
| Unscheduled events | Always |
| Network  | See below. |

**How Network End Blackout Differs from Other Events**
Network end blackout is different from the other events that trigger a blackout because:
+ With Network, blanking starts when the "Network End" instruction is encountered and ends when the "Network Start" instruction is encountered.
+ With other events, blanking starts when the “event start” instruction is encountered and ends when the “event end” instruction is encountered.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
