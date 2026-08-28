---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/assess-query-performance-for-migrating-sql-server-databases-to-mongodb-atlas-on-aws.html
---

# Assess query performance for migrating SQL Server databases to MongoDB Atlas on AWS
<a name="assess-query-performance-for-migrating-sql-server-databases-to-mongodb-atlas-on-aws"></a>

*Battulga Purevragchaa, Amazon Web Services*

*Krishnakumar Sathyanarayana, PeerIslands US Inc*

*Babu Srinivasan, MongoDB*

## Summary
<a name="assess-query-performance-for-migrating-sql-server-databases-to-mongodb-atlas-on-aws-summary"></a>

This pattern provides guidance for loading MongoDB with near real-world data and assessing MongoDB query performance that is as close to the production scenario as possible. The assessment provides input to help you plan your migration to MongoDB from a relational database. The pattern uses [PeerIslands Test Data Generator and Performance Analyzer](https://tools.peerislands.io/) to test query performance.

This pattern is particularly useful for Microsoft SQL Server migration to MongoDB, because performing schema transformations and loading data from current SQL Server instances to MongoDB can be very complex. Instead, you can load near real-world data into MongoDB, understand MongoDB performance, and fine-tune the schema design before you start the actual migration.

## Prerequisites and limitations
<a name="assess-query-performance-for-migrating-sql-server-databases-to-mongodb-atlas-on-aws-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Familiarity with [MongoDB Atlas](https://www.mongodb.com/docs/atlas/getting-started/)
+ Target MongoDB schema
+ Typical query patterns

**Limitations**
+ Data load times and performance will be limited by the MongoDB cluster instance size. We recommend that you choose instances that are recommended for production use to understand real-world performance.
+ PeerIslands Test Data Generator and Performance Analyzer currently supports only online data loads and queries. Offline batch processing (for example, loading data into MongoDB by using Spark connectors) isn’t yet supported.
+ PeerIslands Test Data Generator and Performance Analyzer supports field relations within a collection. It doesn’t support relationships across collections.

**Product editions**
+ This pattern supports both [MongoDB Atlas](https://www.mongodb.com/atlas) and [MongoDB Enterprise Advanced](https://www.mongodb.com/products/mongodb-enterprise-advanced).

## Architecture
<a name="assess-query-performance-for-migrating-sql-server-databases-to-mongodb-atlas-on-aws-architecture"></a>

**Target technology stack**
+ MongoDB Atlas or MongoDB Enterprise Advanced

**Architecture**

![Architecture to assess query performance for migrating SQL Server database to MongoDB Atlas on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/25f0ab73-d587-4bd0-9fc0-ac675d5aa349/images/717caae4-d52e-4c78-bb7d-2ecb5acccd42.png)

PeerIslands Test Data Generator and Performance Analyzer is built by using Java and Angular, and stores its generated data on Amazon Elastic Block Store (Amazon EBS). The tool consists of two workflows: test data generation and performance testing.
+ In test data generation, you create a template, which is the JSON representation of the data model that has to be generated. After you create the template, you can generate the data in a target collection, as defined by the load generation configuration.
+ In performance testing, you create a profile. A profile is a multi-stage testing scenario where you can configure create, read, update, and delete (CRUD) operations, aggregation pipelines, the weightage for each operation, and the duration of each stage. After you create the profile, you can run performance testing on the target database based on the configuration.

PeerIslands Test Data Generator and Performance Analyzer stores its data on Amazon EBS, so you can connect Amazon EBS to MongoDB by using any MongoDB-supported connection mechanism, including peering, allow lists, and private endpoints. By default, the tool doesn’t include operational components; however, it can be configured with Amazon Managed Service for Prometheus, Amazon Managed Grafana, Amazon CloudWatch, and AWS Secrets Manager if required.

## Tools
<a name="assess-query-performance-for-migrating-sql-server-databases-to-mongodb-atlas-on-aws-tools"></a>
+ [PeerIslands Test Data Generator and Performance Analyzer](https://tools.peerislands.io/) includes two components. The Test Data Generator component helps you generate highly customer-specific, real-world data based on your MongoDB schema. The tool is fully UI-driven with a rich data library and can be used to quickly generate billions of records on MongoDB. The tool also provides capabilities to implement relationships between fields in the MongoDB schema. The Performance Analyzer component helps you generate highly customer-specific queries and aggregations, and perform realistic performance testing on MongoDB. You can use the Performance Analyzer to test MongoDB performance with rich load profiles and parameterized queries for your specific use case.

## Best practices
<a name="assess-query-performance-for-migrating-sql-server-databases-to-mongodb-atlas-on-aws-best-practices"></a>

See the following resources:
+ [MongoDB Schema Design Best Practices](https://www.mongodb.com/developer/products/mongodb/mongodb-schema-design-best-practices/) (MongoDB Developer website)
+ [Best Practices of Deploying MongoDB Atlas on AWS](https://www.mongodb.com/presentation/best-practices-of-deploying-mongodb-atlas-on-aws) (MongoDB website)
+ [Connecting Applications Securely to a MongoDB Atlas Data Plane with AWS PrivateLink](https://aws.amazon.com/blogs/apn/connecting-applications-securely-to-a-mongodb-atlas-data-plane-with-aws-privatelink/) (AWS blog post)
+ [Best Practices Guide for MongoDB Performance ](https://www.mongodb.com/basics/best-practices)(MongoDB website)

## Epics
<a name="assess-query-performance-for-migrating-sql-server-databases-to-mongodb-atlas-on-aws-epics"></a>

### Understand your source data
<a name="understand-your-source-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Understand the database footprint of the current SQL Server source. | Understand your current SQL Server footprint. This can be achieved by running queries against the `INFORMATION` schema of the database. Determine the number of tables and size of each table. Analyze the index associated with each table. For more information about SQL analysis, see the blog post [SQL2Mongo: Data Migration Journey](https://engineering.peerislands.io/sql2mongo-data-migration-journey-fec91a421d60) on the PeerIslands website. | DBA |
| Understand the source schema. | Determine the table schema and the business representation of the data (for example, zip codes, names, and currency). Use your existing entity relationship (ER) diagram or generate the ER diagram from the existing database. For more information, see the blog post [SQL2Mongo: Data Migration Journey](https://engineering.peerislands.io/sql2mongo-data-migration-journey-fec91a421d60) on the PeerIslands website. | DBA |
| Understand query patterns. | Document the top 10 SQL queries you use. You can use the **performance\_schema.events\_statements\_summary\_by\_digest** tables that are available in the database to understand the top queries. For more information, see the blog post [SQL2Mongo: Data Migration Journey](https://engineering.peerislands.io/sql2mongo-data-migration-journey-fec91a421d60) on the PeerIslands website. | DBA |
| Understand SLA commitments. | Document the target service-level agreements (SLAs) for database operations. Typical measures include query latency and queries per second. The measures and their targets are typically available in non-functional requirements (NFR) documents. | DBA |

### Define the MongoDB schema
<a name="define-the-mongodb-schema"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Define the target schema. | Define various options for the target MongoDB schema. For more information, see [Schemas](https://www.mongodb.com/docs/atlas/app-services/schemas/) in the MongoDB Atlas documentation. Consider the best practices and design patterns based on the table relations.  | MongoDB engineer |
| Define target query patterns. | Define MongoDB queries and aggregation pipelines. These queries are the equivalent of the top queries you captured for your SQL Server workload. To understand how to construct MongoDB aggregation pipelines, see the [MongoDB documentation](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/). | MongoDB engineer |
| Define the MongoDB instance type. | Determine the size of the instance that you plan to use for testing. For guidance, see the [MongoDB documentation](https://www.mongodb.com/docs/atlas/sizing-tier-selection/). | MongoDB engineer |

### Prepare the target database
<a name="prepare-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the MongoDB Atlas cluster. | To set up a MongoDB cluster on AWS, follow the instructions in the [MongoDB documentation](https://www.mongodb.com/docs/atlas/tutorial/create-new-cluster/). | MongoDB engineer |
| Create users in the target database. | Configure the MongoDB Atlas cluster for access and network security by following the instructions in the [MongoDB documentation](https://www.mongodb.com/docs/atlas/connect-to-database-deployment/). | MongoDB engineer |
| Create appropriate roles in AWS and configure role-based access control for Atlas. | If required, set up additional users by following the instructions in the [MongoDB documentation](https://www.mongodb.com/docs/atlas/security/set-up-unified-aws-access/). Configure [authentication and authorization](https://www.mongodb.com/docs/atlas/security/config-db-auth/) through AWS roles. | MongoDB engineer |
| Set up Compass for MongoDB Atlas access. | Set up the [MongoDB Compass GUI utility](https://www.mongodb.com/products/compass) for ease of navigation and access. | MongoDB engineer |

### Set up the base load by using Test Data Generator
<a name="set-up-the-base-load-by-using-test-data-generator"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install Test Data Generator. | Install [PeerIsland Test Data Generator](https://github.com/PeerIslands/loadgen_binary) in your environment. | MongoDB engineer |
| Configure Test Data Generator to generate the appropriate data. | Create a template by using the data library to generate specific data for each field in the MongoDB schema. For more information, see the [MongoDB Data Generator & Perf. Analyzer](https://vimeo.com/570068857) video. | MongoDB engineer |
| Horizontally scale Test Data Generator to generate the required load. | Use the template you created to start the load generation against the target collection by configuring the required parallelism. Determine the time frames and scale to generate the necessary data. | MongoDB engineer |
| Validate the load in MongoDB Atlas. | Check the data loaded into MongoDB Atlas. | MongoDB engineer |
| Generate required indexes on MongoDB. | Define indexes as required, based on query patterns. For best practices, see the [MongoDB documentation](https://www.mongodb.com/docs/manual/applications/indexes/). | MongoDB engineer |

### Conduct performance testing
<a name="conduct-performance-testing"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up load profiles in Performance Analyzer. | Create a performance testing profile in Performance Analyzer by configuring specific queries and their corresponding weightage, duration of the test run, and stages. For more information, see the [MongoDB Data Generator & Perf. Analyzer](https://vimeo.com/570068857) video. | MongoDB engineer |
| Run performance testing. | Use the performance testing profile you created to start the test against the target collection by configuring the required parallelism. Horizontally scale the performance test tool to run queries against MongoDB Atlas. | MongoDB engineer |
| Record test results. | Record P95, P99 latency for the queries. | MongoDB engineer |
| Tune your schema and query patterns. | Modify indexes and query patterns to address any performance issues. | MongoDB engineer |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down temporary AWS resources. | Delete all temporary resources that you used for Test Data Generator and Performance Analyzer. | AWS administrator |
| Update performance test results. | Understand MongoDB query performance and compare it against your SLAs. If necessary, fine-tune the MongoDB schema and rerun the process. | MongoDB engineer |
| Conclude the project. | Close out the project and provide feedback. | MongoDB engineer |

## Related resources
<a name="assess-query-performance-for-migrating-sql-server-databases-to-mongodb-atlas-on-aws-resources"></a>
+ GitHub repository: [S3toAtlas](https://github.com/mongodb-partners/S3toAtlas)
+ Schema: [MongoDB Schema design](https://www.mongodb.com/developer/products/mongodb/mongodb-schema-design-best-practices/)
+ Aggregation pipelines : [MongoDB aggregation pipelines](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/)
+ MongoDB Atlas sizing : [Sizing tier selection](https://www.mongodb.com/docs/atlas/sizing-tier-selection/)
+ Video: [MongoDB Data Generator](https://vimeo.com/570068857) & Perf. Analyzer
+ References: [MongoDB documentation](https://www.mongodb.com/docs/)
+ Tutorials:** **[MongoDB developer guide, ](https://www.mongodb.com/docs/develop-applications/)[MongoDB Jumpstart](https://www.youtube.com/playlist?list=PL4RCxklHWZ9v2lcat4oEVGQhZg6r4IQGV)
+ AWS Marketplace:** **[MongoDB Atlas on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=c9032c7b-70dd-459f-834f-c1e23cf3d092)
+ AWS Partner Solutions:** **[ MongoDB Atlas on AWS Reference Deployment](https://aws.amazon.com/quickstart/architecture/mongodb-atlas/)

Additional resources:
+ [SQL analysis](https://engineering.peerislands.io/sql2mongo-data-migration-journey-fec91a421d60)
+ [MongoDB Developer Community forums](https://www.mongodb.com/community/forums/)
+ [MongoDB Performance Tuning Questions](https://www.mongodb.com/developer/products/mongodb/performance-tuning-tips/)
+ [Operational Analytics with Atlas and Redshift](https://github.com/mongodb-partners/Atlas_to_Redshift)
+ [Application modernization with MongoDB Atlas and AWS Elastic Beanstalk](https://github.com/mongodb-partners/MEANStack_with_Atlas_on_AWS_EB)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
