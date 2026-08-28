---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/percentile-function.html
---

# percentile
<a name="percentile-function"></a>

The `percentile` function calculates the percentile of the values in measure, grouped by the dimension that's in the field well. There are two varieties of percentile calculation available in Quick:
+ [percentileCont](https://docs.aws.amazon.com/quicksight/latest/user/percentileCont-function.html) uses linear interpolation to determine result.
+ [percentileDisc (percentile)](https://docs.aws.amazon.com/quicksight/latest/user/percentileDisc-function.html) uses actual values to determine result.

The `percentile` function is an alias of `percentileDisc`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
