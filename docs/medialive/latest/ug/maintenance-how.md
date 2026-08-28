---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/maintenance-how.html
---

# How MediaLive performs channel maintenance
<a name="maintenance-how"></a>

At some point during the maintenance window (red mark), MediaLive starts the maintenance. There is no notification that maintenance is about to start on the channel.

There is no need to monitor the channel or to prepare for maintenance during the time leading up to the maintenance window.

MediaLive performs maintenance as follows:
+ If a channel is set up as a standard channel (with two pipelines), MediaLive always performs maintenance on one pipeline at a time. MediaLive stops one pipeline, performs the maintenance, and automatically restarts the pipeline. It then stops the second pipeline, performs the maintenance, and automatically restarts the second pipeline. In this way, there is typically no impact on the output from the channel.
+ If a channel is set up as a single-line channel, MediaLive stops the pipeline, which stops the channel. MediaLive performs the maintenance and restarts the channel. There will be no output from the channel while maintenance is being performed.

**Note**
Setting up with standard channels is an effective way to mitigate the impact of maintenance events. You might want to consider this mitigation for your most important 24x7 channels.

![](http://docs.aws.amazon.com/medialive/latest/ug/images/maintenance.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
