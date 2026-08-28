---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/mv-hevc-supported-encoding.html
---

# Supported encoding settings for MV-HEVC
<a name="mv-hevc-supported-encoding"></a>

MV-HEVC outputs support the same H.265 encoding settings as standard H.265 outputs, including all resolutions, frame rates, rate control modes, and codec profiles. For details about H.265 encoding settings, see [HEVC (H.265)](supported-containers-codecs-details.md#codec-hevc).

MV-HEVC outputs support accelerated transcoding. For more information, see [Accelerated transcoding](accelerated-transcoding.md).

**Note**
MediaConvert automatically forces HVC1 sample entry type for all MV-HEVC outputs. You do not need to set this manually.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
