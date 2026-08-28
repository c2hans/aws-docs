---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/converting-color-space.html
---

# Configuring color space conversion
<a name="converting-color-space"></a>

The following procedure details how to configure a job to convert from one color space to another.

1. Confirm that MediaConvert supports the conversion that you want to do.

1. Set up your transcoding job as usual. For more information, see [Tutorial: Configuring job settings](setting-up-a-job.md).

1. On the **Create job** page, in the **Job** pane on the left, choose your HDR output.

1. At the bottom of the **Encoding settings** section on the right, choose **Preprocessors**.

1. Choose **Color corrector** to display the color correction settings.

1. For **Color space conversion**, choose the color space that you want for your output.

1. If you are converting to HDR 10, specify values for the **HDR master display information** settings.

   These values don't affect the pixel values that are encoded in the video stream. They are intended to help the downstream video player display content in a way that reflects the intentions of the content creator.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
