---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-region.html
---

# Changing AWS Regions
<a name="setup-region"></a>

An AWS Region specifies where your AWS resources are managed. Your default AWS Region is detected when you connect to your AWS account from the AWS Toolkit for Visual Studio Code, automatically displaying in the **AWS Explorer**.

The following sections describe how to add or hide a Region from the **AWS Explorer**.

## Adding a Region to the AWS Explorer
<a name="select-new-region"></a>

Complete the following procedure to add a Region to the AWS Explorer.

1. From VS Code, open the **Command Palette** by expanding **View** on the main menu and choosing **Command Palette**. Or use the following shortcut keys:
   + Windows and Linux – Press **Ctrl\+Shift\+P**.
   + macOS – Press **Shift\+Command\+P**.

1. From the **Command Palette**, search for **AWS: Show or Hide Regions** and choose **AWS: Show or Hide Regions** to display a list of available Regions.

1. From the list, select the AWS Regions that you want to add to the **AWS Explorer**.

1. Choose the **OK** button to confirm your choices and update the **AWS Explorer**.

## Hide a Region from the AWS Explorer
<a name="hide-region"></a>

To hide a Region from the AWS Explorer view, complete the following procedure.

1. From the **AWS Explorer**, locate the AWS Region that you want to hide.

1. Open the context menu for (right-click) the Region you want to hide.

1. Choose **Show or Hide Regions** to open the **AWS: Show or Hide Regions** options in VS Code.

1. Deselect the Regions that you want to hide in the AWS Explorer view.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
