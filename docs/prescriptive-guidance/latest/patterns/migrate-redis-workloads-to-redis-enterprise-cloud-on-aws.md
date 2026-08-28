---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-redis-workloads-to-redis-enterprise-cloud-on-aws.html
---

# Migrate Redis workloads to Redis Enterprise Cloud on AWS
<a name="migrate-redis-workloads-to-redis-enterprise-cloud-on-aws"></a>

*Antony Prasad Thevaraj, Amazon Web Services*

*Srinivas Pendyala, Redis*

## Summary
<a name="migrate-redis-workloads-to-redis-enterprise-cloud-on-aws-summary"></a>

This pattern discusses the high-level process for migrating Redis workloads to Redis Enterprise Cloud on Amazon Web Services (AWS). It describes the migration steps, provides information about the selection of tools available, and discusses the advantages, disadvantages, and steps for using each tool. Optionally, if you require additional help in migrating workloads from Redis, you can engage Redis Professional Services.

If you run Redis OSS or Redis Enterprise Software on premises, you’re familiar with the significant administrative overhead and operational complexity of maintaining your Redis databases in your data center. By migrating your workloads to the cloud, you can significantly reduce this operational burden and take advantage of [Redis Enterprise Cloud](https://redis.com/redis-enterprise-cloud/overview/), which is a fully hosted database as a service (DBaaS) offering from Redis. This migration helps increase your business agility, improves application reliability, and reduces overall costs while you gain access to the newest Redis Enterprise Cloud on AWS features such as 99.999% availability, architectural simplicity, and scale.

There are potential applications for Redis Enterprise Cloud in the financial services, retail, healthcare, and gaming sectors, as well as in use cases that require solutions for fraud detection, real-time inventory, claims processing, and session management. You can use Redis Enterprise Cloud to connect to your AWS resources―for example, to an application server that is running on Amazon Elastic Compute Cloud (Amazon EC2) instances, or to a microservice that is deployed as an AWS Lambda service.

## Prerequisites and limitations
<a name="migrate-redis-workloads-to-redis-enterprise-cloud-on-aws-prereqs"></a>

**Assumptions**
+ You are currently operating an on-premises database system that you want to migrate to the cloud.
+ You have identified the migration requirements for your workloads, including:
  + Data consistency requirements
  + Infrastructure and system environment requirements
  + Data mapping and transformation requirements
  + Functional testing requirements
  + Performance testing requirements
  + Validation requirements
  + Defined cutover strategy
+ You have assessed timelines and cost estimates required for the migration.
+ Your requirements take into consideration the scope of the work and the systems and databases you have identified to be part of the migration.
+ You have identified the stakeholders along with their roles and responsibilities in a responsible, accountable, consulted, informed (RACI) matrix.
+ You have received the necessary agreement and approvals from all stakeholders.

**Cost**

Depending on the technical specifications of your existing source database (for example, memory sizing, throughput, and total data size), a Redis solutions architect can size the target system on Redis Enterprise Cloud.  For general pricing information, see [Redis Pricing](https://redis.com/redis-enterprise-cloud/pricing) on the Redis website.

**People and skills**

The migration process involves the following roles and responsibilities.

|
|
| Role | Description | Skills required |
| --- |--- |--- |
| **Migration solutions architect** | A technical architect who has expertise in defining, planning, and implementing migration strategies | Technical and application-level understanding of source and target systems; experience with migrating workloads to the cloud |
| **Data architect** | A technical architect who has broad experience in defining, implementing, and delivering data solutions for a wide variety of databases | Data modeling for structured and unstructured data, deep understanding and experience in implementing databases for an enterprise |
| **Redis solutions architect** | A technical architect who can help architect an optimally sized Redis cluster for the appropriate use case | Expertise in architecting and deploying Redis solutions for a wide variety of use cases |
| **Cloud solutions architect** | A technical architect who has a deeper understanding of cloud solutions, especially on AWS | Expertise in architecting solutions for the cloud; workload migration and application modernization experience |
| **Enterprise architect** | A technical architect who has a complete understanding of the technical landscape at your organization, who has a shared vision for the future roadmap, and who practices and establishes standardized architectural best practices across all teams in your organization | Software architecture certifications such as TOGAF, foundational software engineering skills, and solutions architecture and enterprise architecture expertise |
| **IT or DevOps engineer** | An engineer who is responsible for creating and maintaining the infrastructure, including monitoring the infrastructure for issues, performing maintenance tasks, and making updates as needed. | Strong understanding of various technologies, including operating systems, networking, and cloud computing; familiarity with programming languages such as Python, Bash, and Ruby, as well as tools such as Docker, Kubernetes, and Ansible |

## Architecture
<a name="migrate-redis-workloads-to-redis-enterprise-cloud-on-aws-architecture"></a>

**Migration options  **

The following diagram shows options for migrating your on-premises (Redis-based or other) data sources to AWS. It shows several migration tools that you can choose from, such as exporting Redis Database (RDB) files to Amazon Simple Storage Service (Amazon S3), using the Redis replication feature, or using AWS DMS.

![Options for migrating on-premises data sources to Redis Enterprise Cloud on AWS](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/384309f6-7218-4a46-83a5-f37ff95c8832/images/4b242a29-d283-49a3-aaea-a970813db6be.png)

1. On-premises data sources: Databases that aren’t based on Redis, such as MySQL, PostgreSQL, Oracle, SQL Server, or MariaDB.

1. On-premises data sources: Redis protocol-based databases such as Redis OSS and Redis Enterprise Software.

1. The simplest way to migrate data from Redis-based databases is to export RDB files and import them into the target Redis Enterprise Cloud on AWS.

1. Alternatively, you can migrate the data from source to target by using the replication feature (`ReplicaOf`) in Redis.

1. If your data migration requirements include transformation of data, you can employ Redis Input/Output Tools (RIOT) to migrate the data.

1. Alternatively, you can use AWS Data Migration Service (AWS DMS) to migrate the data from SQL-based databases.

1. You must use virtual private cloud (VPC) peering for AWS DMS to migrate the data successfully into the target Redis Enterprise Cloud on AWS.

**Target architecture**

The following diagram shows a typical deployment architecture for Redis Enterprise Cloud on AWS and illustrates how it can be used with key AWS services.

![Deployment architecture for Redis Enterprise Cloud on AWS, and use with AWS services](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/384309f6-7218-4a46-83a5-f37ff95c8832/images/f1351537-e710-4a68-8768-89d44870150f.png)

1. You can connect to the business applications that are backed by Redis Enterprise Cloud on AWS.

1. You can run business applications in your own AWS account, in a VPC within that account.

1. You can use Redis Enterprise Cloud database endpoints to connect to your applications. Examples include an application server running on EC2 instances, a microservice deployed as an AWS Lambda service, an Amazon Elastic Container Service (Amazon ECS) application, or an Amazon Elastic Kubernetes Service (Amazon EKS) application.

1. Business applications running in your VPC require a VPC peer connection to the Redis Enterprise Cloud VPC. This enables the business applications to connect securely over private endpoints.

1. Redis Enterprise Cloud on AWS is an in-memory NoSQL database platform deployed as a DBaaS on AWS and is fully managed by Redis.

1. Redis Enterprise Cloud is deployed within a VPC in a standard AWS account that is created by Redis.

1. For security reasons, Redis Enterprise Cloud is deployed in a private subnet that can be accessed at both private and public endpoints. We recommend that you connect your client applications to Redis on private endpoints. If you plan to use a public endpoint, we strongly recommend that you [enable TLS](https://docs.redis.com/latest/rc/security/database-security/tls-ssl/) to encrypt the data between your client applications and Redis Enterprise Cloud.

The Redis migration methodology aligns with the AWS migration methodology, which is illustrated in [Mobilize your organization to accelerate large-scale migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/overview.html) on the AWS Prescriptive Guidance website.

** Automation and scale **

The environment setup tasks for the migration can be automated through AWS Landing Zone and infrastructure as code (IaC) templates for automation and scale. These are discussed in the [Epics ](#migrate-redis-workloads-to-redis-enterprise-cloud-on-aws-epics)section of this pattern.

## Tools
<a name="migrate-redis-workloads-to-redis-enterprise-cloud-on-aws-tools"></a>

Based on your data migration requirements, you can choose from a selection of technological options to migrate your data to Redis Enterprise Cloud on AWS. The following table describes and compares these tools.

|
|
| Tool | Description | Advantages | Disadvantages |
| --- |--- |--- |--- |
| [RDB export](https://docs.redis.com/latest/rc/api/examples/back-up-and-import-data/) and [import](https://docs.redis.com/latest/rc/databases/import-data/) | You export the data from the source (for example, Redis OSS or Redis Enterprise Software) database in the form of RDB files. If your database is provided through a Redis OSS Cluster, you export each master shard to an RDB.<br />You then import all the RDB files in one step. If your source database is based on an OSS Cluster but your target database isn't using the OSS Cluster API, you have to change your application source code to use a standard Redis client library.<br />Data transformation requirements or logical database merges require a more complex process, which is explained under *Logical database merge* later in this table. | + Simple.<br />+ Works with any Redis-based solution that can export data in RDB format as a source (including Redis OSS and Redis Enterprise Software).<br />+ Achieves data consistency with a simple process. | + Doesn’t address data transformation requirements or support logical database merges.<br />+ Time-consuming for larger datasets.<br />+ No delta migration support can lead to longer downtime. |
| [Redis replication feature](https://docs.redis.com/latest/rs/databases/import-export/replica-of/) (active-passive) | You can continuously replicate data from a Redis OSS, Enterprise Software, or Enterprise Cloud database to a Redis Enterprise Cloud database. After the initial synchronization, the Redis replication feature (`ReplicaOf`) performs a delta migration, which means that there’s nearly no observed application downtime.<br />The Redis replication feature is intended to be used in an active-passive way. The target is assumed to be passive and gets fully resynchronized (flushed and synchronized from the source database). Therefore, switching between the source and the target is somewhat more complicated.<br />It’s possible to replicate from a Redis OSS Cluster to a standard clustered Redis Enterprise Cloud database by specifying all the master shards of the OSS Cluster as sources. However, the Redis replication feature allows a maximum of 32 source databases. | + Supports continuous replication (initial data load followed by deltas).<br />+ Nearly no downtime (depends on replication lag).<br />+ Achieves data consistency. | + Only one site is intended to be active, so switching between sites is more complicated.<br />+ Supports a maximum of 32 master shards when you migrate from an OSS Cluster. |
| [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) | You can use AWS DMS to migrate data from any supported source database to a target Redis data store with minimal downtime. For more information, see [Using Redis as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redis.html) in the AWS DMS documentation. | + Supports the migration of both NoSQL and SQL data sources.<br />+ Works well with other AWS services.<br />+ Supports live migration and change data capture (CDC) use cases. | + Redis key-values cannot contain special characters such as %.<br />+ Doesn’t support the migration of data that has special characters in rows or in field names.<br />+ Doesn’t support full large binary object (LOB) mode. |
| Logical database merge | Special database merge requirements might require a custom data migration solution. For example, you might have four logical databases (`SELECT 0..3`) in Redis OSS, but you might want to use a single database endpoint instead of moving the data to multiple Redis Enterprise Cloud databases. Redis Enterprise doesn’t support selectable logical databases, so you would have to transform the source database’s physical data model. For example, you could map each database index to a prefix (`0` to `usr`, `1` to `cmp`, and so on), and then use a migration script or an extract, transform, and load (ETL) tool to output an RDB file, which you can then import into the target database. | + Granular control on shaping the data during migration to the target system by using custom scripts.  | + If you decide not to complete the migration, rollback can be very challenging, especially if newer data has to be rolled back to source systems.<br />+ Cost to build can be high if the goal is to build a one-off solution for a one-time migration.<br />+ Maintenance costs for code, infrastructure, development time, and other areas can be high if migration requirements change frequently.  |

In addition, you can use the following tools and services from AWS.

Assessment and discovery tool:
+ [Migration Evaluator](https://aws.amazon.com/migration-evaluator/)

Application and server migration tools:
+ [AWS Application Migration Service](https://aws.amazon.com/application-migration-service/)

[Database migration tools](https://aws.amazon.com/solutions/database-migrations/):
+ [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
+ [AWS Database Migration Service (AWS DMS)](https://aws.amazon.com/dms/)

[Data migration tools](https://aws.amazon.com/cloud-data-migration/):
+ [AWS Storage Gateway](https://aws.amazon.com/storagegateway/)
+ [AWS DataSync](https://aws.amazon.com/datasync/)
+ [AWS Direct Connect](https://aws.amazon.com/directconnect/)
+ [AWS Snowball](https://aws.amazon.com/snowball/)
+ [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/)

AWS Partner solutions:
+ [AWS Migration Competency Partners](https://aws.amazon.com/migration/partner-solutions/)

## Epics
<a name="migrate-redis-workloads-to-redis-enterprise-cloud-on-aws-epics"></a>

### Complete discovery and assessment tasks
<a name="complete-discovery-and-assessment-tasks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify workloads. | Identify the suitable candidate workloads that you want to migrate. Consider the following before you choose a workload for migration:+ What is the business value in migrating or not migrating this workload?<br />+ Is there a contingency plan if this workload doesn’t successfully migrate to the target system?<br />Ideally, choose a workload that has maximum business impact with minimum risks involved. Keep the overall process iterative and migrate in small increments. | Data architect, Business champions, Migration project sponsors |
| Identify data sources and requirements; design data model. | Redis runs a workshop to accelerate discovery and to define migration planning for the project. As a part of this workshop, Redis teams identify the data sources and source data model requirements, and analyze how these can be remodeled in Redis Enterprise Cloud.<br />The Redis migration team (Professional Services) performs a detailed data model design exercise with your organization. As a part of this exercise, the Redis team:+ Identifies target Redis data structures.<br />+ Defines the data mapping strategy.<br />+ Documents the migration approach and recommendations.<br />+ Reviews and finalizes the data model with the stakeholders. | Redis solutions architect |
| Identify the characteristics of the source database. | Identify the Redis product that is used in the source and target environments. For example:+ Is the source database an OSS Cluster database, a standalone Redis database, or a Redis Enterprise database?<br />+ Will the target database be a Redis Enterprise standard database or an OSS Cluster-compatible database?<br />+ What are the implications concerning the application source code? | Data architect |
| Gather current system SLA and other sizing metrics. | Determine the current service-level agreements (SLAs) expressed in terms of throughput (operations per second), latency, overall memory size per database, and high availability (HA) requirements. | Data architect |
| Identify the characteristics of the target system. | Determine the answers to these questions:+ How much data has to be migrated?<br />+ How long does it take to migrate the given amount of data?<br />+ What are the downtime requirements for the migration? Is it acceptable for your service or application to be unavailable for a specific period? If so, for how long?<br />+ How consistent should the migrated data be? Can the target database be in a slightly inconsistent (outdated) state?<br />+ Does data have to be transformed before it is loaded to the target database? (For example, you might want to convert selectable DB indexes to prefixes before migration.)<br />+ Is the source database reachable from the target database's host (for example, from a peer VPC or from a public endpoint using encryption)?<br />+ Complete a data sizing and Redis Cluster sizing exercise with a Redis technical architect.<br />+ Identify networking requirements, infrastructure requirements, software versions, and software licensing, and procure any components before the migration.<br />+ Are there any security concerns associated with the transfer of this data? | Data architect, Redis solutions architect (optional) |
| Identify dependencies. | Identify the upstream and downstream dependencies of the current system to be migrated. Make sure that the migration work is in alignment with other dependent system migrations. For example, if you’re planning to migrate other business applications from on premises to the AWS Cloud, identify these applications and align them based on project goals, timelines, and stakeholders. | Data architect, enterprise architect |
| Identify migration tools. | Depending on your data migration requirements (such as source data or downtime requirements), you can use any of the tools described previously in the [Tools ](#migrate-redis-workloads-to-redis-enterprise-cloud-on-aws-tools)section. In addition, you can use:+ Bidirectional (active-active) replication by using CRDB deployment.<br />+ Custom export/import scripts (for example, by using `DUMP/RESTORE` commands).<br />+ Additional export/import tools and helper tools such as [RIOT](https://github.com/redis-developer/riot), [ECstats2,](https://github.com/Redislabs-Solution-Architects/ecstats2) or ETL tools.<br />+ IaC tools such as Terraform or AWS CloudFormation templates. | Migration solutions architect, Redis solutions architect |
| Create a contingency plan. | Establish a contingency plan to roll back, in case you encounter problems during migration. | Project management, Technical teams, including architect |

### Complete security and compliance tasks
<a name="complete-security-and-compliance-tasks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Secure the Redis administration console. | To secure the administration console, follow the instructions in the [Redis documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/security/). | IT infrastructure administrator |
| Secure the Redis database. | See the following pages in the Redis documentation to:+ [Define role-based access control](https://docs.redis.com/latest/rc/security/database-security/passwords-users-roles/).<br />+ [Define network security](https://docs.redis.com/latest/rc/security/database-security/network-security/).<br />+ [Enable TLS](https://docs.redis.com/latest/rc/security/database-security/tls-ssl/). |  |
| Secure Redis Cloud APIs. | When you [enable the API](https://docs.redis.com/latest/rc/api/get-started/enable-the-api/), you can [manage the API keys](https://docs.redis.com/latest/rc/api/get-started/manage-api-keys/) for all owners of your Redis Cloud account. For an overview of the security features of the API, see the [API authentication documentation](https://docs.redis.com/latest/rc/api/get-started/) on the Redis website. | IT infrastructure administrator |

### Set up the new environment
<a name="set-up-the-new-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up a new environment on AWS. | This task includes:+ [AWS Landing Zone](https://aws.amazon.com/answers/aws-landing-zone/) setup activities. The landing zone supports:Multi-account deploymentsMinimum security baselineAutomated way to provision new accounts with a security baseline and ISV prerequisites (networking, security configuration, and so on)Notifications, centralized logging, and monitoring<br />+ ISV software configuration activities. This includes configurations that need to be included in the migration, such as product and workload settings and changes.<br />+ IaC activities such as configuring or customizing AWS CloudFormation or Terraform templates. | IT or DevOps engineer |
| Deploy the migration architecture. | 1. Set up Redis Enterprise Cloud on AWS.<br />2. Install migration tools such as RIOT or AWS DMS. See the [Tools ](#migrate-redis-workloads-to-redis-enterprise-cloud-on-aws-tools)section for a list of available tools.<br />3. Establish connectivity between the application, migration, and database layers.<br />4. Create a sample workload that can flow through each layer and migrate a small set of sample data.You are now ready to run the actual data migration pipelines and test them. | IT or DevOps engineer |

### Set up networking
<a name="set-up-networking"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Establish connectivity. | Establish connectivity between the on-premises infrastructure and AWS Cloud resources. Use security groups, AWS Direct Connect, and other resources to achieve this functionality. For more information, see [Connect Your Data Center to AWS](https://aws.amazon.com/getting-started/hands-on/connect-data-center-to-aws/) on the AWS website. | IT or DevOps engineer |
| Set up VPC peering. | Establish VPC peering between the VPCs that run business applications (or the EC2 instances that run migration tools or the AWS DMS replication server) and the VPC that runs Redis Enterprise Cloud. For instructions, see [Get started with Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html) in the Amazon VPC documentation, and [Enable VPC peering](https://docs.redis.com/latest/rc/security/vpc-peering/) in the Redis documentation. | IT or DevOps engineer |

### Migrate data
<a name="migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Choose a data migration tool. | Review the table in the [Tools ](#migrate-redis-workloads-to-redis-enterprise-cloud-on-aws-tools)section to see descriptions, advantages, and disadvantages of these tools:+ RDS export and import<br />+ Redis replication feature (`ReplicaOf`)<br />+ AWS DMS<br />+ Logical database merge<br />The following rows describe the data migration tasks associated with each tool. | Migration solutions architect |
| Option 1: Use RDB export and import. | 1. Disconnect the source: Stop the traffic on the source database (for example, by disconnecting business applications).<br />2. Export: Export the source database’s data as an RDB file.<br />3. Stage: Upload the data to a location that is accessible to the Redis Enterprise Cloud instances on AWS (for example, you can upload them to an S3 bucket or FTP server).<br />4. Import: Import the RDB files (by listing them all in one import step) to your Redis Enterprise Cloud target database.<br />5. Cut over: Move to the target database (for example, by connecting your application connect to it).For more information, see the [Redis documentation](https://docs.redis.com/latest/rc/databases/import-data/). | Migration solutions architect, Redis solutions architect |
| Option 2: Use the Redis replication feature (active-passive). | 1. Connect database: Establish a `ReplicaOf` link between the source and target databases.<br />2. Run an initial sync: Wait until the initial synchronization between the source and target databases is complete.<br />3. Disconnect the source: Stop the traffic on the source database (for example, by disconnecting the application).<br />4. Run delta replication: Wait until the delta is replicated on the target database.<br />5. Cut over: Move to the target database (for example, by connecting your application to it).<br />6. Delete: Remove the `ReplicaOf` link between the source and target databases.For more information, see the [Redis documentation](https://docs.redis.com/latest/rs/databases/import-export/replica-of/). | Migration solutions architect, Redis solutions architect |
| Option 3: Use AWS DMS. | 1. Set up an AWS DMS replication instance: This instance performs all migration processes. For instructions: [Working with an AWS DMS replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html) in the AWS DMS documentation.<br />2. Define the source database: Define the source endpoint. Test the connectivity between the source endpoint and the AWS DMS replication server. For instructions: [Creating source and target endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.Creating.html) in the AWS DMS documentation.<br />3. Set up the target database: Set up Redis Enterprise Cloud on AWS and set up the database to migrate to.<br />4. Define the target database: Define the target endpoint. Make sure that [VPC peering](https://docs.redis.com/latest/rc/security/vpc-peering/) is established between the VPC where AWS DMS is running and the VPC that hosts Redis Enterprise Cloud on AWS. Test the connectivity between the AWS DMS replication server and the target database.<br />5. Create an AWS DMS task: Create a task or a set of tasks to define the tables and replication processes you want to use to migrate the data. For instructions: [Working with AWS DMS tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html) in the AWS DMS documentation.<br />6. Migrate: Migrate the data by running the AWS DMS task.<br />7. Cut over: Move to the target database (for example, by connecting your application to it). | Migration solutions architect, Redis solutions architect |
| Option 4: Use logical database merge. | This option involves using a migration script or ETL tool that can transform the source database’s physical data model and generating an RDB file. Redis Professional Services c­an­­­ help with this step, if needed. | Migration solutions architect, Redis solutions architect |

### Migrate your application
<a name="migrate-your-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Align project management timelines and goals. | Align the migration project goals, milestones, and timelines of the application layer with that of the Redis data migration project. | Project management |
| Align testing activities. | After the application layer is migrated and modernized in the AWS Cloud, point the application layer to the newly migrated Redis Enterprise Cloud on AWS for testing. | Testing |

### Test
<a name="test"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Implement test plans. | Run the data migration routines and the scripts that were developed during the implementation phase in a testing environment, per test requirements, at your site. | Testing |
| Test data quality. | Test data quality after you migrate the data. | Testing |
| Test functionality. | Test data queries and the application layer to ensure that the application is performing at the same level as in the source system. | Testing |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Make the cutover decision.  | After all application-level and database-level testing is complete, the executive leadership team and stakeholders make the final decision regarding whether to cut over to the new environment on AWS based on the final results confirmed by the testing teams. | Project management, Business champions |
| Cut over to the AWS Cloud. | When you have confirmed that everything is in place, point the application layer to the newly migrated data and point clients to the new application layer that is running based on the new Redis Enterprise Cloud system on AWS. | IT or DevOps engineer, Data architect, Migration solutions architect, Redis solutions architect |

## Related resources
<a name="migrate-redis-workloads-to-redis-enterprise-cloud-on-aws-resources"></a>

**Redis resources**
+ [Redis Enterprise Cloud documentation](https://docs.redis.com/latest/rc/)
+ [RIOT](https://github.com/redis-developer/riot) tool (GitHub repository)
+ [Terraform Provider](https://registry.terraform.io/providers/RedisLabs/rediscloud/latest) (download)

**AWS resources**
+ [Demo migrations](https://aws.amazon.com/getting-started/tutorials/)
+ [AWS Partner Solutions](https://aws.amazon.com/quickstart/)
+ [Documentation](https://docs.aws.amazon.com/index.html)
+ [Blog posts](https://aws.amazon.com/blogs/database/category/migration/)
+ [White papers](https://aws.amazon.com/whitepapers/)
+ [Tutorials and videos](https://aws.amazon.com/getting-started/tutorials/)
+ [AWS cloud migration](https://aws.amazon.com/cloud-migration/)
+ [AWS Prescriptive Guidance](https://aws.amazon.com/prescriptive-guidance/)

## Additional information
<a name="migrate-redis-workloads-to-redis-enterprise-cloud-on-aws-additional"></a>

For standard security requirements for migrating Redis workloads to the AWS Cloud, see the [Best Practices for Security, Identity, and Compliance](https://aws.amazon.com/architecture/security-identity-compliance/) on the AWS website, and the [Redis Trust Center](https://trust.redis.io/) on the Redis website.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
