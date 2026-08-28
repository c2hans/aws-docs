---
source_url: https://docs.aws.amazon.com/redshift/latest/mgmt/modify-cluster-subnet-group.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Modifying a cluster subnet group
<a name="modify-cluster-subnet-group"></a>

After you've created a subnet group, you can modify its information on the Amazon Redshift console.The following procedure walks you through how to modify a subnet group for a provisioned cluster.

**To modify a cluster subnet group for a provisioned cluster**

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Configurations**, then choose **Subnet groups**. The list of subnet groups is displayed.

1. Choose the subnet group to modify.

1. For **Actions**, choose **Modify** to display the details of the subnet group.

1. Update information for the subnet group.

1. Choose **Save** to modify the group.

To change or remove subnets in some cases requires extra steps. For example, this AWS Knowledge Center article, [How do I move my provisioned Amazon Redshift cluster into a different subnet?](https://repost.aws//knowledge-center/redshift-move-subnet), describes a use case that covers moving a cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
