---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/automatic-rotation.html
---

# Configuring automatically detected rotation
<a name="automatic-rotation"></a>

If your video has embedded rotation metadata, AWS Elemental MediaConvert can detect it and automatically rotate your video content so that it's oriented correctly in your outputs.

**Note**
AWS Elemental MediaConvert doesn't pass through rotation metadata. Regardless of how you set **Rotate**, job outputs don't have rotation metadata.

**To enable automatic rotation**

1. Check that your input container is .mov or .mp4 and that your input has rotation metadata.

1. On the **Create job** page, in the **Job** pane on the left, in the **Inputs** section, choose the input that has rotation metadata.

1. In the **Video selector** section on the left, for **Rotate**, choose **Automatic**.

**Note**
AWS Elemental MediaConvert doesn't rotate images and motion images that you overlay. If you use the image inserter feature or the motion image inserter feature with the rotate feature, rotate your overlay before you upload it. Specify the position of your overlays as you want them to appear on the video after rotation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
