---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ami_custom_launch-instance.html
---

# Step 1 – Launch a temporary instance
<a name="working-with_ami_custom_launch-instance"></a>

Launch a temporary instance that you can use to install and configure the AWS PCS software and Slurm scheduler. You use this instance to create an AMI compatible with AWS PCS.

**To launch a temporary instance**

1.  Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2).

1.  In the navigation pane, choose **Instances**, then choose **Launch instances** to open the new launch instance wizard.

1.  (Optional) In the **Name and tags** section, provide a name for the instance, such as `PCS-AMI-instance`. The name is assigned to the instance as a resource tag (`Name=PCS-AMI-instance`).

1.  In the **Application and OS Images** section, select an AMI for one of the [supported operating systems](working-with_ami_installers.md#working-with_ami_installers_os).

1.  In the **Instance type** section, select a [supported instance type](working-with_ami_installers.md#working-wth_ami_installers_instance-types).

1.  In the **Key pair** section, select the key pair to use for the instance.

1.  In the **Network settings** section:

   1.  For **Firewall (security groups)**, choose **Select existing security group**, then select a security group that allows inbound SSH access to your instance.

1.  In the **Storage** section, configure the volumes as needed. Make sure to configure sufficient space to install your own applications and libraries.

1.  In the **Summary** panel, choose **Launch instance**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
