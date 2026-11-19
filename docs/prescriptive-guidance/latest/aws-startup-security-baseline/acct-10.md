---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-10.html
---

# ACCT.10 Configure AWS Budgets to monitor your spending

AWS Budgets enables monitoring of monthly costs and usage with notifications when costs are forecast to exceed target thresholds. Cost forecast notifications can indicate unexpected activity, which adds a layer of monitoring alongside other services, such as [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/). Monitoring your AWS costs helps you detect unexpected usage and avoid unplanned charges.

**To set up a budget**

1. See [Create a cost budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) in the AWS Billing and Cost Management documentation.

**Note**
AWS Budgets without actions are free with no budget limit. The first two action-enabled budgets per account are free; each additional action-enabled budget incurs a $0.10 daily cost. For more information, see [AWS Budgets pricing](https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/).
