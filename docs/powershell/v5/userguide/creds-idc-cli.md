---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/creds-idc-cli.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Use the AWS CLI for portal login
<a name="creds-idc-cli"></a>

Starting with version 4.1.538 of the Tools for PowerShell, the recommended method to configure SSO credentials and start an AWS access portal session is to use the [`Initialize-AWSSSOConfiguration`](https://docs.aws.amazon.com/powershell/v5/reference/index.html?page=Initialize-AWSSSOConfiguration.html&tocid=Initialize-AWSSSOConfiguration) and [`Invoke-AWSSSOLogin`](https://docs.aws.amazon.com/powershell/v5/reference/index.html?page=Invoke-AWSSSOLogin.html&tocid=Invoke-AWSSSOLogin) cmdlets, as described in [Authenticating the AWS Tools for PowerShell with AWS](creds-idc.md). If you don't have access to that version of the Tools for PowerShell (or later) or can't use those cmdlets, you can still perform these tasks by using the AWS CLI.

## Configure the Tools for PowerShell to use IAM Identity Center through the AWS CLI.
<a name="idc-config-sdk-cli"></a>

If you haven't already done so, be sure to [Enable and configure IAM Identity Center](creds-idc.md#idc-config-sso) before you proceed.

Information about how to configure the Tools for PowerShell to use IAM Identity Center through the AWS CLI is in **Step 2** in the topic for [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*. After you complete this configuration, your system should contain the following elements:
+ The AWS CLI, which you use to start an AWS access portal session before you run your application.
+ The shared AWS `config` file that contains a [`[default]` profile](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html#file-format-profile) with a set of configuration values that can be referenced from the Tools for PowerShell. To find the location of this file, see [Location of the shared files](https://docs.aws.amazon.com/sdkref/latest/guide/file-location.html) in the *AWS SDKs and Tools Reference Guide*. The Tools for PowerShell uses the profile's SSO token provider to acquire credentials before sending requests to AWS. The `sso_role_name` value, which is an IAM role connected to an IAM Identity Center permission set, should allow access to the AWS services used in your application.

  The following sample `config` file shows a `[default]` profile set up with an SSO token provider. The profile's `sso_session` setting refers to the named `sso-session` section. The `sso-session` section contains settings to initiate an AWS access portal session.

  ```
  [default]
  sso_session = my-sso
  sso_account_id = {{111122223333}}
  sso_role_name = {{SampleRole}}
  region = us-east-1
  output = json

  [sso-session my-sso]
  sso_region = us-east-1
  sso_start_url = {{https://provided-domain.awsapps.com/start}}
  sso_registration_scopes = sso:account:access
  ```

**Important**
Your PowerShell session must have the following modules installed and imported so that SSO resolution can work:
`AWS.Tools.SSO`
`AWS.Tools.SSOOIDC`
If you're using an older version of the Tools for PowerShell and you don't have these modules, you will get an error similar to the following: "Assembly AWSSDK.SSOOIDC could not be found...".

## Start an AWS access portal session
<a name="idc-start-portal-cli"></a>

Before running commands that accesses AWS services, you need an active AWS access portal session so that the Tools for Windows PowerShell can use IAM Identity Center authentication to resolve credentials. Depending on your configured session lengths, your access will eventually expire and the Tools for Windows PowerShell will encounter an authentication error. To sign in to the AWS access portal, run the following command in the AWS CLI.

```
aws sso login
```

Since you are using the `[default]` profile, you do not need to call the command with the `--profile` option. If your SSO token provider configuration is using a named profile, the command is `aws sso login --profile {{named-profile}}` instead. For more information about named profiles, see the [Profiles](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html#file-format-profile) section in the *AWS SDKs and Tools Reference Guide*.

To test if you already have an active session, run the following AWS CLI command (with the same consideration for named profile):

```
aws sts get-caller-identity
```

The response to this command should report the IAM Identity Center account and permission set configured in the shared `config` file.

**Note**
If you already have an active AWS access portal session and run `aws sso login`, you will not be required to provide credentials.
The sign-in process might prompt you to allow the AWS CLI access to your data. Because the AWS CLI is built on top of the SDK for Python (Boto), permission messages may contain variations of the `botocore` name.

## Example
<a name="idc-short-example-cli"></a>

The following is an example of how to use IAM Identity Center with the Tools for PowerShell. It assumes the following:
+ You have enabled IAM Identity Center and configured it as described previously in this topic. The SSO properties are in the `[default]` profile.
+ When you log in through the AWS CLI by using `aws sso login`, that user has at least read-only permissions for Amazon S3.
+ Some S3 buckets are available for that user to view.

Use the following PowerShell commands to display a list of the S3 buckets:

```
Install-Module AWS.Tools.Installer
Install-AWSToolsModule S3
# And if using an older version of the AWS Tools for PowerShell:
Install-AWSToolsModule SSO, SSOOIDC

# In older versions of the AWS Tools for PowerShell, we're not invoking a cmdlet from these modules directly,
# so we must import them explicitly:
Import-Module AWS.Tools.SSO
Import-Module AWS.Tools.SSOOIDC

# Older versions of the AWS Tools for PowerShell don't support the SSO login flow, so login with the CLI
aws sso login

# Now we can invoke cmdlets using the SSO profile
Get-S3Bucket
```

As mentioned above, since you are using the `[default]` profile, you do not need to call the `Get-S3Bucket` cmdlet with the `-ProfileName` option. If your SSO token provider configuration is using a named profile, the command is `Get-S3Bucket -ProfileName {{named-profile}}`. For more information about named profiles, see the [Profiles](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html#file-format-profile) section in the *AWS SDKs and Tools Reference Guide*.

## Additional information
<a name="idc-additional-info-cli"></a>
+ For more options on authentication for the Tools for PowerShell, such as the use of profiles and environment variables, see the [configuration](https://docs.aws.amazon.com/sdkref/latest/guide/creds-config-files.html) chapter in the *AWS SDKs and Tools Reference Guide*.
+ Some commands require an AWS Region to be specified. There are a number of ways to do so, including the `-Region` cmdlet option, the `[default]` profile, and the `AWS_REGION` environment variable. For more information, see [Specify the AWS Region for the AWS Tools for PowerShell](pstools-installing-specifying-region.md) in this guide and [AWS Region](https://docs.aws.amazon.com/sdkref/latest/guide/feature-region.html) in the *AWS SDKs and Tools Reference Guide*.
+ To learn more about best practices, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.
+ To create short-term AWS credentials, see [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the *IAM User Guide*.
+ To learn about other credential providers, see [Standardized credential providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html) in the *AWS SDKs and Tools Reference Guide*.
