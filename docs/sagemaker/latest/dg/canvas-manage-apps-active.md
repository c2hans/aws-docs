---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-apps-active.html
---

# Check for active applications
<a name="canvas-manage-apps-active"></a>

To check if you have any actively running SageMaker Canvas applications, use the following procedure.

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation pane, choose **Dashboard**.

1. In the **LCNC** section, there is a row for Canvas that tells you how many active apps are running. Choose the number to view the list of apps.

The **Status** column displays the status of the application, such as **Ready**, **Pending**, or **Deleted**. If the application is **Ready**, then your SageMaker Canvas workspace instance is active. You can delete the application from the console, or you can reopen Canvas and log out.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
