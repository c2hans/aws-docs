---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/timecode.html
---

# Working with timecodes and timestamps
<a name="timecode"></a>

MediaLive has timecodes for the input pipeline and the output pipeline. The two timecodes are separate from each other. You can't configure the input timecode. You can configure the behavior of the output timecode. You can also configure output to include the output timecode as metadata and/or to burn the output timecode into the video frame.

**Topics**
+ [About timecodes and timestamps](timecodes-about.md)
+ [Configuring the start time for the output timecode](timecode-configure-source.md)
+ [Including timecode metadata in the output](timecode-configure-metadata.md)
+ [Burning the timecode into output](timecode-configure-burnin.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
