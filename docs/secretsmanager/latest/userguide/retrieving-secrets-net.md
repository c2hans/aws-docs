---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-net.html
---

# Get a Secrets Manager secret value using .NET
<a name="retrieving-secrets-net"></a>

In applications, you can retrieve your secrets by calling `GetSecretValue` or `BatchGetSecretValue`in any of the AWS SDKs. However, we recommend that you cache your secret values by using client-side caching. Caching secrets improves speed and reduces your costs.

**Topics**
+ [Get a Secrets Manager secret value using .NET with client-side caching](retrieving-secrets_cache-net.md)
+ [Get a Secrets Manager secret value using the SDK for .NET](retrieving-secrets-net-sdk.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
