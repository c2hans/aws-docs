---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/appcomposer-overview.html
---

# Working with AWS Infrastructure Composer in the Toolkit
<a name="appcomposer-overview"></a>

AWS Infrastructure Composer for the AWS Toolkit for Visual Studio Code allows you to visually design applications through an interactive canvas. You can also use Infrastructure Composer to visualize and modify CloudFormation and AWS Serverless Application Model (AWS SAM) templates. While working with Infrastructure Composer, your changes are stored persistently enabling you to switch seamlessly between editing files directly in the VS Code editor or using the interactive canvas.

For detailed information about AWS Infrastructure Composer, getting started information, and tutorials, see the [AWS Infrastructure Composer](https://docs.aws.amazon.com/application-composer/latest/dg/what-is-composer.html) User Guide.

The following sections describe how to access AWS Infrastructure Composer from the AWS Toolkit for Visual Studio Code.

## Accessing AWS Infrastructure Composer from the Toolkit
<a name="appcomposer-overview-access"></a>

There are 3 main ways that you can access AWS Infrastructure Composer from the Toolkit.

**Accessing AWS Infrastructure Composer from an existing template**

1. From VS Code, open an existing template file in the VS Code editor.

1. From the **editor window**, click the AWS Infrastructure Composer button located in the upper right-hand corner of the editor window.

1. AWS Infrastructure Composer opens and visualizes your template file in the VS Code editor window.

**Accessing AWS Infrastructure Composer from the context menu (right-click)**

1. From VS Code right-click the template file you want to open with AWS Infrastructure Composer.

1. In the context menu, choose the **Open with App Composer** option.

1. AWS Infrastructure Composer opens and visualizes your template file in a new VS Code editor window.

**Accessing AWS Infrastructure Composer from the Command Palette**

1. From VS Code open the Command Palette by pressing **Cmd \+ Shift \+ P** or **Ctrl \+ Shift \+ P** (Windows)

1. In the search field, enter **AWS Infrastructure Composer** and choose **AWS Infrastructure Composer** when it populates in the results.

1. Choose the template file you want to open, AWS Infrastructure Composer opens and visualizes your template file in a new VS Code editor window.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
