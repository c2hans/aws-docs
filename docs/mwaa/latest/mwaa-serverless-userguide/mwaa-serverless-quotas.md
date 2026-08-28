---
source_url: https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/mwaa-serverless-quotas.html
---

# Quotas for Amazon MWAA Serverless
<a name="mwaa-serverless-quotas"></a>

Your AWS account has default quotas for each AWS service. These were formerly called limits. Unless noted otherwise, each quota is Region-specific. You can request increases for some quotas, but other quotas can't be increased.

To view the quotas for Amazon MWAA Serverless, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). In the navigation pane, choose **AWS services** and select **Amazon MWAA Serverless**.

To request a quota increase, refer to [Requesting a Quota Increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*. If the quota isn't available in Service Quotas, use the [limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase).

Your AWS account has these quotas related to Amazon MWAA Serverless in each AWS Region.

| Resource | Default |
| --- | --- |
| Maximum workflows per account | 100 |
| Maximum workflow versions per workflow | 50 |
| Maximum concurrent runs per account | 100 |
| Maximum concurrent runs per workflow | 20 |
| Maximum XCom data in Kilobytes | 100KB |
| Maximum DAG definition size in Kilobytes | 50KB |
| Maximum code storage per account | 75 GB |
| Maximum task execution timeout | 60 minutes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Workflows for Apache Airflow Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
