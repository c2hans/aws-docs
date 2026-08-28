---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/ips-step-plan-inputs.html
---

# Assess the sources
<a name="ips-step-plan-inputs"></a>

When planning a multiple-input MediaLive channel, you must identify all the sources that you need. You must then assess the audio and captions in each source to ensure that the source is suitable for an input-switching scenario.

**Result of this Step**

After this step, you have a set of sources that you can successfully set up as inputs and attach to the channel in order to implement input switching in the channel. You have categorized these sources by their type: live sources or file sources.

**Topics**
+ [Identify the sources](ips-collect-sources.md)
+ [Assess the video in the sources](ips-assess-video.md)
+ [Assess the audio in the sources](ips-assess-audio.md)
+ [Assess the captions in the sources](ips-assess-captions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
