---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating-amazonq.html
---

# How Amazon Q uses Secrets Manager
<a name="integrating-amazonq"></a>

To authenticate Amazon Q to access your data source, you provide your data source access credentials to Amazon Q using an Secrets Manager secret. If you use the console, you can choose to create a new secret or use an existing one. For more information, see [Concepts – Authentication](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connector-concepts.html#connector-authentication) in the *Amazon Q Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
