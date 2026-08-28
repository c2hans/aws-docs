---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-13.html
---

# ACCT.13 Use short-lived credentials for access to your AWS resources
<a name="acct-13"></a>

Determine how your developers access AWS services and resources through the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/). To reduce security risk, avoid using IAM users with long-lived access keys for authentication when developing software or working with production data. Short-lived credentials expire automatically, which reduces the risk of credential exposure.

**Choose the approach that matches your current AWS access pattern**
+ [Sign in with console credentials (Recommended)](https://docs.aws.amazon.com/signin/latest/userguide/command-line-sign-in.html#command-line-sign-in-local-development) – If you use root, IAM users, or federation with IAM for AWS account access, use `aws login` to obtain temporary credentials for AWS CLI or AWS SDK access.
+ [Sign in with IAM Identity Center credentials](https://docs.aws.amazon.com/signin/latest/userguide/command-line-sign-in.html#command-line-sign-in-sso) – If you use IAM Identity Center for AWS account access, this approach provides centralized identity management and automatic credential rotation.
+ **Federated access through your corporate identity provider** – Use your organization's existing identity provider, such as Okta, Active Directory, or Ping Identity, with MFA enforcement.

**To obtain temporary AWS CLI credentials using the **`aws`** login**

1. Install or update the AWS CLI. For more information, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the AWS CLI documentation.

1. Enter `aws login` and follow the authentication prompts.

1. Authenticate using your IAM user credentials and MFA.

After you authenticate, the AWS CLI manages temporary credentials for your session. When your session expires, enter `aws login` again to re-authenticate. For information about session duration settings, see [IAM role session duration](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html) in the IAM documentation.

For AWS Partner integrations and third-party solutions, use short-lived credentials where possible. [IAM temporary delegation for AWS Partners](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-temporary-delegation-partner-guide.html) allows you integrate AWS Partner products by using short-lived credentials instead of long-lived access keys. [IAM Outbound Identity Federation](https://aws.amazon.com/blogs/aws/simplify-access-to-external-services-using-aws-iam-outbound-identity-federation/) allows AWS workloads to authenticate to external solutions by using short-lived tokens instead of long-lived API keys.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
