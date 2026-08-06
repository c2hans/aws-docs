---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/workstreams.html
---

# Workstreams in a large migration
<a name="workstreams"></a>

Large migration projects typically consist of multiple workstreams, and each workstream has a clear scope of tasks. Each workstream is independent but also supports the other workstreams to accomplish the same goal – migrate servers at scale. This section discusses the standard core workstreams for large migrations as well as common supporting workstreams.

## Core workstreams
<a name="core-workstreams"></a>

Core workstreams are needed for every large migration, regardless of company size or segment. The following is an overview of the primary roles of each core workstream:
+ **Foundation workstream** – This workstream is focused on preparing the people and platform for the large migration.
+ **Project governance workstream** – This workstream manages the overall migration project, facilitates communication, and focuses on completing the project within budget and on time.
+ **Portfolio workstream** – The teams in this workstream collect metadata to support the migration, prioritize applications, and perform wave planning.
+ **Migration workstream** – Using the wave plan and collected metadata from the portfolio workstream, the teams in this workstream migrate and cutover the applications and servers.

Information and activities flow from upstream to downstream in a large migration, as shown in the following table. Information comes from the upstream foundation and project governance workstreams, through the portfolio workstream, and into the migration workstream. For example, the portfolio workstream is upstream of the migration workstream because the portfolio workstream prepares the metadata and wave plan that the migration workstream uses to migrate and cutover the applications and servers. Adding additional, supporting workstreams in your large migration project might change the flow of information and activities through the core workstreams.

**Important**
You need to assign a project-level technical leader for your large migration project. This role is not part of any individual workstream but has the total responsibility of all workstreams. This individual oversees all workstreams to make sure they work together and stay focused on the project-level goals.

|
|
| Core workstream name | Upstream workstreams | Downstream workstreams |
| --- |--- |--- |
| Foundation | — | Migration<br />Portfolio |
| Project governance | — | Migration<br />Portfolio |
| Portfolio | Foundation<br />Project governance | Migration |
| Migration | Foundation<br />Project governance<br />Portfolio | — |

The following are the primary functions of each core workstream in the phases of a large migration. The playbooks in this document series are structured to help you navigate the tasks for each workstream in the appropriate phase and stage.

|
|
|   | Foundation | Project governance | Portfolio | Migration |
| --- |--- |--- |--- |--- |
| **Phase 1: Assess** | — | — | — | — |
| **Phase 2: Mobilize** | You might have designed the AWS landing zone or workstreams in this phase.<br />  | You might have designed a project management process in this phase. | You might have completed an initial portfolio assessment and discovery in this phase. | You might have completed a pilot migration in this phase. |
| **Phase 3: Migrate** | Stage 1: Initialize | Establish workstreams and review landing zone design. Prepare for change.<br />Formalize migration principles, teams, and RACI matrix. Complete training. | Develop project management processes and communication and meeting plans. | Develop metadata, wave planning, and application prioritization runbooks. | Develop migration runbooks. |
| Stage 2: Implement | — | Facilitate and communicate the status of waves and the overall migration project. | Collect metadata for the migration, prioritize applications, and plan waves. | Migrate and cutover waves, and iterate the runbooks to increase velocity. |

The following sections describe each of the core workstreams in more detail, including common tasks for each workstream, the expected outcome of each workstream, and the skills required in each workstream.** **It is not required that each individual in the workstream have every skill. A workstream consists of one more cross-functional teams, so each person contributes different skills. But as a team, they should have all the skills listed.

### Foundation workstream
<a name="foundation-workstream.40d390d9-11e3-5d4f-a66a-27f3da403d16"></a>

The foundation workstream consists of two categories: platform foundation and people foundation. Building the platform foundation helps confirm that both the AWS and the on-premises infrastructures are ready to support the large migration. Building a people foundation prepares and trains the project teams for the migration and sets up all workstreams.

