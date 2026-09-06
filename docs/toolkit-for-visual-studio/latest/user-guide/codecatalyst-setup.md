---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/codecatalyst-setup.html
---

# Getting Started with Amazon CodeCatalyst and the AWS Toolkit for Visual Studio with Amazon Q
<a name="codecatalyst-setup"></a>

To get started working with Amazon CodeCatalyst from the AWS Toolkit for Visual Studio with Amazon Q, complete the following.

**Topics**
+ [Installing the AWS Toolkit for Visual Studio with Amazon Q](#codecatalyst-setup-jbgateway)
+ [Creating a CodeCatalyst account and AWS Builder ID](#codecatalyst-setup-id)
+ [Connecting AWS Toolkit for Visual Studio with Amazon Q with CodeCatalyst](#codecatalyst-setup-connect)

## Installing the AWS Toolkit for Visual Studio with Amazon Q
<a name="codecatalyst-setup-jbgateway"></a>

Before you integrate the AWS Toolkit for Visual Studio with Amazon Q with your CodeCatalyst accounts, make sure that you're using a current version of AWS Toolkit for Visual Studio with Amazon Q. For details on how to install and set up the latest version of AWS Toolkit for Visual Studio with Amazon Q, see the [Setting up the AWS Toolkit for Visual Studio with Amazon Q](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/getting-set-up.html) section of this User Guide.

## Creating a CodeCatalyst account and AWS Builder ID
<a name="codecatalyst-setup-id"></a>

In addition to installing the latest version of the AWS Toolkit for Visual Studio with Amazon Q, you must have an active AWS Builder ID and CodeCatalyst account to connect with AWS Toolkit for Visual Studio with Amazon Q. If you don't have an active AWS Builder ID or CodeCatalyst account, see the [Setting up with CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/setting-up-topnode.html) section in the *CodeCatalyst* User Guide.

**Note**
An AWS Builder ID is different from your AWS Credentials. For instructions on how to sign up and authenticate with an AWS Builder ID, see the [Authentication and access: AWS Builder ID](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/builder-id.html) topic in this User Guide.
For detailed information about AWS Builder IDs, see the [AWS Builder ID](https://docs.aws.amazon.com/general/latest/gr/aws_builder_id.html) topic in the *AWS General Reference* User Guide.

## Connecting AWS Toolkit for Visual Studio with Amazon Q with CodeCatalyst
<a name="codecatalyst-setup-connect"></a>

To connect AWS Toolkit for Visual Studio with Amazon Q with your CodeCatalyst account, complete the following steps.

1. From the **Git** menu item in Visual Studio, choose **Clone Repository...**.

1. From the **Browse a Repository** section, select **Amazon CodeCatalyst** as the provider.

1. From the **Connection** section, choose **Connect with AWS Builder ID** to open the CodeCatalyst console in your preferred web browser.

1. From your browser, enter your AWS Builder ID into the provided field and follow the instructions to continue.

1. When prompted, choose **Allow** to confirm the connection between AWS Toolkit for Visual Studio with Amazon Q and your CodeCatalyst account. When the connection process is complete, CodeCatalyst displays a confirmation indicating that it's safe to close your browser.
