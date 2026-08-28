---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/ideal-usage-patterns.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Ideal usage patterns
<a name="ideal-usage-patterns"></a>

 Amazon Redshift is ideal for OLAP using your existing BI tools. Enterprises use Amazon Redshift to do the following:
+  Running enterprise BI and reporting
+  Analyze global sales data for multiple products
+  Store historical stock trade data
+  Analyze ad impressions and clicks
+  Aggregate gaming data
+  Analyze social trends
+  Measure clinical quality, operation efficiency, and financial performance in health care

 With the Amazon Redshift Spectrum feature, Amazon Redshift supports semi-structured data and extends your data warehouse to your data lake. This enables you to:
+  Run as-needed analysis on large volume event data such as log analysis and social media
+  Offload infrequently accessed history data out of the data warehouse
+  Join the external dataset with the data warehouse directly without loading them into the data warehouse

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