|  |
| --- |
| Common tasks | + Build and validate the AWS landing zone<br />+ Prepare the on-premises infrastructure to support the migration, such as making networking or firewall changes, permissions changes, or Active Directory changes<br />+ Set up the project core workstreams and supporting workstreams<br />+ Set up the training plan for the team<br />+ Build the RACI matrices with project managers |
| --- |--- |
| **Expected outcome** | + Source and target platforms are prepared for the large migration.<br />+ People are ready to support the large migration<br />+ All workstreams are set up. |
| **Required skills** | + Deep knowledge of on-premises data centers, including servers, storage, and networking<br />+ Experience with the AWS Cloud and knowledge of AWS compute services, including landing zones and AWS Control Tower<br />+ Experience with large data center or cloud migrations<br />+ Experience building a training plan<br />+ Experience building a cross-functional team |

### Project governance workstream
<a name="project-governance-workstream.353735a8-baef-5a03-8189-8e5063074db5"></a>

The project governance workstream manages the overall migration project and is responsible for delivering the project on budget and on time.

|  |
| --- |
| Common tasks | + Kick off the project<br />+ Set up the governance model<br />+ Set up the Cloud Enablement Engine (CEE)<br />+ Set up the communication plan<br />+ Set up the escalation plan<br />+ Build RACI matrices<br />+ Set up the project management framework<br />+ Set up status reporting and project tracking<br />+ Set up risk and issue tracking<br />+ Continuously manage the project by using the predefined processes and tools  |
| --- |--- |
| **Expected outcome** | + Ensure that every workstream is able to complete their tasks on time<br />+ Ensure collaboration across workstreams<br />+ Ensure that the project achieves the defined business outcomes<br />+ Deliver the project on budget and on time |
| **Required skills** | + Experience with common project management methodologies, such as waterfall, agile, Kanban, and scrum<br />+ Experience with common project management tools, such as Jira, Microsoft Project, and Confluence<br />+ Experience with large migration project management |

### Portfolio workstream
<a name="portfolio-workstream.b18dfedb-412c-5ca5-8f94-3501243cb799"></a>

The portfolio workstream manages all of the migration discovery activities, collects metadata, prioritizes applications, and creates a wave plan to support the migration workstream.

|  |
| --- |
| Common tasks | + Validate the migration strategies and patterns<br />+ Complete portfolio discovery by using discovery tools and configuration management database (CMDB)<br />+ Define the required metadata, collection processes, and storage location<br />+ Prioritize applications<br />+ Perform application deep dives, including dependency analysis and target state design<br />+ Perform wave planning<br />+ Collect migration metadata |
| --- |--- |
| **Expected outcome** | + Continuously create wave plans and collect migration metadata, and then hand off to the migration workstream |
| **Required skills** | + Deep knowledge of on-premises CMDB, data repositories, and content management tools<br />+ Experience with common portfolio discovery tools, such as Flexera One and modelizeIT<br />+ Experience with portfolio assessment and application prioritization<br />+ Experience with application deep dives and application owner interviews<br />+ Experience with application designs for the AWS Cloud<br />+ Experience with wave planning for large migrations<br />+ Experience with automation, including shell scripting, Python, and Microsoft PowerShell |

### Migration workstream
<a name="migration-workstream.6a92cf9c-ee51-511e-8ce6-b893b3d129a8"></a>

The migration workstream manages the migration implementation-related activities, including data replication and cutover. Because the migration team performs the migration and cutover, a common misconception is that the migration workstream does everything in a large migration project. However, the migration workstream is dependent on other workstreams to build the foundation and provide portfolio data to support the migration.

**Tip**
The migration workstream is generally the largest workstream in a large migration project. Depending on the size and strategy of your project, consider dividing this workstream into multiple sub-workstreams. For example:
+ Rehost migration workstream
+ Replatform migration workstream
+ Refactor migration workstream
+ Relocate migration workstream
+ Migration workstream for a specialized workload, such as SAP or databases

