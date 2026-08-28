---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/subnet-group.html
---

# Creating a subnet group for an AWS DMS migration project
<a name="subnet-group"></a>

Before you create an instance profile, configure a subnet group for your instance profile.

**To create a subnet group**

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/).

1. In the navigation pane, choose **Subnet groups**, and then choose **Create subnet group**.

1. For **Name**, enter a unique name of your subnet group.

1. For **Description**, enter a brief description of your subnet group.

1. For **VPC**, choose a VPC that has at least one subnet in at least two Availability Zones.

1. For **Add subnets**, choose subnets to include in the subnet group. You must choose subnets in at least two Availability Zones.

   To connect to Amazon RDS databases, add public subnets into your subnet group. To connect to on-premises databases, add private subnets into your subnet group.

1. Choose **Create subnet group**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
