---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/summary.html
---

# Migration summary
<a name="summary"></a>

The following provides a summary of the MongoDB Atlas on AWS migration environment, including assumptions, tools, and compliance certifications.

|  |  |  |
| --- |--- |--- |
| Workload | Source workload | A wide range of relational, legacy, and other databases, including Oracle Database, SQL Server, PostgreSQL, Azure Cosmos DB, and IBM Db2. |
| Destination workload | MongoDB Atlas |
| Migration | Migration strategy (7 Rs) | Replatform or re-architect |
| Is this an upgrade in the workload version? | See the [upgrade compatibility considerations](https://www.mongodb.com/docs/v4.4/tutorial/upgrade-revision/) in the MongoDB documentation[.](https://www.mongodb.com/docs/v4.4/tutorial/upgrade-revision/) |
| Migration duration | 3 days to 5 weeks (including all the tasks in the associated patterns). The duration might vary based on data size, application complexity, network bandwidth between source and target, and similar factors.   |
| Automated deployment to provision workload infrastructure on AWS | You can use AWS Partner Solutions, CloudFormation, or AWS Cloud Development Kit (AWS CDK). For more information, see the [MongoDB website](https://www.mongodb.com/blog/post/atlas-integrations-aws-cloud-formation-cdk-now-generally-available#:~:text=quick%20demo.-,Option%202%3A%20AWS%20CDK,-After%20its%20launch). |
| Cost | Cost of running ISV workload on AWS | See [MongoDB Pricing](https://www.mongodb.com/pricing) on the MongoDB website.<br />See [AWS Pricing Calculator](https://calculator.aws/#/) for AWS services. |
| Assumptions and prerequisites | Service-level agreements (SLAs) | For availability, see [MongoDB Atlas Service Level Agreement](https://www.mongodb.com/cloud/atlas/sla) on the MongoDB website.<br />Cluster durability depends on a cluster's geographical deployment configuration.<br />For cluster limits, connection limits, organization, and project limits, see [Atlas Service Limits](https://docs.atlas.mongodb.com/reference/atlas-limits/) on the MongoDB website. |
| Recovery time objectives (RTOs) | For information about how MongoDB Atlas automated backup features can meet your strict RTOs, see [Reliability](https://www.mongodb.com/cloud/atlas/reliability) on the MongoDB website. |
| Recovery point objectives (RPOs) | For information about how MongoDB Atlas point-in-time recovery features satisfy RPOs, see [Reliability](https://www.mongodb.com/cloud/atlas/reliability), [Back Up Your Cluster, ](https://docs.atlas.mongodb.com/backup/cloud-backup/overview/)and [Manage Online Archives](https://www.mongodb.com/docs/atlas/online-archive/query-online-archive/) on the MongoDB website. |
| Licensing and operating model for the target AWS account | Software as a service (SaaS) |
| Migration tooling | See [MongoDB Relational Migrator](https://www.mongodb.com/products/relational-migrator) and [Atlas Live Migration Service](https://www.mongodb.com/cloud/atlas/migrate) on the MongoDB website. |
| AWS services used | [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/)[Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc/)[AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/)[AWS PrivateLink](https://aws.amazon.com/privatelink/) (optional) |
| Benchmarks | See [MongoDB Benchmark](https://www.mongodb.com/scale/mongodb-benchmark) on the MongoDB website. |
| Compliance | Compliance certifications | Health Insurance Portability and Accountability Act (HIPAA)General Data Protection Regulation (GDPR)System and Organization Controls (SOC)EU-US Privacy ShieldISO/IEC 27001:2013Payment Card Industry Data Security Standard (PCI DSS)For details, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) on the AWS website and [MongoDB Trust Center](https://www.mongodb.com/cloud/trust) on the MongoDB website. |
| Limitations | System limitations (minimum/maximum requirements) | See [Atlas Service Limits](https://www.mongodb.com/docs/atlas/reference/atlas-limits/) on the MongoDB website. |
