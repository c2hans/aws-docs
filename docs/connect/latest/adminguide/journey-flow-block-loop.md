---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/journey-flow-block-loop.html
---

# Loop
<a name="journey-flow-block-loop"></a>

## Description
<a name="journey-flow-block-loop-description"></a>

Counts the number of times customers are looped through the **Looping** branch.
+ After the loops are completed, the **Complete** branch is followed.

## Configuration tips
<a name="journey-flow-block-loop-configuration-tips"></a>

If you enter 0 for the loop count, the **Complete** branch is followed the first time this block runs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
