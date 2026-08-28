---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-create-getready.html
---

# Getting ready
<a name="input-create-getready"></a>

Before you create any input, you should plan the workflow. Read the following sections:
+ [Preparing the upstream and downstream systems in a workflow](container-planning-uss-dss.md) – You must set up for delivery from the upstream system. The task of creating an input is part of that delivery setup. You must coordinate with your upstream system and content provider.
+ [Implementing pipeline redundancy](plan-redundancy-mode.md) – You must decide if you want to implement pipeline redundancy—whether you set up a standard channel or a single-pipeline channel. Implementing pipeline redundancy provides resiliency in the channel processing pipeline.
+ [Implementing automatic input failover](automatic-input-failover.md) – You must decide if you want to implement automatic input failover. Implementing automatic input failover provides resiliency upstream of the channel, for one of the channel's inputs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
