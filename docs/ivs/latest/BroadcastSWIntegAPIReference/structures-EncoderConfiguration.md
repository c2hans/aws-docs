---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-EncoderConfiguration.html
---

# EncoderConfiguration
<a name="structures-EncoderConfiguration"></a>

Complex type specifying the stream’s video configuration to be used by the encoder.

## Contents
<a name="structures-EncoderConfiguration-contente"></a>
+ **bitrate\_interpolation\_points**
  + List of possible bitrates in kilobits per second providing interpolation points, to allow graceful bitrate degradation. The last value in the list must be the same as `bitrate`. The number of points can vary with the encoder. Each encoder's length of `bitrate_interpolation_points` must be the same for all configurations.
  + Type: Array of integers
  + Required: Yes
+ **framerate**
  + Framerate.
  + Type: [Framerate](structures-Framerate.md) object
  + Required: Yes
+ **gpu\_scale\_type**
  + Scaling algorithm used to scale from canvas dimensions to output dimensions. Default: `OBS_SCALE_BICUBIC`.
  + Type: String
  + Valid Values: `OBS_SCALE_AREA` \| `OBS_SCALE_BICUBIC` \| `OBS_SCALE_BILINEAR` \| `OBS_SCALE_LANCZOS` \| `OBS_SCALE_POINT`
  + Required: No
+ **height**
  + Resolution height in pixels.
  + Type: Integer
  + Valid Range: Minimum value of 64.
  + Required: Yes
+ **settings**
  + Encoder-specific settings.
  + Type: [VideoTrackSettings](structures-VideoTrackSettings.md) object
+ **type**
  + Type of encoder configuration.
  + Type: String
  + Valid Values: `jim_hevc_nvenc` \| `jim_nvenc`
  + Required: No
+ **width**
  + Resolution width in pixels.
  + Type: Integer
  + Valid Range: Minimum value of 64.
  + Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
