---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/access-users.html
---

# Using AWS access keys to authenticate AWS SDKs and tools
<a name="access-users"></a>

Using AWS access keys is an option for authentication when using AWS SDKs and tools.

## Use short-term credentials
<a name="credentials-temporary"></a>

 We recommend configuring your SDK or tool to use [Using IAM Identity Center to authenticate AWS SDK and tools](access-sso.md) to use extended session duration options.

However, to set up the SDK or tool's temporary credentials directly, see [Using short-term credentials to authenticate AWS SDKs and tools](access-temp-idc.md).

## Use long-term credentials
<a name="credentials-long-term"></a>

**Warning**
To avoid security risks, don't use IAM users for authentication when developing purpose-built software or working with real data. Instead, use federation with an identity provider such as [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

### Manage access across AWS accounts
<a name="manage-access-accounts"></a>

As a security best practice, we recommend using AWS Organizations with IAM Identity Center to manage access across all your AWS accounts. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

You can create users in IAM Identity Center, use Microsoft Active Directory, use a SAML 2.0 identity provider (IdP), or individually federate your IdP to AWS accounts. Using one of these approaches, you can provide a single sign-on experience for your users. You can also enforce multi-factor authentication (MFA) and use temporary credentials for AWS account access. This differs from an IAM user, which is a long-term credential that can be shared and which might increase the security risk to your AWS resources.

### Create IAM users for sandbox environments only
<a name="create-iam-user-sandbox"></a>

If you're new to AWS, you might create a test IAM user and then use it to run tutorials and explore what AWS has to offer. It's okay to use this type of credential when you're learning, but we recommend that you avoid using it outside of a sandbox environment.

For the following use cases, it might make sense to get started with IAM users in AWS:
+ Getting started with your AWS SDK or tool and exploring AWS services in a sandbox environment.
+ Running scheduled scripts, jobs, and other automated processes that don't support a human-attended sign-in process as part of your learning.

If you're using IAM users outside of these use cases, then transition to IAM Identity Center or federate your identity provider to AWS accounts as soon as possible. For more information, see [Identity federation in AWS](https://aws.amazon.com/identity/federation/).

### Secure IAM user access keys
<a name="secure-iam-access-keys"></a>

You should rotate IAM user access keys regularly. Follow the guidance in [ Rotating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey) in the *IAM User Guide*. If you believe that you have accidentally shared your IAM user access keys, then rotate your access keys.

IAM user access keys should be stored in the shared AWS `credentials` file on the local machine. Don't store the IAM user access keys in your code. Don't include configuration files that contain your IAM user access keys inside of any source code management software. External tools, such as the open source project [git-secrets](https://github.com/awslabs/git-secrets), can help you from inadvertently committing sensitive information to a Git repository. For more information, see [IAM Identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the *IAM User Guide*.

To set up an IAM user to get started, see [Using long-term credentials to authenticate AWS SDKs and tools](access-iam-users.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdkref` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
