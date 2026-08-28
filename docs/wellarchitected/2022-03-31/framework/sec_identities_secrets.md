---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_identities_secrets.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC02-BP03 Store and use secrets securely
<a name="sec_identities_secrets"></a>

 For workforce and machine identities that require secrets such as passwords to third-party applications, store them with automatic rotation using the latest industry standards in a specialized service, such as for credentials that are not IAM-related and cannot take advantage of temporary credentials, such as database logins, use a service that is designed to handle management of secrets, such as AWS Secrets Manager. Secrets Manager makes it easy to manage, rotate, and securely store encrypted secrets using supported services. Calls to access the secrets are logged in AWS CloudTrail for auditing purposes, and IAM permissions can grant least-privilege access to them.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Use AWS Secrets Manager: [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) is an AWS service that makes it easier for you to manage secrets. Secrets can be database credentials, passwords, third-party API keys, and even arbitrary text.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Getting Started with AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html)
+  [Identity Providers and Federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html)

 **Related videos:**
+  [Best Practices for Managing, Retrieving, and Rotating Secrets at Scale](https://youtu.be/qoxxRlwJKZ4)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
