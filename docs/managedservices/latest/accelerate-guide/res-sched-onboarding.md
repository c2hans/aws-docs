---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/res-sched-onboarding.html
---

# Onboarding AMS Resource Scheduler
<a name="res-sched-onboarding"></a>

Your account is not automatically onboarded to AMS Resource Scheduler when your account is onboarded to the AMS Accelerate operations plan. However, as part of account onboarding to the AMS Accelerate operation plan, or anytime after, you can request your Cloud Service Delivery Manager (CSDM) to onboard the account to AMS Resource Scheduler. Once your CSDM onboards the account, a CloudFormation stack containing AMS Resource Scheduler resources with default configuration, is automatically provisioned into your account.

After the AMS Resource Scheduler is provisioned in your account, we recommend you review the default configuration and, if required, customize configurations such as tag key, timezone, scheduled services, and so forth, based on your preferences. For details on the recommended customizations, see [Customizing AMS Resource Scheduler](res-sched-customizing.md), next.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
