---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-microsoft-workloads-aws/tools-programs-training.html
---

# Migration tools, programs, and training
<a name="tools-programs-training"></a>

This section outlines AWS and AWS Partner tools available to assist with your cloud migration, the training opportunities available to provide your team with the skills they need for migrating to and operating in the cloud, and key migration programs available to accelerate your migration journey and reduce migration costs.

## Tools
<a name="tools"></a>

### Assessment tools
<a name="assessment-tools.8af3d67f-70ea-58a4-8d86-d763f719d1dd"></a>

#### AWS Optimization and Licensing Assessment
<a name="9999999999999999aws--optimization-and-licensing-assessment.43d479ca-1818-547b-8e06-0e4a2d6c5918"></a>

We recommend that use the [AWS Optimization and Licensing Assessment (AWS OLA)](https://aws.amazon.com/optimization-and-licensing-assessment/) to build your migration and licensing strategy on AWS. You can use the AWS OLA to evaluate your Windows environment. The evaluation helps you to identify potential savings on your licensing costs and discover ways to run your resources more efficiently.

AWS OLA is an obligation free program for new and existing customers. You can use AWS OLA to assess and optimize your current on-premises and cloud environments, based on actual resource utilization, third-party licensing, and application dependencies. A third-party study in 2022 by the [Enterprise Strategy Group and Evolve Cloud Services](https://evolvecloudservices.com/esg-whitepaper) calculated that AWS OLA saves customers an average of 45 percent on Microsoft SQL Server licensing costs and 77 percent on Windows Server. Licensing costs equal three times the cost of actually running these workloads in the AWS Cloud so potential savings can have a significant impact on your TCO.

AWS OLA provides you with a report that models your deployment options. These results can help you explore available cost savings across the flexible licensing options offered by AWS. You can also use AWS OLA in combination with [AWS Migration Acceleration Program for Windows](https://aws.amazon.com/windows/map-for-windows/) to get support and resources during your cloud migration.

You can use AWS OLA before, during, or even after your migration. This tool-based approach can help you determine your actual utilization requirements. The AWS OLA makes recommendations for the lowest cost EC2 instance size and type for each workload. It can also help you find the right blend of On-Demand Instances, Spot Instances, Amazon EC2 Dedicated Hosts, savings plans, and other options specific to your environment. Additionally, the AWS OLA provides you with a migration plan, directional business case, and roadmap.

Licensing savings are a significant part of your TCO, and AWS OLA can help you reduce licensing costs by providing Bring Your Own License (BYOL) or license included recommendations based on your existing licensing entitlements and workloads. AWS OLA optimizes your licenses by configuring instances to require fewer licenses while retaining high performance for your applications. AWS OLA also helps you to understand the differences between on-premises licensing compared to licensing in the cloud. You can use this knowledge to adapt your licensing strategy to further reduce costs in the future.

The scope of AWS OLA includes the following use cases:
+ Directional business case, recommendation outlining EC2 instance costs, and configurations based on actual on-premises utilization and data
+ Dedicated Host modeling for Host-level licensing
+ Virtual CPU (vCPU) reduction for SQL instance optimization and consolidation
+ On-premises TCO estimations based on industry averages
+ Modeling VMware Cloud on AWS
**Note**
As of April 30, 2024, VMware Cloud on AWS is no longer resold by AWS or its channel partners. The service will continue to be available through Broadcom. We encourage you to reach out to your AWS representative for details.
+ Recommendations based on your Microsoft license position (regarding license mobility and potential reduction)
+ License impact modelling for T3 Dedicated Hosts
+ SQL and Oracle modelling on Amazon Relational Database Service (Amazon RDS), edition optimization, and analysis of Oracle Real Application Clusters (RAC) and Oracle Exadata
+ Active and passive modeling for SQL high availability license impact
+ Modernization assessment

AWS uses the internal [Migration Evaluator](https://aws.amazon.com/migration-evaluator/) or trusted tools from third-party vendors (or qualified AWS OLA migration partners) to conduct broad-based discovery or securely upload exports if you have an existing inventory. The tool that's used depends on your specific needs and requirements. AWS uses discovery tool outputs and combines them with expert recommendations from third-party licensing consultants to give you an optimized TCO that you can trust.

For more information, see the following resources:
+ [AWS Optimization and Licensing Assessment](https://aws.amazon.com/optimization-and-licensing-assessment/) (AWS documentation)
+ [Optimize Your Windows Workloads for AWS - AWS Online Tech Talks](https://www.youtube.com/watch?v=DsCgx-A8Djs) (YouTube)
+ [Run Optimization and Licensing Assessment](https://pages.awscloud.com/windows-ola-contact-us.html) (AWS documentation)

#### AWS Migration Hub Strategy Recommendations
<a name="9999999999999999mhsrlong-.59e3125a-7e5d-56d5-a9fe-1d64cbdce18f"></a>

[AWS Migration Hub Strategy Recommendations](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/what-is-mhub-strategy.html) helps you plan migration and modernization initiatives by offering migration and modernization strategy recommendations for viable transformation paths for your applications. Strategy Recommendations performs an analysis of your server inventory and runtime environment. It can also perform source code and database analysis. Strategy Recommendations combines this analysis with your business goals, and the transformation preferences of the applications and databases provided to recommend the following:
+ The most effective migration strategy for each of your applications
+ Migration and modernization tools or programs that you can use
+ Application incompatibilities and anti-patterns to resolve for a specific option

Strategy Recommendations recommends migration and modernization strategies for rehosting, replatforming, and refactoring with associated deployment destinations, tools, and programs. For example, Strategy Recommendations might recommend straightforward options, such as rehosting on Amazon EC2 by using AWS Transform MGN. More optimized recommendations might include replatforming to containers by using AWS App2Container or refactoring to open-source technologies such as .NET Core and PostgreSQL.

To use Strategy Recommendations, follow the instructions in [Getting started with Strategy Recommendations](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/getting-started.html).

#### Migration Validator Toolkit PowerShell module
<a name="migration-validator-toolkit-powershell-module.d1dbf80d-ee1a-5d08-9417-ed80f8aada42"></a>

We recommend that you use the [Migration Validator Toolkit PowerShell module](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/accelerate-the-discovery-and-migration-of-microsoft-workloads-to-aws.html) to discover and migrate your Microsoft workloads to AWS. The module works by performing multiple checks and validations for common tasks associated with any Microsoft workload. The Migration Validator Toolkit PowerShell module can help your organization reduce the time and effort involved in discovering what applications and services are running on your Microsoft workloads. The module can also help you identify the configurations of your workloads so that you can find out if your configurations are supported on AWS. The module also provides recommendations for next steps and mitigation actions, so that you can avoid any misconfigurations before, during, or after your migration.

#### AWS Cloud Readiness Assessment
<a name="9999999999999999aws--cloud-readiness-assessment.466a3f39-ce2d-5e2e-b7fc-642ea414b9dd"></a>

We recommend that you use the [AWS Cloud Readiness Assessment](https://cloudreadiness.amazonaws.com/#/cart) to transform your idea of moving to the cloud into a detailed plan that follows AWS Professional Services best practices. You can use the AWS Cloud Readiness Assessment to develop efficient and effective plans for cloud adoption and enterprise cloud migrations, regardless of the size of your organization. This 16-question online survey and assessment report details your cloud migration readiness across six perspectives, including business, people, process, platform, operations, and security.

After you complete an assessment, you can provide your contact details to download a customized cloud migration assessment that charts your readiness and what you can do to improve it. Your summary report includes a heatmap and radar chart with detailed scoring information and resources to help you improve your readiness score. This take-away report cab help you plan and communicate with your stakeholders. For a sample assessment report, see [AWS Cloud Adoption Readiness Assessment Report](https://cloudreadiness.amazonaws.com/bfd2391ccfbac30513c6cc8b5c40e3ae.pdf). To take the assessment, go to the [AWS Cloud Adoption Readiness Assessment](https://cloudreadiness.amazonaws.com/#/cart/assessment).

### Migration tools
<a name="migration-tools.bc3c1678-0b38-5aff-b12a-25c6bafe36c0"></a>

#### AWS Migration Hub
<a name="9999999999999999mhblong-.2ddb1df9-e65e-59ec-8d72-c5bb6b34aa9f"></a>

[AWS Migration Hub](https://aws.amazon.com/migration-hub/) provides a central location to collect server and application inventory data for the assessment, planning, and tracking of migrations to AWS. Migration Hub can also help you accelerate application modernization following migration. Migration Hub network visualization enables you to accelerate migration planning by quickly identifying servers and their dependencies, identifying the role of a server, and grouping servers into applications. To use network visualization, install [AWS Application Discovery Agent](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-agent.html), and then start data collection.

#### AWS Migration Hub Orchestrator
<a name="9999999999999999mholong-.4a4508c0-c4bb-5a73-be79-c5cdff5719f0"></a>

[AWS Migration Hub Orchestrator](https://aws.amazon.com/migration-hub/features/) helps accelerate your application migration to reduce the time and effort of the migration. You can use predefined workflow templates to easily create a migration workflow, customize your workflow per your specific needs, automate the migration steps, and track the migration progress from start to finish in one place. Migration Hub Orchestrator supports the following:
+ Migration of applications based on SAP NetWeaver with SAP HANA databases
+ Rehosting of any applications to Amazon EC2
+ Rehosting of SQL Server databases to Amazon EC2
+ Replatforming of SQL Server databases to Amazon RDS
+ Importing VM images of an Open Virtual Appliance (OVA) or VMware Virtual Machine Disk (VMDK) to an AMI for Amazon EC2

#### AWS Migration Hub dashboard
<a name="9999999999999999mhblong--dashboard.98677d0e-d41c-5905-9fa1-d59c44a76f2f"></a>

The [Migration Hub dashboard](https://aws.amazon.com/migration-hub/features/) shows the latest status and metrics for your rehost and replatform migrations. You can use the dashboard to quickly understand the progress of your migrations and identify and troubleshoot any issues. Migration Hub lets you track the status of your migrations into any AWS Region supported by your migration tools. Regardless of which Regions you migrate into, the migration status appears in Migration Hub when using an integrated tool.

#### AWS Transform MGN
<a name="9999999999999999mgnlong-.06df98e4-a51f-5840-98e3-e062bb450660"></a>

[AWS Transform MGN](https://aws.amazon.com/application-migration-service/) minimizes time-intensive, error-prone manual processes by automating the conversion of your source servers to run natively on AWS. It also simplifies application modernization with built-in and custom optimization options. The use cases for MGN include the following:
+ On-premises workloads such as SAP, Oracle, and SQL Server running on physical servers or on VMware vSphere, Microsoft Hyper-V, and other on-premises infrastructure
+ Cloud-based workloads running from other public clouds to AWS

You can use MGN to access over 200 services that reduce costs, increase availability, and facilitate innovation. Additionally, you can use it to move your Amazon EC2 workloads between AWS Regions, Availability Zones, or accounts more easily to meet your business, resilience, and compliance needs.

Alternatively, as a modernization strategy you can optimize your applications by applying custom modernization actions or selecting built-in actions such as cross-Region disaster recovery, CentOS conversion, and SUSE Linux subscription conversion.

#### AWS Database Migration Service
<a name="9999999999999999dmslong-.a22fad98-504e-580a-8922-a878e5fc494b"></a>

[AWS Database Migration Service (AWS DMS)](https://aws.amazon.com/dms/) is a managed migration and replication service that helps move your database and analytics workloads to AWS quickly, securely, and with minimal downtime and zero data loss. AWS DMS supports migration between 20-plus database and analytics engines, including SQL Server.

AWS DMS enables you to use a managed databases model to migrate from legacy or on-premises databases to managed cloud services through a simplified migration process, which gives developers time to innovate. You can also use AWS DMS to break free from licensing costs, accelerate business growth, and use purpose-built databases to innovate and build faster for any use case at scale for one-tenth the cost.

You can also use AWS DMS to do the following:
+ Replicate backup files
+ Create redundancies of business-critical databases and data stores to minimize downtime and data loss
+ Build data lakes to perform real-time processing on change data from your data stores
+ Integrate data marts by building data lakes
+ Perform real-time processing on change data from your data stores

### Migration Partner tools
<a name="migration-partner-tools.52632f6e-a469-57ac-b67f-ef4ab41cbfac"></a>

#### CloudBasix
<a name="cloudbasix.aef7eb2d-e836-5dd6-ad26-e56f878c84a9"></a>

[CloudBasix](https://cloudbasic.net/about/) makes cloud-native workload optimization and data integration products. You can use its flagship product, [CLOUDBASIX for RDS SQL Server Read Replicas and Disaster Recovery (DR)](https://aws.amazon.com/marketplace/pp/prodview-fwh7aybhloazy), to enable the following:
+ In-Region read replicas
+ Cross-Region DR
+ Inter-cloud Azure to AWS disaster recovery
+ AI-driven data lakes and data houses
+ Integration for Amazon Redshift and Snowflake

### Management tools
<a name="management-tools.f9436154-7f1d-56e9-b614-5430f6be4624"></a>

#### Amazon CloudWatch Application Insights
<a name="9999999999999999ailong-.85c26809-c360-5167-9c5c-5b4621e693a6"></a>

[Amazon CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html) facilitates observability for your applications and underlying AWS resources. It helps you set up the best monitors for your application resources to continuously analyze data for signs of problems with your applications. CloudWatch Application Insights, which is powered by Amazon SageMaker AI and other AWS technologies, provides automated dashboards that show potential problems with monitored applications. This can help you quickly isolate ongoing issues with your applications and infrastructure.

When you add your applications to CloudWatch Application Insights, it scans the resources in the applications and recommends and configures metrics and logs on CloudWatch for application components. Example application components include SQL Server backend databases and Microsoft IIS or web tiers. CloudWatch Application Insights analyzes metric patterns using historical data to detect anomalies and continuously detects errors and exceptions from your application, operating system, and infrastructure logs. It correlates these observations using a combination of classification algorithms and built-in rules. Then, CloudWatch Application Insights automatically creates dashboards that show the relevant observations and problem severity information to help you prioritize your actions. For common problems in .NET and SQL application stacks—such as application latency, SQL Server failed backups, memory leaks, large HTTP requests, and canceled I/O operations—it provides additional insights that point to a possible root cause and steps for resolution. Built-in integration with [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) enables you to resolve issues by running the relevant Systems Manager Automation document.

#### AWS License Manager
<a name="9999999999999999liclong-.970ce7b2-b193-555b-9c5f-29847b246147"></a>

[AWS License Manager](https://aws.amazon.com/license-manager/) makes it easier for you to manage your software licenses from vendors, such as Microsoft, SAP, Oracle, and IBM, across AWS and your on-premises environments. You can use License Manager to streamline license management by switching between license types and automating the discovery, tracking, and reporting of existing licenses. You can also simplify the windows BYOL experience through the managing of a collection of Amazon EC2 Dedicated Hosts as a single entity with automated allocation, release, and recovery. Additionally, you can handle marketplace licenses across accounts by automating the distribution and activation of software entitlements and workloads across AWS accounts for end users.

#### AWS Backup
<a name="9999999999999999bkplong-.4db0e2dd-516b-5c47-8e5d-8831321eddeb"></a>

[AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) is a cost-effective, fully managed, policy-based service that simplifies data protection at scale. You can use AWS Backup to make cloud-native backups for key data stores, such as your buckets, volumes, databases, and file systems across AWS services. AWS Backup centralizes your data's protection by providing data protection management for your applications running in hybrid environments, such as VMware workloads and AWS Storage Gateway volumes. You can also centrally manage polices for configuring, managing, and governing your backup activity across your organization's AWS accounts, resources, and AWS Regions.

#### AWS Systems Manager Fleet Manager
<a name="9999999999999999syslong--fleet-manager.995d1b30-7461-5ea7-bce3-ad51889d72ee"></a>

[Fleet Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet.html), a capability of AWS Systems Manager, is a unified user interface (UI) experience that helps you remotely manage your nodes running on AWS or on premises. With Fleet Manager, you can view the health and performance status of your entire server fleet from one console. You can also gather data from individual nodes to perform common troubleshooting and management tasks from the console. This includes connecting to Windows instances by using the Remote Desktop Protocol (RDP), viewing folder and file contents, Windows registry management, operating system user management, and more. You can use Fleet Manager if you want to centralize the management of your node fleet or your Amazon Elastic Container Service (Amazon ECS) clusters.

## Programs
<a name="programs"></a>

### AWS Migration Acceleration Program
<a name="9999999999999999aws--migration-acceleration-program.09820661-0ab9-5d90-af05-e6f0f1cdc0ff"></a>

The AWS[ Migration Acceleration Program (MAP)](https://aws.amazon.com/migration-acceleration-program/) is a comprehensive and proven cloud migration program based upon AWS experience migrating thousands of enterprise customers to the cloud. Enterprise migrations can be complex and time-consuming, but MAP can help you accelerate your cloud migration and modernization journey with an outcome-driven methodology.

MAP provides tools that reduce costs and automate and accelerate implementation, tailored training approaches and content, expertise from Partners in the AWS Partner Network, a global partner community, and AWS investment. MAP also uses a proven three-phased framework to help you achieve your migration goals. Through MAP, you can build strong AWS cloud foundations while reducing risk, boosting productivity, improving operational resilience, and offsetting the initial cost of migrations. You can also take advantage of the performance, security, and reliability of the cloud.

### AWS Windows Migration Accelerator
<a name="9999999999999999aws--windows-migration-accelerator.664b4ea5-b7a2-52c4-b987-933129157855"></a>

[AWS Windows Migration Accelerator](https://aws.amazon.com/application-migration-service/windows/) helps reduce the cost of your migration by using AWS Promotional Credit when you accelerate the migration of Windows servers using [AWS Transform MGN](https://aws.amazon.com/application-migration-service/). AWS Windows Migration Accelerator incentives can be applied on top of other agreed upon sales incentives and promotional programs. If you use MGN to migrate at least 40 servers to AWS in one month, including a minimum of 15 Windows servers, you may be eligible to receive a $200 AWS Promotional Credit per Windows server, until December 31, 2023. If you migrate more than 80 servers, including at least 25 Windows servers, in a calendar month, the discount increases to $250 AWS Promotional Credit for each Windows server you migrate to AWS using MGN. Migrated servers must be migrated from locations outside of AWS and continuously run on AWS for at least four weeks after migration.

### AWS Migration Acceleration Program for Windows
<a name="9999999999999999aws--migration-acceleration-program-for-windows.060ee688-7bcf-5e0a-8ff4-00dde2e1137d"></a>

The [AWS Migration Acceleration Program (MAP) for Windows](https://aws.amazon.com/windows/map-for-windows/), an extension of the existing AWS MAP program, is designed to help organizations reach their migration goals even faster with AWS services, best practices, tools, and incentives. AWS uses a three-step approach to help you reduce the uncertainty, complexity, and cost of migrating to the cloud. In addition, MAP can help you modernize current and legacy versions of Windows Server and SQL Server workloads to reduce costs by using cloud solutions such as SQL Server running on Linux, Aurora, container-based services, and Lambda. Cloud-native or open-source solutions can help you break free from the high costs of commercial licensing.

### AWS Countdown
<a name="9999999999999999aws--countdown.2a3200e7-8cb4-57b0-be29-ee6ce7219d16"></a>

[AWS Countdown](https://aws.amazon.com/premiumsupport/aws-countdown/) offers architecture and scaling guidance and operational support during the preparation and implementation of planned events, such as shopping holidays, product launches, and migrations. For these events, AWS Countdown helps you assess operational readiness, identify and mitigate risks, and implement your event confidently with AWS experts by your side. The program is included in the Enterprise Support plan and is available to Business Support customers for an additional fee.

AWS experts lead a highly focused engagement to provide you with architectural and operational guidance for your planned event using a prescriptive, phased approach that helps you do the following:
+ Understand your success criteria and desired business outcome
+ Assess the readiness of your AWS environment, help identify and mitigate risks, and document your plan
+ Confidently host your event with AWS experts by your side
+ Analyze results post-event and scale services to normal operating levels, so you can focus on planning your next event

## Training
<a name="training"></a>

### Self-paced, interactive, and classroom training
<a name="self-paced--interactive--and-classroom-training.d3c00da1-704a-58f4-900c-e49991fdeec2"></a>

AWS offers both digital and classroom training to support you in your migration journey. You can start learning with hundreds of self-paced digital training courses built by the experts at AWS. Then, you can gain hands-on skills by completing interactive training with the [AWS Skill Builder](https://explore.skillbuilder.aws/learn). With classroom training you can ask questions, work through solutions in person, and get feedback from AWS-accredited instructors with deep technical knowledge. For more information, explore [AWS Training and Certification](https://www.aws.training/) offerings.

### AWS Partner training
<a name="9999999999999999aws--partner-training.64c25e64-4428-5475-bc3b-61f60675ac3d"></a>

AWS Partners also offer digital training as self-paced courses covering a range of topics from AWS Cloud fundamentals to machine learning at top online learning platforms such as EdX and Coursera. For more information, explore [AWS Partner Training and Certification](https://aws.amazon.com/partners/training/) offerings. You can be certified by role and solution. For example, roles include Cloud Practitioner, Solutions Architect, Developer, and SysOps Administrator. Solutions include Advanced Networking, Data Analytics, Databases, Machine Learning, Security, Storage, and more.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
