---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/codecatalyst-setup.html
---

# Getting Started with CodeCatalyst and the AWS Toolkit for JetBrains
<a name="codecatalyst-setup"></a>

To get started working with CodeCatalyst from the JetBrains Gateway, complete the following.

## Downloading JetBrains Gateway
<a name="codecatalyst-setup-jbgateway"></a>

Before you integrate the AWS Toolkit with your CodeCatalyst accounts, make sure that you're using the current version of JetBrains Gateway. To download the latest version of JetBrains Gateway, choose the JetBrains Gateway distribution you want from the following links:
+ [JetBrains Gateway for Linux](https://download.jetbrains.com/product?code=GW&latest&distribution=linux)
+ [JetBrains Gateway for Windows]( https://download.jetbrains.com/product?code=GW&latest&distribution=windows)
+ [JetBrains Gateway for macOS](https://download.jetbrains.com/product?code=GW&latest&distribution=mac)
+ [JetBrains Gateway for macOS Apple Silicon](https://download.jetbrains.com/product?code=GW&latest&distribution=macM1)

## Installing the AWS Toolkit for JetBrains Gateway
<a name="codecatalyst-setup-toolkit"></a>

To connect JetBrains with your CodeCatalyst account, you must install the latest version of the toolkit extension. You can find the latest version and complete the installation of the toolkit directly from the JetBrains **Plugins Marketplace**.

To install the AWS Toolkit plugin from the JetBrains **Plugins Marketplace**, complete the following steps:

1. From the JetBrains Gateway main screen, choose the **Settings/Preferences ** icon, located in the bottom-left corner of the application.

1. choose **Settings/Preferences** to open the **Settings/Preferences** view.

1. In the **Settings/Preferences** view, choose **Plugins** to open the **Plugins** view.
**Note**
The **Plugins** view can open in either the **Marketplace** view or the **Installed** view.
If this is your first time installing the AWS Toolkit for JetBrains Gateway, select the **Plugins Marketplace** view to continue.
If you have a previous version of the AWS Toolkit for JetBrains Gateway, update it from the **Installed** view.

1. From the **Marketplace** view, enter the text `AWS Toolkit` and choose the **AWS Toolkit** plugin entry when it appears.

1. Choose **Install** to download and install the **AWS Toolkit for JetBrains Gateway**.
**Note**
JetBrains Gateway displays the status of your download and installation progress. After the toolkit is successfully installed, the JetBrains Gateway **Connections** explorer updates with the **Amazon CodeCatalyst** plugin icon.

## Creating a CodeCatalyst account and setting up authentication
<a name="codecatalyst-setup-id"></a>

To work with CodeCatalyst from the AWS Toolkit for JetBrains, you must have an active CodeCatalyst account and set up either an AWS Builder ID or IAM Identity Center authentication to connect with JetBrains Gateway. If you don't have an active CodeCatalyst account, AWS Builder ID, or IAM Identity Center authentication set up, see the [Setting up with CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/setting-up-topnode.html) section in the *CodeCatalyst* User Guide.

## Authenticate and connect JetBrains Gateway with CodeCatalyst
<a name="codecatalyst-setup-connect"></a>

To authenticate with AWS and connect JetBrains Gateway with your CodeCatalyst account, complete the following steps.

**Note**
To authenticate with AWS using IAM Identity Center, you must be running AWS Toolkit for JetBrains version 2.6 or later.

1. From the JetBrains Gateway **Connections** explorer, choose the **Amazon CodeCatalyst** plugin to open the **Amazon CodeCatalyst** plugin view.

1. From the **CodeCatalyst** plugin view, choose **Sign in** to open the **AWS Toolkit: Setup Authentication** dialog.

1. From the **AWS Toolkit: Setup Authentication** dialog, choose the tab for your preferred authentication method: **IAM Identity Center** or **AWS Builder ID**.

1. From the tab of your preferred authentication method, complete any required fields, then choose the **Connect** button to open the **AWS authentication portal** in your default web browser.

1. From your web browser, confirm the security code matches the code presented in your IDE to proceed.

1. When prompted, choose **Allow** to confirm the connection between JetBrains and your AWS account. When the connection process is complete, your web browser displays a confirmation indicating that it's safe to close the window and return to your IDE.

1. The JetBrains Gateway **CodeCatalyst** plugin view is updated to the **Dev Environments** view.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for JetBrains. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-jetbrains` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
