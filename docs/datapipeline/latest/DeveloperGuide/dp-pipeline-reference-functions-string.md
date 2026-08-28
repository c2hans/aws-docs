---
source_url: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-pipeline-reference-functions-string.html
---

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# String Functions
<a name="dp-pipeline-reference-functions-string"></a>

 The following functions are available for working with string values.

| Function | Description |
| --- | --- |
| \+ | Concatenation. Non-string values are first converted to strings.<br />Example: `#{"hel" + "lo"}`<br />Result: `"hello"` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
