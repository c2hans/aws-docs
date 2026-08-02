---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/encoding-options.html
---

# Encoding options
<a name="encoding-options"></a>

The Video on Demand on AWS solution leverages MediaConvert job templates to define the solution’s encoding options. The solution can encode your source videos into H.264 and H.265; SD, HD, and 4K MP4; and SD and HD HTTP Live Streaming (HLS), and Dynamic Adaptive Streaming over HTTP (DASH). The workflow can be configured to encode all videos in the same or to use metadata files to apply encoding settings on a video-by-video basis.

By default, the solution creates three custom templates that produce UHD, HD, and SD output. Each template creates HTTP Live Streaming (HLS). Additionally, the solution supports Microsoft Smooth Streaming (MSS) and Common Media Application Format (CMAF) outputs.

The workflow selects one of the three templates, based on the resolution of the source video. You can also customize the solution to work with any valid MediaConvert template. For more information, refer to [MediaConvert templates](mediaconvert-templates.md).

## Quality-defined variable bitrate mode
<a name="quality-defined-variable-bitrate-mode"></a>

This solution leverages MediaConvert [Quality-Defined Variable Bitrate](https://aws.amazon.com/media/tech/quality-defined-variable-bitrate-qvbr/) (QVBR) encoding mode which ensures consistent, high-quality video transcoding with the smallest file size for any type of source video content. With QVBR, the encoder determines the right number of bits to use for each part of the video to maintain the video quality that you specify. The solution configures the encoding templates to activate QBVR mode with the recommended settings for each output. For more information, refer to [MediaConvert templates](mediaconvert-templates.md).

## Accelerated transcoding
<a name="accelerated-transcoding"></a>

This solution includes an option to activate Accelerated Transcoding in MediaConvert which increases the processing speed of file-based video encoding jobs by up to 25 times. For more information, refer to the [MediaConvert documentation](https://docs.aws.amazon.com/mediaconvert/latest/ug/accelerated-transcoding.html).

**Important**
There are 2 options to turn on acceleration. The **Preferred** option turns on acceleration, but falls back to standard encoding if the source file isn’t supported. The **Enabled** option applies acceleration to every encoding job, and the job will fail if the source file is not supported.

## Frame capture
<a name="frame-capture"></a>

This solution can also create a set of thumbnails from your source videos. If this feature is turned on, the solution will create a set of thumbnails for each selected output. The thumbnails are stored in the Amazon S3 bucket with your video output.
