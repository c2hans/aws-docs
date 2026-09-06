---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/account-connect.html
---

# Connecting the AWS Toolkit for JetBrains to your AWS account
<a name="account-connect"></a>

Most Amazon Web Services (AWS) and resources are managed through an AWS account. An AWS account isn't required to use the AWS Toolkit for JetBrains, however Toolkit functions are limited without a connection.

If you've previously set up an AWS account and authentication through another AWS service (such as the AWS Command Line Interface), then the AWS Toolkit for JetBrains automatically detects your credentials and guides you through the connection process.

## Prerequisites
<a name="prereqs"></a>

If you're new to AWS or haven't created an account, then there are 3 main steps to connect the AWS Toolkit for JetBrains with your AWS account:

1. **Signing up for an AWS account**: You can sign up for an AWS account from the [AWS sign up](https://portal.aws.amazon.com/billing/signup#/start/email) portal. For detailed information on setting up a new AWS account, see the [Overview](https://docs.aws.amazon.com/SetUp/latest/UserGuide/setup-overview.html) topic in the *AWS Setup User Guide*.

1. **Setting up authentication**: There are 3 primary methods to authenticate with your AWS account from the AWS Toolkit for JetBrains. To learn more about each of these methods, see the [Authentication and access](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/auth-access.html) topic in this User Guide.

1. **Connecting with your AWS account from the AWS Toolkit for JetBrains**: After you've created an AWS account and set up authentication, you can connect the AWS Toolkit for JetBrains with your AWS account by completing the *Connecting to AWS from the AWS Toolkit for JetBrains* procedure, located in the following section.

## Opening the Sign In panel
<a name="signinpanel"></a>

If this is your first time using the AWS Toolkit for JetBrains, the **AWS Toolkit Sign In** panel automatically opens in JetBrains.

To access the AWS Sign In panel at anytime, complete the following procedure.

1. From the Toolkit, open **AWS Connection Settings** by choosing the **ellipses** icon in the connection panel.

1. From **AWS Connection Settings**, choose **Setup Authentication...** to open the **AWS Toolkit Sign In** pane.

1. From the **AWS Toolkit Sign In** panel, select your authentication method and follow the on-screen prompts.

The following is an image of the **AWS Toolkit Sign In** panel.

![AWS Toolkit sign-in panel with Workforce and IAM Credential options and Continue button.](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/awssigninpane2024.png)

## Connecting to AWS from the AWS Toolkit for JetBrains
<a name="connecting-to-aws"></a>

The following sections describe how to authenticate and connect the AWS Toolkit for JetBrains with AWS to access the AWS Explorer and Amazon CodeCatalyst.

**Note**
Authentication with AWS Builder ID or IAM Identity Center launches the AWS authorization portal in your default web browser. Each time your credentials expire this process must be repeated to renew the connection between your AWS account and the AWS Toolkit for JetBrains.

### Authentication for the AWS Explorer
<a name="explorer"></a>

To get started working with the AWS Explorer in the Toolkit, authenticate and connect with either your IAM credentials or IAM Identity Center credentials.

The following procedures describe how to authenticate and connect the Toolkit with your AWS account.

**Authenticate and connect with IAM Identity Center**

1. From the **AWS Toolkit Sign In** panel, select the **Workforce** button, then choose the **Continue** button to advance to the **Sign in with SSO** screen.

1. From the **IAM Identity Center** screen, enter your **Profile Name**, **Start URL**, and select your **Region** in the drop down, then choose the **Continue** button to open the **AWS SSO Login Required** dialog.
**Note**
Choose the **Region** that matches the region associated with your IAM Identity Center credentials.

1. From the **AWS SSO Login Required** dialog, choose the **Proceed To Browser** button to open the **AWS Authorization request** website in your default web browser.

1. Follow the prompts in your default web browser, you're notified when the authorization process is complete, it is safe to return to close your browser, and return to JetBrains.

**Authenticate and connect with IAM Credentials**

1. From the **AWS Toolkit Sign In** panel, select the **IAM Credentials** button, then choose the **Continue** button to advance to the **IAM Credentials** screen.

1. From the **IAM Credentials** screen, enter your **Profile Name**, **Access Key**, and **Secret Key**, then choose the **Continue** button to add the profile to your config file and connect the Toolkit with your AWS account.

1. The AWS Explorer updates to display your AWS services and resources when authentication is complete.

## Authentication for Amazon CodeCatalyst
<a name="catalyst"></a>

To get started working with CodeCatalyst from the Toolkit, authenticate and connect with your AWS Builder ID.

Complete the following steps to authenticate with your AWS account from the Toolkit, with your existing AWS Builder ID credentials.

**Authenticate and connect with an AWS Builder ID**

1. From the **AWS Toolkit Sign In** panel, select the **Workforce** button, then choose the **Continue** button to advance to the **Sign in with SSO** screen.

1. From the **Sign in with SSO** screen, choose the **Skip to sign-in** link to open the **AWS Authorization request** website in your default web browser.

1. Follow the prompts in your default web browser, you're notified when the authorization process is complete, it is safe to return to close your browser, and return to JetBrains.

**Authenticate and connect with IAM Identity Center**

1. From the **AWS Toolkit Sign In** panel, select the **Workforce** button, then choose the **Continue** button to advance to the **Sign in with SSO** screen.

1. From the **IAM Identity Center** screen, enter your **Profile Name**, **Start URL**, and select your **Region** in the drop down, then choose the **Continue** button to open the **AWS SSO Login Required** dialog.
**Note**
Choose the **Region** that matches the region associated with your IAM Identity Center credentials.

1. From the **AWS SSO Login Required** dialog, choose the **Proceed To Browser** button to open the **AWS Authorization request** website in your default web browser.

1. Follow the prompts in your default web browser, you're notified when the authorization process is complete, it is safe to return to close your browser, and return to JetBrains.
