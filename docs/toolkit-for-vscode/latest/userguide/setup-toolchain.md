---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-toolchain.html
---

# Configuring your toolchain
<a name="setup-toolchain"></a>

The AWS Toolkit for Visual Studio Code supports multiple languages across all the AWS services. The following sections describe how to configure your toolchain for different languages.

## Configure a toolchain for .NET Core
<a name="setup-toolchain-for-net"></a>

1. Ensure that you have the AWS Toolkit for VS Code [installed](setup-toolkit.md#setup-install).

1. Install the [C\# extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.csharp). This extension enables VS Code to debug .NET Core applications.

1. Open an AWS Serverless Application Model (AWS SAM) application, or [create one](sam-get-started.md#serverless-apps-create).

1. Open the folder that contains `template.yaml`.

## Configure a toolchain for Node.js
<a name="setup-toolchain-for-node"></a>

1. Ensure that you have the AWS Toolkit for VS Code [installed](setup-toolkit.md#setup-install).

1. Open an AWS SAM application, or [create one](sam-get-started.md#serverless-apps-create).

1. Open the folder that contains `template.yaml`.
**Note**
When debugging a TypeScript Lambda function directly from the source code (launch configuration has `"target": "code"`), the TypeScript compiler must be installed either globally or in your project's `package.json`.

## Configure a toolchain for Python
<a name="setup-toolchain-for-python"></a>

1. Ensure that you have the AWS Toolkit for VS Code [installed](setup-toolkit.md#setup-install).

1. Install the [Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python). This extension enables VS Code to debug Python applications.

1. Open an AWS SAM application, or [create one](sam-get-started.md#serverless-apps-create).

1. Open the folder that contains `template.yaml`.

1. Open a terminal at the root of your application, and configure `virtualenv` by running `python -m venv ./.venv`.
**Note**
You only need to configure `virtualenv` once per system.

1. Activate `virtualenv` by running one of the following:
   + Linux or macOS (Bash): `source ./.venv/bin/activate`
   + Windows (PowerShell): `./.venv/Scripts/Activate.ps1`
   + Windows (Command Prompt): `.venv\Scripts\activate.bat`

## Configure a toolchain for Java
<a name="setup-toolchain-for-java"></a>

1. Ensure that you have the AWS Toolkit for VS Code [installed](setup-toolkit.md#setup-install).

1. Install the [Java extension and Java 11](https://marketplace.visualstudio.com/items?itemName=redhat.java). This extension enables VS Code to recognize Java functions.

1. Install the [Java debugger extension](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-debug). This extension enables VS Code to debug Java applications.

1. Open an AWS SAM application, or [create one](sam-get-started.md#serverless-apps-create).

1. Open the folder that contains `template.yaml`.

## Configure a toolchain for Go
<a name="setup-toolchain-for-go"></a>

1. Ensure that you have the AWS Toolkit for VS Code [installed](setup-toolkit.md#setup-install).

1. Go 1.14 or higher is required for debugging Go Lambda functions.

1. Install the [Go extension](https://marketplace.visualstudio.com/items?itemName=golang.Go).
**Note**
Version 0.25.0 or higher is required for debugging Go1.15\+ runtimes.

1. Install Go tools using the [command palette](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/toolkit-navigation.html#command-locations):

   1. From the command palette, choose `Go: Install/Update Tools`.

   1. From the set of check boxes, select `dlv` and `gopls`.

1. Open an AWS SAM application, or [create one](sam-get-started.md#serverless-apps-create).

1. Open the folder that contains `template.yaml`.

## Using Your toolchain
<a name="use-toolchain"></a>

Once you have your toolchain set up, you can use it to [run or debug](sam-get-started.md#serverless-apps-debug) the AWS SAM application.
