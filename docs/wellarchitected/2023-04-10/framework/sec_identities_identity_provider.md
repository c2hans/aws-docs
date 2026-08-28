---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sec_identities_identity_provider.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC02-BP04 Rely on a centralized identity provider
<a name="sec_identities_identity_provider"></a>

 For workforce identities, rely on an identity provider that allows you to manage identities in a centralized place. This makes it easier to manage access across multiple applications and services, because you are creating, managing, and revoking access from a single location. For example, if someone leaves your organization, you can revoke access for all applications and services (including AWS) from one location. This reduces the need for multiple credentials and provides an opportunity to integrate with existing human resources (HR) processes.

For federation with individual AWS accounts, you can use centralized identities for AWS with a SAML 2.0-based provider with AWS Identity and Access Management. You can use any provider— whether hosted by you in AWS, external to AWS, or supplied by the AWS Partner—that is compatible with the [SAML 2.0](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html) protocol. You can use federation between your AWS account and your chosen provider to grant a user or application access to call AWS API operations by using a SAML assertion to get temporary security credentials. Web-based single sign-on is also supported, allowing users to sign in to the AWS Management Console from your sign in website.

For federation to multiple accounts in your AWS Organizations, you can configure your identity source in [AWS IAM Identity Center (IAM Identity Center)](http://aws.amazon.com/single-sign-on/), and specify where your users and groups are stored. Once configured, your identity provider is your source of truth, and information can be [synchronized](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-automatically.html) using the System for Cross-domain Identity Management (SCIM) v2.0 protocol. You can then look up users or groups and grant them IAM Identity Center access to AWS accounts, cloud applications, or both.

IAM Identity Center integrates with AWS Organizations, which allows you to configure your identity provider once and then [grant access to existing and new accounts](https://docs.aws.amazon.com/singlesignon/latest/userguide/useraccess.html) managed in your organization. IAM Identity Center provides you with a default store, which you can use to manage your users and groups. If you choose to use the IAM Identity Center store, create your users and groups and assign their level of access to your AWS accounts and applications, keeping in mind the best practice of least privilege. Alternatively, you can choose to [Connect to Your External Identity Provider ](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-idp.html)using SAML 2.0, or [Connect to Your Microsoft AD Directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-ad.html) using AWS Directory Service. Once configured, you can sign into the AWS Management Console, or the AWS mobile app, by authenticating through your central identity provider.

For managing end-users or consumers of your workloads, such as a mobile app, you can use [Amazon Cognito](http://aws.amazon.com/cognito/). It provides authentication, authorization, and user management for your web and mobile apps. Your users can sign in directly with sign-in credentials, or through a third party, such as Amazon, Apple, Facebook, or Google.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Centralize administrative access: Create an Identity and Access Management (IAM) identity provider entity to establish a trusted relationship between your AWS account and your identity provider (IdP). IAM supports IdPs that are compatible with OpenID Connect (OIDC) or SAML 2.0 (Security Assertion Markup Language 2.0).
  +  [Identity Providers and Federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html)
+  Centralize application access: Consider Amazon Cognito for centralizing application access. It lets you add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily. [Amazon Cognito](https://aws.amazon.com/cognito/) scales to millions of users and supports sign-in with social identity providers, such as Facebook, Google, and Amazon, and enterprise identity providers via SAML 2.0.
+  Remove old users and groups: After you start using an identity provider (IdP), remove users and groups that are no longer required.
  +  [Finding unused credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html)
  +  [Deleting an IAM group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_delete.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
+  [Security Partner Solutions: Access and Access Control](https://aws.amazon.com/security/partner-solutions/#access-control)
+  [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)
+  [The AWS Account Root User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html)

 **Related videos:**
+  [Best Practices for Managing, Retrieving, and Rotating Secrets at Scale](https://youtu.be/qoxxRlwJKZ4)
+  [Managing user permissions at scale with AWS IAM Identity Center](https://youtu.be/aEIqeFCcK7E)
+  [Mastering identity at every layer of the cake](https://www.youtube.com/watch?v=vbjFjMNVEpc)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
