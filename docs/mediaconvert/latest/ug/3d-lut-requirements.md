---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/3d-lut-requirements.html
---

# 3D LUTs job settings requirements
<a name="3d-lut-requirements"></a>

When you include 3D LUTs as part of your MediaConvert job, you must also include the following settings:

**Input color space**
Specify which inputs use this 3D LUT, according to the input's color space.

**Input mastering luminance**
(Optional) Include **Input mastering luminance** only when your input has an **HDR10** or **P3D65 (HDR)** color space. Otherwise, keep blank. Use to select between inputs with different mastering luminances.

**Output color space**
Specify which outputs use this 3D LUT, according to the output's color space.

**Output mastering luminance**
(Optional) Include **Output mastering luminance** only when your output has an **HDR10** or **P3D65 (HDR)** color space. Otherwise, keep blank. Use to select between outputs with different mastering luminances.

**.cube file**
Specify an Amazon S3, HTTP, or HTTPS URL for your .cube file. MediaConvert accepts .cube files up to 8MB in size.

**Color corrector**
Specify an output color space in the **Color corrector** preprocessor for your video output.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
