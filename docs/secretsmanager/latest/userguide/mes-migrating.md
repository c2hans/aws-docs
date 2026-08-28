---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-migrating.html
---

# Migrating existing secrets
<a name="mes-migrating"></a>

You have an option to migrate your existing partner secrets to managed external secrets. This can be done with an [UpdateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UpdateSecret.html) call. You must update the secret value and metadata as mentioned in the guide. If you already have custom rotation logic set up for these secrets, you must first cancel the rotation using a [CancelRotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CancelRotateSecret.html) call.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
