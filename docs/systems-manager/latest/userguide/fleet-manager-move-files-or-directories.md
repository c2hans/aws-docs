---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-move-files-or-directories.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Copying, cutting, and pasting OS files or directories using Fleet Manager
<a name="fleet-manager-move-files-or-directories"></a>

You can use Fleet Manager to copy, cut, and paste OS files on a managed node.

**To copy or cut and paste files or directories using Fleet Manager**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Fleet Manager**.

1. Select the link of the managed node with the files you want to copy, or cut and paste.

1. Choose **Tools, File system**.

1. To copy or cut a file, select the **File name** of the directory that contains the file you want to copy or cut. To copy or cut a directory, choose the button next to the directory that you want to copy or cut. Then proceed to step 8.

1. Choose the button next to the file you want to copy or cut.

1. In the **Actions** menu, choose **Copy** or **Cut**.

1. In the **File system** view, choose the button next to the directory you want to paste the file in.

1. In the **Actions** menu, choose **Paste**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
