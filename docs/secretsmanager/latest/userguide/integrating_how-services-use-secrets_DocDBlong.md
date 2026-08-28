---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_DocDBlong.html
---

# How Amazon DocumentDB (with MongoDB compatibility) uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_DocDBlong"></a>

Amazon DocumentDB (with MongoDB compatibility) is a fully managed document database service that supports MongoDB workloads. Amazon DocumentDB integrates with Secrets Manager to manage primary user passwords for your clusters, enhancing security and simplifying credential management.

Amazon DocumentDB generates the password, stores it in Secrets Manager, and manages the secret settings. By default, Amazon DocumentDB rotates the secret every seven days, but you can modify the rotation schedule if needed. When you create or modify an Amazon DocumentDB cluster, you can specify that it should manage the primary user password in Secrets Manager. For more information, see [Password management with Amazon DocumentDB and Secrets Manager](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-secrets-manager.html) in the *Amazon DocumentDB Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
