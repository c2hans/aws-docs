---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/access-login.html
---

# Using console credentials to authenticate AWS SDKs and tools
<a name="access-login"></a>

Using console credentials is the recommended method of providing AWS credentials when developing an AWS application in your local environment or other non-AWS compute service environments. If you are developing on an AWS resource, such as Amazon Elastic Compute Cloud (Amazon EC2) or AWS CloudShell, we recommend getting credentials from that service instead.

You can also authenticate through IAM Identity Center [Using IAM Identity Center to authenticate AWS SDK and tools](access-sso.md). This option is a common way for organizations to manage access for their workforce and requires Identity Center to be enabled.

## How does it work?
<a name="access-login-how"></a>

[Login for AWS local development using console credentials ](https://docs.aws.amazon.com/signin/latest/userguide/command-line-sign-in.html) lets you use your existing AWS Management Console sign-in credentials for programmatic access to AWS services. After a browser-based authentication flow, AWS generates temporary credentials that work across local development tools like the AWS CLI, Tools for PowerShell and AWS SDKs. This feature simplifies the process of configuring and managing AWS CLI credentials, especially if you prefer interactive authentication over managing long-term access keys.

With this process, you can authenticate using your root credentials created during initial account setup, IAM users, or a federated identity from your identity provider.

If you use SDKs for development, the SDK clients will use the temporary credentials through the [AWS SDKs and Tools standardized credential providers](standardized-credentials.md). You can also configure the [Login credentials provider](feature-login-credentials.md).

Authenticating via the login command is supported by both AWS CLI and Tools for PowerShell:
+ [Login for AWS local development using console credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html)
+ [Login using console credentials](https://docs.aws.amazon.com/powershell/v5/userguide/creds-idc.html#login-con-creds) in the AWS Tools for PowerShell user guide
