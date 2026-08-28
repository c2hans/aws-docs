---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/understanding-identity-source.html
---

# Understanding your identity source
<a name="understanding-identity-source"></a>

IAM Identity Center uses an identity source to define where users are managed. There are two types of identity sources:

IAM Identity Center directory
This option is the default identity source. Users are created and managed directly within IAM Identity Center. You can create users through the Deadline Cloud console or the IAM Identity Center console. Users receive email invitations to join your organization, and passwords are managed within IAM Identity Center.

External identity provider (IdP)
Users are federated from an external system such as Okta, Microsoft Entra ID, or other SAML 2.0 identity providers. Users must be created in the external system first. The Deadline Cloud console cannot create users when an external IdP is configured, but you can assign permissions to existing users. Passwords are managed by the external IdP.

To check your identity source configuration or change it, see [Manage your identity source](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source.html) in the IAM Identity Center User Guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
