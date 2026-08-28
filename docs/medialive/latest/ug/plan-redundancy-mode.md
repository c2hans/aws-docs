---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/plan-redundancy-mode.html
---

# Implementing pipeline redundancy
<a name="plan-redundancy-mode"></a>

You can set up a MediaLive channel with two encoding pipelines, to provide resiliency within the channel processing pipeline.

When you set up a channel with two encoding pipelines, both pipelines ingest the source content and produce output. If the current pipeline fails, the downstream system can detect that it is no longer receiving content and can switch to the other output. There is no disruption to the downstream system. MediaLive restarts the second pipeline within a few minutes.

A channel that has two encoding pipelines is called a *standard channel*.

If you don't want to implement pipeline redundancy, you set up the channel as a *single-pipeline channel*. If the single pipeline fails, MediaLive stops producing output to deliver to the downstream system.

**Topics**
+ [Deciding whether to implement pipeline redundancy](pipeline-redundancy-guidelines.md)
+ [Setting up a standard channel](standard-channel-procedure.md)
+ [Setting up a single-pipeline channel with upgrade options](single-channel-upgrade.md)
+ [Setting up a single-pipeline channel without upgrade potential](single-pipeline-no-upgrade.md)
+ [Changing pipeline redundancy in an existing channel](pipeline-redundancy-change.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
