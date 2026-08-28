---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/using-variable-frame-rate-inputs.html
---

# Using variable frame rate inputs in AWS Elemental MediaConvert
<a name="using-variable-frame-rate-inputs"></a>

Some videos have a frame rate that varies over the duration of the video. Some cameras—for example, the cameras in many smartphones—automatically generate video that uses more frames for high-action sequences and fewer frames for sequences with less motion. MediaConvert supports variable frame rate (VFR) inputs, but creates only constant frame rate (CFR) outputs.

The default setting for output frame rate is **Follow source**. **Follow source** causes different behavior depending on whether your input video has a constant or variable frame rate.
+ For constant frame rate inputs, **Follow source** results in outputs that have the same frame rate as the input video.
+ For variable frame rate inputs, **Follow source** results in outputs that have a constant frame rate output, with a frame rate that is the average of the input frame rates, rounded up to the nearest whole number standard frame rate: 1, 5, 10, 15, 24, 30, 50, or 60 fps.

**Feature restrictions**
MediaConvert support for variable frame rate video is limited in these ways:
+ Variable frame rates are supported as input only. Outputs are only constant frame rate.
+ Variable frame rate inputs are supported in these containers only: MP4, MOV, WEBM, and MKV.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
