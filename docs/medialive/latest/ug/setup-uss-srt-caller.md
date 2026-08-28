---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/setup-uss-srt-caller.html
---

# Ensure correct setup in the upstream system
<a name="setup-uss-srt-caller"></a>

An operator at the upstream server must set up the source content on the upstream system. Make sure that the operator sets up as follows:
+ They set up to deliver the correct number of sources:
  + If the MediaLive channel is a standard channel, set up two sources for the content. Make sure that the two source contents are identical in terms of video resolution and bitrate.
  + If the MediaLive channel is a single-pipeline channel, set up one source for the content.
+ They set up to make the content available at the agreed URLs, and they use the agreed application names and instance names. These URLs are the URLs that you obtained [earlier in this section](setup-mp4-obtain-info.md), and that you configured into the RTMP input. They correspond to the URLs shown in [the diagram after this procedure](setup-result-rtmp-push.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
