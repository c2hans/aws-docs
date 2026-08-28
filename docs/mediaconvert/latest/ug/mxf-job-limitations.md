---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/mxf-job-limitations.html
---

# MXF output requirements
<a name="mxf-job-limitations"></a>

MediaConvert restricts MXF jobs in these ways:
+ You can put MXF outputs in a **File group** output group only.
+ You must choose a video codec that is supported with your MXF profile. The following table details which codecs are supported with each profile. For more information, see [List of codecs supported within each MXF profile](codecs-supported-with-each-mxf-profile.md).
+ You must set up your output audio tracks according to the requirements of the MXF profile. This applies whether you specify the profile or have MediaConvert automatically select it for you. For more information, see [Audio settings requirements for different MXF profiles](output-audio-requirements-for-each-mxf-profile.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
