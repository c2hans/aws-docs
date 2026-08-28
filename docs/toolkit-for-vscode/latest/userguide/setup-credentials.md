---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-credentials.html
---

# AWS IAM credentials
<a name="setup-credentials"></a>

AWS IAM credentials authentication with your AWS account through locally stored access keys.

For details about how to authenticate and connect the AWS toolkit with your existing AWS IAM credentials, see the [Connect to AWS](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/connect.html) topic in this User Guide.

The following sections describe how to set up IAM credentials to authenticate with your AWS account from the AWS Toolkit for Visual Studio Code.

**Important**
Before setting up IAM credentials to authenticate with your AWS account, note that:
If you've already set IAM credentials through another AWS service (such as the AWS CLI), then the AWS Toolkit for Visual Studio Code automatically detects those credentials and makes them available in VS Code.
AWS recommends using IAM Identity Center authentication. For additional information about AWS IAM best practices, see the [Security best practice in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) section of the AWS *Identity and Access Management* User Guide.
To avoid security risks, don't use IAM users for authentication when developing purpose-built software or working with real data. Instead, use federation with an identity provider such as [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) in the *AWS IAM Identity Center User Guide*.

## Creating an IAM user
<a name="setup-credentials-iam"></a>

Before you can set up the AWS Toolkit for Visual Studio Code to authenticate with your AWS account, you need to complete **Step 1: Create your IAM user** and **Step 2: Get your access keys** in the [Authenticate using long-term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html) topic in the *AWS SDKs and Tools Reference Guide*.

**Note**
**Step 3: Update the shared credentials file** in the *AWS SDKs and Tools Reference Guide* is optional.
If you complete Step 3, the AWS Toolkit for Visual Studio Code automatically detects your credentials during the [Creating a shared credentials file from the AWS Toolkit for Visual Studio Code](#setup-credentials-about-files) located below.
If you haven't completed Step 3, the AWS Toolkit for Visual Studio Code walks you through the process of creating a `credentials file` as described in the [Creating a shared credentials file from the AWS Toolkit for Visual Studio Code](#setup-credentials-about-files) located below.

## Creating a shared credentials file from the AWS Toolkit for Visual Studio Code
<a name="setup-credentials-about-files"></a>

Your *shared config file* and *shared credentials file* store configuration and credential information for your AWS accounts. For more information about shared configuration and credentials, see the [Where are configuration settings stored?](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-where) section in the *AWS Command Line Interface User Guide*.

**Creating a shared credentials file through the AWS Toolkit for Visual Studio Code**

1. Open the command pallet by pressing **Shift\+Command\+P** (**Ctrl\+Shift\+P** Windows).

1. Enter **AWS: Add a New Connection** into the search field.

1. Select **AWS: Add a New Connection** to open the **AWS Toolkit Sign In** panel.

1. From the **AWS Toolkit Sign In** panel, choose **IAM Credential**, then select the **Continue** button to proceed.

1. Enter the **Profile Name**, **Access Key**, and **Secret Key** of your AWS account in the provided fields, then choose the **Continue** button to add the profile to your config file and connect the Toolkit with your AWS account.

1. The Toolkit **AWS Explorer** updates to display your AWS services and resources when authentication is complete and a connection has been established.

**Note**
In this example, assume that {{[Profile\_Name]}} contains syntax errors and causes authentication to fail.

```
{{[Profile_Name]}}
xaws_access_key_id= {{AKIAI44QH8DHBEXAMPLE}}
xaws_secret_access_key= {{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
```
The following is an example of a log message that's generated in response to a failed authentication attempt.

```
2022-11-02 22:01:54 [ERROR]: Profile {{[Profile_Name]}} is not a valid Credential Profile: not supported by the Toolkit
2022-11-02 22:01:54 [WARN]: Shared Credentials Profile {{[Profile_Name]}} is not valid. It will not be used by the toolkit.
```

## Add additional credential profiles
<a name="add-credential-profiles"></a>

You can add multiple credentials to your configuration files. To do so, open the **Command Palette** and choose **AWS Toolkit Create Credentials Profile**. This will open the credentials file. On this page, you can add a new profile below your first profile, as shown in the following example:

```
# Amazon Web Services Credentials File used by AWS CLI, SDKs, and tools
# This file was created by the AWS Toolkit for Visual Studio Code extension.
#
# Your AWS credentials are represented by access keys associated with IAM users.
# For information about how to create and manage AWS access keys for a user, see:
# https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html
#
# This credential file can store multiple access keys by placing each one in a
# named "profile". For information about how to change the access keys in a
# profile or to add a new profile with a different access key, see:
# https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html
#
{{[Profile1_Name]}}
# The access key and secret key pair identify your account and grant access to AWS.
aws_access_key_id = {{AKIAIOSFODNN7EXAMPLE}}
# Treat your secret key like a password. Never share your secret key with anyone. Do
# not post it in online forums, or store it in a source control system. If your secret
# key is ever disclosed, immediately use IAM to delete the access key and secret key
# and create a new key pair. Then, update this file with the replacement key details.
aws_secret_access_key = {{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
{{[Profile2_Name]}}
aws_access_key_id = {{AKIAI44QH8DHBEXAMPLE}}
aws_secret_access_key = {{je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
