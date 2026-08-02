---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/dolby-vision-job-limitations-and-requirements.html
---

# Dolby Vision input format support and job setting requirements
<a name="dolby-vision-job-limitations-and-requirements"></a>

The tables in this section describe Dolby Vision input format support and job setting requirements for implementation with AWS Elemental MediaConvert.

The following table describes input format requirements for Dolby Vision Profile 5 or Profile 8.1 outputs.

| Supported inputs with Dolby Vision metadata | Supported inputs without Dolby Vision metadata | Supported output Dolby Vision profile |
| --- | --- | --- |
| IMF, MXF[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/dolby-vision-job-limitations-and-requirements.html)<br />QuickTime (.mov)[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/dolby-vision-job-limitations-and-requirements.html) | HDR10[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/dolby-vision-job-limitations-and-requirements.html)<br /> SDR [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/dolby-vision-job-limitations-and-requirements.html) | Profile 5<br />Profile 8.1 |

The following table describes feature limitations and job requirements for Dolby Vision outputs.

| Feature | Job setting requirement |
| --- | --- |
| Maximum number of input videos or input clips<br />(For Profile 8.1 outputs) | One per job |
| Input Frame rate | All inputs must have the same frame rate. Frame rate conversion is not supported. |
| Input Image inserter | Supported <br />(The brightness of your image will vary along with your video content.) |
| Output Frame rate | Follow source |
| Output Image inserter | **Disabled** |
| Output Video codec | HEVC (H.265) |
| Output Color metadata | Insert |
| Output video Resolution (w x h) | Maximum width: 4096Maximum height: 4096 |
| Output video codec Profile | Main10/Main or Main10/High |
| Captions Destination type | Burn-in captions are not supported. |
| Respond to AFD | None |
| Color corrector preprocessor | Disabled |
| Timecode burn-in preprocessor | Disabled |
| Noise reducer preprocessor | Disabled |
| Motion image inserter | Disabled |
| Queue type | **On-demand queue** |
