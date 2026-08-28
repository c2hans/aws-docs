---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/setup-troubleshoot.html
---

# Troubleshooting installation issues for the AWS Toolkit for Visual Studio
<a name="setup-troubleshoot"></a>

The following information is known to resolve common installation issues while setting up the AWS Toolkit for Visual Studio.

If you encounter an error while installing the AWS Toolkit for Visual Studio or it's unclear whether or not the installation was complete, review the information in each of the following sections.

## Administrator permissions for Visual Studio
<a name="setup-troubleshoot-admin"></a>

The AWS Toolkit for Visual Studio extension requires administrator permissions to ensure that all AWS services and features are accessible.

If you have local administrator permissions it's possible that your administrator permissions don't extend directly to your Visual Studio instance.

To launch Visual Studio with administrator permissions locally:

1. From Windows, locate the Visual Studio application launcher (icon).

1. Open the context menu for (right-click) the Visual Studio icon to open the context menu.

1. Select **Run as administrator** from the context menu.

To launch Visual Studio with administrator permissions remotely:

1. From Windows, locate the application launcher for the application that you are using to connect to your remote instance of Visual Studio.

1. Open the context menu for (right-click) the application to open the context menu.

1. Select **Run as administrator** from the context menu.

**Note**
Whether you are launching the program locally or connecting remotely, Windows may prompt you to confirm your administrative credentials.

## Obtaining an installation log
<a name="setup-troubleshoot-install-log"></a>

If you have completed the steps in the previous *Administrator permissions* section located above and it's confirmed that you're running or connecting to Visual Studio with administrator permissions, then obtaining an installation log file can help diagnose other issues.

To manually install the AWS Toolkit for Visual Studio from a `.vsix` file and generate an installation log file, complete the following steps.

1. From the [AWS Toolkit for Visual Studio](https://aws.amazon.com/visualstudio/) landing page, follow the **Download** link and save the `.vsix` file of the AWS Toolkit for Visual Studio version you want to install.

1. From the Visual Studio main menu, expand the **Tools** header, expand the **Command Line** sub menu, then choose **Visual Studio Developer Command Prompt**.

1. From the **Visual Studio Developer Command Prompt** enter the `vsixinstaller` command with the following format:

   `vsixinstaller /logFile:[file path to log file] [file path to Toolkit installation file]`

1. Replace`[file path to log file]` with the file name and full file path of the directory you want the installation log to be created in. An example of the `vsixinstaller` command with your specified file path and file name resembles the following:

   `vsixinstaller /logFile:C:\Users\Documents\install-log.txt [file path to AWSToolkitPackage.vsix]`

1. Replace `[file path to Toolkit installation file]` with the full file path of the directory where the `AWSToolkitPackage.vsix` is located.

   An example of the `vsixinstaller` command with the full file path to the Toolkit installation file should resemble the following:

   `vsixinstaller /logFile:[file path to log file] C:\Users\Downloads\AWSToolkitPackage.vsix`

1. Check to make sure your file name and paths are correct, then run the `vsixinstaller` command.

   An example of a complete `vsixinstaller` command resembles the following:

   `vsixinstaller /logFile:C:\Users\Documents\install-log.txt C:\Users\Downloads\AWSToolkitPackage.vsix`

## Installing different Visual Studio extensions
<a name="setup-troubleshoot-extensions"></a>

If you've obtained an installation log file and you're still unable to determine why the installation process is failing, check to see if you're able to install other Visual Studio extensions. Installing different Visual Studio extensions can provide additional insight to your installation issues. In the event that you're unable to install any Visual Studio extensions, it may be necessary to troubleshoot issues with Visual Studio, instead of AWS Toolkit for Visual Studio.

## Contacting support
<a name="setup-troubleshoot-contact"></a>

If you've reviewed all of the sections contained in this guide and require additional resources or support, you can view past issues or open a new issue from the [AWS Toolkit for Visual Studio Github Issues](https://github.com/aws/aws-toolkit-visual-studio/issues/) site.

To help expedite a solution to your issue:
+ Check past and current issues to see if others have encountered a similar situation.
+ Keep detailed notes of each step you've taken to address the issue.
+ Save any log files you've obtained from installing the AWS Toolkit for Visual Studio or other extensions.
+ Attach your AWS Toolkit for Visual Studio installation logfiles to the new issue.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-visual-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