|  |
| --- |
| Common tasks | + Validate the migration wave plans<br />+ Build the migration runbooks<br />+ Use AWS migration services to transfer data, such as AWS Application Migration Service (AWS MGN), AWS Database Migration Service (AWS DMS), and AWS DataSync<br />+ Install and uninstall software on source and target servers as needed support the migration<br />+ Write automation scripts to automate migration activities<br />+ Launch target AWS environments, such as Amazon Elastic Compute Cloud (Amazon EC2) instances, for testing or cutover<br />+ Work with change management team for changes and cutovers<br />+ Perform migration cutover<br />+ Support application owners during application testing<br />+ If cutover fails, help roll back the server |
| --- |--- |
| **Expected outcome** | + Complete migration cutover and application go-live in target AWS accounts |
| **Required skills** | + Deep knowledge of on-premises data centers, including servers, storage, and networking<br />+ Experience with the AWS Cloud and knowledge of AWS compute services, including landing zone and AWS Control Tower<br />+ Experience with AWS migration services, including Application Migration Service, AWS DMS, DataSync, and AWS Snow Family<br />+ Experience with large data center or cloud migrations and cutovers<br />+ Experience with automation, including shell scripting, Python, and Microsoft PowerShell |

## Supporting workstreams
<a name="supporting-workstreams"></a>

Supporting workstreams support the core workstreams. These workstreams are optional, and you might decide to use them based on your use case and the current stage of your migration. The following are some common supporting workstreams that you might want to include in your large migration project:
+ **Security and compliance workstream** – This workstream defines and builds the security standards for the target AWS infrastructure and supports migrations.
+ **Cloud operations (Cloud Ops) workstream** – This workstream manages applications after cutover, when the hypercare period is complete.
+ **Application testing workstream** – This workstream performs application testing before and during the cutover.
+ **Specializedworkload migration workstream** – This workstream supports migrations for specific, specialized workloads, such as SAP or databases.

You might not need a dedicated workstream for these activities. It is common to have an individual or set of individuals be responsible for these activities and then embed those individuals in one of the core workstreams. For example, every large migration requires a security and compliance person because you need to make sure your target infrastructure is secure and compliant. However, security and compliance assessments and decisions are typically performed early in the migration, most commonly in the mobilize phase. If you have already completed this, you do not need a dedicated workstream to repeat the same tasks. However, it is recommended that you embed a security and compliance person in the migration workstream in order to support the migration activities.

When you add supporting workstreams, it modifies the flow of information and activities through the core workstreams. The following table is an example of how adding workstreams changes this flow. Your supporting workstreams might differ from the examples in this table.

|
|
| Workstream name | Type | Upstream workstreams | Downstream workstreams |
| --- |--- |--- |--- |
| Migration | Core | Foundation<br />Project governance<br />Portfolio<br />Security and compliance | Application testing<br />Cloud operations<br />  |
| Portfolio | Core | Foundation<br />Project governance<br />Security and compliance | Migration |
| Project governance | Core | — | Migration<br />Portfolio |
| Foundation | Core | — | Migration<br />Portfolio<br />Cloud operations |
| Security and compliance | Supporting | — | Migration<br />Portfolio |
| Cloud operations | Supporting | Migration<br />Application testing<br />Foundation | — |
| Application testing | Supporting | Migration | Cloud operations |
| Specialized workload migration | Supporting | Foundation<br />Project governance<br />Portfolio<br />Security and compliance | Application testing<br />Cloud operations |

### Security and compliance workstream
<a name="security-and-compliance-workstream.eef96041-bedc-514b-b135-1cb5476d74b0"></a>

The security and compliance workstream defines and builds the security standards for AWS infrastructure and supports migrations. Using the standards established by this workstream, application owners typically define the security and compliance requirements for each application. You might decide to have the security and compliance workstream review and approve the requirements for some or all applications.

|  |
| --- |
| Common tasks | + Define the security requirements for the AWS landing zone, such as centralized logging, encryption, AWS Identity and Access Management (IAM) policies, and Active Directory integration<br />+ Define the compliance requirements, such as HIPAA, personally identifiable information (PII), Service Organization Control (SOC), and Federal Risk and Authorization Management Program (FedRAMP)<br />+ Define the security requirements for the migration, such as firewall, security group, and IAM role requirements<br />+ Manage changes for security-related tasks, such as changes to firewalls, security groups, and permissions |
| --- |--- |
| **Expected outcome** | + Complete migration cutover and application go-live in target AWS accounts |
| **Required skills** | + Deep knowledge of on-premises data centers, including servers, storage, and networking<br />+ Deep knowledge of the specialized workload in scope<br />+ Experience with the AWS Cloud and knowledge of AWS compute services, including landing zones and AWS Control Tower<br />+ Experience with AWS migration tools, including Application Migration Service, AWS DMS, DataSync, and AWS Snow Family<br />+ Experience with large data center or cloud migrations and cutovers |

