---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/serverlessland-overview.html
---

# Working with AWS Serverless Land
<a name="serverlessland-overview"></a>

AWS Serverless Land in the AWS Toolkit for Visual Studio Code is a collection of features that assists you with building event-driven architectures. The following topic sections describe how to work with Serverless Land in the AWS Toolkit. For detailed information about Serverless Land, see the [Serverless Land](https://serverlessland.com/) web application.

## Accessing Serverless Land
<a name="w2aac17c51b9b5"></a>

There are 3 main entry points to access Serverless Land in the AWS Toolkit:
+ The VS Code Command Palette
+ The AWS Toolkit Explorer
+ The AWS Toolkit **Application Builder** explorer

### Opening Serverless Land from the VS Code Command Palette
<a name="w2aac17c51b9b5b7b1"></a>

To open Serverless Land from the VS Code Command Palette, complete the following steps.

1. From VS Code, open the Command Palette by pressing **option\+shift\+p** (Mac) or **control\+shift\+p** (Windows).

1. From the VS Code Command Palette, enter **AWS Create application with Serverless template** into the search bar.

1. Choose **AWS: Create application with Serverless template** when it populates in the list.

1. The Serverless Land wizard opens to the **Select a Pattern for you application (1/5)** screen in VS Code when the process is complete.

### Opening Serverless Land from the AWS Toolkit Explorer.
<a name="w2aac17c51b9b5b7b3"></a>

To open Serverless Land from the AWS Toolkit Explorer, complete the following steps.

1. From the AWS Toolkit Explorer, expand the region that you want to open Serverless Land in.

1. Open the context menu for (right-click) the Lambda node.

1. Choose **Create application with Serverless template** from the context menu.

1. The Serverless Land wizard opens to the **Select a Pattern for you application (1/5)** screen in VS Code when the process is complete.

### Opening Serverless Land from the Application Builder explorer
<a name="w2aac17c51b9b5b7b5"></a>

To open Serverless Land from the AWS Toolkit Application Builder explorer, complete the following steps.

1. From the AWS Toolkit Explorer, navigate to the Application Builder explorer.

1. Right-click the Application Builder explorer and choose **Create application with Serverless template** from the context menu.

1. The Serverless Land wizard opens to the **Select a Pattern for you application (1/5)** screen in VS Code when the process is complete.

## Creating an application with Serverless template
<a name="w2aac17c51b9b7"></a>

To create an application with Serverless template, complete the following steps.

1. From the Serverless Land wizard **Select a Pattern for you application (1/5)** screen, choose a Pattern for the base of your application.
**Note**
To view a preview and more details about a particular Pattern, choose the **Open in Serverless Land** icon located next to the Pattern you want to view. The Serverless Land Pattern opens in your default web browser.

1. From the **Select Runtime (2/5)** screen, choose a runtime for your project.

1. From the **Select IaC (3/5)** screen, choose an IaC option for your project.

1. From the **Select a project location (4/5)** screen, choose a location to store your project.

1. From the **Enter Project Name (5/5)** screen, enter a name for your new application.

1. Your new application displays in the VS Code explorer and your project `readme.md` opens in the VS Code editor, when the procedure is complete.
**Note**
After your new application is created, additional actions that are specific to your application type can be found in the `readme.md` file. Additionally, your AWS Serverless Application Model (AWS SAM) applications can be opened with AWS Application Builder for local testing, debugging, and more.
For details about working with Application Builder in the AWS Toolkit, see the [Working with the AWS Application Builder explorer](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/appbuilder-overview-overview.html) topic in this User Guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
