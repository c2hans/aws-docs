---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/percentileOver-function.html
---

# percentileOver
<a name="percentileOver-function"></a>

The `percentileOver` function calculates the *n*th percentile of a measure partitioned by a list of dimensions. There are two varieties of the `percentileOver` calculation available in Quick:
+ [percentileContOver](https://docs.aws.amazon.com/quicksight/latest/user/percentileContOver-function.html) uses linear interpolation to determine result.
+ [percentileDiscOver](https://docs.aws.amazon.com/quicksight/latest/user/percentileDiscOver-function.html) uses actual values to determine result.

The `percentileOver` function is an alias of `percentileDiscOver`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
