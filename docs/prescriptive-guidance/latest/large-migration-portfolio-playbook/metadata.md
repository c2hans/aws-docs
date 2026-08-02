---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/metadata.html
---

# Task 2: Defining metadata processes
<a name="metadata"></a>

In the previous task, you validated the initial discovery data, the migration strategies, and the migration patterns for your large migration. In this task, you identify what metadata is required and decide how you will collect it. This task consists of the following steps:
+ [Step 1: Define the required metadata](#metadata-1)
+ [Step 2: Build the metadata storage and collection processes](#metadata-2)
+ [Step 3: Document metadata requirements and collection processes in a runbook](#metadata-3)

As you complete the steps in this section, consider the entire migration cycle from a metadata perspective. Consider portfolio assessment, wave planning, migration, testing, post-cutover activities, and then analyze all possible use cases and related use cases. Thinking about the information that you need to complete the full migration process helps you identify all of the metadata for that pattern.

## Step 1: Define the required metadata
<a name="metadata-1"></a>

Before you can determine the required metadata attributes, you must understand the migration pattern. For example, you need different metadata for migrating a server to Amazon EC2 and for migrating a database to Amazon RDS. Most patterns are made up of many small tasks. In order to perform the migration pattern, you need to know what metadata attributes are required and then collect the metadata for that application. You must determine and gather the required metadata in the initialization stage so that you can perform the migration efficiently and without delay in the implementation stage.

The person or team that defines the metadata attributes begins by defining the steps and tasks needed to perform the migration pattern. The tasks determine what metadata is needed, so working through each task builds a comprehensive collection of the required metadata. The person who determines what metadata is required typically needs to have a comprehensive understanding of how to complete the migration pattern. Coordination with the person writing the migration runbook might be required. For more information, see the [Migration playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/welcome.html).

During a large migration, there are many processes spread across all workstreams that have a dependency on metadata. Having timely and accurate metadata has broad and significant impact to the success of a large migration.

In this step, you define the pattern or task and then use the definition to identify the metadata required.

### Identify the key components of the migration patterns and supporting tasks
<a name="identify-the-key-components-of-the-migration-patterns-and-supporting-tasks.8dac77f9-0f27-51ac-a4c6-1218eeb98b61"></a>

In this step, for each migration pattern or supporting task, you define the key components, such as the action, source object, target object, and tools used. You then name the pattern or task based on your answers.

*Supporting tasks* include the operational activities that the portfolio and migration workstreams need to perform during the migration, such as wave planning, application prioritization, dependency analysis, governance, disaster recovery, performance testing, or user-acceptance testing. Because you need metadata to support these tasks, you perform these steps for both the migration patterns and the supporting tasks.

1. **Action**– Identify the migration strategy or supporting task. Remember that one action might have other actions associated with it. For example, you might want to define operations for migration. Example actions include:
   + Migration strategy, such as rehost, replatform, or relocate
   + Wave planning
   + Application prioritization and dependency analysis
   + Operation
   + Governance
   + Disaster recovery
   + Testing, such as performance testing or user-acceptance testing (UAT)

1. **Source object**– Identify the source object on which the action will be performed. Example source objects include:
   + Waves
   + Server
   + Database
   + File share
   + Application

1. **Tools**– Identify the services or tools used to perform the action. You might use more than one tool or service. Example tools include:
   + AWS Transform MGN
   + AWS DataSync
   + AWS Database Migration Service (AWS DMS)
   + AWS Backup
   + Performance monitoring tools

1. **Target object**– Identify the target object, service, or location where the source will reside when the action is complete. Example objects, services, or locations include:
   + Amazon Elastic Compute Cloud (Amazon EC2)
   + Amazon Relational Database Service (Amazon RDS)
   + Amazon Elastic File System (Amazon EFS)
   + Amazon Elastic Container Service (Amazon ECS)
   + Wave plan

1. **Pattern name** – Combine your answers to the previous steps as follows:

   <action> <source object> on/to <target object> using <tool>

   The following are examples:
   + Rehost (action) waves, applications, or servers (source object) to Amazon EC2 (target object) using MGN or Cloud Migration Factory (tools)
   + Replatform (action) file shares (source object) to Amazon EFS (target object) using DataSync (tool)
   + Replatform (action) databases (source object) to Amazon RDS (target object) using AWS DMS (tool)
   + Performance monitoring (action) of applications (source object) on Amazon EC2 (target object) using Amazon CloudWatch (tool)
   + Back up (action) servers (source object) on Amazon EC2 (target object) using AWS Backup (tools) after migration
   + Wave planning (action) waves, applications, or servers (source object) to create a wave plan (target object)

The following is an example of how you might record *Pattern 1: Rehost to Amazon EC2 using MGN or Cloud Migration Factory* from the migration patterns table.

|  |
| --- |
| Pattern ID | 1 |
| --- |--- |
| **Pattern name** | Rehost to Amazon EC2 using MGN or Cloud Migration Factory |
| **Action** | Rehost migration |
| **Source object** | Waves, applications, or servers |
| **Tools** | MGN or Cloud Migration Factory |
| **Target object** | Amazon EC2 |

### Determine the metadata required for each pattern or task
<a name="determine-the-metadata-required-for-each-pattern-or-task.69f10ea8-7355-5ae5-a1a7-5076512bf79a"></a>

Now that you have defined the pattern or task, you determine the metadata required for the source object, target object, tools, and other business information. To explain this process, this playbook uses *Pattern 1: Rehost to Amazon EC2 using MGN or Cloud Migration Factory* from the migration patterns table as an example. Note that for some patterns or tasks, some steps might not apply.

1. **Analyze the target object –**Working backwards from the target object, manually create the object and identify the metadata needed to support it. Capture the metadata as demonstrated in the following table.

   For example, when you create an EC2 instance, you must choose an instance type, storage type, storage size, subnet, security group, and tags. The following table includes examples of metadata attributes that you might need if your target object is an EC2 instance.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/metadata.html)

1. **Analyze the tools –** Use the tool to create a target object and check for differences. Capture the tool-specific metadata as demonstrated in the following table, and remove the attributes from the previous table if it is not supported by the migration tool. For example, you cannot customize the OS type and storage size for MGN because the rehost migration tool is like-for-like. Therefore, you would remove target OS and target disk size if these attributes were included in the previous table. In the previous example table, all attributes are supported by the tool, so no action is required.

   The following table includes examples of metadata that you might need for the tools.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/metadata.html)

1. **Analyze the source object** – Determine the required metadata for the source object by assessing the actions as follows:
   + To migrate servers, you need to know the source server name and fully qualified domain name (FQDN) in order to connect to the server.
   + To migrate applications along with their servers, you need to know the application name, application environment, and application-to-server mapping.
   + To perform a portfolio assessment, prioritize applications, or define a move group, you need to know the application-to-server mapping, application-to-database mapping, and application-to-application dependencies.
   + To manage waves, you need to know the wave ID and the start and end times of the wave.

   The following table includes examples of metadata that you might need for the source object.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/metadata.html)

