---
source_url: https://docs.aws.amazon.com/glue/latest/dg/facebook-page-insights-connector-limitations.html
---

# Limitations and notes for Facebook Page Insights connector
<a name="facebook-page-insights-connector-limitations"></a>

The following are limitations or notes for the Facebook Page Insights connector:
+ Most metrics will update once every 24 hours.
+ Only the last two years of insights data is available.
+ Only 90 days of insights can be viewed at one time when using the `since` and `until` parameters.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
