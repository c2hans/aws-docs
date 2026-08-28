---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/tools-steps.html
---

# Migration tools and high-level migration steps
<a name="tools-steps"></a>

After you deploy MongoDB Atlas on AWS, you can use the following tools to migrate data from the source (a public cloud, your data center, or a third-party DBaaS provider) to MongoDB Atlas on AWS, with minimal impact on your applications. There are three basic steps for the simplified data migration process:

1. Deploy your new cluster.

1. Live migrate the data.

1. Cut over in seconds when ready.

You can use the following migration tools for the second step:
+ [Atlas Live Migration Service](live-migration.md)
+ [MongoDB Relational Migrator](relational-migrator.md)

## Choosing the right tool for your migration
<a name="choosing-the-right-tool-for-your-migration.a3f45458-1d0b-554f-9ecb-79e54b160ab6"></a>

If you are already running MongoDB instances in your source environment, we recommend that you use the Altas Live Migration Service, with minimal impact to your applications. If you want to migrate a relational database workload to MongoDB, use the MongoDB Relational Migrator.

For common migration scenarios, see the following AWS Prescriptive Guidance patterns:
+ [Migrate a self-hosted MongoDB environment to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud.html)
+ [Migrate a relational database to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-relational-database-to-mongodb-atlas.html)
+ [Stream data from IBM Db2, SAP, Sybase, and other databases to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/stream-data-from-ibm-db2-to-mongodb-atlas.html)

For additional migration scenarios, see the MongoDB website:
+ [Live Migrate (Pull) a Replica Set into Atlas (MongoDB Before 6.0.13)](https://docs.atlas.mongodb.com/import/live-import/?from=migration-site)
+ [Migrating from a self-managed replica set on AWS to MongoDB Atlas](https://docs.mongodb.com/guides/cloud/migrate-from-aws-to-atlas/)
+ [Atlas Live Migration service and documentation](https://www.mongodb.com/cloud/atlas/migrate)
+ [RDBMS to MongoDB Migration Guide](https://www.mongodb.com/resources/solutions/use-cases/rdbms-mongodb-migration-guide)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
