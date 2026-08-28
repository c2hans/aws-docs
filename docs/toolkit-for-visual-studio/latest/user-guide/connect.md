---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/connect.html
---

# Connecting to AWS
<a name="connect"></a>

The following sections describe how to get started with the AWS Toolkit for Visual Studio with Amazon Q. The first time you launch Visual Studio after installing the extension, a **Getting Started** displays in the editor window. From the **Getting Started** tab you can complete the following actions.
+ Enable or disable Amazon Q and the AWS Toolkit.
+ Add and authenticate with new credentials.
+ Authenticate with existing credentials.
+ Access documentation and tutorials to help you get started working with Amazon Q and the AWS Toolkit.

## Prerequisites
<a name="connecting-to-aws"></a>

To get started working with Amazon Q and the AWS Toolkit, you need to authenticate with AWS credentials. If you've previously set up an AWS account and authentication through another AWS tool or service (such as the AWS Command Line Interface), then the AWS Toolkit automatically detects your credentials. If you're new to AWS or haven't created an account, then you can sign up for an AWS account from the [AWS sign up portal]( https://portal.aws.amazon.com/billing/signup). For detailed information on setting up a new AWS account, see the [Overview](https://docs.aws.amazon.com/SetUp/latest/UserGuide/setup-overview.html) topic in the *AWS Setup User Guide*.

## Connecting to AWS from the Toolkit
<a name="connect-to-aws"></a>

To connect to your AWS accounts from the AWS Toolkit, open the **Getting Started** tab at any time by completing the following.

**Opening the **Getting Started** tab in Visual Studio**

1. From Visual Studio, expand **Extensions** from the main menu and then expand the **AWS Toolkit** sub-menu.

1. Choose **Getting started**.

1. The **Getting Started** tab opens in the Visual Studio editor window.

From the **Getting Started** tab, there are 2 main sections:
+ **Features:** In this section you can enable or disable features like Amazon Q and the AWS Toolkit.
+ **Documentation and Tutorials:** A collection of references to your enabled features.
**Note**
The Documentation and Tutorials section is only visible when one or more features is enabled.

## Amazon Q Developer
<a name="whisperer"></a>

From the Amazon Q section in the **Getting Started** tab, you can enable or disable Amazon Q, add a new connection, or switch to a different AWS connection. Before you can view or access any of these actions, Amazon Q must be enabled. To enable Amazon Q click the **Enable** button.

When Amazon Q is disabled, all Amazon Q features and functions are completely removed from Visual Studio. Enabling Amazon Q automatically opens the **Setup authentication for Amazon Q** in the **Getting Started** tab. To proceed, you must authenticate with your AWS IAM Identity Center credentials to access the **Professional Tier** or your AWS Builder ID to access the **Free Tier**. For detailed information about each of the tier options, see the [Understanding tiers of service for Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-tiers.html) topic in the *Amazon Q Developer* User Guide.

To proceed complete one of the following procedures.

**Professional tier authentication with IAM Identity Center**
**Note**
The **Profile Name**, **Start URL**, **Profile Region**, or **SSO Region** fields that are required to authenticate with the Professional tier are typically provided by an administrator at your company or organization. For detailed information about IAM Identity Center credentials, see the [What is IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) topic in the *AWS IAM Identity Center* User Guide.

1. From the **Getting Started: AWS Toolkit with Amazon Q** screen, choose the **Sign in** button in the Amazon Q tile to navigate to the **Setup authentication for Amazon Q** screen.

1. From the **Setup authentication for Amazon Q** screen, navigate to the **Professional tier** section, fill in the required fields and choose the **Connect** button.

1. Confirm that you want to open the AWS Authorize request portal in your default web browser.

1. Complete the steps required by the AWS Authorize request portal, you're notified when it's safe to close your browser and return to Visual Studio

1. In the **Getting Started** tab, Amazon Q updates to show you're connected with IAM Identity Center when the process is complete.

