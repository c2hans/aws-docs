---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/mho.html
---

# AWS Migration Hub Orchestrator
<a name="mho"></a>

**Note**
AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform/).

[AWS Migration Hub Orchestrator](https://console.aws.amazon.com/migrationhub/orchestrator/) helps you orchestrate and automate the migration of SQL Server databases to Amazon EC2 or Amazon RDS. This feature of AWS Migration Hub helps you get started quickly by using predefined workflow templates that are built based on best practices. Migration Hub Orchestrator automates error-prone manual tasks involved in the migration process, such as checking environment readiness and connections. You can also use Migration Hub Orchestrator to orchestrate and accelerate migrations for .NET applications, SAP workloads, and virtual machine images, in addition to your SQL Server databases. You can access this tool through the [Migration Hub Orchestrator console](https://console.aws.amazon.com/migrationhub/orchestrator/). For SQL Server migration, Migration Hub Orchestrator supports three use cases:
+ Rehost SQL Server on Amazon EC2. You can choose specific SQL servers and rehost them on Amazon EC2 by using automated native backup and restore in Migration Hub Orchestrator. To learn more, see [Rehost SQL server on Amazon EC2](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/rehost-sql-ec2.html) in the Migration Hub Orchestrator documentation.
+ Replatform SQL Server on Amazon RDS. You can choose specific SQL Server databases and replatform them on Amazon RDS by using automated native backup and restore in Migration Hub Orchestrator. To learn more, see [Replatform SQL server on Amazon RDS](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/replatform-sql-rds.html) in the Migration Hub Orchestrator documentation.
+ Rehost Windows and SQL Server applications on Amazon EC2. You can lift and shift your Windows servers running .NET and SQL Server to Amazon EC2 by using the *Rehost applications on Amazon EC2 template*. To learn more, see [Rehost applications on Amazon EC2](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/rehost-on-ec2.html) in the Migration Hub Orchestrator documentation.

Migration Hub Orchestrator helps avoid schedule and budget overruns in your SQL Server migrations. Other key benefits include:
+ Migrate applications by using a prescriptive methodology. You can get started quickly with the predefined workflow templates, which are based on proven migration best practices. You can also customize your migration workflow by adding, reordering, and removing steps based on your needs. For example, you can add a step for cutover approval.
+ Automate manual steps. Migration Hub Orchestrator automates manual tasks such as installing agents, importing on-premises images, provisioning your target environment on AWS, and verifying source and target environments. Automation saves you time and costs while reducing errors.
+ Orchestrate migration workflow. Migration Hub Orchestrator orchestrates the tools used in migration steps by reusing the inventory metadata, configuration specification, and environment context to minimize the number of inputs that these tools require.

For additional information, see the following resources:
+ [Migration Hub Orchestrator console](https://console.aws.amazon.com/migrationhub/orchestrator/)
+ [Rehost applications on Amazon EC2](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/rehost-on-ec2.html) (Migration Hub Orchestrator documentation)
+ [Replatform SQL server on Amazon RDS](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/replatform-sql-rds.html) (Migration Hub Orchestrator documentation)
+ [Migration workflows](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/migration-workflows.html) (Migration Hub Orchestrator documentation)
+ [Using Migration Hub Orchestrator to simplify and accelerate Microsoft SQL Server migrations](https://aws.amazon.com/blogs/modernizing-with-aws/aws-migration-hub-orchestrator-sql-server-migrations-to-aws/) (AWS blog post)
+ [Simplify migrating your Windows Server images with AWS Migration Hub Orchestrator](https://aws.amazon.com/blogs/modernizing-with-aws/simplify-migrating-your-windows-server-images-with-aws-migration-hub-orchestrator/) (AWS blog post)
