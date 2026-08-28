---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enable-capacity-manager-account.html
---

# Enabling EC2 Capacity Manager at the account-level
<a name="enable-capacity-manager-account"></a>

Enable Capacity Manager at the account-level to monitor and analyze your EC2 capacity usage within a single AWS account. After you enable it, Capacity Manager collects data about your On-Demand Instances, Spot Instances, and Capacity Reservations to help you identify optimization opportunities and track usage patterns.

## Enable Capacity Manager at the account-level
<a name="enable-account-capacity-manager"></a>

------
#### [ Console ]

**To enable Capacity Manager for your account**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Capacity Manager**.

1. On the Capacity Manager page, choose **Enable in Region**.

------
#### [ AWS CLI ]

**To enable Capacity Manager for your account**
Run the following command:

```
aws ec2 enable-capacity-manager
```

------
#### [ PowerShell ]

**To enable Capacity Manager for your account**
Use the [Enable-EC2CapacityManager](https://docs.aws.amazon.com/powershell/latest/reference/items/Enable-EC2CapacityManager.html) cmdlet.

```
Enable-EC2CapacityManager
```

------

**Note**
After you enable Capacity Manager, it collects and aggregates 14 days of historical data. This process might take a few hours.
While collecting your historical data, an `initial-ingestion-in-progress` state is displayed. During this collection period you might observe gaps in your historical data. When data collection is complete, an `ingestion-complete` state is displayed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
