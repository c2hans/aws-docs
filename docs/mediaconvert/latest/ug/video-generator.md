---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/video-generator.html
---

# Generating black video
<a name="video-generator"></a>

This guide shows you how to generate black video with AWS Elemental MediaConvert. To generate black video, you can add an input and include **Video generator**, or create a video output from an input that doesn't have video.

Workflows to consider when generating black video:
+ Insert black video at the beginning of your content.
+ Insert black video between two inputs.
+ Insert black video at the end of your content.
+ Create a black video track for an audio-only or captions-only input.
+ Any previous combination.

**Topics**
+ [How to generate black video](configuring-video-generator.md)
+ [Feature limitations for Video generator](video-generator-limitations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
