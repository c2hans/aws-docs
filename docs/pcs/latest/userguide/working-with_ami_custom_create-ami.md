---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ami_custom_create-ami.html
---

# Step 5 – Create an AMI compatible with AWS PCS
<a name="working-with_ami_custom_create-ami"></a>

After you have installed the required software components, you create an AMI that you can reuse to launch instances in AWS PCS compute node groups.

**Important**
AWS PCS currently requires a kernel with IPv4 support for local node communication, even when you use AWS PCS in an IPv6-only network.

**To create an AMI from your temporary instance**

1.  Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2).

1. In the navigation pane, choose **Instances**.

1.  Select the temporary instance that you created. Choose **Actions**, **Image**, **Create image**.

1.  For **Create image**, do the following:

   1.  For **Image name**, enter a descriptive name for the AMI.

   1.  (Optional) For **Image description**, enter a brief description of the purpose of the AMI.

   1.  Choose **Create image**.

1.  In the navigation pane, choose **AMIs**.

1.  Locate the AMI that you created in the list. Wait for its status to change from **Pending** to **Available**, then use it with a AWS PCS compute node group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
