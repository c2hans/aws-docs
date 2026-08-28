---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/working-with-stacksets.html
---

# Deploy containment and EC2 Triage roles
<a name="working-with-stacksets"></a>

AWS Security Incident Response doesn't enable containment by default. To allow the service to take containment actions on your behalf during a security incident, you must deploy AWS Identity and Access Management roles to each account in your organization where you want containment capabilities. The recommended approach is to use AWS CloudFormation StackSets with service-managed permissions, which automatically deploys the roles to all current and future accounts in your organization.

**Topics**
+ [Deploy the IAM roles with a StackSet](deploy-iam-roles-stackset.md)
+ [Select a CloudFormation template for your containment roles](cloudformation-templates.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
