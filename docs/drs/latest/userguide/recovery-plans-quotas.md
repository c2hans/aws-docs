---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/recovery-plans-quotas.html
---

# Recovery plan quotas
<a name="recovery-plans-quotas"></a>

The following quotas apply to recovery plans in each AWS account and Region:

| Resource | Quota |
| --- | --- |
| Recovery plans per account, per Region | 1,000 |
| Steps per recovery plan | 20 |
| Source servers per recovery plan, across all steps | 100 |
| Concurrent executions per recovery plan | 1 |
| Wait step duration | 1–120 minutes |
| Maximum duration of a single execution | 24 hours |

The AWS Elastic Disaster Recovery service quotas that apply to an individual recovery, such as the number of concurrent recovery jobs and the number of source servers per account, also apply to the recoveries that a plan starts. A plan does not raise or bypass those quotas.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
