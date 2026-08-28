---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/setup-basic-onetime-setup.html
---

# Basic set up
<a name="setup-basic-onetime-setup"></a>

## Overview
<a name="setup-overview"></a>

To successfully develop applications that access AWS services using the AWS SDK for Kotlin, the following requirements must be met.
+ You must be able to [sign in to the AWS access portal](#setup-awsaccount) available in the AWS IAM Identity Center.
+ The [permissions of the IAM role](/singlesignon/latest/userguide/permissionsetsconcept.html) configured for the SDK must allow access to the AWS services that your application requires. The permissions associated with the **PowerUserAccess** AWS managed policy are sufficient for most development needs.
+ A development environment with the following elements:
  +  [Shared configuration files](/sdkref/latest/guide/file-format.html) that are set up in at least one of the following ways:
    + The `config` file contains [IAM Identity Center single sign-on settings](#setup-sso-access) so that the SDK can get AWS credentials.
    + The `credentials` file contains temporary credentials.
  + An [installation of Java 8 or later](#setup-envtools).
  + A [build automation tool](#setup-envtools) such as [Maven](https://maven.apache.org/download.cgi) or [Gradle](https://gradle.org/install/).
  + A text editor to work with code.
  + (Optional, but recommended) An IDE (integrated development environment) such as [IntelliJ IDEA](https://www.jetbrains.com/idea/download/#section=windows) or [Eclipse](https://www.eclipse.org/ide/).

    When you use an IDE, you can also integrate AWS Toolkits to more easily work with AWS services. The [AWS Toolkit for IntelliJ](/toolkit-for-jetbrains/latest/userguide/welcome.html) and [AWS Toolkit for Eclipse](/toolkit-for-eclipse/v1/user-guide/welcome.html) are two toolkits that you can use.
+ An active AWS access portal session when you are ready to run your application. You use the AWS Command Line Interface to [initiate the sign-in process](#setup-login-sso) to IAM Identity Center’s AWS access portal.

**Important**
The instructions in this setup section assume that you or organization uses IAM Identity Center. If your organization uses an external identity provider that works independently of IAM Identity Center, find out how you can get temporary credentials for the SDK for Kotlin to use. Follow these instructions to add temporary credentials to the `~/.aws/credentials` file.
If your identity provider adds temporary credentials automatically to the `~/.aws/credentials` file, make sure that the profile name is `[default]` so that you do not need to provide a profile name to the SDK or AWS CLI.

## Sign-in ability to the AWS access portal
<a name="setup-awsaccount"></a>

The AWS access portal is the web location where you manually sign in to the IAM Identity Center. The format of the URL is `d-xxxxxxxxxx.awsapps.com/start` or ` {{your_subdomain}}.awsapps.com/start`.

If you are not familiar with the AWS access portal, follow the guidance for account access in the [IAM Identity Center authentication](/sdkref/latest/guide/access-sso.html) topic in the AWS SDKs and Tools Reference Guide.

## Set up single sign-on access for the SDK
<a name="setup-sso-access"></a>

After you complete Step 2 in the [programmatic access section](/sdkref/latest/guide/access-sso.html#idcGettingStarted) in order for the SDK to use IAM Identity Center authentication, your system should contain the following elements.
+ The AWS CLI, which you use to start an [AWS access portal session](#setup-login-sso) before you run your application.
+ An `~/.aws/config` file that contains a [default profile](/sdkref/latest/guide/file-format.html#file-format-profile). The SDK for Kotlin uses the profile’s SSO token provider configuration to acquire credentials before sending requests to AWS. The `sso_role_name` value, which is an IAM role connected to an IAM Identity Center permission set, should allow access to the AWS services used in your application.

  The following sample `config` file shows a default profile set up with SSO token provider configuration. The profile’s `sso_session` setting refers to the named `sso-session` section. The `sso-session` section contains settings to initiate an AWS access portal session.

  ```
  [default]
  sso_session = my-sso
  sso_account_id = 111122223333
  sso_role_name = SampleRole
  region = us-east-1
  output = json

  [sso-session my-sso]
  sso_region = us-east-1
  sso_start_url = https://provided-domain.awsapps.com/start
  sso_registration_scopes = sso:account:access
  ```

For more details about the settings used in the SSO token provider configuration, see [SSO token provider configuration](/sdkref/latest/guide/feature-sso-credentials.html#sso-token-config) in the AWS SDKs and Tools Reference Guide.

If your development environment is not set up for programmatic access as previously shown, follow [Step 2 in the SDKs Reference Guide](/sdkref/latest/guide/access-sso.html#idcGettingStarted).

## Sign in using the AWS CLI
<a name="setup-login-sso"></a>

Before running an application that accesses AWS services, you need an active AWS access portal session in order for the SDK to use IAM Identity Center authentication to resolve credentials. Run the following command in the AWS CLI to sign in to the AWS access portal.

```
aws sso login
```

Since you have a default profile setup, you don’t need to call the command with a `--profile` option. If your SSO token provider configuration uses a named profile, the command is `aws sso login --profile named-profile`.

To test if you already have an active session, run the following AWS CLI command.

```
aws sts get-caller-identity
```

The response to this command should report the IAM Identity Center account and permission set configured in the shared `config` file.

**Note**
If you already have an active AWS access portal session and run `aws sso login`, you will not be required to provide credentials.
However, you will see a dialog that requests permission for `botocore` to access your information. `botocore` is the foundation for the AWS CLI .
Select **Allow** to authorize access to your information for the AWS CLI and SDK for Kotlin.

## Install Java and a build tool
<a name="setup-envtools"></a>

Your development environment needs the following:
+ JDK 8 or later. The AWS SDK for Kotlin works with the [Oracle Java SE Development Kit](https://www.oracle.com/java/technologies/javase-downloads.html) and with distributions of Open Java Development Kit (OpenJDK) such as [Amazon Corretto](https://aws.amazon.com/corretto/), [Red Hat OpenJDK](https://developers.redhat.com/products/openjdk), and [AdoptOpenJDK](https://adoptopenjdk.net/).
+ A build tool or IDE that supports Maven Central such as Apache Maven, Gradle, or IntelliJ.
  + For information about how to install and use Maven, see [http://maven.apache.org/](http://maven.apache.org/).
  + For information about how to install and use Gradle, see [https://gradle.org/](https://gradle.org/).
  + For information about how to install and use IntelliJ IDEA, see [https://www.jetbrains.com/idea/](https://www.jetbrains.com/idea/).

## Use temporary credentials
<a name="setup-use-temporary-creds"></a>

As an alternative to [configuring IAM Identity Center single sign-on access](#setup-sso-access) for the SDK, you can configure your development environment with temporary credentials.

### Set up a local credentials file for temporary credentials
<a name="_set_up_a_local_credentials_file_for_temporary_credentials"></a>

1.  [Create a shared credentials file](/sdkref/latest/guide/file-location.html)

1. In the credentials file, paste the following placeholder text until you paste in working temporary credentials:

   ```
   [default]
   aws_access_key_id=<value from AWS access portal>
   aws_secret_access_key=<value from AWS access portal>
   aws_session_token=<value from AWS access portal>
   ```

1. Save the file. The file `~/.aws/credentials` should now exist on your local development system. This file contains the [[default] profile](/sdkref/latest/guide/file-format.html#file-format-profile) that the SDK for Kotlin uses if a specific named profile is not specified.

1.  [Sign in to the AWS access portal](/singlesignon/latest/userguide/howtosignin.html)

1. Follow these instructions under the [Manual credential refresh](/singlesignon/latest/userguide/howtogetcredentials.html#how-to-get-temp-credentials) heading to copy IAM role credentials from the AWS access portal.

   1. For step 4 in the linked instructions, choose the IAM role name that grants access for your development needs. This role typically has a name like **PowerUserAccess** or **Developer**.

   1. For step 7, select the **Manually add a profile to your AWS credentials file** option and copy the contents.

1. Paste the copied credentials into your local `credentials` file and remove the generated profile name. Your file should resemble the following:

   ```
   [default]
   aws_access_key_id=AKIAIOSFODNN7EXAMPLE
   aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
   aws_session_token=IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZVERYLONGSTRINGEXAMPLE
   ```

1. Save the `credentials` file

The SDK for Kotlin will access these temporary credentials when it create a service client and use them for each request. The settings for the IAM role chosen in step 5a determine [how long the temporary credentials are valid](/singlesignon/latest/userguide/howtosessionduration.html). The maximum duration is twelve hours.

After the temporary credentials expire, repeat steps 4 through 7.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
