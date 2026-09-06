---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/credentials.html
---

# Authenticating with AWS using AWS SDK for PHP Version 3
<a name="credentials"></a>

You must establish how your code authenticates with AWS when developing with AWS services. You can configure programmatic access to AWS resources in different ways depending on the environment and the AWS access available to you.

To choose your method of authentication and configure it for the SDK, see [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide*.

## Set up authentication with IAM Identity Center for local development
<a name="use-idc-for-auth"></a>

We recommend that new users who are developing locally and are not given a method of authentication by their employer should set up AWS IAM Identity Center. This method includes installing the AWS CLI for ease of configuration and for regularly signing in to the AWS access portal. If you choose this method, your environment should contain the following elements after you complete the procedure for [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*:
+ The AWS CLI, which you use to start an AWS access portal session before you run your application.
+ A [shared AWS`config` file](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) that has a `[default]` profile with a set of configuration values that can be referenced by the SDK. To find the location of this file, see [Location of the shared files](https://docs.aws.amazon.com/sdkref/latest/guide/file-location.html) in the *AWS SDKs and Tools Reference Guide*.
+  The shared `config` file contains the [`region`](https://docs.aws.amazon.com/sdkref/latest/guide/feature-region.html) setting. This sets the default AWS Region that the SDK uses for requests. This Region is used for SDK service requests that aren't explicitly configured with a `region` property.
+  The SDK uses the profile's [SSO token provider configuration](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sso-credentials.html#feature-sso-credentials-profile) to acquire credentials before sending requests to AWS. The `sso_role_name` value, which is an IAM role connected to an IAM Identity Center permission set, allows access to the AWS services used in your application.

  The following sample `config` file shows a default profile set up with SSO token provider configuration. The profile's `sso_session` setting refers to the named [`sso-session` section](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html#section-session). The `sso-session` section contains settings to initiate an AWS access portal session.

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

The AWS SDK for PHP does not need additional packages (such as `SSO` and `SSOOIDC`) to be added to your application to use IAM Identity Center authentication.

## Start an AWS access portal session
<a name="accessportal"></a>

Before running an application that accesses AWS services, you need an active AWS access portal session for the SDK to use IAM Identity Center authentication to resolve credentials. Depending on your configured session lengths, your access will eventually expire and the SDK will encounter an authentication error. To sign in to the AWS access portal, run the following command in the AWS CLI.

```
aws sso login
```

If you followed the guidance and have a default profile setup, you do not need to call the command with a `--profile` option. If your SSO token provider configuration is using a named profile, the command is `aws sso login --profile named-profile`.

To optionally test if you already have an active session, run the following AWS CLI command.

```
aws sts get-caller-identity
```

If your session is active, the response to this command reports the IAM Identity Center account and permission set configured in the shared `config` file.

**Note**
If you already have an active AWS access portal session and run `aws sso login`, you will not be required to provide credentials.
The sign-in process might prompt you to allow the AWS CLI access to your data. Because the AWS CLI is built on top of the SDK for Python, permission messages might contain variations of the `botocore` name.

## Learn more about authentication
<a name="credother"></a>
+ For more details about using IAM Identity Center for authentication, see [Understand IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/understanding-sso.html) in the *AWS SDKs and Tools Reference Guide*
+ To learn more about best practices, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.
+ To create short-term AWS credentials, see [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the *IAM User Guide*.
+ To learn about other credential providers that AWS SDK for PHP can use, see [Standardized credential providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html) in the *AWS SDKs and Tools Reference Guide*.
