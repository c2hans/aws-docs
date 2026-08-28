---
source_url: https://docs.aws.amazon.com/elemental-server/latest/ug/requirements-for-the-overlay-file.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Overlay File Requirements
<a name="requirements-for-the-overlay-file"></a>

Set up the image files that you want to insert over your video as follows:
+ **File type**: Use files with the extension `.png `or `.tga`.
+ **Aspect ratio**: Use any aspect ratio; the aspect ratio of the overlay file doesn't need to match the aspect ratio of the underlying video.
+ **Size in pixels**: Use any size. If the overlaid graphic is larger than the output video frame, the service crops the graphic at the edge of the frame.
**Note**
In jobs that scale the video resolution, whether your overlay scales with your video depends on where you specify the graphic overlay. For more information, see [Sizing Your Overlay to Account for Scaling](about-overlay-scaling.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
