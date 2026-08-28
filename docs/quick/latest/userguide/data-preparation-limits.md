---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/data-preparation-limits.html
---

# Data preparation limits
<a name="data-preparation-limits"></a>

Amazon Quick Sight's data preparation experience is designed to handle enterprise-scale datasets while maintaining optimal performance. The following limits ensure reliable functionality.

## Dataset size limits (SPICE)
<a name="dataset-size-limits"></a>
+ **Output size**: Up to 2TB or 2 billion rows
+ **Total input size**: Combined input sources cannot exceed 2TB
+ **Secondary tables size**: Combined size is limited to 20GB

**Note**
Primary tables are those with maxiumum size in a workflow; all others are secondary.

## Workflow structure limits
<a name="workflow-structure-limits"></a>
+ **Maximum steps**: Up to 256 transformation steps per workflow
+ **Source tables**: Maximum 32 import steps per workflow
+ **Output columns**: Up to 2048 columns at any step in the workflow and final output table with 2000 columns
+ **Divergent paths**: Maximum 5 paths from a single step (SPICE only, not applicable for DirectQuery)
+ **Dataset as a source**: Up to 10 levels for both SPICE and DirectQuery

These limits are designed to balance flexibility with performance, enabling complex data transformations while ensuring optimal analysis capabilities.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
