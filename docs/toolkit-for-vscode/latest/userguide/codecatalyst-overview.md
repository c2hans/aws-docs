---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/codecatalyst-overview.html
---

# Working with Amazon CodeCatalyst resources in VS Code
<a name="codecatalyst-overview"></a>

The following sections provide an overview of the Amazon CodeCatalyst resource management features that are available from the Toolkit for VS Code.

For more information about Dev Environments and how you can access them from CodeCatalyst, see the [Dev Environments](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment.html) section in the *Amazon CodeCatalyst* User Guide.

The following sections describe how to create, open, and work with Dev Environments from VS Code.

**Topics**
+ [Clone a repository](#codecatalyst-overview-clone)
+ [Opening a Dev Environment](#codecatalyst-overview-open)
+ [Creating a CodeCatalyst Dev Environment](#codecatalyst-overview-create)
+ [Creating a Dev Environment from a third-party repository](#codecatalyst-devenvironment-link-repo)
+ [CodeCatalyst commands in VS Code](#codecatalyst-overview-commands)

## Clone a repository
<a name="codecatalyst-overview-clone"></a>

CodeCatalyst is a cloud-based service that requires you to be connected to the cloud to work on CodeCatalyst projects. If you prefer to work on a project locally, you can clone your CodeCatalyst repositories to your local machine and sync it with your CodeCatalyst project online, the next time that you're connected to the cloud.

To clone a repository from your CodeCatalyst account to VS Code with the AWS Toolkit, complete the following steps:

**Note**
If you are cloning a repository from a 3rd party service, you may be prompted to authenticate with that service's credentials.
While the repository is being cloned, VS Code displays the progress in the **Cloning Repository** status window. After the repository is cloned, the **Would you like to open the cloned repository?** message appears.

1. From the Toolkit for VS Code, expand the **DEVELOPER TOOLS** explorer.

1. Expand **CodeCatalyst**, choose **Clone Repository**.

1. From the **Select a CodeCatalyst Repository** dialog, search for the repository that you want to clone, then select it to open the **Choose a folder to clone** dialog.

1. Choose **Select Repository Location** to close the prompt and begin cloning the repository.

1. From the dialog window, choose one of the following to complete the cloning process:
   + To open your repository in your current VS Code window, choose **Open**.
   + To open your repository in a new VS Code window, choose **Open in new window**.
   + To complete the cloning process without opening your repository, close the dialog window.

## Opening a Dev Environment
<a name="codecatalyst-overview-open"></a>

To open an existing Dev Environment in VS Code, complete the following steps.

**Note**
Selecting the Dev Environment starts the process to connect VS Code with CodeCatalyst by opening your Dev Environment. During this process, VS Code displays progress updates in a CodeCatalyst status window. The status window updates when the process is complete.
If the Dev Environment fails to open, the status updates with information about why the process failed and a link to open the process logs.
If the process is successful, your Dev Environment opens in a new window, from VS Code.

1. From the Toolkit for VS Code, expand the **DEVELOPER TOOLS** explorer.

1. Expand **CodeCatalyst** and choose **Open Dev Environment** to open the **Select a CodeCatalyst Dev Environment** dialog in VS Code.

1. From the **Select a CodeCatalyst Dev Environment** dialog, choose the **Dev Environment** that you want to open.

## Creating a CodeCatalyst Dev Environment
<a name="codecatalyst-overview-create"></a>

To create a new Dev Environment, complete the following steps:

**Note**
When creating a new Dev Environment, observe the following:
AWS recommends that you specify an alias because it simplifies organization and improves search capabilities for Dev Environments.
Dev Environments saves your work persistently. This means that your Dev Environment can be stopped without losing your work. Stopping your Dev Environment reduces the costs that are required to keep you Dev Environment up and running.
**Storage** is the only setting that can't be changed after your Dev Environment has been created.
VS Code displays the progress of your Dev Environment being created in a status window. After the Dev Environment is created, VS Code opens the Dev Environment in a new window and the **Do you trust the authors of the files in this folder?** prompt also appears. Agree to the terms and conditions to continue working in your Dev Environment.

1. From the Toolkit for VS Code, expand the **DEVELOPER TOOLS** explorer.

1. Expand **CodeCatalyst**, and choose the **Create Dev Environment** option to open the **Create a CodeCatalyst Dev Environment** menu in VS Code.

1. From the **Source Code** section, choose one of the following options:
   + **Use an existing CodeCatalyst Repository**: Creates a Dev Environment from an existing CodeCatalyst repository. You must select the CodeCatalyst **Project** and **Branch**.
   + **Create an empty Dev Environment**: Creates an empty Dev Environment.

1. (Optional) From the **Alias** section, enter an alternate name for your Dev Environment.

1. (Optional) From the **Dev Environments Configuration** section, change the following settings to meet your specific needs.
   + **Compute**: Choose **Edit Compute** to change the amount of processing power and RAM that's assigned to your system.
   + **Timeout**: Choose **Edit Timeout** to change the amount of system idle time allowed before your Dev Environment is stopped.
   + **Storage**: Choose **Edit Storage Size** to change the amount of storage space that's assigned to your system.

1. Choose **Create Dev Environment** to create your new cloud development environment.

## Creating a Dev Environment from a third-party repository
<a name="codecatalyst-devenvironment-link-repo"></a>

You can create Dev Environments from a third-party repository by linking to the repository as a source.

Linking to a third-party repository as a source is handled at the project level in CodeCatalyst. For instructions and additional details on how to connect a third-party repository to your Dev Environment, see the [Linking a source repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-repositories-link.html) topic in the *Amazon CodeCatalyst* User Guide.

## CodeCatalyst commands in VS Code
<a name="codecatalyst-overview-commands"></a>

There are additional VS Code commands that are assigned to CodeCatalyst-related features that aren't displayed directly in the AWS Toolkit.

To view a list of commands that are assigned to CodeCatalyst from the command palette, complete the following steps:

1. From the Toolkit for VS Code, expand the **DEVELOPER TOOLS** explorer.

1. Choose **Show CodeCatalyst Commands** to open the **Command Palette** with a pre-populated search for `CodeCatalyst`.

1. Select a CodeCatalyst command from the list to activate it.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
