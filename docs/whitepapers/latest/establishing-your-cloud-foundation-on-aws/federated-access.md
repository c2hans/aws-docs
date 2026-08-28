---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/federated-access.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Federated access
<a name="federated-access"></a>

Federation is a common approach to building access control systems which manage users centrally within a central Identity Providers (IdP) and govern their access to multiple applications and services acting as Service Providers (SP).

An identity provider enables you to manage your user identities outside of the application, service, or solution; and give these external user identities permissions to use AWS resources in your account. This is useful if your organization already has its own identity system, such as a corporate user directory or managed identity service. The process of federation allows you to centrally manage user credentials which grant access to applications. The centralization of user credentials in one data store allows you to effectively manage the lifecycle of the user and impose security requirements such as password policies, MFA requirements, and service principals. If a user leaves the company, they can simply delete the user’s corporate identity, which then also revokes access to all your federated environments.

When you use an identity provider, you don't have to create custom sign-in code or manage your own user identities. The IdP provides that for you. Your external users sign in through a well-known IdP, such as a log in with Amazon, Facebook, or Google. You can give those external identities permissions to use AWS resources in your account. Identity providers help keep your AWS account secure because you don't have to distribute or embed long-term security credentials in your application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
