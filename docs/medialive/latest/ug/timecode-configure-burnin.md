---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/timecode-configure-burnin.html
---

# Burning the timecode into output
<a name="timecode-configure-burnin"></a>

You can set up any video encode in a MediaLive channel to burn in the output timecode. The time code will become part of the video.

Note that the timecode burnin feature is independent of the timecode metadata feature. You don't have to enable timecode metadata in order to burn in the timecode.

**To burn the timecode into the video output**

1. On the **Create Channel **page, in the **Output groups **section, choose an output group, then choose an output.

1. Display the **Stream settings **section, and then choose the **Video **section. In **Codec settings**, choose the codec for this video encode. More fields appear.

1. Choose **Timecode**, then in **Timecode burn-in settings**, choose **Timecode burnin**. More fields appear.

1. Set the style and position of the timecode in the video frame. In the optional **Prefix** field, enter any descriptor. For example, **UTC-1**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
