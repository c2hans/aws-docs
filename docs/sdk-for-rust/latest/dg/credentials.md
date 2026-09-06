---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/credentials.html
---

# Authenticating with AWS using AWS SDK for Rust
<a name="credentials"></a>

You must establish how your code authenticates with AWS when developing with AWS services. You can configure programmatic access to AWS resources in different ways depending on the environment and the AWS access available to you.

To choose your method of authentication and configure it for the SDK, see [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide*.

We recommend that new users who are developing locally and are not given a method of authentication by their employer should set up AWS IAM Identity Center. This method includes installing the AWS CLI for ease of configuration and for regularly signing in to the AWS access portal.

 If you choose this method, complete the procedure for [Login for AWS local development using console credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-login.html) in the *AWS SDKs and Tools Reference Guide*. Afterwards, your environment should contain the following elements:
+ The AWS CLI, which you use to start an AWS access portal session before you run your application.
+ A [shared AWS`config` file](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) having a `[default]` profile with a set of configuration values that can be referenced from the SDK. To find the location of this file, see [Location of the shared files](https://docs.aws.amazon.com/sdkref/latest/guide/file-location.html) in the *AWS SDKs and Tools Reference Guide*.
+  The shared `config` file sets the [`region`](https://docs.aws.amazon.com/sdkref/latest/guide/feature-region.html) setting. This sets the default AWS Region that the SDK uses for AWS requests. This Region is used for SDK service requests that aren't specified with a Region to use.
+  The SDK uses the profile’s [Login credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-login-credentials.html) configuration to acquire credentials before sending requests to AWS. The `login_session` value, which stores the identity of the management console session that you selected during the login workflow, allows access to the AWS services used in your application.

  The following sample `config` file shows a default profile set up with Login credentials provider configuration console session selected during the login workflow. The profile's `login_session` setting refers to the named console session selected during the workflow:

  ```
  [default]
  login_session = arn:aws:iam::{{0123456789012}}:user/{{username}}
  region = us-east-1
  ```
**Note**
You must enable the `credentials-login` feature of the `aws-config` crate to make use of this credential provider.

## More authentication information
<a name="credother"></a>

Human users, also known as *human identities*, are the people, administrators, developers, operators, and consumers of your applications. They must have an identity to access your AWS environments and applications. Human users that are members of your organization - that means you, the developer - are known as *workforce identities*.

Use temporary credentials when accessing AWS. You can use an identity provider for your human users to provide federated access to AWS accounts by assuming roles, which provide temporary credentials. For centralized access management, we recommend that you use AWS IAM Identity Center (IAM Identity Center) to manage access to your accounts and permissions within those accounts. For more alternatives, see the following:
+ To learn more about best practices, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.
+ To create short-term AWS credentials, see [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the *IAM User Guide*.
+ To learn about other credential providers supported by SDK for Rust, see [Standardized credential providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html) in the *AWS SDKs and Tools Reference Guide*.
