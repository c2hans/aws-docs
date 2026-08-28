---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_migration-hub.html
---

# How AWS Migration Hub uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_migration-hub"></a>

AWS Migration Hub provides a single location to track migration tasks across multiple AWS tools and partner solutions.

AWS Migration Hub Orchestrator simplifies and automates the migration of servers and enterprise applications to AWS. Migration Hub Orchestrator uses a secret for the connection information to your source server. For more information, in the *AWS Migration Hub Orchestrator User Guide*, see:
+ [Migrate SAP NetWeaver applications to AWS](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/migrate-sap.html)
+ [Rehost applications on Amazon EC2](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/rehost-on-ec2.html)

Migration Hub Strategy Recommendations offers migration and modernization strategy recommendations for viable transformation paths for your applications. Strategy Recommendations can analyze SQL Server databases, using a secret for the connection information. For more information, see [Strategy Recommendations database analysis](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/database-analysis.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
