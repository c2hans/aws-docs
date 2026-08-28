---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-ffmpeg-encode.html
---

# Encode video with FFmpeg on Deadline Cloud
<a name="examples-jb-ffmpeg-encode"></a>

The [ffmpeg\_encode\_video](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/ffmpeg_encode_video) job bundle takes a directory of sequentially numbered image files and encodes them into an MP4 video using FFmpeg. The bundle is useful as a standalone utility for converting render output to video, or as a reference for adding a video encoding step to a multi-step render pipeline.

The bundle includes the following features:
+ Encodes numbered image sequences (PNG, EXR, JPEG, and others) into H.264 MP4 video.
+ Supports customizable frame rate, quality (CRF), and encoding speed presets.
+ Uses `####` hash-mark patterns for input file naming, automatically converted to FFmpeg's printf-style `%04d` format.
+ Works with job attachments or shared file systems.
+ Produces broadcast-safe output with BT.709 color space and `faststart` for web streaming.

FFmpeg is not available from the `deadline-cloud` conda channel. To run this bundle on a service-managed fleet, use `conda-forge` as the `CondaChannels` parameter for the queue environment.

Submit the bundle:

```
deadline bundle submit ffmpeg_encode_video/ \
  -p InputDir={{path-to-frames}} \
  -p InputFilePattern="render.####.png" \
  -p StartFrame=1 \
  -p EndFrame=250 \
  -p OutputDir={{path-for-output}} \
  -p OutputFileName="my_video.mp4"
```

To add video encoding to an existing render job, copy the `EncodeVideo` step from this bundle's template into your own template, add a `dependencies` entry so the encode step runs after rendering, and add `conda-forge` to the `CondaChannels` parameter. For a complete multi-step pipeline example, see [Render a turntable video with Maya and Arnold on Deadline Cloud](examples-jb-turntable.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
