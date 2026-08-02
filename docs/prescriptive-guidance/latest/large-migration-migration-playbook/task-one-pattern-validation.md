---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/task-one-pattern-validation.html
---

# Task 1: Validating the migration patterns and metadata
<a name="task-one-pattern-validation"></a>

In this task, you validate the migration patterns identified in the assessment and wave planning activities in the portfolio workstream, and then you validate the migration metadata source. The goal is to verify that sufficient data has been collected to support each migration pattern.

This task consists of the following steps:
+ [Step 1: Validate the migration patterns](#step-one-validate-patterns)
+ [Step 2: Validate the migration metadata and wave plan](#step-two-validate-metadata)

## Step 1: Validate the migration patterns
<a name="step-one-validate-patterns"></a>

In the portfolio workstream, you performed an initial assessment of the application portfolio, selected migration strategies, and identified migration patterns for each strategy. This information should be contained in your portfolio assessment runbook. For more information, see the [Portfolio playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/).

In this step, you review the migration strategies, verify that you have identified all migration patterns, and confirm that you are ready to draft migration runbooks. You might repeat this task throughout the project, and as your understanding of the portfolio matures, it is likely you will identify additional migration patterns in later stages of the migration.

1. **Review the migration strategies for the portfolio**

   A *migration strategy* is the approach used to migrate an on-premises application to the AWS Cloud. There are seven migration strategies for moving applications to the cloud, known as the *7 Rs*. Common strategies for large migrations include rehost, replatform, relocate, and retire. Refactor is not recommended for large migrations because it involves modernizing the application during the migration. This is the most complex of the migration strategies, and it can be complicated to manage for a large number of applications. Instead, we recommend rehosting, relocating, or replatforming the application and then modernizing the application after the migration is complete. For more information about the 7 Rs, see the [Guide for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/).

   Based on the output of the initial portfolio assessment, you have a list of all the required migration strategies for the portfolio and determined how much of the portfolio is allocated to each strategy. For example:
   + Rehost - 70%
   + Replatform - 20%
   + Retire - 10%

1. **Verify that the migration patterns for the portfolio**

   A *migration pattern* is a repeatable migration task that details the strategy, the destination, and the application or service used. In this step, you verify that the migration patterns include detailed information, such as which tools to use and which AWS services are targeted. For example:
   + Rehost to Amazon Elastic Compute Cloud (Amazon EC2) by using AWS Application Migration Service (AWS MGN) or Cloud Migration Factory
   + Replatform to Amazon EC2 by using AWS CloudFormation templates to build new infrastructure in the AWS Cloud
   + Replatform to Amazon Relational Database Service (Amazon RDS) by using AWS Database Migration Service (AWS DMS) or a native database technology
   + In the [Portfolio playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/), you map each migration pattern to its migration strategy and document the results in a table like the following example.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/task-one-pattern-validation.html)

## Step 2: Validate the migration metadata and wave plan
<a name="step-two-validate-metadata"></a>

In this step, you validate the source location of the migration metadata. You check that the data structure, such as the available columns in an Excel document, is suitable to hold the required metadata, and you check that all the metadata is available.

1. **Validate the migration metadata for your migration patterns**

   Each migration pattern needs a different set of migration metadata in order to migrate the servers and apps. For example, a rehost migration to Amazon EC2 requires that you provide specifications for the target instance, such as the VPC subnet, security group, and instance type information. However, a storage migration, database migration, or replatform migration requires a different set of migration metadata. You typically define migration metadata requirements in the portfolio assessment runbook, but you need to make sure that you have sufficient metadata to support each of your migration patterns. For more information about metadata identification and collection, see the [Portfolio playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/).

1. **Validate the source location of the migration metadata and the wave plan**

   You typically document the source location of the migration metadata in your metadata management runbook. Ideally, the location acts as a single source of truth, such as a wave-planning spreadsheet. It is also possible that the metadata is still in multiple places, including the following common locations:
   + Discovery tool
   + Configuration management database (CMDB)
   + App owner questionnaire
   + Migration wave-planning spreadsheet

   Validate the following for the metadata source location:

   1. Is the source catalog being maintained with locations of all metadata sources and owners?

   1. Does the source location (for example, wave-planning spreadsheet) have all the required migration metadata?

   1. Are there clear instructions for accessing each metadata source?

   1. If there is no single source, is each metadata source clearly mapped to its attributes?

   1. Is there a clear wave plan for the servers and apps, and are at least five waves ready for the migration workstream?

   1. Is there a process to update the sources? If so, what is the frequency and notification process?

## Task exit criteria
<a name="task-one-pattern-validation-exit"></a>

When you have met the following exit criteria, proceed to the next task:
+ You have validated the list of clearly defined migration patterns.
+ The source location of the migration metadata has all the required metadata for each pattern, or a process is in place to capture any missing metadata.
+ You have validated the wave plan and migration metadata for at least five waves, and you have defined a process for notifications and updates.
