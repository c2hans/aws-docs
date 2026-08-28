---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/cloudwatch-pricing.html
---

# Pricing
<a name="cloudwatch-pricing"></a>

 The Amazon CloudWatch data source for Grafana uses the `ListMetrics` and `GetMetricData` CloudWatch API calls to list and retrieve metrics. Pricing for CloudWatch Logs is based on the amount of data ingested, archived, and analyzed via CloudWatch Logs Insights queries. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing).

 Every time you pick a dimension in the query editor, Grafana issues a `ListMetrics` request. Whenever you change the queries in the query editor, one new request to GetMetricData will be issued.

 API requests to retrieve data samples use the `GetMetricData` operation. This operation provides better support for CloudWatch metric math. It also supports the automatic generation of search expressions when using wildcard characters or turning off the **Match Exact** option. The `GetMetricData` operation incurs charges. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
