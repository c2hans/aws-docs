---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-srt-pull.html
---

# Channel input—SRT caller input
<a name="input-srt-pull"></a>

To verify that the input is set up correctly, look at the **SRT caller settings** section. It shows the locations of the source video. This is the locations of the SRT listener. You specified these locations when you created the input:
+ If the channel is set up as a standard channel, you specified two locations.
+ If the channel is set up as a single-pipeline channel, you specified one.

For example, the information for one location, when source encryption is disabled:
+ **SRT listener address: 192.0.2.120**
+ **SRT listener port: 7001**
+ **Stream ID: mystream**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
