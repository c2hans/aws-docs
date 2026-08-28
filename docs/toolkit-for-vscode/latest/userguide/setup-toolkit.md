---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-toolkit.html
---

# Installing the AWS Toolkit for Visual Studio Code
<a name="setup-toolkit"></a>

## Prerequisites
<a name="setup-prereq"></a>

To get started working with AWS Toolkit for Visual Studio Code from VS Code, the following perquisites must be met. To learn more about accessing all of the AWS services and resources available from the AWS Toolkit for Visual Studio Code, see the [Optional prerequisites](#setup-prereq-opt) section of this guide.
+ VS Code requires a Windows, macOS, or Linux operating system.
+ The AWS Toolkit for Visual Studio Code requires you to work from VS Code version 1.73.0 or a later version.

For additional information about VS Code or to download the latest version of VS Code, see the [VS Code downloads](https://code.visualstudio.com/downloads) website.

## Downloading and installing the AWS Toolkit for Visual Studio Code
<a name="setup-install"></a>

You can download, install, and set up the AWS Toolkit for Visual Studio Code through the VS Code Marketplace in your IDE. Alternatively, you can download the AWS Toolkit for Visual Studio Code installation files by navigating to the [ VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-toolkit-vscode) from your web browser.

**Installing the AWS Toolkit for Visual Studio Code from the VS Code IDE Marketplace**

1. Open the AWS Toolkit for Visual Studio Code extension in your VS Code IDE with the following link: [Open the VS Code Marketplace](vscode:extension/amazonwebservices.aws-toolkit-vscode).
**Note**
If VS Code is not already running on your machine, this operation may take a few moments while VS Code is loading.

1. From the AWS Toolkit for Visual Studio Code extension in the VS Code Marketplace, choose **Install** to begin the installation process.

1. When prompted, choose to restart VS Code to complete the installation process.

## Optional prerequisites
<a name="setup-prereq-opt"></a>

Before you can use certain features of the AWS Toolkit for Visual Studio Code, you must have the following:
+ **Amazon Web Services (AWS) account**: An AWS account isn't a requirement to use the AWS Toolkit for Visual Studio Code, but functionality is significantly limited without it. To obtain an AWS account, go to the [AWS home page](https://aws.amazon.com/). Choose **Create an AWS Account**, or **Complete Sign Up** (if you've visited the site before).
+ **Code Development** – The relevant SDK for the language that you want to use. You can download from the following links, or use your favorite package manager:
  + .NET SDK: [https://dotnet.microsoft.com/download](https://dotnet.microsoft.com/download)
  + Node.js SDK: [https://nodejs.org/en/download](https://nodejs.org/en/download)
  + Python SDK: [https://www.python.org/downloads](https://www.python.org/downloads)
  + Java SDK: [https://aws.amazon.com/corretto/](https://aws.amazon.com/corretto/)
  + Go SDK: [https://golang.org/doc/install](https://golang.org/doc/install)
+ **AWS SAM CLI** – This is an AWS CLI tool that helps you develop, test, and analyze your serverless applications locally. This isn't required for installing the toolkit. However, we recommend that you install it (and Docker, described next) because it's required for any AWS Serverless Application Model (AWS SAM) functionality, such as [Creating a new serverless application (local)](sam-get-started.md#serverless-apps-create).

  For more information, see [Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) in the *[AWS Serverless Application Model Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)*.
+ **Docker** – The AWS SAM CLI requires this open-source software container platform. For more information and download instructions, see [Docker](https://www.docker.com/).
+ **Package Manager** – A package manager so you can download and share application code.
  + .NET: [NuGet](https://www.nuget.org/downloads)
  + Node.js: [npm](https://www.npmjs.com/package/npm)
  + Python: [pip](https://pypi.org/project/pip/)
  + Java: [Gradle](https://gradle.org/install/) or [Maven](https://maven.apache.org/download.cgi)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
