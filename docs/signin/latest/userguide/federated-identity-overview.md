---
source_url: https://docs.aws.amazon.com/signin/latest/userguide/federated-identity-overview.html
---

# Sign in as a federated identity
<a name="federated-identity-overview"></a>

A federated identity is a user that can access secure AWS account resources with external identities. External identities can come from a corporate identity store (such as LDAP or Windows Active Directory) or from a third party (such as Login in with Amazon, Facebook, or Google). Federated identities don't sign in with the AWS Management Console or AWS access portal. The type of external identity in use determines how federated identities sign in.

This sign-in method is only supported for accounts created with Sign up for AWS (advanced). For more information, see [Compare sign-up options](https://docs.aws.amazon.com/accounts/latest/reference/sign-up-for-aws.html) in the *AWS Account Management Reference Guide*.

Administrators must create a custom URL that includes `https://signin.aws.amazon.com/federation`. For more information, see [ Enabling custom identity broker access to the AWS Management Console](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html).

**Note**
Your administrator creates federated identities. Contact your administrator for more details on how to sign in as a federated identity.

For more information about federated identities, see [About web identity federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Sign-In. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
