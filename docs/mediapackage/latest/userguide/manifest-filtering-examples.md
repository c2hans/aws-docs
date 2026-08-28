---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/manifest-filtering-examples.html
---

# Manifest filtering examples in AWS Elemental MediaPackage
<a name="manifest-filtering-examples"></a>

These are MediaPackage manifest filtering examples.

**Example 1: Include only videos with specific heights**
You want to include only videos with heights that the most popular playback devices support. You set the `video_height` to filter out video streams that don't meet one of these height requirements: 240p through 360p, 720p through 1080p, 1440, or 2160p.

`?aws.manifestfilter=video_height%3A240-360%2C720-1080%2C1440%2C2160`

**Example 2: Target a player that supports AVC and a 44.1k audio sample rate**
The viewer is playing content on a device that can only support AVC and a 44.1k audio sample rate. You set the `video_codec` and `audio_sample_rate` to filter out streams that don't fit these requirements.

`?aws.manifestfilter=audio_sample_rate%3A0-44100%3Bvideo_codec%3Ah264`

**Example 3: Restrict 4k HEVC content**
Your 4K HEVC stream is 15 Mbps, and all your other streams are less than 9 Mbps. To exclude the 4K stream from the stream set, you set a threshold of 9,000,000 bits per second to filter out the higher bitrate.

`?aws.manifestfilter=video_bitrate:0-9000000`

**Example 4: Include video between 23.976 and 30 frames per second**
To only include video within a certain frame rate range, use `video_framerate`. This parameter accepts floating-point numbers with up to three optional decimal values.

`?aws.manifestfilter=video_framerate:23.976-30`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
