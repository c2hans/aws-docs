---
source_url: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-pipeline-reference-functions-math.html
---

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# Mathematical Functions
<a name="dp-pipeline-reference-functions-math"></a>

The following functions are available for working with numerical values.

| Function | Description |
| --- | --- |
| \+ | Addition.<br />Example: `#{1 + 2}`<br />Result: `3` |
| - | Subtraction.<br />Example: `#{1 - 2}`<br />Result: `-1` |
| \* | Multiplication.<br />Example: `#{1 * 2}`<br />Result: `2` |
| / | Division. If you divide two integers, the result is truncated.<br />Example: `#{1 / 2}`, Result: `0`<br />Example: `#{1.0 / 2}`, Result: `.5` |
| ^ | Exponent.<br />Example: `#{2 ^ 2}`<br />Result: `4.0` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
