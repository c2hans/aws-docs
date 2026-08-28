---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-using-customermanagedapps-setup.html
---

# Setting up your own OAuth 2.0 application
<a name="trustedidentitypropagation-using-customermanagedapps-setup"></a>

Trusted identity propagation enables a customer managed application to request access to data in AWS services on behalf of a user. Data access management is based on a user’s identity, so administrators can grant access based on users' existing user and group memberships. The user's identity, actions performed on their behalf, and other events are recorded in service-specific logs and CloudTrail events.

With trusted identity propagation, a user can sign in to a customer managed application, and that application can pass the user's identity in requests to access data in AWS services.

**Important**
To access an AWS service, customer managed applications must obtain a token from a trusted token issuer, which is external to IAM Identity Center. A *trusted token issuer* is an OAuth 2.0 authorization server that creates signed tokens. These tokens authorize applications that initiate requests for access to AWS services (receiving applications). For more information, see [Using applications with a trusted token issuer](using-apps-with-trusted-token-issuer.md).

**Topics**
+ [Set up customer managed OAuth 2.0 applications for trusted identity propagation](customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2.md)
+ [Specify trusted applications](trustedidentitypropagation-using-customermanagedapps-specify-trusted-apps.md)
+ [Using applications with a trusted token issuer](using-apps-with-trusted-token-issuer.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
