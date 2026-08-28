---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-console.html
---

# Get a secret value using the AWS console
<a name="retrieving-secrets-console"></a>

**To retrieve a secret (console)**

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. In the list of secrets, choose the secret you want to retrieve.

1. In the **Secret value** section, choose **Retrieve secret value**.

   Secrets Manager displays the current version (`AWSCURRENT`) of the secret. To see [other versions](whats-in-a-secret.md#term_version) of the secret, such as `AWSPREVIOUS` or custom labeled versions, use the [Get a secret value using the AWS CLI](retrieving-secrets_cli.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
