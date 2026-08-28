---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dynatrace-connection-limitations.html
---

# Dynatrace limitations
<a name="dynatrace-connection-limitations"></a>

The following are limitations or notes for Dynatrace:
+ Dynatrace doesn’t support either field based or record based partitioning.
+ For the Select All feature, if you provide the "field" in the filter then it will not allow records to be more then 10 per page.
+ The maximum page size supported is 500. If you select any of the [`evidenceDetails, impactAnalysis, recentComments`] fields while creating the flow then records per page will be defaulted to 10.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
