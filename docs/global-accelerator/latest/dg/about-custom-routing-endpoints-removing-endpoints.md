---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoints-removing-endpoints.html
---

# Remove a VPC subnet endpoint for a custom routing accelerator
<a name="about-custom-routing-endpoints-removing-endpoints"></a>

You can remove an Amazon Virtual Private Cloud (VPC) subnet endpoint from your custom routing accelerator so that user traffic no longer goes to destination Amazon EC2 instances in the subnet.

The steps in this section explain how to remove a VPC subnet endpoint on the AWS Global Accelerator console. To learn about using API operations with AWS Global Accelerator, see the [AWS Global Accelerator API Reference](https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html).

# To remove an endpoint

1. Open the Global Accelerator console at [ https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home).

1. On the **Accelerators** page, choose a custom routing accelerator.

1. In the **Listeners** section, for **Listener ID**, choose the ID of a listener.

1. In the **Endpoint groups** section, for **Endpoint group ID**, choose the ID of the endpoint group (AWS Region) of the VPC subnet endpoint that you want to remove.

1. Choose **Remove endpoint**.

1. In the confirmation dialog box, choose **Remove**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
