---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-rtmp-pull.html
---

# Channel input—RTMP pull input
<a name="input-rtmp-pull"></a>

To verify that the input is set up correctly, look at the **Input destinations** section. It shows the locations of the source video. You specified these locations when you created the input:
+ If the channel is set up as a standard channel, you specified two locations.
+ If the channel is set up as a single-pipeline channel, you specified one.

For example:

**rtmp://203.0.113.13:1935/live/curling/**

**rtmp://198.51.100.54:1935/live/curling/**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
