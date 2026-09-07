---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-relational-database-to-mongodb-atlas.html
---

# Migrate a relational database to MongoDB Atlas on AWS
<a name="migrate-relational-database-to-mongodb-atlas"></a>

*Battulga Purevragchaa and Igor Alekseev, Amazon Web Services*

*Babu Srinivasan, MongoDB*

## Summary
<a name="migrate-relational-database-to-mongodb-atlas-summary"></a>

This pattern describes the steps for migrating from a relational database such as SQL Server, MySQL, or PostgreSQL to MongoDB Atlas in the AWS Cloud. It uses [MongoDB Relational Migrator](https://www.mongodb.com/products/relational-migrator) to help accelerate the data migration from relational databases to MongoDB Atlas.

The pattern accompanies the guide [Migrating to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/) on the AWS Prescriptive Guidance website. It provides the implementation steps for one of the migration scenarios that are discussed in that guide. For additional migration scenarios, see the following patterns on the AWS Prescriptive Guidance website:
+ [Migrate a self-hosted MongoDB environment to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud.html)
+ [Stream data from IBM Db2, SAP, Sybase, and other databases to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/stream-data-from-ibm-db2-to-mongodb-atlas.html)

The pattern is intended for [AWS System Integrator (SI) Partners](https://aws.amazon.com/managed-services/partners/) and AWS users.

## Prerequisites and limitations
<a name="migrate-relational-database-to-mongodb-atlas-prereqs"></a>

**Prerequisites**
+ A source relational database (Oracle Database, SQL Server, PostgreSQL, MySQL, SAP/Sybase ASE, and others) to migrate to MongoDB Atlas.
+ Familiarity with relational databases, MongoDB Atlas, and AWS services. This pattern explains some of the migration steps at a high level. Additional details will be added in future versions.

**Product versions**
+ MongoDB version 5.0 or later

## Architecture
<a name="migrate-relational-database-to-mongodb-atlas-architecture"></a>

The following diagram shows the migration from a relational database management system (RDBMS) database to MongoDB Atlas on AWS.

![Architecture for migrating from RDBMS to MongoDB Atlas on AWS.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4e3ea0f1-21e8-4641-a9ee-732355f20baf/images/8eacf3ec-f480-4912-9002-6a50800fe9bf.png)

For MongoDB Atlas reference architectures that support different usage scenarios, see[ Migrating to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/architecture.html) on the AWS Prescriptive Guidance website.

## Tools
<a name="migrate-relational-database-to-mongodb-atlas-tools"></a>
+ [MongoDB Atlas](https://www.mongodb.com/atlas) is a fully managed database as a service (DBaaS) for deploying and managing MongoDB databases in the cloud.
+ [MongoDB Relational Migrator](https://www.mongodb.com/products/relational-migrator) provides a smooth transition of data from traditional relational databases to MongoDB. It helps automate the conversion process and transforms the structured data model of relational databases into the flexible document format provided by MongoDB. The Relational Migrator preserves data integrity and relationships to simplify the migration. Organizations can take advantage of the scalability, performance, and versatility benefits that MongoDB provides while retaining the familiarity of their existing data.

## Best practices
<a name="migrate-relational-database-to-mongodb-atlas-best-practices"></a>

For best practices for using MongoDB on AWS, see the posts on the [AWS Partner Network Blog](https://aws.amazon.com/blogs/apn/tag/mongodb-atlas/).

## Epics
<a name="migrate-relational-database-to-mongodb-atlas-epics"></a>

### Discovery and assessment
<a name="discovery-and-assessment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Determine the parameters and size of the relational database. | Estimate the working set size by using the Relational Migrator recommendations and information from `db.stats()` for the total index space. Assume that a percentage of your data space will be accessed frequently. This task should take approximately one week. For more information and examples for this and the other stories in this epic, see the [Related resources](#migrate-relational-database-to-mongodb-atlas-resources) section. | App owner, DBA |
| Estimate network bandwidth requirements. | To estimate your network bandwidth requirements, multiply the average document size by the number of documents served per second. Consider the maximum traffic that any node on your cluster will bear as the basis. To calculate downstream data transfer rates from your cluster to client applications, use the sum of the total documents returned over a period of time. If your applications read from secondary nodes, divide this number of total documents by the number of nodes that can serve read operations. To find the average document size for a database, use the `db.stats().avgObjSize` command. This task will typically take one day. | DBA |
| Select the Atlas tier. | Follow the instructions in the [MongoDB documentation](https://www.mongodb.com/docs/atlas/sizing-tier-selection/) to select the correct Atlas cluster tier. | DBA |
| Plan for cutover. | Plan for application cutover. | DBA, App owner |

### Set up a new MongoDB Atlas environment on AWS
<a name="set-up-a-new-mongodb-atlas-environment-on-aws"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a new MongoDB Atlas cluster on AWS. | In MongoDB Atlas, choose **Build a Cluster**. In the **Create New Cluster** dialog box, select AWS as the cloud provider. | DBA |
| Select AWS Regions and global cluster configuration. | Select from the list of available AWS Regions for your Atlas cluster. Configure global clusters if required. | DBA |
| Select the cluster tier. | Select your preferred cluster tier. Your tier selection determines factors such as memory, storage, and IOPS specification. | DBA |
| Configure additional cluster settings. | Configure additional cluster settings such as MongoDB version, backup, and encryption options. For more information about these options, see the [Related resources](#migrate-relational-database-to-mongodb-atlas-resources) section. | DBA |

### Configure security and compliance
<a name="configure-security-and-compliance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the access list. | To connect to the Atlas cluster, you must add an entry to the project’s access list. Atlas uses TLS/SSL to encrypt the connections to the virtual private cloud (VPC) for your database. To set up the access list for the project and for more information about the stories in this epic, see the [Related resources](#migrate-relational-database-to-mongodb-atlas-resources) section. | DBA |
| Authenticate and authorize users. | You must create and authenticate the database users who will access the MongoDB Atlas clusters. To access clusters in a project, users must belong to that project, and they can belong to multiple projects. | DBA |
| Create custom roles. | (Optional) Atlas supports creating custom roles in cases where the built-in Atlas database user permissions don’t cover the set of permissions you want. | DBA |
| Set up VPC peering. | (Optional) Atlas supports [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) with other VPCs on AWS. | AWS administrator |
| Set up an AWS PrivateLink endpoint. | (Optional) You can set up private endpoints on AWS by using AWS PrivateLink. For more information, see the [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html). | AWS administrator |
| Enable two-factor authentication. | (Optional) Atlas supports two-factor authentication (2FA) to help users control access to their Atlas accounts. | AWS administrator |
| Set up user authentication and authorization with LDAP. | (Optional) Atlas supports performing user authentication and authorization with Lightweight Directory Access Protocol (LDAP). | DBA |
| Set up unified AWS access. | (Optional) Some Atlas features, including Atlas Data Lake and encryption at rest using customer key management, use AWS Identity and Access Management (IAM) roles for authentication. | AWS administrator |
| Set up encryption at rest using AWS KMS. | (Optional) Atlas supports using AWS Key Management Service (AWS KMS) to encrypt storage engines and cloud provider backups. | AWS administrator |
| Set up client-side field-level encryption. | (Optional) Atlas supports client-side field level encryption, including automatic encryption of fields. | AWS administrator |

### Migrate data
<a name="migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add MongoDB Relational Migrator to the access list. | Add the Relational Migrator to the access list for your source database. This helps prepare the source environment to connect to the target Atlas cluster. | DBA |
| Assess the relational database objects. | Launch MongoDB Relational Migrator and connect to your relational database. Start the assessment. | DBA |
| Accept the migration patterns or choose to alter them based on your business needs. | Either accept the database patterns recommended by the Relational Migrator based on the initial assessment and performance parameters, or choose to alter them based on your business requirements. | DBA |
| Launch your target replica set in MongoDB Atlas. | Launch your target replica set in MongoDB Atlas. In Relational Migrator, choose **I'm ready to migrate**. | DBA |

### Configure operational integration
<a name="configure-operational-integration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Connect to the MongoDB Atlas cluster. | Make sure that MongoDB Atlas cluster connectivity works as expected. | App owner |
| Interact with cluster data. | Verify the cluster data. | DBA |
| Monitor your clusters. | Verify that your clusters are set up correctly. | DBA |
| Back up and restore cluster data. | Schedule backups with a regular cadence for cluster data. | DBA |

## Related resources
<a name="migrate-relational-database-to-mongodb-atlas-resources"></a>

All of the following links, unless noted otherwise, go to webpages in the MongoDB documentation.

**Migration guide**
+ [Migrating to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/) (AWS Prescriptive Guidance)

**Discovery and assessment**
+ [Memory](https://docs.atlas.mongodb.com/sizing-tier-selection/#memory)
+ [Sizing example with Atlas sample data sets](https://www.mongodb.com/docs/atlas/sizing-tier-selection/#example--the-service-sample-data-sets)
+ [Sizing example for mobile applications](https://www.mongodb.com/docs/atlas/sizing-tier-selection/#example--mobile-app)
+ [Network Traffic](https://docs.atlas.mongodb.com/sizing-tier-selection/#network-traffic)
+ [Cluster Auto-Scaling](https://www.mongodb.com/docs/atlas/sizing-tier-selection/#cluster-auto-scaling)
+ [Atlas sizing template](https://view.highspot.com/viewer/5f438f47a4dfa042e97130c5)

**Configuring security and compliance**
+ [Configure IP Access List Entries](https://docs.atlas.mongodb.com/security/ip-access-list/)
+ [Configure Database Users](https://docs.atlas.mongodb.com/security-add-mongodb-users/)
+ [Configure Access to the Atlas UI](https://docs.atlas.mongodb.com/organizations-projects/)
+ [Configure Custom Database Roles](https://docs.atlas.mongodb.com/security-add-mongodb-roles)
+ [Configure Database Users](https://docs.atlas.mongodb.com/security-add-mongodb-users/#atlas-user-privileges)
+ [Set up a Network Peering Connection](https://docs.atlas.mongodb.com/security-vpc-peering/)
+ [Learn About Private Endpoints in Atlas](https://docs.atlas.mongodb.com/security-private-endpoint/)
+ [Manage Your Multi-Factor Authentication Options](https://docs.atlas.mongodb.com/security-two-factor-authentication/)
+ [Set up User Authentication and Authorization with LDAP](https://docs.atlas.mongodb.com/security-ldaps/)
+ [Atlas Data Lake](https://docs.mongodb.com/datalake/)
+ [Encryption at Rest using Customer Key Management](https://docs.atlas.mongodb.com/security-kms-encryption/)
+ [Methods to assume a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html) (IAM documentation)
+ [Client-Side Field Level Encryption](https://docs.mongodb.com/manual/core/security-client-side-encryption)
+ [Automatic Encryption](https://docs.mongodb.com/manual/core/security-automatic-client-side-encryption)
+ [MongoDB Atlas Security Controls](https://webassets.mongodb.com/_com_assets/cms/MongoDB_Atlas_Security_Controls-v7k3rbhi3p.pdf)
+ [MongoDB Trust Center](https://www.mongodb.com/cloud/trust)
+ [Configure Security Features for Clusters](https://docs.atlas.mongodb.com/setup-cluster-security/)

**Setting up a new MongoDB Atlas environment on ****AWS**
+ [Cloud Providers and Regions](https://docs.atlas.mongodb.com/cloud-providers-regions/)
+ [Manage Global Clusters](https://docs.atlas.mongodb.com/global-clusters/)
+ [Select Cluster Tier](https://www.mongodb.com/docs/atlas/manage-clusters/#select-cluster-tier)
+ [Configure Additional Settings](https://docs.atlas.mongodb.com/cluster-additional-settings/)
+ [Get Started with Atlas](https://docs.atlas.mongodb.com/getting-started/)
+ [Configure Access to the Atlas UI](https://docs.atlas.mongodb.com/organizations-projects/)

**Migrating data**
+ [Migrate or Import Data](https://www.mongodb.com/docs/atlas/import/)

**Monitoring clusters**
+ [Monitor Your Clusters](https://docs.atlas.mongodb.com/monitoring-alerts/)

**Integrating operations**
+ [Connect to a Cluster](https://docs.atlas.mongodb.com/connect-to-cluster/)
+ [Interact with Your Data](https://docs.atlas.mongodb.com/data-explorer/)
+ [Monitor Your Clusters](https://docs.atlas.mongodb.com/monitoring-alerts/)
+ [Back Up, Restore, and Archive Data](https://docs.atlas.mongodb.com/backup-restore-cluster/)
