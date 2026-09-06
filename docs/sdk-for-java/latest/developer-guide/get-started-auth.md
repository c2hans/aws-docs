---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started-auth.html
---

# Authenticating with AWS using the AWS SDK for Java 2.x
<a name="get-started-auth"></a>

 You must establish how the AWS SDK for Java 2.x authenticates with AWS when you develop with AWS services. The SDK manages credential discovery, signature creation, and credential refreshing completely behind the scenes, letting you focus on your application logic.

## Set up for authentication
<a name="setup-auth"></a>

The [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) topic in the AWS SDKs and Tools Reference Guide describes the different authentication approaches.

For local development the recommended approach is to use short-term credentials by logging into the AWS CLI with your console login credentials. Recommended if you use root, IAM users, or federation with IAM for AWS account access. Follow the instructions at [Access credentials for interactive development work using AWS SDK for Java 2.x](credentials-temporary.md).

After following the instructions in AWS SDKs and Tools Reference Guide, your system should be set up to allow the SDK to sign requests:

### 1. Local development using short-term credentials
<a name="setup-login"></a>

For local development the recommended approach is to use short-term credentials by logging into the AWS CLI with your console login credentials. Recommended if you use root, IAM users, or federation with IAM for AWS account access.

For instructions, see [Using credentials providers in the AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-temporary.html).

### 2. Setup for single sign-on access for the SDK
<a name="setup-credentials"></a>

After you complete Step 2 in the [programmatic access section](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html#idcGettingStarted) so that the SDK can use IAM Identity Center authentication, your system should contain the following elements.
+ The AWS CLI, which you use to start an [AWS access portal session](#setup-login-sso) before you run your application.
+ An `~/.aws/config` file that contains a [default profile](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html#file-format-profile). The SDK for Java uses the profile's SSO token provider configuration to acquire credentials before sending requests to AWS. The `sso_role_name` value, which is an IAM role connected to an IAM Identity Center permission set, should allow access to the AWS services used in your application.

  The following sample `config` file shows a default profile set up with SSO token provider configuration. The profile's `sso_session` setting refers to the named `sso-session` section. The `sso-session` section contains settings to initiate an AWS access portal session.

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

For more details about the settings used in the SSO token provider configuration, see [SSO token provider configuration](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sso-credentials.html#sso-token-config) in the AWS SDKs and Tools Reference Guide.

If your development environment is not set up for programmatic access as previously shown, follow [Step 2 in the SDKs Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html#idcGettingStarted).

### 3. Sign in using the AWS CLI
<a name="setup-login-sso"></a>

Before running an application that accesses AWS services, you need an active AWS access portal session in order for the SDK to use IAM Identity Center authentication to resolve credentials. Run the following command in the AWS CLI to sign in to the AWS access portal.

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
However, you will see a dialog that requests permission for `botocore` to access your information. `botocore` is the foundation for the AWS CLI .
Select **Allow** to authorize access to your information for the AWS CLI and SDK for Java.

## Additional authentication options
<a name="setup-additional"></a>

For more options on authentication for the SDK, such as the use of profiles and environment variables, see the [configuration](https://docs.aws.amazon.com/sdkref/latest/guide/creds-config-files.html) chapter in the AWS SDKs and Tools Reference Guide.
