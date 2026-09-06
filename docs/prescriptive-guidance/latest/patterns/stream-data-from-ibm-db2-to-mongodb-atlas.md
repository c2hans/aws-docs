---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/stream-data-from-ibm-db2-to-mongodb-atlas.html
---

# Stream data from IBM Db2, SAP, Sybase, and other databases to MongoDB Atlas on AWS
<a name="stream-data-from-ibm-db2-to-mongodb-atlas"></a>

*Battulga Purevragchaa and Igor Alekseev, Amazon Web Services*

*Babu Srinivasan, MongoDB*

## Summary
<a name="stream-data-from-ibm-db2-to-mongodb-atlas-summary"></a>

This pattern describes the steps for migrating data from IBM Db2 and other databases such as mainframe databases and Sybase to MongoDB Atlas on the AWS Cloud. It uses [AWS Glue](https://aws.amazon.com/glue/) to help accelerate the data migration to MongoDB Atlas.

The pattern accompanies the guide [Migrating to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/) on the AWS Prescriptive Guidance website. It provides the implementation steps for one of the migration scenarios that are discussed in that guide. For additional migration scenarios, see the following patterns on the AWS Prescriptive Guidance website:
+ [Migrate a self-hosted MongoDB environment to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud.html)
+ [Migrate relational databases to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-relational-database-to-mongodb-atlas.html)

The pattern is intended for [AWS Managed Services Partners](https://aws.amazon.com/managed-services/partners/) and AWS users.

## Prerequisites and limitations
<a name="stream-data-from-ibm-db2-to-mongodb-atlas-prereqs"></a>

**Prerequisites**
+ A source database such as SAP, Sybase, IBM Db2, and others to migrate to MongoDB Atlas.
+ Familiarity with databases such as SAP, Sybase, IBM Db2, MongoDB Atlas, and AWS services.

**Product versions**
+ MongoDB version 5.0 or later.

## Architecture
<a name="stream-data-from-ibm-db2-to-mongodb-atlas-architecture"></a>

The following diagram illustrates batch data load and data streaming by using AWS Glue Studio, Amazon Kinesis Data Streams, and MongoDB Atlas.

This reference architecture uses AWS Glue Studio to create extract, transform, and load (ETL) pipelines to migrate data to MongoDB Atlas. An AWS Glue crawler integrates with MongoDB Atlas to facilitate data governance. The data can be either ported in batch or streamed to MongoDB Atlas by using Amazon Kinesis Data Streams.

**Batch data load**

![Migrating data to MongoDB Atlas in batch mode.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/805a376f-35f4-44cc-b4b0-8bf4d95c1e5d/images/68d87202-95ba-4e2a-9b3b-27dd6db6165e.png)

For more information about the batch data migration, see the AWS blog post [Compose your ETL jobs for MongoDB Atlas with AWS Glue](https://aws.amazon.com/blogs/big-data/compose-your-etl-jobs-for-mongodb-atlas-with-aws-glue/).

**Data streaming**

![Migrating data to MongoDB Atlas in data streaming mode.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/805a376f-35f4-44cc-b4b0-8bf4d95c1e5d/images/b007a116-f463-418f-9721-647d80177e3b.png)

For MongoDB Atlas reference architectures that support different usage scenarios, see [Migrating to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/architecture.html) on the AWS Prescriptive Guidance website.

## Tools
<a name="stream-data-from-ibm-db2-to-mongodb-atlas-tools"></a>

●      [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a fully managed ETL service. It helps you reliably categorize, clean, enrich, and move data between data stores and data streams.

●      [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) helps you collect and process large streams of data records in real time.

●      [MongoDB Atlas](https://www.mongodb.com/atlas) is a fully managed database as a service (DbaaS) for deploying and managing MongoDB databases in the cloud.

## Best practices
<a name="stream-data-from-ibm-db2-to-mongodb-atlas-best-practices"></a>

For guidelines, see [Best Practices Guide for MongoDB](https://github.com/mongodb-partners/mongodb_atlas_as_aws_bedrock_knowledge_base/blob/main/data/MongoDB_Best_Practices_Guide.pdf) in the MongoDB GitHub repository.

## Epics
<a name="stream-data-from-ibm-db2-to-mongodb-atlas-epics"></a>

### Discovery and assessment
<a name="discovery-and-assessment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Determine the cluster size. | Estimate the working set size by using the information from `db.stats()` for the total index space. Assume that a percentage of your data space will be accessed frequently. Or, you can estimate your memory requirements based on your assumptions. This task should take approximately one week. For more information and examples for this and the other stories in this epic, see the links in the [Related resources](#stream-data-from-ibm-db2-to-mongodb-atlas-resources) section. | MongoDB DBA, Application architect |
| Estimate network bandwidth requirements. | To estimate your network bandwidth requirements, multiply the average document size by the number of documents served per second. Consider the maximum traffic that any node on your cluster will bear as the basis. To calculate downstream data transfer rates from your cluster to client applications, use the sum of the total documents returned over a period of time. If your applications read from secondary nodes, divide this number of total documents by the number of nodes that can serve read operations. To find the average document size for a database, use the `db.stats().avgObjSize` command. This task will typically take one day. | MongoDB DBA |
| Select the Atlas tier. | Follow the instructions in the [MongoDB documentation](https://www.mongodb.com/docs/atlas/manage-clusters/) to select the correct Atlas cluster tier.  | MongoDB DBA |
| Plan for cutover. | Plan for application cutover. | MongoDB DBA, Application architect |

### Set up a new MongoDB Atlas environment on AWS
<a name="set-up-a-new-mongodb-atlas-environment-on-aws"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a new MongoDB Atlas cluster on AWS. | In MongoDB Atlas, choose **Build a Cluster**, and select AWS as the cloud provider. | MongoDB DBA |
| Select AWS Regions and global cluster configuration. | Select from the list of available AWS Regions for your Atlas cluster. Configure global clusters if required. | MongoDB DBA |
| Select the cluster tier. | Select your preferred cluster tier. Your tier selection determines factors such as memory, storage, and IOPS specification. | MongoDB DBA |
| Configure additional cluster settings. | Configure additional cluster settings such as MongoDB version, backup, and encryption options. For more information about these options, see the [Related resources](#stream-data-from-ibm-db2-to-mongodb-atlas-resources) section. | MongoDB DBA |

### Configure security and compliance
<a name="configure-security-and-compliance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the access list. | To connect to the Atlas cluster, you must add an entry to the [project’s access list](https://www.mongodb.com/docs/atlas/setup-cluster-security/#configure-security-features-for-clusters). Atlas uses Transport Layer Security (TLS) / Secure Sockets Layer (SSL) to encrypt the connections to the virtual private cloud (VPC) for your database. To set up the access list for the project and for more information about the stories in this epic, see the links in the [Related resources](#stream-data-from-ibm-db2-to-mongodb-atlas-resources) section.  | MongoDB DBA |
| Authenticate and authorize users. | You must create and authenticate the database users who will access the MongoDB Atlas clusters. To access the clusters in a project, users must belong to that project, and they can belong to multiple projects. You can also enable authorization with AWS Identity and Access Management (IAM). For more information, see [Set Up Authentication with IAM](https://www.mongodb.com/docs/atlas/security/aws-iam-authentication/#set-up-authentication-with-aws-iam) in the MongoDB documentation. | MongoDB DBA |
| Create custom roles. | (Optional) Atlas supports creating [custom roles](https://www.mongodb.com/docs/atlas/reference/custom-role-actions/) if the built-in Atlas database user privileges don’t cover your desired set of privileges. | MongoDB DBA |
| Set up VPC peering. | (Optional) Atlas supports [VPC peering](https://www.mongodb.com/docs/atlas/security-vpc-peering/#set-up-a-network-peering-connection) with other AWS VPCs. | MongoDB DBA |
| Set up an AWS PrivateLink endpoint. | (Optional) You can set up private endpoints on AWS by using [AWS PrivateLink](https://www.mongodb.com/docs/atlas/security-private-endpoint/). | MongoDB DBA |
| Enable two-factor authentication. | (Optional) Atlas supports two-factor authentication (2FA) to help users control access to their Atlas accounts. | MongoDB DBA |
| Set up user authentication and authorization with LDAP. | (Optional) Atlas supports performing user authentication and authorization with Lightweight Directory Access Protocol (LDAP). | MongoDB DBA |
| Set up unified AWS access. | (Optional) Some Atlas features, including Atlas Data Lake and encryption at rest using customer key management, use IAM roles for authentication. | MongoDB DBA |
| Set up encryption at rest by using AWS KMS. | (Optional) Atlas supports using AWS Key Management Service (AWS KMS) to encrypt storage engines and cloud provider backups. | MongoDB DBA |
| Set up CSFLE. | (Optional) Atlas supports [client-side field-level encryption (CSFLE)](https://www.mongodb.com/docs/upcoming/core/csfle/#client-side-field-level-encryption), including automatic encryption of fields.  | MongoDB DBA |

### Migrate data
<a name="migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch your target replica set in MongoDB Atlas. | Launch your target replica set in MongoDB Atlas. In Atlas Live Migration Service, choose **I'm ready to migrate**. | MongoDB DBA |
| Establish the connection of AWS Glue with MongoDB Atlas. | Use an AWS Glue crawler to connect AWS Glue with MongoDB Atlas (target database). This step helps prepare the target environment for migration. For more information, see the [AWS Glue documentation](https://docs.aws.amazon.com/glue/latest/dg/console-connections.html). | MongoDB DBA |
| Establish the connection of AWS Glue with the source database or source stream. | This helps prepare the target environment for migration. | MongoDB DBA |
| Set up the data transformation. | Configure the transformation logic to migrate the data from the legacy structured schema to the flexible schema of MongoDB. | MongoDB DBA |
| Migrate the data. | Schedule the migration in AWS Glue Studio. | MongoDB DBA |

### Configure operational integration
<a name="configure-operational-integration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Connect to the cluster. | Connect to the MongoDB Atlas cluster. | App developer |
| Interact with data. | Interact with cluster data. | App developer |
| Monitor the clusters. | Monitor your MongoDB Atlas clusters. | MongoDB DBA |
| Back up and restore data. | Back up and restore cluster data. | MongoDB DBA |

## Troubleshooting
<a name="stream-data-from-ibm-db2-to-mongodb-atlas-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| If you encounter issues | See [Troubleshooting](https://github.com/mongodb/mongodbatlas-cloudformation-resources/tree/master#troubleshooting) in the MongoDB Atlas CloudFormation Resources repository. |

## Related resources
<a name="stream-data-from-ibm-db2-to-mongodb-atlas-resources"></a>

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
+ [Backu Up, Restore, and Archive Data](https://docs.atlas.mongodb.com/backup-restore-cluster/)

**GitHub repository**
+ [Stream data to MongoDB Atlas using AWS Glue](https://github.com/mongodb-partners/Stream_Data_into_MongoDB_AWS_Glue?tab=readme-ov-file#troubleshooting)
