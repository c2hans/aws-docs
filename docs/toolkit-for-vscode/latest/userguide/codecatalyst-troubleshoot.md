---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/codecatalyst-troubleshoot.html
---

# Troubleshooting Amazon CodeCatalyst and VS Code
<a name="codecatalyst-troubleshoot"></a>

The following topics address potential technical issues when working with Amazon CodeCatalyst and VS Code.

**Topics**
+ [VS Code version](#codecatalyst-troubleshoot-vsc)
+ [Permissions for Amazon CodeCatalyst](#codecatalyst-troubleshoot-permission)
+ [Connecting to a Dev Environment from the Toolkit for VS Code](#codecatalyst-troubleshoot-connecting)

## VS Code version
<a name="codecatalyst-troubleshoot-vsc"></a>

Your version of VS Code is expected to set up a handler for `vscode://` URIs on your system. Without this handler, you can't access all CodeCatalyst features from the AWS Toolkit. For example, you encounter an error when launching a Dev Environment from VS Code Insiders. This is because VS Code Insiders handles `vscode-insiders://` URIs and doesn't handle `vscode://` URIs.

## Permissions for Amazon CodeCatalyst
<a name="codecatalyst-troubleshoot-permission"></a>

The following are file permission requirements for working with CodeCatalyst from the AWS Toolkit for Visual Studio Code:
+ Set your own access permissions for your `~/.ssh/config` file to `read` and `write`. Restrict `write` permissions for all other users.
+ Set your access permissions for the `~/.ssh/id_dsa ` and `~/.ssh/id_rsa` files to `read` only. Restrict `read`, `write` and `execute` permissions for all other users.
+ Your `globals.context.globalStorageUri.fsPath` file must be in a writable location.

## Connecting to a Dev Environment from the Toolkit for VS Code
<a name="codecatalyst-troubleshoot-connecting"></a>

If you receive the following error when attempting to connect to a Dev Environment from the AWS Toolkit for Visual Studio Code:

*Your `~/.ssh/config` has an `aws-devenv-*` section that might be out of date.*
+ Choose the **Open config. . .** button to open your `~/.ssh/config` file in the VS Code **Editor**.
+ From the **Editor**, select and delete the contents of the `Host aws-devenv-*` section.
+ Save the changes you made to the `Host aws-devenv-*` of `~/.ssh/config`. Then, close the file.
+ Reattempt to connect to a Dev Environment from the Toolkit for VS Code.
