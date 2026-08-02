---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/connect.html
---

# Connecting to AWS
<a name="connect"></a>

Most Amazon Web Services (AWS) resources are managed through an AWS account. An AWS account isn't required to use the AWS Toolkit for Visual Studio Code, however Toolkit functions are limited without a connection.

If you've previously set up an AWS account and authentication through another AWS service (such as the AWS Command Line Interface), then the AWS Toolkit for Visual Studio Code automatically detects your credentials.

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com//accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Prerequisites
<a name="connecting-to-aws"></a>

If you're new to AWS or haven't created an account, then there are 2 main steps to connect the AWS Toolkit for Visual Studio Code with your AWS account:

1. **Setting up authentication**: There are 3 primary methods to authenticate with your AWS account from the AWS Toolkit for Visual Studio Code. To learn more about each of these methods, see the [Authentication and Access](https://docs.aws.amazon.com//toolkit-for-vscode/latest/userguide/establish-credentials.html) topic in this User Guide.

1. **Authenticating with AWS from the Toolkit**: You can connect with your AWS account from the Toolkit by completing the procedures in the following sections of this User Guide.

## Opening the Sign In panel
<a name="sign-in-pannel"></a>

Complete one of the following procedures to open the **AWS Toolkit Sign In** panel.

**To open the **AWS Toolkit Sign In** panel from the AWS Explorer:**

1. From the AWS Toolkit for Visual Studio Code, expand **EXPLORER**.

1. Expand the **More Actions...** menu by selecting the **...** icon.

1. From the **More Actions...** menu, choose **Connect to AWS** to open the **AWS Toolkit Sign In** panel.

**To open the **AWS Toolkit Sign In** panel using the VS Code command pallet:**

1. Open the command pallet by pressing **Shift\+Command\+P** (**Ctrl\+Shift\+P** Windows).

1. Enter **AWS: Add a New Connection** into the search field.

1. Select **AWS: Add a New Connection** to open the **AWS Toolkit Sign In** panel.

## Connecting to AWS from the Toolkit
<a name="connect-to-aws"></a>

### Authenticate and connect with SSO
<a name="w2aac11c11c25b3"></a>

To authenticate and connect with AWS using AWS IAM Identity Center, complete the following procedure.

**Note**
Authentication with AWS Builder ID or IAM Identity Center launches the AWS authorization portal in your default web browser. Each time your credentials expire this process must be repeated to renew the connection between your AWS account and the AWS Toolkit for Visual Studio Code.

**Authenticate and connect with AWS IAM Identity Center**

1. From the **AWS Toolkit Sign In** panel, choose the **Workforce** tab, then select the **Continue** button to proceed.

1. From the **Sign in with IAM Identity Center** panel, enter the **Start URL** for your organization. This URL is provided to you by an admin or help desk at your company.

1. Select your AWS **Region** from the drop-down menu. This is the AWS region that hosts your identity directory.

1. Choose the **Continue** button and confirm that you want to open the **AWS Authorization request** website in your default web browser.

1. Follow the prompts in your default web browser, you're notified when the authorization process is complete, it's safe to close your browser, and return to VS Code.

### Authenticate and connect with IAM Credentials
<a name="w2aac11c11c25b5"></a>

To authenticate and connect with AWS using IAM Credentials, complete the following procedure.

**Authenticate and connect with IAM Credentials**

1. From the **AWS Toolkit Sign In** panel, choose **IAM Credential**, then select the **Continue** button to proceed.

1. Enter the **Profile Name**, **Access Key**, and **Secret Key** of your AWS account in the provided fields, then choose the **Continue** button to add the profile to your config file and connect the Toolkit with your AWS account.

1. The Toolkit **AWS Explorer** updates to display your AWS services and resources when authentication is complete and a connection has been established.

## Authentication for Amazon CodeCatalyst
<a name="catalyst"></a>

To get started working with CodeCatalyst from the Toolkit, authenticate and connect with either your AWS Builder ID or IAM Identity Center credentials.

The following procedures describe how to authenticate and connect the Toolkit with your AWS account.

**Authenticate and connect with an AWS Builder ID**

1. From the **AWS Toolkit Sign In** panel, choose the **Workforce** tab, then select the **Continue** button to proceed.

1. At the top of the **Sign in with SSO** panel, choose the **Skip to sign-in** link.

1. Follow the prompts in your default web browser, you're notified when the authorization process is complete, it's safe to close your browser, and return to VS Code.

**Authenticate and connect with IAM Identity Center**

1. From the **AWS Toolkit Sign In** panel, choose the **Workforce** tab, then select the **Continue** button to proceed.

1. From the **Sign in with IAM Identity Center** panel, enter the **Start URL** for your organization. This URL is provided to you by an admin or help desk at your company.

1. Select your AWS **Region** from the drop-down menu. This is the AWS region that hosts your identity directory.

1. Choose the **Continue** button and confirm that you want to open the **AWS Authorization request** website in your default web browser.

1. Follow the prompts in your default web browser, you're notified when the authorization process is complete, it's safe to close your browser, and return to VS Code.
