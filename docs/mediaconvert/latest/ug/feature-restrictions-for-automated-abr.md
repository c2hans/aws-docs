---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/feature-restrictions-for-automated-abr.html
---

# Job settings limitations for automated ABR
<a name="feature-restrictions-for-automated-abr"></a>

Jobs that include automated ABR output groups are restricted in the following ways:
+ You must use an on-demand queue. You can't use a reserved queue.
+ You can enable automated ABR in jobs and job templates only. You can't use automated ABR in output presets.
+ In a job that includes an automated ABR output group, all ABR output groups must use automated ABR.
+ Your output **Video codec** must be **AVC (H.264)** or **HEVC (H.265)**.
+ Your output video **Scaling behavior** must be **Default**, **Stretch to output**, **Fit**, or **Fill**. You can't use **Fit without upscaling**.
+ You must specify these required settings when you create your JSON job specification manually. The MediaConvert console sets them for you when you enable automated ABR.
  + Set `qualityTuningLevel` to `MULTI_PASS_HQ`.
  + Set `rateControlMode` to `QVBR`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
