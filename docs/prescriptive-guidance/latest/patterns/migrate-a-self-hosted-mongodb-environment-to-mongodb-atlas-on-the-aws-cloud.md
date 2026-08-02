---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud.html
---

# Migrate a self-hosted MongoDB environment to MongoDB Atlas on AWS
<a name="migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud"></a>

*Battulga Purevragchaa and Igor Alekseev, Amazon Web Services*

*Babu Srinivasan, MongoDB*

## Summary
<a name="migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud-summary"></a>

This pattern describes the steps for migrating from a self-managed MongoDB environment (including MongoDB Community Server, Enterprise Server, Enterprise Advanced, mLab, or any managed MongoDB cluster) to MongoDB Atlas in the AWS Cloud. It uses the [Atlas Live Migration Service](https://www.mongodb.com/cloud/atlas/migrate) to help accelerate the data migration from MongoDB to MongoDB Atlas.

The pattern accompanies the guide [Migrating to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/) on the AWS Prescriptive Guidance website. It provides the implementation steps for one of the migration scenarios that are discussed in that guide. For additional migration scenarios, see the following patterns on the AWS Prescriptive Guidance website:
+ [Migrate a relational database to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-relational-database-to-mongodb-atlas.html)
+ [Stream data from IBM Db2, SAP, Sybase, and other databases to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/stream-data-from-ibm-db2-to-mongodb-atlas.html)

The pattern is intended for [AWS Systems Integrator (SI) Partners](https://aws.amazon.com/managed-services/partners/) and AWS users.

## Prerequisites and limitations
<a name="migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud-prereqs"></a>

**Prerequisites**
+ A source MongoDB Enterprise Advanced, Community Server, or other self-managed MongoDB environment to migrate to MongoDB Atlas.
+ Familiarity with MongoDB, MongoDB Atlas, and AWS services. This pattern explains some of the migration steps at a high level. Additional details will be added in future versions.

**Product versions**
+ MongoDB version 6.0.13 or later

## Architecture
<a name="migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud-architecture"></a>

The following diagram shows the Atlas Live Migration Service that is used to migrate data from a MongoDB Enterprise Advanced database and a MongoDB Community database to MongoDB Atlas on AWS. Use this service when you need to migrate large, complex databases to MongoDB Atlas with minimal downtime and continuous data synchronization. This pattern uses Atlas Live Migration Service.

![Migrating data with MongoDB Atlas Live Migration Service.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/52cdb923-64ff-4ee2-b129-93b9a139e24b/images/372134c4-ba47-4e48-bd0d-8b43017773b8.png)

The following diagram shows the MongoDB mirror service (`mongomirror`) that you can also use to migrate data from a MongoDB Enterprise Advanced database and a MongoDB Community database to MongoDB Atlas on AWS over a secured [AWS PrivateLink](https://aws.amazon.com/privatelink/) connection. Use `mongomirror` for ongoing data replication between on-premises MongoDB and MongoDB Atlas. This tool is ideal for disaster recovery or phased migrations but is outside the scope of this pattern.

![Migrating data with mongomirror tool.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/52cdb923-64ff-4ee2-b129-93b9a139e24b/images/53488a9b-2210-4b3d-b517-b618c1e0182c.png)

For more MongoDB Atlas reference architectures that support different usage scenarios, see [Migrating to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/architecture.html) on the AWS Prescriptive Guidance website.

## Tools
<a name="migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud-tools"></a>
+ [MongoDB Atlas](https://www.mongodb.com/atlas) is a fully managed database as a service (DbaaS) for deploying and managing MongoDB databases in the cloud.
+ [Atlas Live Migration Service](https://www.mongodb.com/cloud/atlas/migrate) is a free MongoDB utility that helps migrate databases to Atlas. This service keeps the source database in sync with the destination database until cutover. When you’re ready to cut over, you stop your application instances, point them to the destination Atlas cluster, and restart them. To access this service, choose **Database options** from your MongoDB Atlas cluster.
+ [mongomirror](https://www.mongodb.com/docs/atlas/import/mongomirror/) is a tool for manually migrating data from an existing MongoDB replica set to a MongoDB Atlas replica set. `mongomirror` doesn’t require you to shut down your existing replica set or applications, doesn’t import user or role data, or copy the configuration database. You can download `mongomirror` from the [MongoDB documentation](https://www.mongodb.com/docs/atlas/import/mongomirror/#download-mongomirror).

## Best practices
<a name="migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud-best-practices"></a>

For best practices for using MongoDB on AWS, see the posts on the [AWS Partner Network Blog](https://aws.amazon.com/blogs/apn/tag/mongodb-atlas/).

## Epics
<a name="migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud-epics"></a>

### Discovery and assessment
<a name="discovery-and-assessment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Determine the cluster size. | Estimate the working set size by using the information from `db.stats()` for the total index space. Assume that a percentage of your data space will be accessed frequently. Or, you can estimate your memory requirements based on your own assumptions. This task should take approximately one week. For more information and examples for this and the other stories in this epic, see the [Related resources](#migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud-resources) section. | DBA, App owner |
| Estimate network bandwidth requirements. | To estimate your network bandwidth requirements, multiply the average document size by the number of documents served per second. Consider the maximum traffic that any node on your cluster will bear as the basis. To calculate downstream data transfer rates from your cluster to client applications, use the sum of the total documents returned over a period of time. If your applications read from secondary nodes, divide this number of total documents by the number of nodes that can serve read operations. To find the average document size for a database, use the `db.stats().avgObjSize` command. This task will typically take one day. | DBA |
| Select the Atlas tier. | Follow the instructions in the [MongoDB documentation](https://www.mongodb.com/docs/atlas/sizing-tier-selection/) to select the correct Atlas cluster tier. | DBA |
| Plan for cutover. | Plan for application cutover. | DBA, App owner |

### Set up a new MongoDB Atlas environment on AWS
<a name="set-up-a-new-mongodb-atlas-environment-on-aws"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a new MongoDB Atlas cluster on AWS. | Log in to Atlas and open the **Overview** page for your project. Choose the **Create** button to create a cluster. For more information, see the [MongoDB documentation](https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/). | DBA |
| Select AWS Regions and global cluster configuration. | Select from the list of available AWS Regions for your Atlas cluster. Configure global clusters if required. For more information, see the [MongoDB documentation](https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/#select-your-preferred-region.). | DBA |
| Select the cluster tier. | Select your preferred cluster tier. Your tier selection determines factors such as memory, storage, and IOPS specification.  | DBA |
| Configure additional cluster settings. | Configure additional cluster settings such as MongoDB version, backup, and encryption options. For more information about these options, see the [Related resources](#migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud-resources) section. | DBA |

### Configure security and compliance
<a name="configure-security-and-compliance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Authenticate and authorize users. | You must create and authenticate the database users who will access the MongoDB Atlas clusters. To access clusters in a project, users must belong to that project, and they can belong to multiple projects. Atlas also supports authentication based on AWS Identity and Access Management (IAM). For more information, see the [MongoDB documentation](https://www.mongodb.com/docs/atlas/security/aws-iam-authentication/#set-up-authentication-with-aws-iam). | DBA |
| Create custom roles. | (Optional) Atlas supports creating custom roles in cases where the built-in Atlas database user permissions don’t cover the set of permissions you want. | DBA |
| Set up VPC peering. | (Optional) Atlas supports [virtual private cloud (VPC) peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) with other VPCs on AWS. | AWS administrator |
| Set up an AWS PrivateLink endpoint. | (Optional) You can set up private endpoints on AWS by using AWS PrivateLink. For more information, see the [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html). | AWS administrator |
| Enable two-factor authentication. | (Optional) Atlas supports two-factor authentication (2FA) to help users control access to their Atlas accounts. | AWS administrator |
| Set up user authentication and authorization with LDAP. | (Optional) Atlas supports performing user authentication and authorization with Lightweight Directory Access Protocol (LDAP). | AWS administrator |
| Set up unified AWS access. | (Optional) Some Atlas features, including Atlas Data Lake and encryption at rest using customer key management, use IAM roles for authentication. | AWS administrator |
| Set up encryption at rest using AWS KMS. | (Optional) Atlas supports using AWS Key Management Service (AWS KMS) to encrypt storage engines and cloud provider backups. | AWS administrator |
| Set up client-side field-level encryption. | (Optional) Atlas supports client-side field level encryption, including automatic encryption of fields. | AWS administrator |

### Migrate data
<a name="migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Select your target replica set in MongoDB Atlas. | Navigate to the destination Atlas cluster and choose the ellipsis (...) button. On the cluster list, this button appears below the cluster name. In cluster details, the button appears on the right, next to the **Connect** and **Configuration** buttons. For more information, see the [MongoDB documentation](https://www.mongodb.com/docs/atlas/import/c2c-pull-live-migration/#procedure). | DBA |
| Add the Atlas Live Migration Service to the access list. | Add the Atlas Live Migration Service to the access list in your AWS source cluster. This helps prepare the source environment to connect to the target Atlas cluster. | DBA |
| Perform migration with Atlas Live Migration Service. | Choose **Start migration**. When the **Prepare to Cutover** button turns green, perform the cutover. Review Atlas cluster performance metrics. Consider updating the database connection in all application layers to point to the new database. | DBA |

### Configure operational integration
<a name="configure-operational-integration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Connect to the MongoDB Atlas cluster. | Make sure that MongoDB Atlas cluster connectivity works as expected. | App owner |
| Interact with cluster data. | Test the cluster data. | DBA |
| Monitor your clusters. | Verify that your clusters are set up correctly. | DBA |
| Back up and restore cluster data. | Schedule backups with a regular cadence for cluster data. | DBA |

## Troubleshooting
<a name="migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Error: Could not reach specified source | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud.html) |
| Error: Could not resolve hostname | No IP address was found for the given hostname. Confirm that the given hostname is correct and publicly accessible. |
| Any other error | If you encounter any other errors, see [Troubleshoot Live Migration (Pull)](https://www.mongodb.com/docs/atlas/import/live-import-troubleshooting/) in the MongoDB documentation. |

## Related resources
<a name="migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud-resources"></a>

All of the following links, unless noted otherwise, go to webpages in the MongoDB documentation.

**Migration guide**
+ [Migrating to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/) (AWS Prescriptive Guidance)

**Legacy migration**
+ [Migration of older versions of MongoDB](https://www.mongodb.com/docs/atlas/legacy-migration/)

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

**Training**
+ [Live Migration with MongoDB Atlas](https://learn.mongodb.com/courses/live-migration-with-mongodb-atlas)

## Additional information
<a name="migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud-additional"></a>

For additional information, see the following topics in the MongoDB documentation:
+ To move data to a serverless instance, [use Compass to export and import data](https://www.mongodb.com/docs/compass/current/import-export/), or migrate data with self-managed tools. To learn more, see [Serverless Instance Limitations](https://www.mongodb.com/docs/atlas/reference/serverless-instance-limitations/).
+ To load data into a new cluster in Atlas, see [Load Data into Atlas.](https://www.mongodb.com/docs/atlas/sample-data/#std-label-sample-data)
+ To make a copy of your cluster for testing purposes, see [Backup Methods for a Self-Managed Deployment](https://www.mongodb.com/docs/manual/core/backups/).
+ If the application that you want to migrate requires a near-continuous uptime, contact [MongoDB Support](https://www.mongodb.com/docs/atlas/support/#std-label-request-support) and share your uptime requirements and cluster configuration.
+ For additional information, see [Migrate or Import Data](https://www.mongodb.com/docs/atlas/import/).