**Free tier authentication with AWS Builder ID**
**Note**
For additional details about AWS Builder ID, see the [Sign in with AWS Builder ID](https://docs.aws.amazon.com/signin/latest/userguide/sign-in-aws_builder_id.html) topic in the *AWS Sign-in* User Guide.

1. From the **Getting Started: AWS Toolkit with Amazon Q** screen, choose the **Sign in** button in the Amazon Q tile to navigate to the **Setup authentication for Amazon Q** screen.

1. From the **Setup authentication for Amazon Q** screen, navigate to the **Free Tier** section and choose the **Sign up or Sign in** button.

1. Confirm that you want to open the AWS Authorize request portal in your default web browser.

1. Complete the steps required by the AWS Authorize request portal, you're notified when it's safe to close your browser and return to Visual Studio.

1. In the **Getting Started** tab, Amazon Q updates to show you're connected with your AWS Builder ID when the process is complete.

After you've authenticated with either your IAM Identity Center or AWS Builder ID credentials, you can access Amazon Q in Visual Studio. Additionally, you're able to perform the following actions in the **Getting Started** tab:
+ **Sign out**: disconnects your current credential connection from all Amazon Q functions. Amazon Q remains enabled, but most features don't work.
+ **Disable Amazon Q**: Completely disables all Amazon Q features in Visual Studio.

## AWS Toolkit
<a name="explorer"></a>

From the AWS Toolkit section in the **Getting Started with the AWS Toolkit** tab, you can enable or disable the AWS Toolkit, add a new connection, or switch to a different AWS connection. Before you can view or access any of these actions, the AWS Toolkit must be enabled. To enable the AWS Toolkit, click the **Enable** button.

When the AWS Toolkit is enabled, **Setup authentication for AWS Toolkit** automatically loads in the **Getting Started with the AWS Toolkit** tab. To proceed, you must authenticate with either your **AWS IAM Identity Center** credentials or your **IAM User Role** credentials.

**Note**
For detailed information about IAM Identity Center credentials, see the [What is IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) topic in the *AWS IAM Identity Center* User Guide. For detailed information about IAM User Role credentials, see the [AWS Access keys: Long-term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html) topic in the *AWS SDKs and Tools* reference guide.

**Authenticate and connect with IAM Identity Center**

1. From the **Getting Started: AWS Toolkit with Amazon Q** screen, choose the **Sign in** button in the AWS Toolkit tile to navigate to the **Setup authentication for AWS Toolkit** screen.

1. From the **Setup Authentication for AWS Toolkit** screen, choose **IAM Identity Center (Successor to Single Sign-on)** from the **Profile Type** drop-down menu.

1. From the **Choose from an existing Profile or add new** drop-down menu, choose an existing profile or select **Add new profile** to add new profile information.
**Note**
If you choose an existing profile, go to step 7.

1. In the **Profile Name** field, enter the **profile name** associated with the IAM Identity Center account that you want to authenticate with.

1. In the **Start URL** text field, enter the **Start URL** that's attached to your IAM Identity Center credentials.

1. From the **Profile Region (defaults to us-east-1)** drop-down menu, choose the **Profile Region** that's defined by the IAM Identity Center user profile you're authenticating with.

1. From the **SSO Region (defaults to us-east-1)** drop-down menu, choose the **SSO Region** that's defined by your IAM Identity Center credentials.

1. Choose the **Connect** button to open the **AWS Authorize request** site in your default web browser.

1. Follow the prompts in your default web browser, you're notified when the authorization process is complete, it's safe to close your browser, and return to Visual Studio.

1. In the **Getting Started** tab, the AWS Toolkit section updates to show you're connected with IAM Identity Center when the process is complete.

**Authenticate and connect with IAM User Role credentials**

1. From the **Getting Started: AWS Toolkit with Amazon Q** screen, choose the **Sign in** button in the AWS Toolkit tile to navigate to the **Setup authentication for AWS Toolkit** screen.

1. From the **Setup authentication for AWS Toolkit** screen, choose **IAM User Role** from the **Profile Type** drop-down menu.

1. In the **Choose from an existing Profile or add new** drop-down menu, choose **Add new profile**.
**Note**
If you're choosing an existing profile name from the list, skip to **Step 8**.

1. In the **Profile Name** text field, enter a name for your new profile.

1. In the **Access Key ID** text field, enter the **Access Key ID** for the profile you want to authenticate with.

1. In the **Secret Key** text field, enter the **Secret Key** for the profile you want to authenticate with.

1. From the **Storage Location (defaults to Shared Credentials File)** drop-down menu, specify whether you want to store your credentials with a **Shared Credentials** file or with **.NET Encrypted Store**.

1. From the **Profile Region (defaults to us-east-1)** drop-down menus, choose the **Partition** and **Profile Region** that are attached to the profile you want to authenticate with.

1. Choose the **Connect** button to add this profile to your AWS storage location and/or authenticate with AWS.

1. In the **Getting Started** tab, the AWS Toolkit section updates to show you're connected with your IAM User role credentials when the process is complete.

After you've authenticated with either your IAM Identity Center or IAM User Role credentials, you can access the AWS Explorer in the Toolkit for Visual Studio. Additionally, you're able to **Sign out** and **Disable the AWS Toolkit for Visual Studio with Amazon Q** from the **Getting Started** tab.

## Documentation and Tutorials
<a name="w2aac11c13c17"></a>

The documentation and Tutorials section automatically updates with documentation and tutorial suggestions based on your AWS service and feature preferences. These references are only visible when at least one feature has been enabled.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-visual-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
