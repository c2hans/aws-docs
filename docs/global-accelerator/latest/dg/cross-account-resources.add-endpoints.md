---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.add-endpoints.html
---

# Add cross-account endpoints in AWS Global Accelerator
<a name="cross-account-resources.add-endpoints"></a>

Follow the steps in this section to add a cross-account endpoints using the Global Accelerator console.

This section explains how to add cross-account endpoints by using the AWS Global Accelerator console. To learn about using API operations with Global Accelerator, see the [AWS Global Accelerator API Reference](https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html).

# To add a cross-account endpoint

1. When you create or update an accelerator, in the **Endpoints** section, choose **Add endpoint**.

1. On the **Add endpoints** page, select **Add a resource specified in a cross-account attachment**.

1. In the drop-down menu, select an AWS account that has created a cross-account attachment that includes you or the accelerator as a principal.

1. For **Endpoint type**, choose the type of resource that you want to add.

   Note that only the resource types included in the cross-account attachment appear in the drop-down menu.

1. For **Endpoint**, choose resource that you want to add.

   Note that only resources that are included in the cross-account attachment appear in the drop-down menu. To see resources that are not enabled by a cross-account attachment, clear the **Add a resource specified in a cross-account attachment** check box.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
