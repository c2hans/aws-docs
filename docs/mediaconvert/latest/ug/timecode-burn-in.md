---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/timecode-burn-in.html
---

# Burning in timecodes on the video frames
<a name="timecode-burn-in"></a>

The **Timecode burn-in** setting determines whether a given output has visible timecodes inscribed into the video frames themselves. The timecodes are not an overlay, but rather a permanent part of the video frames.

**To burn in timecodes in an output (console)**

1. On the **Create job** page, in the **Job** pane on the left, choose an output.

1. Under **Stream settings**, **Preprocessors**, choose **Timecode burn-in**.

1. Optionally, provide values for the **Prefix**, **Font size**, and **Position** settings. Even if you don't provide these values, timecodes are burned into your output using these default values:
   + **Prefix**: no prefix
   + **Font size**: **Extra Small (10)**
   + **Position**: **Top Center**

   For details about each of these settings, choose the **Info** link next to **Timecode burn-in**.

**To burn in timecodes in an output (API, SDK, and AWS CLI)**

1. In your JSON job specification, include the setting [TimecodeBurnin](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobs.html#jobs-prop-videopreprocessor-timecodeburnin). `TimecodeBurnin` is located in `Settings`, `OutputGroups`, `Outputs`, `VideoDescription`, `VideoPreprocessors`.

1. Optionally, provide values for the settings that are children of `TimecodeBurnin`. If you don't provide these values, timecodes are burned into your output using these default values:
   + `Prefix`: *no prefix*
   + `FontSize`: `10`
   + `Position`: `TOP_CENTER`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
