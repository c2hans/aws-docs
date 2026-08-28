---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/scheduled-input-switching.html
---

# Setting up for input switching
<a name="scheduled-input-switching"></a>

You can set up a MediaLive channel to ingest multiple sequential inputs, rather than setting it up to ingest only one input. You set up this *multiple-input channel* by attaching more than one input to the channel, and then adding actions in the channel's schedule that specify when to switch from one input to another.

**Topics**
+ [About multiple-input channels and input switching](ips-overview.md)
+ [Rules and limits for input switches](ips-limits.md)
+ [Setting up for input switching](setup-ips.md)
+ [Deleting actions from the schedule](ips-manage-schedule.md)
+ [Starting and restarting a channel that has multiple inputs](ips-start-channel-multi-inputs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