### Cloud operations workstream
<a name="cloud-operations-workstream.b41411c7-662b-5384-be36-7c7b4c5b4151"></a>

The cloud operations workstream supports the applications after migration cutover. Sometimes cloud operations is in a separate workstream with dedicated resources, but most commonly, these resources come from existing IT operations teams. In that case, no dedicated workstream is required.

|  |
| --- |
| Common tasks | + Monitor and back up the migrated servers and applications<br />+ Manage the business-as-usual service requests from the application teams, such as increasing the disk size or changing instance types<br />+ Resolve any application issues and outages as needed<br />+ Manage the patching policies and schedules<br />+ Manage the maintenance tasks and requests |
| --- |--- |
| **Expected outcome** | + Migrated servers and applications are running smoothly on AWS<br />+ Respond to service requests from users and resolve any issues |
| **Required skills** | + Deep understanding of how the on-premises data center currently operates<br />+ Experience with common AWS operations services, such as Amazon CloudWatch, AWS Config, AWS CloudTrail, AWS Backup, AWS Support<br />+ Experience with troubleshooting, and understands the SLA<br />+ Experience with supporting large migrations |

### Application testing workstream
<a name="application-testing-workstream.2f86210c-fca9-5244-99d6-c538780673b5"></a>

The application testing workstream supports application testing before and during the cutover. This workstream is more common in projects where system integrators manage the data centers because the application owners don't have sufficient knowledge to perform the application tests. In most cases, the application owner performs these activities, and a dedicated application testing workstream is not required.

|  |
| --- |
| Common tasks | + Perform application testing before the cutover<br />+ Perform application testing during the cutover<br />+ Make application changes as needed to work in the new environment<br />+ Make a go or no-go decision for applications based on testing results during cutover |
| --- |--- |
| **Expected outcome** | + Complete application testing on time during cutover<br />+ Make application changes as needed to support the target environment |
| **Required skills** | + Deep knowledge of the applications and how they operate on premises<br />+ Experience with the AWS Cloud, especially the target AWS services<br />+ Experience with large migrations |

### Migration workstream for a specialized workload
<a name="migration-workstream-for-a-specialized-workload.96b440eb-ee07-5b1c-b6d3-22db73891738"></a>

You can create a migration workstream that is dedicated to specialized workloads. Generally, you can build standard migration patterns and runbooks to migrate servers and applications at scale, and these are managed by the migration workstream. However, in some cases, certain applications require special migration processes. For example, you might need a special process in order to migrate Hadoop workloads, SAP HANA databases, or mission-critical applications that cannot tolerate the standard amount of down time. For more information about specialized workloads, see *MAP specialized workloads* at [AWS Migration Acceleration Program](https://aws.amazon.com/migration-acceleration-program/).

|  |
| --- |
| Common tasks | + Validate the migration wave plans<br />+ Build migration runbooks<br />+ Use migration tools or native application tools to transfer data<br />+ Launch target AWS environments, such as EC2 instances, for testing or cutover<br />+ Work with the change management team for changes and cutovers<br />+ Perform migration cutover<br />+ Support application owners during application testing<br />+ If cutover fails, roll back the application or server |
| --- |--- |
| **Expected outcome** | + Complete migration cutover and application go-live in target AWS accounts |
| **Required skills** | + Deep knowledge of on-premises data centers, including servers, storage, and networking<br />+ Deep knowledge of the specialized workload in scope<br />+ Experience with the AWS Cloud and knowledge of AWS compute services, including landing zones and AWS Control Tower<br />+ Experience with AWS migration tools, including Application Migration Service, AWS DMS, DataSync, and AWS Snow Family<br />+ Experience with large data center or cloud migrations and cutovers<br />+ Experience with migrating the specialized workload |
