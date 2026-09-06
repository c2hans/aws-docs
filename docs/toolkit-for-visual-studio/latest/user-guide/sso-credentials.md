---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/sso-credentials.html
---

# AWS IAM Identity Center credentials in AWS Toolkit for Visual Studio
<a name="sso-credentials"></a>

AWS IAM Identity Center is the recommended best practice for managing your AWS account authentication.

For detailed instructions on how to set up IAM Identity Center for Software Development Kits (SDKs) and the AWS Toolkit for Visual Studio, see the [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) section of the *AWS SDKs and Tools Reference Guide*.

## Authenticating with IAM Identity Center from the AWS Toolkit for Visual Studio
<a name="adding-sso-profile"></a>

To authenticate with IAM Identity Center from the AWS Toolkit for Visual Studio by adding an IAM Identity Center profile to your `credentials` or `config` file, complete the following steps.

1. From your preferred text editor, open the AWS credentials information stored in the `<hone-directory>\.aws\credentials` file.

1. From the `credentials file` under the section `[default]`, add a template for a named IAM Identity Center profile. The following is an example template:
**Important**
Do not use the word *profile* when creating an entry in the `credential` file because creates a conflict with the `credential` file naming conventions.
Include the prefix word `profile_` only when configuring a named profile in the `config` file.

   ```
   [{{sso-user-1}}]
   sso_start_url = {{https://example.com/start}}
   sso_region = {{us-east-2}}
   sso_account_id = {{123456789011}}
   sso_role_name = {{readOnly}}
   region = {{us-west-2}}
   ```
+ **`sso_start_url`**: The URL that points to your organization's IAM Identity Center user portal.
+ **`sso_region`**: The AWS Region that contains your IAM Identity Center portal host. This can be different from the AWS Region specified later in the default `region` parameter.
+ **`sso_account_id`**: The AWS account ID that contains the IAM role with the permission that you want to grant to this IAM Identity Center user.
+ **`sso_role_name`**: The name of the IAM role that defines the user's permissions when using this profile to get credentials through IAM Identity Center.
+ **`region`**: The default AWS Region that this IAM Identity Center user signs into.

**Note**
You can also add an IAM Identity Center enabled profile to your AWS CLI by running the `aws configure sso` command. After running this command, you provide values for the IAM Identity Center start URL (`sso_start_url`) and the AWS Region (`region`) that hosts the IAM Identity Center directory.
For more information, see [Configuring the AWS CLI to use AWS Single Sign-On](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) in the *AWS Command Line Interface User Guide*.

### Signing in with IAM Identity Center
<a name="sso-sign-in"></a>

When signing in with an IAM Identity Center profile, the default browser is launched to the `sso_start_url` specified in your `credential file`. You must verify your IAM Identity Center login before you can access your AWS resources in AWS Toolkit for Visual Studio. If your credentials expire, you'll have to repeat the connection process to obtain new temporary credentials.
