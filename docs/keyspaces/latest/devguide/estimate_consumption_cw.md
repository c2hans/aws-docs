---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/estimate_consumption_cw.html
---

# Estimate read and write capacity consumption with Amazon CloudWatch in Amazon Keyspaces
<a name="estimate_consumption_cw"></a>

To estimate and monitor read and write capacity consumption, you can use a CloudWatch dashboard. For more information about available metrics for Amazon Keyspaces, see [Amazon Keyspaces metrics and dimensions](metrics-dimensions.md).

To monitor read and write capacity units consumed by a specific statement with CloudWatch, you can follow these steps.

1. Create a new table with sample data

1. Configure a Amazon Keyspaces CloudWatch dashboard for the table. To get started, you can use a dashboard template available on [Github](https://github.com/aws-samples/amazon-keyspaces-cloudwatch-cloudformation-templates).

1. Run the CQL statement, for example using the `ALLOW FILTERING` option, and check the read capacity units consumed for the full table scan in the dashboard.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