1. **Consider other attributes –** In addition to the primary action, consider other actions and attributes related to the target object or application. For the example pattern, *Pattern 1: Rehost to Amazon EC2 using MGN or Cloud Migration Factory*, the action is rehost, and the target object is Amazon EC2. Other related actions for this target object might include backing up to Amazon EC2, monitoring the EC2 instance after the migration, and using tags to manage costs associated with the EC2 instance. You might also want to consider other application attributes that help you manage the migration, such as the application owner, who you might need to contact for questions or cutover purposes.

   The following table includes examples of additional metadata that are commonly used. This table includes tags for your target EC2 instance. For more information about tags and how to use them, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the Amazon EC2 documentation.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/metadata.html)

1. **Create a table** – Combine all of the metadata identified in the previous steps into a single table.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/metadata.html)

1. **Repeat** – Repeat this process until you have documented the required metadata for each pattern.

## Step 2: Build the metadata storage and collection processes
<a name="metadata-2"></a>

In the previous step, you defined the metadata required to support your migration. In this step, you build a process for collecting and storing the metadata. This step consists of two tasks:

1. Analyze the required metadata from the previous step and identify the source.

1. Define a process for efficiently storing and collecting the metadata.

### Analyze the metadata sources
<a name="analyze-the-metadata-sources.9eefd459-d5d0-5da3-8770-23634fdeb289"></a>

There are many common metadata sources. Usually, the first thing you can access is a high-level asset inventory, which is typically exported from a configuration management database (CMDB) or from another existing tool. However, you need to collect metadata from other sources as well, using both automated and manual processes.

The following table contains common sources, the standard collection process for that source, and the common metadata types that you can expect to find from that source.

