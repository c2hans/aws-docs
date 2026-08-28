---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.SecretsManager.html
---

# Supported Regions and Aurora DB engines for Secrets Manager integration
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.SecretsManager"></a>

With AWS Secrets Manager, you can replace hard-coded credentials in your code, including database passwords, with an API call to Secrets Manager to retrieve the secret programmatically. For more information about Secrets Manager, see [AWS Secrets Manager User Guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/).

You can specify that Amazon Aurora manages the master user password in Secrets Manager for an Aurora DB cluster. Aurora generates the password, stores it in Secrets Manager, and rotates it regularly. For more information, see [Password management with Amazon Aurora and AWS Secrets Manager](rds-secrets-manager.md).

Secrets Manager integration is available in all AWS Regions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
