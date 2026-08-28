---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/video-overlays-restrictions.html
---

# Video overlay feature limitations
<a name="video-overlays-restrictions"></a>

Video overlays have the following restrictions:
+ MediaConvert does not support audio playback or separate captions for video overlays. During a video overlay, any audio or captions from your base input video will continue uninterrupted.
+ Video overlays are specific to individual video inputs. For example, if your job settings include three video inputs, you can add an individual video overlay to **Input 1**, **Input 2**, and/or **Input 3**. You cannot however add a single video overlay that spans across all three inputs.
+ You can include up to 99 video overlays in your job settings and up to 99 input clips in each video overlay.
+ MediaConvert does not support transparency for video overlays. Any alpha channels present in your input will be black in your output.
+ For consistency in color and formatting in your output video image, we recommend that you specify video overlay files with accurate and complete color metadata.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
