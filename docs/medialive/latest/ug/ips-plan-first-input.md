---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/ips-plan-first-input.html
---

# Identify the first input for the channel
<a name="ips-plan-first-input"></a>

Identify an input that you will set up as the first input in the list of input attachments for the MediaLive channel:
+ This input won't be the first input to ingest because you will use the schedule to switch to the first input to ingest.
+ It can't be a dynamic file input. It must be either a live input or a static file input in order for the channel to start.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
