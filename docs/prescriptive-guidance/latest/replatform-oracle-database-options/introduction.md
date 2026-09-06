---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/introduction.html
---

# Replatform options for Oracle Database on AWS
<a name="introduction"></a>

*Song Hu, Mohit Montu, and Rajeev Pardipuram, Amazon Web Services*

Migrating Oracle Database from on premises to Amazon Web Services (AWS) requires an optimal strategy. There are seven common strategies, which are often referred to as the 7 Rs:
+ Retire
+ Retain
+ Rehost
+ Relocate
+ Repurchase
+ Replatform
+ Refactor/re-architect

Choosing the optimal migration strategy depends on business need, resource requirements, time, and financial constraints. For more information, see [Overview of the 7 Rs of Database Migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-migration/planning-phase.html) and [Determining the R Type for Migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/prioritization-and-migration-strategy.html#migration-r-type).

Replatform is a good candidate to move workloads quickly to AWS. It offers the following benefits:
+ Introduces some level of optimization to take advantage of cloud capabilities
+ Reduces the amount of time spent on managing the database
+ Avoids the need to redesign or rewrite applications

After you select replatform as your migration strategy, the next steps are to evaluate different options that are available and to select the most appropriate one.

This guide walks through different options available for replatforming Oracle databases by using Amazon Relational Database Service (Amazon RDS). The guide discusses advantages and limitations that you can compare against your specific workload to identify the most appropriate approach for your business. The comparison is divided into three phases based on the AWS migration process best practices:
+ Phase 1: Assess
+ Phase 2: Mobilize
+ Phase 3: Migrate and modernize

This guide is intended for database administrators, solutions architects, and operations or infrastructure managers who are planning to migrate on-premises Oracle databases to AWS.
