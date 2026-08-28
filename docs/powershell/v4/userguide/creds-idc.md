---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/creds-idc.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# Configure tool authentication with AWS
<a name="creds-idc"></a>

You must establish how your code authenticates with AWS when developing with AWS services. There are different ways in which you can configure programmatic access to AWS resources, depending on the environment and the AWS access available to you.

To see various methods of authentication for the Tools for PowerShell, see [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide*.

This topic assumes that a new user is developing locally, has not been given a method of authentication by their employer, and will be using AWS IAM Identity Center to obtain temporary credentials. If your environment doesn't fall under these assumptions, some of the information in this topic might not apply to you, or some of the information might have already been given to you.

Configuring this environment requires several steps, which are summarized as follows:

1. [Enable and configure IAM Identity Center](#idc-config-sso)

1. [Configure the Tools for PowerShell to use IAM Identity Center.](#idc-config-sdk)

1. [Start an AWS access portal session](#idc-start-portal)

## Enable and configure IAM Identity Center
<a name="idc-config-sso"></a>

To use AWS IAM Identity Center, it must first be enabled and configured. To see details about how to do this for PowerShell, look at **Step 1** in the topic for [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*. Specifically, follow any necessary instructions under **I do not have established access through IAM Identity Center**.

## Configure the Tools for PowerShell to use IAM Identity Center.
<a name="idc-config-sdk"></a>

**Note**
Starting with version 4.1.538 of the Tools for PowerShell, the recommended method to configure SSO credentials and start an AWS access portal session is to use the [`Initialize-AWSSSOConfiguration`](https://docs.aws.amazon.com/powershell/v4/reference/index.html?page=Initialize-AWSSSOConfiguration.html&tocid=Initialize-AWSSSOConfiguration) and [`Invoke-AWSSSOLogin`](https://docs.aws.amazon.com/powershell/v4/reference/index.html?page=Invoke-AWSSSOLogin.html&tocid=Invoke-AWSSSOLogin) cmdlets, as described in this topic. If you don't have access to that version of the Tools for PowerShell (or later) or can't use those cmdlets, you can still perform these tasks by using the AWS CLI. To find out how, see [Use the AWS CLI for portal login](creds-idc-cli.md).

The following procedure updates the shared AWS `config` file with SSO information that the Tools for PowerShell uses to obtain temporary credentials. As a consequence of this procedure, an AWS access portal session is also started. If the shared `config` file already has SSO information and you just want to know how to start an access portal session using the Tools for PowerShell, see the next section in this topic, [Start an AWS access portal session](#idc-start-portal).

1. If you haven't already done so, open PowerShell and install the AWS Tools for PowerShell as appropriate for your operating system and environment, including the common cmdlets. For information about how to do this, see [Installing the AWS Tools for PowerShell](pstools-getting-set-up.md).

   For example, if installing the modularized version of the Tools for PowerShell on Windows, you would most likely run commands similar to the following:

   ```
   Install-Module -Name AWS.Tools.Installer
   Install-AWSToolsModule AWS.Tools.Common
   ```

1. Run the following command. Replace the example property values with values from your IAM Identity Center configuration. For information about these properties and how to find them, see [IAM Identity Center credential provider settings](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sso-credentials.html#feature-sso-credentials-profile) in the *AWS SDKs and Tools Reference Guide*.

   ```
   $params = @{
     ProfileName = 'my-sso-profile'
     AccountId = '{{111122223333}}'
     RoleName = '{{SamplePermissionSet}}'
     SessionName = 'my-sso-session'
     StartUrl = '{{https://provided-domain.awsapps.com/start}}'
     SSORegion = '{{us-west-2}}'
     RegistrationScopes = 'sso:account:access'
   };
   Initialize-AWSSSOConfiguration @params
   ```

   Alternatively, you can simply use the cmdlet by itself, `Initialize-AWSSSOConfiguration`, and the Tools for PowerShell prompts you for the property values.

   Considerations for certain property values:
   + If you simply followed the instructions to [enable and configure IAM Identity Center](#idc-config-sso), the value for `-RoleName` might be `PowerUserAccess`. But if you created an IAM Identity Center permission set specifically for PowerShell work, use that instead.
   + Be sure to use the AWS Region where you have configured IAM Identity Center.

1. At this point, the shared AWS `config` file contains a profile called `my-sso-profile` with a set of configuration values that can be referenced from the Tools for PowerShell. To find the location of this file, see [Location of the shared files](https://docs.aws.amazon.com/sdkref/latest/guide/file-location.html) in the *AWS SDKs and Tools Reference Guide*.

   The Tools for PowerShell uses the profile's SSO token provider to acquire credentials before sending requests to AWS. The `sso_role_name` value, which is an IAM role connected to an IAM Identity Center permission set, should allow access to the AWS services used in your application.

   The following sample shows the profile that was created by using the command shown above. Some of the property values and their order might be different in your actual profile. The profile's `sso-session` property refers to the section named `my-sso-session`, which contains settings to initiate an AWS access portal session.

   ```
   [profile my-sso-profile]
   sso_account_id={{111122223333}}
   sso_role_name={{SamplePermissionSet}}
   sso_session=my-sso-session

   [sso-session my-sso-session]
   sso_region={{us-west-2}}
   sso_registration_scopes=sso:account:access
   sso_start_url={{https://provided-domain.awsapps.com/start/}}
   ```

1. If you already have an active AWS access portal session, the Tools for PowerShell informs you that you are already logged in.

   If that's not the case, the Tools for PowerShell attempts to automatically open the SSO authorization page in your default web browser. Follow the prompts in your browser, which might include an SSO authorization code, username and password, and permission to access AWS IAM Identity Center accounts and permission sets.

   The Tools for PowerShell informs you that SSO login was successful.

## Start an AWS access portal session
<a name="idc-start-portal"></a>

Before running commands that accesses AWS services, you need an active AWS access portal session so that the Tools for PowerShell can use IAM Identity Center authentication to resolve credentials. To sign in to the AWS access portal, run the following command in PowerShell, where `-ProfileName my-sso-profile` is the name of the profile that was created in the shared `config` file when you followed the procedure in the previous section of this topic.

```
Invoke-AWSSSOLogin -ProfileName my-sso-profile
```

If you already have an active AWS access portal session, the Tools for PowerShell informs you that you are already logged in.

If that's not the case, the Tools for PowerShell attempts to automatically open the SSO authorization page in your default web browser. Follow the prompts in your browser, which might include an SSO authorization code, username and password, and permission to access AWS IAM Identity Center accounts and permission sets.

The Tools for PowerShell informs you that SSO login was successful.

To test if you already have an active session, run the following command after installing or importing the `AWS.Tools.SecurityToken` module as needed.

```
Get-STSCallerIdentity -ProfileName my-sso-profile
```

The response to the `Get-STSCallerIdentity` cmdlet reports the IAM Identity Center account and permission set configured in the shared `config` file.

## Example
<a name="idc-short-example"></a>

The following is an example of how to use IAM Identity Center with the Tools for PowerShell. It assumes the following:
+ You have enabled IAM Identity Center and configured it as described previously in this topic. The SSO properties are in the `my-sso-profile` profile, which was configured earlier in this topic.
+ When you log in through the `Initialize-AWSSSOConfiguration` or `Invoke-AWSSSOLogin` cmdlets, the user has at least read-only permissions for Amazon S3.
+ Some S3 buckets are available for that user to view.

Install or import the `AWS.Tools.S3` module as needed and then use the following PowerShell command to display a list of the S3 buckets.

```
Get-S3Bucket -ProfileName my-sso-profile
```

## Additional information
<a name="idc-additional-info"></a>
+ For more options on authentication for the Tools for PowerShell, such as the use of profiles and environment variables, see the [configuration](https://docs.aws.amazon.com/sdkref/latest/guide/creds-config-files.html) chapter in the *AWS SDKs and Tools Reference Guide*.
+ Some commands require an AWS Region to be specified. There are a number of ways to do so, including the `-Region` cmdlet option, the `[default]` profile, and the `AWS_REGION` environment variable. For more information, see [Specify AWS Regions](pstools-installing-specifying-region.md) in this guide and [AWS Region](https://docs.aws.amazon.com/sdkref/latest/guide/feature-region.html) in the *AWS SDKs and Tools Reference Guide*.
+ To learn more about best practices, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.
+ To create short-term AWS credentials, see [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the *IAM User Guide*.
+ To learn about other credential providers, see [Standardized credential providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

**Topics**
+ [Enable and configure IAM Identity Center](#idc-config-sso)
+ [Configure the Tools for PowerShell to use IAM Identity Center.](#idc-config-sdk)
+ [Start an AWS access portal session](#idc-start-portal)
+ [Example](#idc-short-example)
+ [Additional information](#idc-additional-info)
+ [Use the AWS CLI](creds-idc-cli.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
