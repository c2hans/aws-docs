---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html
---

# Using long-term credentials to authenticate AWS SDKs and tools
<a name="access-iam-users"></a>

**Warning**
To avoid security risks, don't use IAM users for authentication when developing purpose-built software or working with real data. Instead, use federation with an identity provider such as [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

If you use an IAM user to run your code, then the SDK or tool in your development environment authenticates by using long-term IAM user credentials in the shared AWS `credentials` file. Review the [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp) topic and transition to IAM Identity Center or other temporary credentials as soon as possible.

## Important warnings and guidance for credentials
<a name="iam-warnings-and-guidelines"></a>

**Warnings for credentials**
+ ***Do NOT*** use your account's root credentials to access AWS resources. These credentials provide unrestricted account access and are difficult to revoke.
+ ***Do NOT*** put literal access keys or credential information in your application files. If you do, you create a risk of accidentally exposing your credentials if, for example, you upload the project to a public repository.
+ ***Do NOT*** include files that contain credentials in your project area.
+ Be aware that any credentials stored in the shared AWS `credentials` file are stored in plaintext.

**Additional guidance for securely managing credentials**

For a general discussion of how to securely manage AWS credentials, see [Best practices for managing AWS access keys](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html) in the [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/). In addition to that discussion, consider the following:
+ Use [IAM roles for tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) for Amazon Elastic Container Service (Amazon ECS) tasks.
+ Use [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) for applications that are running on Amazon EC2 instances.

## Prerequisites: Create an AWS account
<a name="signup"></a>

To use an IAM user to access AWS services, you need an AWS account and AWS credentials.

1. **Create an account.**

   To create an AWS account, see [Getting started: Are you a first-time AWS user?](https://docs.aws.amazon.com/accounts/latest/reference/welcome-first-time-user.html) in the *AWS Account Management Reference Guide*.

1. **Create an administrative user.**

   Avoid using your root user account (the initial account you create) to access the management console and services. Instead, create an administrative user account, as explained in [Create an administrative user](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) in the *IAM User Guide*.

   After you create the administrative user account and record the login details, **be sure to sign out of your root user account** and sign back in using the administrative account.

Neither of these accounts are appropriate for doing development on AWS or for running applications on AWS. As a best practice, you need to create users, permission sets, or service roles that are appropriate for these tasks. For more information, see [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the *IAM User Guide*.

## Step 1: Create your IAM user
<a name="step1authIamUser"></a>
+ Create your IAM user by following the [Creating IAM users (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console) procedure in the *IAM User Guide*. When creating your IAM user:
  + We recommend you select **Provide user access to the AWS Management Console**. This allows you to view AWS services related to the code that you are running in a visual environment, such as checking AWS CloudTrail diagnostic logs or uploading files to Amazon Simple Storage Service, which is helpful when debugging your code.
  + For **Set permissions** - **Permission options**, select **Attach policies directly** for how you want to assign permissions to this user.
    + Most "Getting Started" SDK tutorials use the Amazon S3 service as an example. To provide your application with full access to Amazon S3, select the `AmazonS3FullAccess` policy to attach to this user.
  + You can ignore the optional steps of that procedure regarding setting permission boundaries or tags.

## Step 2: Get your access keys
<a name="stepGetKeys"></a>

1. In the navigation pane of the IAM console, select **Users** and then select the **User name** of the user that you created previously.

1. On the user's page, select the **Security credentials** page. Then, under **Access keys**, select **Create access key**.

1. For **Create access key Step 1**, choose either **Command Line Interface (CLI)** or **Local code**. Both options generate the same type of key to use with both the AWS CLI and the SDKs.

1. For **Create access key Step 2**, enter an optional tag and select **Next**.

1. For **Create access key Step 3**, select **Download .csv file** to save a `.csv` file with your IAM user's access key and secret access key. You need this information for later.
**Warning**
Use appropriate security measures to keep these credentials safe.

1. Select **Done**.

## Step 3: Update the shared `credentials` file
<a name="stepauthIamUser"></a>

1. Create or open the shared AWS `credentials` file. This file is `~/.aws/credentials` on Linux and macOS systems, and `%USERPROFILE%\.aws\credentials` on Windows. For more information, see [Location of Credentials Files](https://docs.aws.amazon.com/credref/latest/refdocs/file-location.html).

1. Add the following text to the shared `credentials` file. Replace the example ID value and example key value with the values in the `.csv` file that you downloaded earlier.

   ```
   [default]
   aws_access_key_id = {{AKIAIOSFODNN7EXAMPLE}}
   aws_secret_access_key = {{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
   ```

1. Save the file.

The shared `credentials` file is the most common way to store credentials. These can also be set as environment variables, see [AWS access keys](feature-static-credentials.md) for environment variable names. This is a way to get you started, but we recommend you transition to IAM Identity Center or other temporary credentials as soon as possible. After you transition away from using long-term credentials, remember to delete these credentials from the shared `credentials` file.
