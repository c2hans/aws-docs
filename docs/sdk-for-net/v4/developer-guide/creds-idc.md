---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/creds-idc.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Authenticating the AWS SDK for .NET with AWS
<a name="creds-idc"></a>

You must establish how your code authenticates with AWS when developing with AWS services. There are different ways in which you can configure programmatic access to AWS resources, depending on the environment and the AWS access available to you.

To see various methods of authentication for the SDK, see [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide*.

This topic assumes that a new user is developing locally, has not been given a method of authentication by their employer, and will be using AWS IAM Identity Center to obtain temporary credentials. If your environment doesn't fall under these assumptions, some of the information in this topic might not apply to you, or some of the information might have already been given to you.

 Configuring this environment requires several steps, which are summarized as follows:

1. [Login using console credentials](#login-con-creds)

1. [Enable and configure IAM Identity Center](#idc-config-sso)

1. [Configure the SDK to use IAM Identity Center.](#idc-config-sdk)

1. [Start an AWS access portal session](#idc-start-portal)

## Login using console credentials
<a name="login-con-creds"></a>

You can use your existing AWS Management Console sign-in credentials for programmatic access to AWS services. After a browser-based authentication flow, AWS generates temporary credentials that work across local development tools like the AWS CLI, AWS Tools for PowerShell and the AWS SDK for .NET v4.

With this process, you can authenticate using root credentials created during initial account set up, an IAM user, or a federated identity from your identity provider, and AWS CLI or AWS Tools for PowerShell automatically manages the temporary credentials for you. This approach enhances security by eliminating the need to store long-term credentials locally. When you run the `Invoke-AWSLogin ` cmdlet from AWS Tools for PowerShell or the `aws login` command from AWS CLI, you can select from your active console sessions, or sign in through the browser-based authentication flow and this will automatically generate temporary credentials. The temporary credential token will expire in 15 minutes, but the AWS SDK for .NET v4 automatically refresh the token when needed during your requests.

**Important**
If you're using the console credentials for authentication, your application must reference the following NuGet packages so that AWS Signin resolution can work:
**AWSSDK.Signin**
Failure to reference these packages will result in a runtime exception.
+ [AWS Tools for PowerShell login creds Developer Guide.](https://docs.aws.amazon.com/powershell/v5/userguide/creds-idc.html#login-con-creds)
+ [Login for AWS local development using console credentials using AWS CLI.](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html)

The `config` file would look like this once you’ve login following the steps given above for AWS Tools for PowerShell or AWS CLI.

```
[default]
login_session = arn:aws:iam::{{0123456789012}}:user/{{username}}
region = us-east-1

[my-dev-profile]
login_session = arn:aws:iam::{{0123456789012}}:user/{{username}}
region = us-east-1
```

## Enable and configure IAM Identity Center
<a name="idc-config-sso"></a>

To use IAM Identity Center, it must first be enabled and configured. To see details about how to do this for the SDK, look at **Step 1** in the topic for [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*. Specifically, follow any necessary instructions under **I do not have established access through IAM Identity Center**.

## Configure the SDK to use IAM Identity Center.
<a name="idc-config-sdk"></a>

Information about how to configure the SDK to use IAM Identity Center is in **Step 2** in the topic for [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*. After you complete this configuration, your system should contain the following elements:
+ The AWS CLI, which you use to start an AWS access portal session before you run your application.
+ The shared AWS `config` file that contains a [`[default]` profile](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html#file-format-profile) with a set of configuration values that can be referenced from the SDK. To find the location of this file, see [Location of the shared files](https://docs.aws.amazon.com/sdkref/latest/guide/file-location.html) in the *AWS SDKs and Tools Reference Guide*. The AWS SDK for .NET uses the profile's SSO token provider to acquire credentials before sending requests to AWS. The `sso_role_name` value, which is an IAM role connected to an IAM Identity Center permission set, should allow access to the AWS services used in your application.

  The following sample `config` file shows a default profile set up with SSO token provider. The profile's `sso_session` setting refers to the named `sso-session` section. The `sso-session` section contains settings to initiate an AWS access portal session.

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
If you're using AWS IAM Identity Center for authentication, your application must reference the following NuGet packages so that SSO resolution can work:
`AWSSDK.SSO`
`AWSSDK.SSOOIDC`
Failure to reference these packages will result in a *runtime* exception.

## Start an AWS access portal session
<a name="idc-start-portal"></a>

Before running an application that accesses AWS services, you need an active AWS access portal session for the SDK to use IAM Identity Center authentication to resolve credentials. Depending on your configured session lengths, your access will eventually expire and the SDK will encounter an authentication error. To sign in to the AWS access portal, run the following command in the AWS CLI.

```
aws sso login
```

Since you have a default profile setup, you do not need to call the command with a `--profile` option. If your SSO token provider configuration is using a named profile, the command is `aws sso login --profile {{named-profile}}`.

To test if you already have an active session, run the following AWS CLI command.

```
aws sts get-caller-identity
```

The response to this command should report the IAM Identity Center account and permission set configured in the shared `config` file.

**Note**
If you already have an active AWS access portal session and run `aws sso login`, you will not be required to provide credentials.
The sign-in process might prompt you to allow the AWS CLI access to your data. On the approval screen, the client name begins with `botocore-client-`, named for `botocore`, a Python library that the AWS CLI uses.

## Additional information
<a name="idc-additional-info"></a>
+ For additional information about using IAM Identity Center and SSO in a development environment, see [Single sign-on](sso.md) in the [Advanced auth](advanced-auth.md) section. This information includes alternative and more advanced methods, as well as tutorials that show you how to use these methods.
+ For more options on authentication for the SDK, such as the use of profiles and environment variables, see the [configuration](https://docs.aws.amazon.com/sdkref/latest/guide/creds-config-files.html) chapter in the *AWS SDKs and Tools Reference Guide*.
+ To learn more about best practices, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.
+ To create short-term AWS credentials, see [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the *IAM User Guide*.
+ To learn about other credential providers, see [Standardized credential providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html) in the *AWS SDKs and Tools Reference Guide*.
