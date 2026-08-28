---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/about-overlay-scaling.html
---

# Sizing your overlay for scaling
<a name="about-overlay-scaling"></a>

In jobs that scale the video resolution, whether your overlay scales with your video depends on where you specify the image overlay. Motion image overlays and input overlays scale with the video; output overlays don't.

For example, suppose that the input video for your job is 1080 x 1920 and you specify three outputs at 720 x 1280, 480 x 640, and 360 x 480. Your square logo would be 10% of the width of your frames, and your overlay images would have the following resolutions:
+ For a motion image overlay or an input image overlay, provide an image that is 108 x 108. The service appropriately sizes each overlay on each output.
+ For an output image overlay on your 720 x 1280 output, provide an image that is 72 x 72.
+ For an output image overlay on your 480 x 640 output, provide an image that is 48 x 48.
+ For an output image overlay on your 360 x 480 output, provide an image that is 36 x 36.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
