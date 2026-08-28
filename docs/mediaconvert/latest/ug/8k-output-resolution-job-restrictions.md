---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/8k-output-resolution-job-restrictions.html
---

# 8K output requirements
<a name="8k-output-resolution-job-restrictions"></a>

When your MediaConvert job has outputs with 8k (8192x4320) resolutions, your job is restricted in these ways:
+ You can't create Dolby Vision outputs.
+ You must send your job to an on-demand queue. Reserved queues can't run 8k jobs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
