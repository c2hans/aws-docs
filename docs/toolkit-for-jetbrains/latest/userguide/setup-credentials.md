---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/setup-credentials.html
---

# AWS IAM credentials
<a name="setup-credentials"></a>

AWS Identity and Access Management (AWS IAM) Credentials authenticate with your AWS account through locally-stored access keys.

For instructions on how to authenticate with your existing IAM Credentials in the AWS Toolkit for JetBrains, see the [Connecting to AWS](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/account-connect.html) topic in this User Guide.

The following sections describe how to set up new IAM Credentials.

**Important**
Before setting up IAM credentials to authenticate with your AWS account, note that:
If you've already set IAM credentials through another AWS service (such as the AWS CLI), then the AWS Toolkit for JetBrains automatically detects those credentials and makes them available.
AWS recommends using IAM Identity Center authentication. For additional information about AWS IAM best practices, see the [Security best practice in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) section of the AWS *Identity and Access Management* User Guide.
To avoid security risks, don't use IAM users for authentication when developing purpose-built software or working with real data. Instead, use federation with an identity provider such as [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) in the *AWS IAM Identity Center User Guide*.

## Prerequisites
<a name="prereqs"></a>

Before you can configure the AWS Toolkit for JetBrains to authenticate with IAM user credentials, the following prerequisites must be met. If you've already set up IAM user credentials through another service (such as the AWS Command Line Interface), then you can skip the prerequisite steps and proceed to the following sections.

1. **Create an IAM user**. For detailed instructions on how to create an IAM user, see [Step 1: Create your IAM user](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html#step1authIamUser) in the *AWS SDKs and Tools Reference Guide*.

1. **Get your IAM user access keys**. For detailed instructions on how to get your IAM user access keys, see [Step 2: Get your access keys](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html#stepGetKeys) in the *AWS SDKs and Tools Reference Guide*.

1. **Optional: Update the shared credentials file**. For detailed instructions on how to update the shared credentials file, see [Step 3: Update the shared credentials file](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html#stepauthIamUser) in the *AWS SDKs and Tools Reference Guide*.
**Note**
If the optional prerequisite **Step 3: Update the shared credentials file** has been completed, the AWS Toolkit for JetBrains automatically detects your credentials during the **Creating a shared credentials file from the AWS Toolkit for JetBrains** procedure described in the following section.

## Creating a shared credentials file from the AWS Toolkit for JetBrains
<a name="setup-credentials-first-connect"></a>

Your *shared config file* and *shared credentials file* store configuration and credential information for your AWS accounts. For more information about shared configuration and credentials, see the [Where are configuration settings stored?](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-where) section in the *AWS Command Line Interface User Guide*.

**Creating a shared credentials file from the AWS Toolkit for JetBrains**

1. From the AWS Toolkit for JetBrains open **AWS Connection Settings** by choosing the **...** (ellipsis) icon.

1. From the **AWS Connection Settings** menu, choose **Set up authentication** to open the **AWS Toolkit for JetBrains** connection UI.

1. From the **AWS Explorer** section of the **Authenticate with AWS Toolkit** connection UI, choose the **Authenticate with IAM** link to open the **AWS Toolkit: Setup Authentication** dialog.

1. From the **IAM Credentials** tab, enter your **Profile Name**, **Access Key ID**, and **Secret Access Key**, then choose the **Connect** button to add the profile to your config file and connect the Toolkit with your AWS account.

1. The Toolkit **AWS Explorer** updates to display your AWS services and resources when authentication is complete and a connection has been established.

## Configuring shared credentials
<a name="setup-credentials-first-configure"></a>

The following procedure describes how to configure your shared credentials files from the AWS Toolkit for JetBrains.

1. From the AWS Toolkit for JetBrains, choose **\+ Add Connection to AWS** to open the **AWS Toolkit: Add Connection** dialog box.

1. From the **AWS Toolkit: Add Connection** dialog box, choose **Edit AWS Credential files(s)** to open your **Credential File**.

1. When your `credentials file` opens in the JetBrains, locate the section labeled `[default]`.

1. From the `[default]` section, locate the entry `#aws_access_key_id =`, remove the `#` and enter your AWS access key. The entry should look similar to the following:

   **aws\_access\_key\_id = AKIAIOSFODNN7EXAMPLE**

1. From the `[default]` section, locate the entry `#aws_secret_access_key =`, remove the `#` and enter your AWS secret access key. The entry should look similar to the following:

   **aws\_secret\_access\_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY**

   The final version of your updated credentials file resembles the following:

   ```
   [default]
   # The access key and secret key pair identify your account and grant access to AWS.
   # Treat your secret key like a password. Never share your secret key with anyone. Do
   # not post it in online forums, or store it in a source control system. If your secret
   # key is ever disclosed, immediately use IAM to delete the access key and secret key
   # and create a new key pair. Then, update this file with the replacement key details.
   aws_access_key_id = AKIAIOSFODNN7EXAMPLE
   aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
   ```

1. Save your changes to the file, the AWS Toolkit for JetBrains automatically detects your updated credentials and connects to your AWS account.

   **aws\_secret\_access\_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for JetBrains. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-jetbrains` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