|
|
| Metadata source | Collection type | Metadata type |
| --- |--- |--- |
| Discovery tools | Automated | Source server |
| CMDB | Automated | Source server |
| Inventory from other tools, such as [RVTools](https://www.robware.net/) for VMware vSphere | Automated | Source server |
| Application owner questionnaire | Manual | Source server, target server, wave |
| Application owner interview | Manual | Source server, target server, wave |
| Application design documentation | Manual | Target server |
| Landing zone design documentation | Manual | Target server, tools |

After listing all the possible sources of your metadata, you analyze the metadata type and map each source to the metadata attributes that you identified in the previous step.

1. Get a complete list of metadata attributes from [Step 1: Define the required metadata](#metadata-1).

1. Analyze each metadata type and determine which types cannot be retrieved using an automated process. This is usually the **target server metadata** and **wave metadata** types because these require decisions from the application owners. For example, which subnet and security group will you use for the target EC2 instances?

1. Analyze each metadata attribute and map it to a metadata source in the previous table. It is common to have a combination of multiple sources. You can use discovery tools to collect some source server metadata. For information about using discovery tools to collect metadata, see [Get started with automated portfolio discovery](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/get-started-with-automated-portfolio-discovery.html) on the AWS Prescriptive Guidance website.

1. Create a table to map the metadata attribute to its type and source. The following table is an example.

|
|
| Metadata attribute | Metadata type | Metadata sources |
| --- |--- |--- |
| app\_name | Source application | CMDB |
| app\_owner | Source application | CMDB |
| app\_to\_server\_mapping | Source application | CMDB, discovery tools, or application owner questionnaire |
| app\_to\_DB\_mapping | Source application | CMDB, discovery tools, or application owner questionnaire |
| app\_to\_app\_dependencies | Source application | CMDB, discovery tools, or application owner questionnaire |
| server\_name | Source server | CMDB |
| server\_FQDN | Source server | CMDB |
| server\_OS\_family | Source server | CMDB |
| server\_IP | Source server | Discovery tools |
| disk\_size | Source server | Discovery tools |
| instance\_type | Target server | Discovery tools |
| target\_subnet | Target server | Application owner questionnaire |
| target\_security\_group | Target server | Application owner questionnaire |
| AWS\_Region | Target server | Application owner questionnaire |
| AWS\_account\_ID | Target server | Application owner questionnaire |
| replication\_server\_subnet | Tools (Application Migration Service) | Landing zone design documentation |
| replication\_server\_security\_group | Tools (Application Migration Service) | Landing zone design documentation |
| Name | Target server (tag) | Application owner questionnaire |
| business\_unit | Target server (tag) | Application owner questionnaire |
| cost\_center | Target server (tag) | Application owner questionnaire |
| wave\_ID | Wave planning | Application owner interview |
| wave\_start\_date | Wave planning | Application owner interview |
| wave\_cutover\_date | Wave planning | Application owner interview |

### Define a single metadata store
<a name="define-a-single-metadata-store.88b9b992-4a21-57ba-85c3-88bd9cc6cb1a"></a>

After mapping each metadata attribute to its source, you define where to store the metadata. Regardless of how and where you store the metadata, you need to choose only one repository. This ensures that you have a single source of truth. Storing metadata in multiple places is a common mistake in large migrations.

#### Option 1: Store metadata in a spreadsheet in a shared repository
<a name="option-1--store-metadata-in-a-spreadsheet-in-a-shared-repository.0a80b46a-5df1-54cc-a19d-790d320597de"></a>

Although this option might sound like a very manual process, it is the most common data store for large migrations. It is also common to store the spreadsheet in a shared repository, such as a Microsoft SharePoint site.

A Microsoft Excel spreadsheet is easy to customize and doesn't take a long time to build. The disadvantages are that it will get very complex if you have a lot of metadata and that it can be difficult to manage the relationships between assets, such as between the server, application, and database. The other challenge is version management. You need to limit write access to only a few people, or you need to use an automated process to update the spreadsheet.

You can use the attached *Dashboard template for wave planning and migration *(Excel format) as a starting point for building your own data store spreadsheet.

#### Option 2: Store metadata in a purpose-built tool
<a name="option-2--store-metadata-in-a-purpose-built-tool.315721fe-224f-53dc-80f2-33f3660eec6c"></a>

You can use a prebuilt tool, such as [TDS Transition Manager](https://www.transitionaldata.com/software/) (TDS website), to store your data, or you can build your own tool. When you build your own tool, you need database tables just like Excel spreadsheet tabs in option 1. For example:
+ Server table
+ Application table
+ Database table
+ Application-to-server and application-to-database mapping table
+ Wave-planning table
+ Application owner questionnaire table

### Define the metadata collection processes
<a name="define-the-metadata-collection-processes.cdaf2c10-eeb8-5019-a1a1-7e89ec3c9298"></a>

In the previous steps, you mapped the metadata to its source and defined a data store where you will collect the metadata. In this step, you build processes to effectively collect the metadata. You should minimize the manual copy-and-paste process and use automation to collect the metadata from each source. There are three steps:

1. Build an extract, transform, and load (ETL) script for each metadata source based on the metadata mapping table.

1. Build a scheduled task that imports metadata from each source automatically on a regular basis.

1. Build an export process or provide application programming interface (API) access to the metadata stored in the repository.

The following table is an example of the metadata attributes collected by each ETL script. The metadata is stored in the location you defined in the previous section, such as a spreadsheet or purpose-built tool.

|
|
| Metadata attribute | Metadata type | Metadata source | Collection process |
| --- |--- |--- |--- |
| app\_name | Source application | CMDB | ETL script – CMDB |
| app\_owner | Source application | CMDB | ETL script – CMDB |
| app\_to\_server\_mapping | Source application | CMDB | ETL script – CMDB |
| app\_to\_DB\_mapping | Source application | CMDB | ETL script – CMDB |
| app\_to\_app\_dependencies | Source application | Discovery tool | ETL script – discovery tool |
| server\_name | Source server | CMDB | ETL script – CMDB |
| server\_FQDN | Source server | CMDB | ETL script – CMDB |
| server\_OS\_family | Source server | CMDB | ETL script – CMDB |
| server\_OS\_version | Source server | CMDB | ETL script – CMDB |
| disk\_size | Source server | Discovery tool | ETL script – discovery tool |
| instance\_type | Target server | Discovery tool | ETL script – discovery tool |
| target\_subnet | Target server | Application owner questionnaire | ETL script – application owner |
| target\_security\_group | Target server | Application owner questionnaire | ETL script – application owner |
| AWS\_Region | Target server | Application owner questionnaire | ETL script – application owner |
| AWS\_account\_ID | Target server | Application owner questionnaire | ETL script – application owner |
| Name | Target server (tag) | Application owner questionnaire | ETL script – application owner |
| business\_unit | Target server (tag) | Application owner questionnaire | ETL script – application owner |
| cost\_center | Target server (tag) | Application owner questionnaire | ETL script – application owner |
| wave\_ID | Wave planning | Application owner interview | ETL script – application owner |
| wave\_start\_date | Wave planning | Application owner interview | ETL script – application owner |
| wave\_cutover\_date | Wave planning | Application owner interview | ETL script – application owner |

## Step 3: Document metadata requirements and collection processes in a runbook
<a name="metadata-3"></a>

In this task, you document your decisions in a *metadata management runbook*. During the migration, your portfolio workstream adheres to this runbook as the standard procedures for collecting and storing metadata.

1. Open the attached *Runbook template for metadata management* (Microsoft Word format). This serves as a starting point for building your own runbook.

1. In the *Metadata attributes* section, create a metadata attributes table for each migration pattern, and populate the tables with the metadata attributes identified in [Step 1: Define the required metadata](#metadata-1).

1. In the *Source locations* section, document the sources you identified in [Step 2: Build the metadata storage and collection processes](#metadata-2).

1. In the *Source location access instructions* section, document the steps a user would need to follow in order to access the metadata source locations.

1. In the *Metadata store* section, document the steps a user would need to follow in order to access the metadata store you created in [Step 2: Build the metadata storage and collection processes](#metadata-2).

1. In the *Data collection types* section, identify the data collection process that you will use for each metadata source. Ideally, you should automate all metadata collection by using automation scripts.

1. In the *Data collection by metadata attribute *section, for each metadata attribute, identify the following according to the instructions in [Step 2: Build the metadata storage and collection processes](#metadata-2):
   + Metadata type
   + Metadata source
   + Metadata store
   + Collection type

1. In the *Collect metadata* section, update the process as needed for your use case. This is the process the portfolio workstream follows in the implementation stage when they collect metadata for waves.

1. Verify that your runbook is complete and accurate. This runbook should be a source of truth during the migration.

1. Share your metadata management runbook with the team for review.

## Task exit criteria
<a name="metadata-exit-criteria"></a>

Continue to the next task when you have completed the following:
+ You have prepared a single repository for storing the collected metadata.
+ In your metadata management runbook, you have defined and documented the following:
  + The metadata attributes required for each migration pattern
  + Metadata sources and detailed instructions for how to access each source
  + The metadata store and detailed instructions for how to access it
  + The processes used to collect metadata
  + A mapping table that maps metadata attributes to the metadata sources and collection processes
