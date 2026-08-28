---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/mxf.html
---

# Creating MXF outputs
<a name="mxf"></a>

MXF is an output container format that carries video content for editing, archiving, and exchange. The MXF format is governed by a set of specifications, some of which define *MXF profiles*, also called shims. These MXF profiles lay out constraints on encoding settings including video codec, resolution, and bitrate.

To make sure that your outputs comply with these specifications, you can use the MediaConvert automatic profile selection. When you do that, MediaConvert automatically encodes the correct profile, based on the values you choose for your codec, resolution, and bitrate. For more information, see [Working with default MXF profiles](default-automatic-selection-of-mxf-profiles.md).

You can also explicitly choose your MXF profile. When you do so in the MediaConvert console, MediaConvert automatically populates the dropdown list for **Video codec** with only valid codecs. When you aren't using automatic profile selection, refer to the relevant specifications for constraints on your resolution and bitrate.

**Note**
When you manually specify your MXF profile, you must set up your output in a way that is compatible with that specification. You can submit jobs with incompatible MXF profiles and encoding settings, but those jobs will fail.

**Topics**
+ [List of codecs supported within each MXF profile](codecs-supported-with-each-mxf-profile.md)
+ [Job settings to create an MXF output](setting-up-an-mxf-job.md)
+ [Working with default MXF profiles](default-automatic-selection-of-mxf-profiles.md)
+ [MXF output requirements](mxf-job-limitations.md)
+ [XDCAM RDD9 output requirements](xdcam-rdd9.md)
+ [Audio settings requirements for different MXF profiles](output-audio-requirements-for-each-mxf-profile.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
