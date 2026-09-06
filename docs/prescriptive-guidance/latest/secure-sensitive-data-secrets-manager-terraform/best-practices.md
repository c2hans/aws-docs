---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/best-practices.html
---

# Best practices for creating, rotating, and using secrets
<a name="best-practices"></a>

This section discusses best practices and standards that you can follow when coding application and infrastructure for deployment through Terraform. It contains the following:
+ [Generating random passwords by using AWS Secrets Manager](generate-random-passwords.md) –** **Generate a random secret of specified complexity, as per the your organization's compliance policy.
+ [Using AWS Lambda to rotate secrets](rotate-secrets.md) – AWS Lambda can be scheduled to run automatically for rotation of secrets.
+ [Limiting access to secrets](limiting-access.md) – Restrict who can access secrets and how they access them.
+ [Using a hierarchical naming convention for secrets](naming-convention.md) – Define and use a naming convention that helps you manage secrets at scale.
