---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/auto-rotate-requirements.html
---

# Input file requirements for video rotation
<a name="auto-rotate-requirements"></a>

You can use rotation for inputs that have the following video characteristics:
+ Progressive video
+ Chroma subsampling scheme 4:2:2 or 4:2:0

In addition to the general input restrictions for the rotate feature, to use *automatic* rotation your input file must conform to these limitations:
+ Input container: .mov or .mp4
+ Rotation metadata specifying 90, 180, or 270-degree rotation

  If your rotation metadata is within one degree less or more than the values listed here, the service will round to a supported value.

**Note**
If your input file has rotation metadata that specifies a rotation other than those listed here, the service defaults to no rotation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
