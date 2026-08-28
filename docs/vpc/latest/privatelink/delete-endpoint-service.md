---
source_url: https://docs.aws.amazon.com/vpc/latest/privatelink/delete-endpoint-service.html
---

# Delete an endpoint service
<a name="delete-endpoint-service"></a>

When you are finished with an endpoint service, you can delete it. You can't delete an endpoint service if there are any endpoints connected to the endpoint service that are in the `available` or `pending-acceptance` state.

Deleting an endpoint service does not delete the associated load balancer and does not affect the application servers registered with the load balancer target groups.

**To delete an endpoint service using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoint services**.

1. Select the endpoint service.

1. Choose **Actions**, **Delete endpoint services**.

1. When prompted for confirmation, enter **delete** and then choose **Delete**.

**To delete an endpoint service using the command line**
+ [delete-vpc-endpoint-service-configurations](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpc-endpoint-service-configurations.html) (AWS CLI)
+ [Remove-EC2EndpointServiceConfiguration](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2EndpointServiceConfiguration.html) (Tools for Windows PowerShell)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
