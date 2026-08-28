---
source_url: https://docs.aws.amazon.com/glue/latest/dg/pendo-connector-limitations.html
---

# Limitations
<a name="pendo-connector-limitations"></a>

The following are limitations for the Pendo connector:
+ Pagination is not supported in Pendo.
+ Filtration is supported only by the Aggregate API objects(`Account`, `Event`, `Feature Event`, `Guide Events`, `Page Event`, `Poll Event`, `Track Event`, and `Visitor`)
+ DateTimeRange is mandatory filter parameter for Aggregate API objects (`Event`, `Feature Event`, `Guide Events`, `Page Event`, `Poll Event,` `Track Event`)
+ The dayRange period will be rounded down to the start of the period in the time zone. For example, if provided filter is `2023-01-12T07:55:27.065Z` then this time period will be rounded to the start of period, that is `2023-01-12T00:00:00Z` .

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
