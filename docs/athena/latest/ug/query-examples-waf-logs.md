---
source_url: https://docs.aws.amazon.com/athena/latest/ug/query-examples-waf-logs.html
---

# Example queries for AWS WAF logs
<a name="query-examples-waf-logs"></a>

Many of the example queries in this section use the partition projection table created previously. Modify the table name, column values, and other variables in the examples according to your requirements. To improve the performance of your queries and reduce cost, add the partition column in the filter condition.

**Topics**
+ [Count referrers, IP addresses, or matched rules](query-examples-waf-logs-count.md)
+ [Query using date and time](query-examples-waf-logs-date-time.md)
+ [Query for blocked requests or addresses](query-examples-waf-logs-blocked-requests.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
