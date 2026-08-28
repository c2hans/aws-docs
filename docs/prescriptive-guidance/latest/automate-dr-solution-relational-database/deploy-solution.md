---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/deploy-solution.html
---

# Deploy the solution
<a name="deploy-solution"></a>

After you set up the prerequisites, follow the instructions in the [DR Orchestrator Framework pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-cross-region-failover-and-failback-by-using-dr-orchestrator-framework.html). Instructions are included for Amazon RDSAurora, and Amazon ElastiCache. To test the solution, review the prerequisites and limitations, and deploy example databases on AWS.

## Prerequisites
<a name="prerequisites.49a332c6-5afb-56e8-a334-0f46ba800ca0"></a>
+ An active [AWS account](https://aws.amazon.com/free/) to deploy this solution.
+ Permissions to create [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) buckets and the resources used in the [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) templates.
+ Before you run the `DR Orchestrator FAILBACK` state machine:
  + Manually [modify the RDS instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html) or [modify the Amazon Aurora DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Modifying.html), and disable `DeletionProtection`.
  + Take a [DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html) before deleting the Amazon RDS instance or Aurora cluster if you plan to perform root cause analysis (RCA).

## Limitations
<a name="limitations.bb5215b2-5623-5f41-9280-69268dc85668"></a>
+ Feature availability and support vary across specific versions of each database engine and across AWS Regions. For more information on feature and Region availability for cross-Region replication, see [Cross-Region read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.CrossRegionReadReplicas.html).
+ This solution has been tested using a primary database instance with one read replica. If you want to use more than one read replica, test the solution thoroughly before implementing it in a production environment.
+ For Amazon RDS, the solution supports only the following engines: [Amazon RDS for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html), [Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html), and [Amazon RDS for MariaDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html).

## Deploy example databases on AWS
<a name="deploy-example-databases-on-9999999999999999aws-.26a499d2-d163-5630-bf0f-ddd24711f3c7"></a>

To demonstrate the cross-Region DR solution for databases on AWS, you can deploy [Amazon RDS for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html), [Amazon Aurora MySQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.html), and [Amazon ElastiCache (Redis OSS) - Global Datastore](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html). Use the instructions in the `App-Stack` `README` file of the [aws-cross-region-dr-databases ](https://github.com/aws-samples/aws-cross-region-dr-databases/tree/main/App-Stack)GitHub repository. In this example, the primary Region is `us-east-1`, and the secondary Region is `us-west-2`.

The application stack uses the AWS CloudFormation [Outputs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html) section to export the parameters that are used by DR Orchestrator Framework to automate the failover and failback of AWS databases.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
