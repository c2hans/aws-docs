---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/opl-frame-accuracy.html
---

# About output locking and frame accuracy
<a name="opl-frame-accuracy"></a>

You can implement output locking to produce video outputs that are *frame accurate *with each other. The frames from several outputs are *locked *together.

Frame accuracy means that two frames with the same timecode are identical in the following ways:
+ The same content—the same picture on the video frame.
+ The same segment number, manifest data, and so on.
+ The same presentation timestamp (PTS).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
