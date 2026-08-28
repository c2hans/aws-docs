---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.create-attachment.html
---

# Create a cross-account attachment in AWS Global Accelerator
<a name="cross-account-resources.create-attachment"></a>

Follow the steps in this section to create a cross-account attachment using the AWS Global Accelerator console.

This section explains how to create a cross-acount attachment by using the AWS Global Accelerator console. To learn about using API operations with Global Accelerator, see the [AWS Global Accelerator API Reference](https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html).

# To create a cross-account attachment

1. Open the Global Accelerator console at [ https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home).

1. Choose **Create cross-account attachment**.

1. On the **Create cross-account attachment** page, enter a name for the attachment.

1. Add the AWS accounts or the ARNs for the accelerators, or both, that you want to allow to add your resources.

1. Select the resources that you want to allow to be used. For example, to add resources that can added as endpoints, for each resource, choose an AWS Region. Then, from the drop-down menus, select an endpoint type (resource type) and the endpoint (resource) to add.

1. Choose **Create attachment**.

Note: To see the new cross-account attachment in your list of attachments, refresh the **Cross-account attachments** page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
