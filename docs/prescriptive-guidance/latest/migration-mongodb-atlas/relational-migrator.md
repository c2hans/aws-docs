---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/relational-migrator.html
---

# MongoDB Relational Migrator

[MongoDB Relational Migrator](https://www.mongodb.com/products/tools/relational-migrator) is a tool to help you migrate relational database workloads to MongoDB Atlas. Relational Migrator allows you to:
+ Design an effective MongoDB schema that is derived from an existing relational schema.
+ Migrate data from Oracle, SQL Server, MySQL, PostgreSQL, or Sybase ASE to MongoDB, while transforming your current schema to the target schema.
+ Generate code artifacts to reduce the time required to update application code.

The Relational Migrator assists in the following migration activities:
+ **Schema mapping and modeling**. You can [view your schema](https://www.mongodb.com/docs/relational-migrator/diagrams/diagrams/#std-label-rm-diagrams) by using entity-relationship style diagrams and edit mapping rules to shape the target schema. You can split or merge tables across collections, or use [embedded array](https://www.mongodb.com/docs/relational-migrator/mapping-rules/mapping-rule-options/embedded-array/#std-label-rm-embedded-array) and [embedded document](https://www.mongodb.com/docs/relational-migrator/mapping-rules/mapping-rule-options/embedded-documents/#std-label-rm-embedded-documents) mapping rules to embed tables. You can use [calculated fields](https://www.mongodb.com/docs/relational-migrator/mapping-rules/fields/calculated-fields/calculated-fields/#std-label-rm-calculated-fields) (JavaScript expressions) to transform columns from your source relational database into custom MongoDB fields.
+ **Schema recommendations**. You can use [mapping rules suggested by Relational Migrator](https://www.mongodb.com/docs/relational-migrator/mapping-rules/new-rules-suggested-mappings/#std-label-rm-new-rules-from-mappings) to speed up schema mapping, and apply the mapping to your collections.
+ **Synchronized data**. You can replicate data from Oracle, MySQL, SQL Server, PostgreSQL, or Sybase ASE to MongoDB Atlas. During one-time or continuous replication, you can automatically transform data by using [rules to map the columns in your relational database to MongoDB fields](https://www.mongodb.com/docs/relational-migrator/mapping-rules/mapping-rules/#std-label-rm-mapping-rules).
+ **Converting application code**. MongoDB supports C\#, Java, JavaScript, JSON, and [multiple template frameworks.](https://www.mongodb.com/docs/relational-migrator/code-generation/generate-app-code/#std-label-rm-code-generation-templates) You can use the code generation feature to create code for entity classes, persistence layers, and APIs, to accelerate your development tasks.

For more information about this migration option, see [Migrate a relational database to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-relational-database-to-mongodb-atlas.html).
