---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/ug/delete-service-network.html
---

# Delete a VPC Lattice service network
<a name="delete-service-network"></a>

Before you can delete a service network, you must first delete all associations that the service network might have with any service, resource configuration, VPC, or VPC endpoint. When you delete a service network, we also delete all resources related to the service network, such as the resource policy, auth policy, and access log subscriptions.

**To delete a service network using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **VPC Lattice**, choose **Service networks**.

1. Select the check box for the service network, and then choose **Actions**, **Delete service network**.

1. When prompted for confirmation, enter **confirm**, and then choose **Delete**.

**To delete a service network using the AWS CLI**
Use the [delete-service-network](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/delete-service-network.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
