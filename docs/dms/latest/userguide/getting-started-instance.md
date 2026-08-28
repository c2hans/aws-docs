---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/getting-started-instance.html
---

# Create an instance profile for DMS Schema Conversion
<a name="getting-started-instance"></a>

Before you create an instance profile, configure a subnet group for your instance profile. For more information about creating a subnet group for your AWS DMS migration project, see [Creating a subnet group](subnet-group.md).

You can create an instance profile as described in the following procedure. In this instance profile, you specify network and security settings for your DMS Schema Conversion project.

**To create an instance profile**

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/).

1. In the navigation pane, choose **Instance profiles**, and then choose **Create instance profile**.

1. For **Name**, enter a unique name for your instance profile. For example, enter **sc-instance**.

1. For **Network type**, choose **IPv4** to create an instance profile that supports only IPv4 addressing. To create an instance profile that supports IPv4 and IPv6 addressing, choose **Dual-stack mode**.

1. For **Virtual private cloud (VPC)**, choose the VPC that you created in the prerequisites step.

1. For **Subnet group**, choose the subnet group for your instance profile. To connect to Amazon RDS databases, use a subnet group that includes public subnets. To connect to on-premises databases, use a subnet group that includes private subnets.

1. Choose **Create instance profile**.

To create a migration project, use this instance profile.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
