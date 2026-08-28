---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/tams-input.html
---

# Processing content from TAMS servers
<a name="tams-input"></a>

When you create jobs with AWS Elemental MediaConvert, you can process live and archived content directly from Time-addressable Media Store (TAMS) servers. MediaConvert communicates with your TAMS server to retrieve specific time segments and automatically generates the necessary manifests for processing.

Some use cases for TAMS inputs might include:
+ Extract highlights from live events for social media distribution.
+ Process archived broadcast content for new programming or documentaries.
+ Integrate with existing broadcast infrastructure and content management systems.

**Topics**
+ [How MediaConvert processes TAMS content](tams-input-processing.md)
+ [Configuring a job with TAMS inputs](tams-input-use.md)
+ [Time range format](tams-input-timerange.md)
+ [Gap handling options](tams-input-gap-handling.md)
+ [Requirements for TAMS inputs](tams-input-requirements.md)
+ [Troubleshooting TAMS inputs](tams-input-troubleshooting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
