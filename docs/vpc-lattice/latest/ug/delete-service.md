---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/ug/delete-service.html
---

# Delete a VPC Lattice service
<a name="delete-service"></a>

To delete a VPC Lattice service, you must first delete all associations that the service might have with any service network. If you delete a service, all resources related to the service, such as the resource policy, auth policy, listeners, listener rules, and access log subscriptions, are also deleted.

**To delete a service using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **VPC Lattice**, choose **Service**.

1. On the **Services** page, select the service that you want to delete, and then choose **Actions**, **Delete service**.

1. When prompted for confirmation, choose **Delete**.

**To delete a service using the AWS CLI**
Use the [delete-service](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/delete-service.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
