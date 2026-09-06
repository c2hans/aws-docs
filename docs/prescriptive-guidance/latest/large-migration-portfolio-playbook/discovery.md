---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/discovery.html
---

# Task 1: Performing the initial discovery
<a name="discovery"></a>

The first step of portfolio assessment in a large migration project is to understand the information you have today, the business and technical drivers, and any migration strategy decisions that have already been made. The outcome of the portfolio assessment is to continuously feed the migration metadata, wave plan, and migration strategies into the migration workstream. Based on the information collected, you analyze the gaps and decide the next steps. You can skip some of the sections in this playbook if you have completed the analysis and tasks already. This task consists of the following steps:
+ [Step 1: Validate the discovery data](#discovery-1)
+ [Step 2: Identify the business and technical drivers](#discovery-2)
+ [Step 3: Validate the migration strategies](#discovery-3)
+ [Step 4: Validate the migration patterns](#discovery-4)

## Step 1: Validate the discovery data
<a name="discovery-1"></a>

In the mobilize phase, you might have completed your initial portfolio assessment, and if so, you can reuse that discovery data in the migrate phase. If not, don't worry. This playbook will walk you through what is needed to support your large migration.

Large migrations usually have a lot of data. For example, you have:
+ Metadata about the source servers, applications, and databases
+ Information about your IT portfolio from your configuration management database (CMDB)
+ Data from discovery tools that helps you better understand the current state and dependencies
+ Metadata for target AWS resources

### About the types of metadata
<a name="about-the-types-of-metadata.ab1cc618-d29e-5d21-9495-9a1d376eecf6"></a>

The following are the three primary types of metadata that are required to support a large migration:
+ **Source portfolio metadata**– Source portfolio metadata is the metadata about your source servers, applications, and databases. You can get the metadata from an existing CMDB, discovery tools, or even from the application owner. You can find a comprehensive list of this metadata type here, and the following are some examples:
  + Server name
  + Server IP address
  + Server operating system (OS)
  + Server storage, CPU, memory, and input/output operations per second (IOPS)
  + Application name
  + Application owner
  + Application-to-application dependencies
  + Business unit
  + Application-to-server mapping
  + Application-to-database mapping
  + Database type and size
  + Storage type and size
  + Dependencies metadata
  + Performance and usage data
+ **Target environment metadata **– This is a metadata type that helps you migrate the servers to the target environment. You need to make decisions about the target environment. You can get some of this metadata from discovery tools. The following are some examples of this metadata type:
  + Target subnet
  + Target security group
  + Target instance type
  + Target AWS Identity and Access Management (IAM) role
  + Target IP address
  + Target AWS account ID
  + Target AWS Region
  + Target AWS service
  + Target application architecture design
+ **Wave planning metadata **– Wave planning metadata is the metadata type that helps you manage the migration. The following are examples of this metadata type:
  + Wave ID
  + Wave start time
  + Wave cutover time
  + Wave owner
  + Wave to application/server/database/move group mapping

### Validate your discovery data
<a name="validate-your-discovery-data.cc8141c7-bfdf-5a71-80fc-897872211b7b"></a>

It is important to understand your current discovery data before making any decisions. You likely don't have all of the information at this stage of the migration. This playbook helps you define the metadata requirements and helps you collect the metadata efficiently. Ask yourself the following questions to identify what metadata is currently available and where it might be located:
+ Have you used any tools to conduct a migration assessment, such as Migration Evaluator?
+ Have you deployed any discovery tools in your environment, such as Flexera One Cloud Migration and Modernization?
+ Do you have a CMDB that has the most up-to-date information for your IT portfolio?
+ Have you finished the initial portfolio assessment in the mobilize phase?
+ Have you completed the initial wave planning?
+ Have you completed the initial target environment design?
+ What is the source of each metadata type?
+ Do you have access to all the metadata?
+ How do you access all the metadata?
+ Have you documented the process of accessing metadata?

## Step 2: Identify the business and technical drivers
<a name="discovery-2"></a>

Business and technology drivers are critical when considering the high-level migration strategies and patterns for each application. You must understand the drivers that are unique to your migration. You use these business and technical drivers when validating your migration strategies and defining application mapping rules.

### Common business drivers
<a name="common-business-drivers.f871a8e2-c4ec-57ec-9350-8b6b4556164d"></a>

*Business drivers* are factors related to business goals or limitations that you must consider when planning a large migration, such as contracts expiring, rapid growth, or budget. The following are common business drivers:
+ **Exiting a data center** – You need to migrate as quickly as possible to the cloud. For example, a data center contract is about to expire.
+ **Reducing operational cost and risks** – You want to reduce the costs or risks associated with operating an on-premises environment.
+ **Flexibility** –You need to move to the cloud as a strategic direction in order to prepare for change in the business's future.
+ **Growing the business** – You need to be able to quickly accelerate development and innovation or accommodate rapid growth.
+ **Using data intelligently** – You want to take advantage of cloud-based artificial intelligence, machine learning, and Internet of Things (IoT) that can forecast your company's growth and provide insights into customer behavior.
+ **Improving security and compliance** – You need to leverage the compliance programs that are already built into the AWS Cloud infrastructure, or you want to leverage the software-based security tools that can warn you of a possible threat to your data.
+ **Resource availability **– Having limited resources or limited internal experience might lead you to select strategies that move the application without modification.

### Common technical drivers
<a name="common-technical-drivers.bae8eda5-3bcd-5f2f-bf00-08c7f0fd9d12"></a>

*Technical drivers* are factors related to technical goals or limitations that you must consider when planning a large migration, such as the current architecture. The following are common technical drivers:
+ **Hardware or software end-of-support** – Your hardware or software is close to the end of its lifecycle, and you need to refresh it because the vendor no longer supports it.
+ **Technology integration** – You gain access to global infrastructure that enables you to rapidly and strategically scale your application. You can go global quickly with global services and infrastructure ready for you to tap.
+ **Storage and compute limitations** – Your data center does not have capacity for more storage or servers, and you need to find another place to expand.
+ **Scalability and resiliency requirements** – Your applications have experienced downtime in the past, and you want to use the cloud to improve the recovery point objective (RPO) and recovery time objective (RTO).
+ **Modernizing application architecture** – You want to take advantage of the cloud and change your applications to be cloud-native.
+ **Improving performance** – Your application performance is poor during peak seasons, you want to scale up and down automatically to match the demand.

### Update the runbook
<a name="update-the-runbook.8cfabbe4-aef8-5757-a943-5831a29fa8b3"></a>

1. Open the attached *Runbook template for application prioritization* (Microsoft Word format).

1. In the *Business and technical drivers* section, record the drivers you identified for your large migration project.

1. Save your application prioritization runbook.

## Step 3: Validate the migration strategies
<a name="discovery-3"></a>

Selecting migration strategies is critical to a large migration. You must verify that the migration strategies you select meet organizational expectations, limitations, and requirements. For more information about the available migration strategies, see the [Guide for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/welcome.html).

You might have selected migration strategies in the mobilize phase or during the initial portfolio assessment. In this step, you use the business and technical drivers in order to select and validate the migration strategies for your portfolio.

Your migration strategies might change as you continue to assess the portfolio and begin the migration. At this stage, the goal is to understand the general distribution of your portfolio to each migration strategy. Selecting migration strategies is critical to the next step, validating the detailed migration patterns.

### Select and validate the migration strategies
<a name="select-and-validate-the-migration-strategies.2f539630-63a1-5ed8-9d81-2b5160abbc26"></a>

Evaluate the portfolio and select the migration strategies as follows:

1. Review all of the technical and business drivers you identified in the previous step, and prioritize the drivers based on your business needs.

1. Map each business and technical driver to a migration strategy. The following table is an example.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/discovery.html)

1. By weighing each business and technical driver and evaluating your portfolio at a high level, estimate how the applications should be distributed amongst each migration strategy. It is common to see conflicts between the drivers. Project stakeholders need to work together and make final decisions to resolve the conflicts. The following is an example of how you might distribute your portfolio to each migration strategy:
   + Rehost – 60%
   + Replatform – 15%
   + Retire – 10%
   + Retain – 5%
   + Repurchase – 5%
   + Refactor – 5%

Do not proceed with the migration until you have selected high-level migration strategies for your portfolio.

### Update the runbook
<a name="update-the-runbook.b726ea2c-e0a0-5c40-a471-882edbb2d4a3"></a>

1. Open your application prioritization runbook.

1. In the *Migration strategies *section, record how the application workload is distributed among the seven migration strategies. For example:
   + Rehost – 60%
   + Replatform – 15%
   + Retire – 10%
   + Retain – 5%
   + Repurchase – 5%
   + Refactor – 5%

1. Save your application prioritization runbook.

## Step 4: Validate the migration patterns
<a name="discovery-4"></a>

### About migration patterns
<a name="about-migration-patterns.cb7a46f7-1b96-5d94-ba43-30db2f81195c"></a>

A *migration pattern* is a repeatable migration task that details the migration strategy, the migration destination, and the migration application or service used. An example is *Rehost to Amazon Elastic Compute Cloud (Amazon EC2) using AWS Transform MGN*. The following AWS services and solutions are frequently referenced in common migration patterns:
+ AWS App2Container
+ AWS Transform MGN (AWS MGN)
+ AWS CloudFormation
+ AWS Database Migration Service (AWS DMS)
+ AWS DataSync Discovery
+ Amazon Elastic Compute Cloud (Amazon EC2)
+ Amazon Elastic Container Service (Amazon ECS)
+ Amazon Elastic File System (Amazon EFS)
+ AWS Cloud Migration Factory Solution
+ Amazon Relational Database Service (Amazon RDS)
+ AWS Schema Conversion Tool (AWS SCT)
+ AWS Transfer Family

Similar to selecting migration strategies, you might have already identified your migration patterns in an earlier phase. However, you must validate them and make sure the patterns have been defined and documented. The following table lists common migration strategies and patterns.

|
|
| ID | Strategy | Pattern |
| --- |--- |--- |
| 1 | Rehost | Rehost to Amazon EC2 using MGN or Cloud Migration Factory |
| 2 | Replatform | Replatform to Amazon RDS using AWS DMS and AWS SCT |
| 3 | Replatform | Replatform to Amazon EC2 using AWS CloudFormationCloudFormation templates build new infrastructure in the AWS Cloud. |
| 4 | Replatform | Replatform to Amazon EFS using AWS DataSync Discovery or AWS Transfer Family |
| 5 | Replatform | Replatform to Amazon ECS using AWS App2Container |
| 6 | Replatform | Replatform mainframe or midrange servers to Amazon EC2 using an emulator |
| 7 | Replatform | Replatform from Windows to Linux on Amazon EC2 |
| 8 | Retire | Retire the application |
| 9 | Retain | Retain on premises |
| 10 | Repurchase | Repurchase and upgrade to SaaS |
| 11 | Refactor or re-architect | Re-architect the application |

### Update the runbook
<a name="update-the-runbook.6490585b-445f-50f8-8b7c-16a9c2999a5d"></a>

At this point, you define the patterns at the portfolio level. Later in this playbook, you map each application to its corresponding migration pattern.

1. Open your application prioritization runbook.

1. In the* Migration patterns* section, record the migration patterns you have identified and validated. Assign each pattern a unique ID and note the migration strategy for the pattern.

1. Save your application prioritization runbook.

Note that migration patterns might change as you progress. You might change your migration strategies and patterns later, as you find new information, change the scope of the workload, or even decide to use new AWS services.

## Task exit criteria
<a name="discovery-exit-criteria"></a>

If you have not yet identified your migration strategies and patterns from a high-level, portfolio perspective, we highly recommend you work with the technical teams to define them before moving on to the next task. Portfolio assessment and wave planning are dependent on understanding the migration strategies and patterns. You do not need to have a comprehensive list of migration patterns before you proceed. You can add new patterns and adjust your strategies as you go.

Continue to the next task when you have completed the following:
+ You have access to the latest discovery data and understand it.
+ You have identified the business and technical drivers for your migration.
+ You have selected and validated migration strategies, based on your business and technical drivers.
+ You have selected and validated migration patterns.
+ You have documented the following in your application prioritization runbook:
  + Business and technical drivers
  + Migration strategies
  + Migration patterns
