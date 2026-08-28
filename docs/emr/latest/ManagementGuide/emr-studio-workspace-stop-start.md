---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-workspace-stop-start.html
---

# Resolve Workspace connectivity issues
<a name="emr-studio-workspace-stop-start"></a>

To resolve Workspace connectivity issues, you can stop and restart a Workspace. When you restart a Workspace, EMR Studio launches the Workspace in a different Availability Zone or a different subnet that is associated with your Studio.

**To stop and restart an EMR Studio Workspace**

1. Close the Workspace in your browser.

1. Navigate to the **Workspace** list in the console.

1. Select your Workspace from the list and choose **Actions**.

1. Choose **Stop** and wait for the Workspace status to change from **Stopping** to **Idle**.

1. Choose **Actions** again, and then choose **Start** to restart the Workspace.

1. Wait for the Workspace status to change from **Starting** to **Ready**, then choose the Workspace name to reopen it in a new browser tab.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
