---
source_url: https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode-pools.html
---

# Running mode for WorkSpaces Pools
<a name="running-mode-pools"></a>

The running mode of a WorkSpaces Pool determines its immediate availability and how you pay for it. You can choose between the following running modes when you create a WorkSpaces Pool:
+ **AutoStop** — Instances of a WorkSpaces Pool are billed an hourly usage fee based on the bundle chosen, only for the instances that are connected to users. Instances within a WorkSpaces Pool that are not connected to users are billed a low stopped-instance hourly fee. When users initiate their session, they start streaming after 1-2 minutes.
+ **AlwaysOn** — Running instances of a WorkSpaces Pool are billed the applicable hourly usage fee, even when users aren't connected. This mode is best for users who don’t want to wait for their streaming to start.

For more information, see [WorkSpaces Pricing](https://aws.amazon.com/workspaces/pricing/).

**Topics**
+ [Modify the running mode](modify-running-mode-pool.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
