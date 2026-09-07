---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/creds-idc.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Authenticating the AWS Tools for PowerShell with AWS
<a name="creds-idc"></a>

You must establish how your code authenticates with AWS when developing with AWS services. There are different ways in which you can configure programmatic access to AWS resources, depending on the environment and the AWS access available to you.

To see various methods of authentication for the Tools for PowerShell, see [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide*.

This topic assumes that a new user is developing locally, has not been given a method of authentication by their employer, and will be using AWS IAM Identity Center to obtain temporary credentials. If your environment doesn't fall under these assumptions, some of the information in this topic might not apply to you, or some of the information might have already been given to you.

Configuring this environment requires several steps, which are summarized as follows:

1. [Login using console credentials](#login-con-creds)

1. [Enable and configure IAM Identity Center](#idc-config-sso)

1. [Configure the Tools for PowerShell to use IAM Identity Center.](#idc-config-sdk)

1. [Start an AWS access portal session](#idc-start-portal)

## Login using console credentials
<a name="login-con-creds"></a>

You can use your existing AWS Management Console sign-in credentials for programmatic access to AWS services. After a browser-based authentication flow, AWS Tools for PowerShell generates temporary credentials that work across local development tools like the AWS SDKs, AWS Tools for PowerShell and AWS CLI. This feature simplifies the process of configuring and managing CLI credentials, especially if you prefer interactive authentication over managing long-term access keys.

With this process, you can authenticate using root credentials created during initial account set up, an IAM user, or a federated identity from your identity provider, and Tools for PowerShell automatically manages the temporary credentials for you. This approach enhances security by eliminating the need to store long-term credentials locally.

When you run the `Invoke-AWSLogin` cmdlet, you can select from your active console sessions, or sign in through the browser-based authentication flow and this will automatically generate temporary credentials. AWS Tools for PowerShell will automatically refresh these credentials for up to 12 hours.

Once configured, your session can be used in AWS Tools for PowerShell and all other AWS SDKs and Tools.

### Prerequisites
<a name="idc-invoke-login-prerequisites"></a>
+ Access to sign into the AWS Management Console as a root user, IAM user, or through federation with IAM. If you use IAM Identity Center, go to [Configure the Tools for PowerShell to use IAM Identity Center.](#idc-config-sdk) instead.
+ Ensure the IAM identity has the appropriate permissions. Attach the [SignInLocalDevelopmentAccess](https://docs.aws.amazon.com/signin/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-SignInLocalDevelopmentAccess) managed policy to your IAM user, role, or group. If you sign in as a root user, no additional permissions are required.

### Log in to AWS with the Invoke-AWSLogin Cmdlet
<a name="idc-invoke-login"></a>

Run the `Invoke-AWSLogin` cmdlet to authenticate using your existing AWS Management Console credentials. If you have not previously configured a profile, you will be prompted for additional information.

To sign in or configure a profile follow the below steps.

1. Make sure you have imported the correct module you have installed from the installation guide.
**Note**
We have three different modules for PowerShell - `AWS.Tools`, `AWSPowerShell.NetCore` and `AWSPowerShell`. See [What are the AWS Tools for PowerShell?](pstools-welcome.md) for more information.
   + In your PowerShell terminal, run the cmdlet. This will use the `default` profile.

     ```
     PS > Invoke-AWSLogin
     ```
   + To sign in to a named profile or create a new one, use the `-ProfileName` parameter.

     ```
     PS > Invoke-AWSLogin -ProfileName 'my-dev-profile'
     ```
   + If this is a new profile or no AWS Region has been specified or configured in any of your previous profiles/environment variables, the cmdlet prompts you to provide a region.

     ```
     Press Ctrl+C to cancel the following login prompts.

     Specify AWS Region
     No AWS region has been configured. The AWS region is the geographic location of your AWS resources.

     If you've used AWS before and already have resources in your account, tell us which region they were created in. If you
      haven't created resources in your account before, you can pick the region closest to you:
     https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html

     AWS Region:
     ```

1. The AWS Tools for PowerShell attempts to open your default browser for the sign in process of your AWS account.

   ```
   Using region 'us-west-2'
   Attempting to open the login page for 'us-west-2' in your default browser.
   If the browser does not open, use the following URL to complete your login:
   https://signin.us-west-2.amazonaws.com/authorize?<abbreviated>

   If you cannot connect to this URL, make sure that you have specified a valid region.
   ```
   + If the device using AWS Tools for PowerShell does not have a browser, you can use the `-Remote` parameter to provide a URL for you to open on a browser-enabled device.

     ```
     PS > Invoke-AWSLogin -Remote
     ```
   + If you used the `-Remote` parameter, instructions to manually start the sign in process are displayed based on the type of authorization you are using. The URL displayed is a unique URL starting with: https://signin.us-east-1.amazonaws.com/authorize. Once you complete the browser log in, you will need to copy and paste the resulting authorization code back in the terminal.

     ```
     Press Ctrl+C to cancel the following login prompts.
     Using region 'us-west-2' determined by profile/environment defaults. To override, specify '-Region' parameter.
     Please complete the login workflow via the following URL:

     https://us-west-2.signin.aws.amazon.com/v1/authorize?<abbrievated>

     Please enter the authorization code displayed in the browser:
     ```

1. In the browser, select your credentials to use from the displayed list and then return to your terminal.
   + If the profile you are configuring has a previously configured login session that does not match your new session, the AWS Tools for PowerShell prompts you to confirm that you are switching the session that corresponds to the existing profile.

     ```
     WARNING: Previously profile default was configured for arn:aws:iam::0123456789012:user/ReadOnly,
                     and is now being updated to arn:aws:iam::0123456789012:user/Admin.

     Do you wish to change the identity that default is associated with? (y/n)
     ```

1. A final message describes the completed profile configuration.

   ```
   Login completed successfully for profile 'my-dev-profile'.
   ```

   The authentication token is cached to disk under the .aws/login/cache directory with a hash filename based on the resolved profile.

#### Generated configuration file
<a name="idc-generated-config"></a>

These steps result in creating the default or specified profile in the config file that looks like the following:

```
[default]
login_session = arn:aws:iam::0123456789012:user/username
region = us-east-1

[my-dev-profile]
login_session = arn:aws:iam::0123456789012:user/username
region = us-east-1
```

#### Run a command with your profile
<a name="idc-run-command"></a>

Once signed in, you can use your credentials to invoke Tools for PowerShell cmdlets with the associated profile. The following example calls the `Get-STSCallerIdentity` cmdlet using the default profile:

```
PS > Get-STSCallerIdentity
```

To check for a specific session, use the `-ProfileName` parameter.

```
PS > Get-STSCallerIdentity -ProfileName 'my-dev-profile'
```

The temporary credential token will expire in 15 minutes, but the AWS Tools for PowerShell and SDKs automatically refresh the token when needed during your requests. The overall session will be valid for up to 12 hours, after which you must run the `Invoke-AWSLogin` cmdlet again.

#### Signing out of your session using the `Invoke-AWSLogout` cmdlet
<a name="idc-logout"></a>

When you are done with your session, you can let your credentials expire, or run the `Invoke-AWSLogout` cmdlet to delete your cached credentials. If no profile is specified in the CLI or in the AWS\_PROFILE environment variable, the command signs you out of your default profile. The following example signs you out of your default profile.

```
PS > Invoke-AWSLogout
```

To sign out of a specific profile session, use the `-ProfileName` parameter.

```
PS > Invoke-AWSLogout -ProfileName 'my-dev-profile'
```

To sign out of all the profile sessions you've logged in, use the `-All` parameter.

```
PS > Invoke-AWSLogout -All
```

#### Cached Credentials
<a name="idc-cached-credentials"></a>

The temporary cached credentials, as well as the metadata required to refresh them are stored by default in `%USERPROFILE%\.aws\login\cache` on Windows or `~/.aws/login/cache` on Linux and MacOS.

You can override this location by setting the `AWS_LOGIN_CACHE_DIRECTORY` environment variable.

## Enable and configure IAM Identity Center
<a name="idc-config-sso"></a>

To use AWS IAM Identity Center, it must first be enabled and configured. To see details about how to do this for PowerShell, look at **Step 1** in the topic for [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*. Specifically, follow any necessary instructions under **I do not have established access through IAM Identity Center**.

## Configure the Tools for PowerShell to use IAM Identity Center.
<a name="idc-config-sdk"></a>

**Note**
Starting with version 4.1.538 of the Tools for PowerShell, the recommended method to configure SSO credentials and start an AWS access portal session is to use the [`Initialize-AWSSSOConfiguration`](https://docs.aws.amazon.com/powershell/v5/reference/index.html?page=Initialize-AWSSSOConfiguration.html&tocid=Initialize-AWSSSOConfiguration) and [`Invoke-AWSSSOLogin`](https://docs.aws.amazon.com/powershell/v5/reference/index.html?page=Invoke-AWSSSOLogin.html&tocid=Invoke-AWSSSOLogin) cmdlets, as described in this topic. If you don't have access to that version of the Tools for PowerShell (or later) or can't use those cmdlets, you can still perform these tasks by using the AWS CLI. To find out how, see [Use the AWS CLI for portal login](creds-idc-cli.md).

The following procedure updates the shared AWS `config` file with SSO information that the Tools for PowerShell uses to obtain temporary credentials. As a consequence of this procedure, an AWS access portal session is also started. If the shared `config` file already has SSO information and you just want to know how to start an access portal session using the Tools for PowerShell, see the next section in this topic, [Start an AWS access portal session](#idc-start-portal).

1. If you haven't already done so, open PowerShell and install the AWS Tools for PowerShell as appropriate for your operating system and environment, including the common cmdlets. For information about how to do this, see [Get started with the AWS Tools for PowerShell](pstools-getting-set-up.md).

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
+ Some commands require an AWS Region to be specified. There are a number of ways to do so, including the `-Region` cmdlet option, the `[default]` profile, and the `AWS_REGION` environment variable. For more information, see [Specify the AWS Region for the AWS Tools for PowerShell](pstools-installing-specifying-region.md) in this guide and [AWS Region](https://docs.aws.amazon.com/sdkref/latest/guide/feature-region.html) in the *AWS SDKs and Tools Reference Guide*.
+ To learn more about best practices, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.
+ To create short-term AWS credentials, see [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the *IAM User Guide*.
+ To learn about other credential providers, see [Standardized credential providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

**Topics**
+ [Login using console credentials](#login-con-creds)
+ [Enable and configure IAM Identity Center](#idc-config-sso)
+ [Configure the Tools for PowerShell to use IAM Identity Center.](#idc-config-sdk)
+ [Start an AWS access portal session](#idc-start-portal)
+ [Example](#idc-short-example)
+ [Additional information](#idc-additional-info)
+ [Use the AWS CLI](creds-idc-cli.md)
