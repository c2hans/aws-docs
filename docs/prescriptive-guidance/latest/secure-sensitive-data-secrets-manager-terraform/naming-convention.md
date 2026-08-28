---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/naming-convention.html
---

# Using a hierarchical naming convention for secrets
<a name="naming-convention"></a>

When you ingest and store secrets in AWS Secrets Manager, use a defined naming convention. For example, your naming convention might be `<client name>/<dev or prod>/<project>/<version>`. Choosing a naming convention that makes sense for your organization. Use a hierarchical structure that progresses from most general information to most specific information.

This helps you manage secrets, especially when a centralized account is used for many secrets across your AWS environment. A hierarchical naming convention can help you in the following ways:
+ It helps you separates access to different secrets. For example, you can define which project or environment should have access to which secrets.
+ It helps you establish fine-grained access controls to secrets based on their names.

The following code sample shows an example naming convention that can help you manage secrets at scale.

```
resource "aws_secretsmanager_secret" "initiatesecret" {
  name                    = "org-name/dev-env/project-name"
  kms_key_id              = var.kmskeyarn
  recovery_window_in_days = var.recoverywindow
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
