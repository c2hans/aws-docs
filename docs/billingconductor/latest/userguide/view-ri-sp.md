---
source_url: https://docs.aws.amazon.com/billingconductor/latest/userguide/view-ri-sp.html
---

# View your Savings Plans and Reservations inventory
<a name="view-ri-sp"></a>

You can view Savings Plans and Reservations inventory for AWS accounts in Billing Conductor billing groups. The primary billing group account can see the inventory of accounts in the billing group. Savings Plans and Reservations are shared only within billing groups, despite preferences in the billable domain.

Billing group managed accounts, or billing group members, can view Reservations and Savings Plans inventory if they were purchased in that account.

**To view your Savings Plans inventory (billing group primary account only)**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Savings Plans**, under **Inventory**.

**To view your Reservations inventory (billing group primary account only)**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Reservations**, under **Overview**.

If you're using AWS Organizations, management accounts can view Savings Plans and Reservations inventory.

**Note**
For billing group member accounts, Queued Savings Plans are only visible in the **Account inventory** page of the AWS account purchasing the Savings Plans (not in the **Organizations inventory** for primary accounts).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
