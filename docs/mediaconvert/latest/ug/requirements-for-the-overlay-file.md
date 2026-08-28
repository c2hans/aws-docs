---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/requirements-for-the-overlay-file.html
---

# Requirements for the overlay file
<a name="requirements-for-the-overlay-file"></a>

Set up the image files that you want to insert over your video as follows:
+ **File type**: Use .png or .tga.
+ **Aspect ratio**: Use any aspect ratio; it doesn't need to match the aspect ratio of the underlying video.
+ **Size in pixels**: Use any size. If the overlaid image is larger than the output video frame, the service crops the image at the edge of the frame.
**Note**
In jobs that scale the video resolution, whether your overlay scales with your video depends on where you specify the image overlay. For more information, see [Sizing overlays](about-overlay-scaling.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
