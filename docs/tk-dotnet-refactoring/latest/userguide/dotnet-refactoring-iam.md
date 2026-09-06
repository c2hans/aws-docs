---
source_url: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/dotnet-refactoring-iam.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# AWS Identity and Access Management (IAM)
<a name="dotnet-refactoring-iam"></a>

If you use Toolkit for .NET Refactoring with a license included Visual Studio Amazon Machine Image (AMI) on Amazon EC2, you can use the `refactoringtoolkit-RefactoringToolkitCallerRole` without providing credentials or modifying configuration files. For more information, see [Install Toolkit for .NET Refactoring](dotnet-refactoring-installation.md) in this guide.

If you are not using Toolkit for .NET Refactoring with Amazon EC2 or if you prefer to create a user and assign roles to the user, follow the steps in this section to create the user, create access keys, and configure your AWS profile.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Create access keys for your user](#dotnet-refactoring-iam-access-key)
+ [Configure your AWS profile](#dotnet-refactoring-iam-profile)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Create access keys for your user
<a name="dotnet-refactoring-iam-access-key"></a>

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access? | To | By |
| --- | --- | --- |
| IAM | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.+  For the AWS CLI, see [Login for AWS local development](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs, see [Login for AWS local development](https://docs.aws.amazon.com/sdkref/latest/guide/access-login.html) in the *AWS SDKs and Tools Reference Guide*.  |
| Workforce identity<br />(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.+  For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*.  |
| IAM | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions in [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the IAM User Guide. |
| IAM | (Not recommended)Use long-term credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.+  For the AWS CLI, see [Authenticating using IAM user credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs and tools, see [Authenticate using long-term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html) in the *AWS SDKs and Tools Reference Guide*. <br />+  For AWS APIs, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the *IAM User Guide*.  |

## Configure your AWS profile
<a name="dotnet-refactoring-iam-profile"></a>

After you have created a user, you can configure your AWS named profile to apply settings and credentials to be applied when you run commands.

**Configure AWS profile in the assessment tool**

1. In the Toolkit for .NET Refactoring assessment tool, navigate to **Set up Toolkit for .NET Refactoring**.

1. Choose **Add a profile** under **AWS named profile**.

1. Enter your new **Profile name**, **AWS access key ID**, and **AWS secret access key**.

1. Choose **Add**.

**Configure AWS profile using the AWS CLI**

1. Run the following AWS CLI command to create a profile for Toolkit for .NET Refactoring. The profile is named `default` in the credentials file.

   ```
   aws configure
   ```

1. For each prompt, enter the corresponding information.
   + `AWS Access Key ID`
   + `AWS Secret Access Key`
   + `Default region name` (For example, `us-west-2`)
   + `Default output format`

1. After you configure the profile using the AWS CLI, Toolkit for .NET Refactoring will display the `default` profile under **AWS named profile** on the **Set up Toolkit for .NET Refactoring** page of the assessment tool.

For more information about configuring the AWS CLI, see [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the *AWS CLI User Guide*.
