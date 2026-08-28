---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/xdcam-rdd9.html
---

# XDCAM RDD9 output requirements
<a name="xdcam-rdd9"></a>

MediaConvert supports the following combinations of encoding settings when your output **MXF profile** is **XDCAM RDD9**.

In this table, read down the rows to find the **Resolution** that you want. Then read across to find a valid combination of **Bitrate**, **Frame rate**, **Interlace mode**, **GOP size**, and **Codec profile**.

| Resolution | Bitrate(s) | Frame rate(s) | Interlace mode | GOP size | Codec profile |
| --- | --- | --- | --- | --- | --- |
| 1280x720 | 25M<br />35M<br />50M | 23.976<br />50<br />59.94 | Progressive | 12 | Main (HD420) |
| 1280x720 | 50M | 23.976<br />25<br />50<br />59.94 | Progressive | 12 | HD422 |
| 1280x720 | 50M | 29.97 | Progressive | 15 | HD422 |
| 1440x1080 | 17.5M<br />25M<br />35M | 23.976<br />25 | Progressive | 12 | Main (HD420) |
| 1440x1080 | 17.5M<br />25M<br />35M | 29.97 | Progressive | 15 | Main (HD420) |
| 1440x1080 | 17.5M<br />25M<br />35M | 25 | Interlaced | 12 | Main (HD420) |
| 1440x1080 | 17.5M<br />25M<br />35M | 29.97 | Interlaced | 15 | Main (HD420) |
| 1920x1080 | 50M | 23.976<br />25 | Progressive | 12 | HD422 |
| 1920x1080 | 50M | 29.97 | Progressive | 15 | HD422 |
| 1920x1080 | 50M | 25 | Interlaced | 12 | HD422 |
| 1920x1080 | 50M | 29.97 | Interlaced | 15 | HD422 |

For additional information about MXF RDD9 requirements, see the SMPTE RDD 9:2013 MXF interoperability specification.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
