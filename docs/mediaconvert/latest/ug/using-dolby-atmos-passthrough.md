---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/using-dolby-atmos-passthrough.html
---

# Configuring Dolby Atmos passthrough
<a name="using-dolby-atmos-passthrough"></a>

AWS Elemental MediaConvert can create Dolby Digital Plus with Atmos outputs by either encoding audio in 9.1.6, 7.1.4, or 5.1.4 PCM mono channels, or by passing through already encoded Dolby Digital Plus with Atmos content.

You set up your job to pass through Dolby Digital Plus with Atmos content in the same way that you pass through Dolby Digital and Dolby Digital Plus content.

**To set up a Dolby Atmos job, passing through finished audio content**

1. Open the MediaConvert console at [https://console.aws.amazon.com/mediaconvert](https://console.aws.amazon.com/mediaconvert).

1. Choose **Create job**.

1. Set up your input audio and video as described in [Tutorial: Configuring job settings](setting-up-a-job.md).

1. Set up your output groups, outputs, and video output selectors as described in [Tutorial: Configuring job settings](setting-up-a-job.md) and [Creating outputs](output-settings.md). Choose supported containers as listed in [Supported output formats](reference-codecs-containers.md).

1. Create audio output selectors as described in [Tutorial: Configuring job settings](setting-up-a-job.md) and [Creating outputs](output-settings.md).

   Set them up as follows:

   1. In the **Job** pane on the left, choose an output that includes audio.

   1. In the **Encoding settings** section, choose **Audio 1**.

   1. For **Audio codec**, choose **Passthrough**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
