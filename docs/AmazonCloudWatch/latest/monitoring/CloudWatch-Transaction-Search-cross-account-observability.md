---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-cross-account-observability.html
---

# Monitoring spans across accounts
<a name="CloudWatch-Transaction-Search-cross-account-observability"></a>

 Spans sent to X-Ray are ingested and managed in a log group called `aws/spans`. To monitor spans across multiple accounts, you must [enable Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-getting-started.html) across all source and monitoring accounts and [enable cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) for logs and traces. When you enable cross-account observability, you can search up to 10,000 accounts and get visibility into traces across accounts. This feature is provided at no extra cost for the `aws/spans` log group. If you enable cross-account observability for trace summaries, the first trace summary copy is free. For more information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
