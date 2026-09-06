---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/deep-dive.html
---

# Task 4: Defining the application deep dive process
<a name="deep-dive"></a>

Now that you are finished establishing rules and processes for application prioritization, you perform an application deep dive that will help you refine the priority of each application. You perform the application deep dive on one application at a time, in order from the highest to lowest priority. For projects with multiple portfolio teams, each team can perform an application deep dive on a different application at the same time.

During the deep dive, you might encounter some unexpected issues, such as dependencies, that affect the complexity of migrating the application. When this happens, you should modify your complexity scoring criteria you defined in the previous step and update the score sheet accordingly in order to get more accurate complexity scores for future applications. You can then update the application priorities by using the new complexity scores.

This task consists of the following steps:
+ [Step 1: Define the application workshop process](#deep-dive-1)
+ [Step 2: Define the application mapping process](#deep-dive-2)
+ [Step 3: (Optional) Define the application target state](#deep-dive-3)
+ [Step 4: Finalize the application deep dive process](#deep-dive-4)

## Step 1: Define the application workshop process
<a name="deep-dive-1"></a>

The workshop process is one of the most efficient approaches to an application deep dive. Using this process, you collaborate with the stakeholders, application owners, and the portfolio team to assess and analyze the application. The goal is to clearly understand the current state of the application, including its architecture, business purpose, dependencies, and environment. You then use this detailed information about the size and complexity of the application to design the application's target state.

Each workshop typically lasts 1–8 hours, although you might find that additional time is needed for high-complexity applications. You can also break the workshop into multiple meetings, depending on the availability of resources, your preference, and the size and complexity of the application.

### Identify the expected outcomes
<a name="identify-the-expected-outcomes.7020feb3-47a2-59c1-a47e-91b447838d7d"></a>

Before conducting an application workshop, you should set an agenda and define the *expected outcomes* of the workshop, or information that you need to collect in the workshop. This allows the workshop participants to prepare for the workshop, helps keep the meeting on target, and ensures that by the end of the workshop, you have all of the information necessary to prioritize, wave plan, and migrate the application.

We recommend that you define a standard set of expected outcomes and document these in your application prioritization runbook. When preparing a workshop, you use the standard expected outcomes and add new ones for the specific application.

Define the standard set of expected outcomes for application workshops as follows:

1. Open your application prioritization runbook.

1. In the *Application workshop expected outcomes* section, establish a standard set of expected outcomes for application workshops. When preparing a workshop, you can customize these for the specific needs of the application.

1. Save the application prioritization runbook.

1. Maintain the expected outcomes in the application prioritization runbook. As you conduct application workshops and continue with portfolio assessment and wave planning, you might identify new expected outcomes or refine your existing outcomes.

The following are examples of expected outcomes for the application workshop.

|
|
| **Priority** | **Expected outcome of application workshop** |
| --- |--- |
| 1 | Clear understanding of the application's current architecture, including associated servers, dependencies, the environment, and the application tier. |
| 2 | The team has collected the metadata to support the design of the target architecture. The following metadata is required:+ Target AWS account ID<br />+ Target AWS Region<br />+ Target subnet<br />+ Target security groups |
| 3 | The application owner questionnaire is complete, and all key questions are answered. |
| 4 | The team has collected all application documentation, such as the user guide, application architecture documentation, testing documentation, design documentation, and application programming interface (API) documentation. |

### Define the application workshop rules
<a name="define-the-application-workshop-rules.dc42a200-1c7e-5388-89c6-1a57fc98d5d3"></a>

Before conducting an application workshop, you should define the rules that will govern your workshop. Common rules include workshop length, tools that might be needed in the workshop, and any scheduling considerations or deadlines that need to be considered. This helps keep the meeting on target and ensures that decisions made in the workshop align with the migration schedule.

We recommend that you document the application workshop rules in your application prioritization runbook.

Define your application workshop rules as follows:

1. Open your application prioritization runbook.

1. In the *Application workshop rules* section, define the rules that govern your workshops.

1. Save the application prioritization runbook.

1. Maintain the rules in the application prioritization runbook. As you conduct application workshops and continue with portfolio assessment and wave planning, you might identify new rules or refine your existing ones.

The following are examples of rules for the application workshop.

|
|
| **Priority** | **Workshop rule** |
| --- |--- |
| 1 | Workshops should be scheduled for a maximum of 2 hours per session on Tuesdays and Thursdays. |
| 2 | There is a scheduled freeze of the infrastructure December 1–January 15. |
| 3 | There is a hands-on workshop for migration tools. |
| 4 | The data center contract will expire on March 31. Workloads must be evacuated by March 31 to avoid penalties and costly contract extensions. |
| 5 | Biometric application and time and attendance application will be retained. |

### Define the application workshop process
<a name="define-the-application-workshop-process.ca7b2c58-8bff-5469-9694-7117f258a650"></a>

It is important that you define a standard process for conducting application workshops. This ensures a consistent experience and sets expectations for the workshop participants, which can improve the efficiency of the workshop.

There are three stages to the application workshop process:
+ **Prepare for the workshop** – Preparing for the workshop helps ensure that the session goes smoothly and that participants know what is expected. To prepare for the workshop, you establish an agenda and define the expected outcomes, you identify participants, tools, and the information needed in the workshop, and you schedule the workshop. Scheduling the workshop at least one week in advance gives the team time to block their calendar, prepare for the workshop, and collect any useful information.
+ **Conduct the workshop** – When conducting the workshop, you limit the discussion to the items on the agenda and ensure that you meet the expected outcomes. Note topics that you think are helpful but are not included in your agenda. It can be helpful to record the workshop.
+ **Finalize the workshop outcomes** – After the workshop, your team should have a clear understanding of the current state of the application and potential pain points, risks, challenges, and blockers that could affect prioritization and migration. Common tasks after the workshop include: reprioritizing the application, drafting the future state of the application, and updating the runbook with any expected outcomes, rules, or process changes that might be helpful in the next workshop.

The *Runbook template for application prioritization* includes a standard step-by-step process for preparing, conducting, and finalizing an application workshop. Define your application workshop process as follows:

1. Open your application prioritization runbook.

1. In the *Application workshop process* section, modify the standard process to meet the needs of your use case.

1. Save the application prioritization runbook.

1. Maintain the process in the application prioritization runbook. As you conduct application workshops, you might identify changes that you want to make to this process.

### Step exit criteria
<a name="step-exit-criteria.465d755f-9ecf-5c9b-97d8-aeefdb6e2144"></a>
+ You have defined the workshop agenda and the resources and artifacts required to support the workshop.
+ You have defined the expected outcome of the workshop and identified the information you need to collect in the workshop.
+ You have conducted a trial of the workshop process and have the information needed to support application mapping and design the target state.
+ You have documented the following in your application prioritization runbook:
  + Application workshop expected outcomes
  + Application workshop rules
  + Application workshop process

## Step 2: Define the application mapping process
<a name="deep-dive-2"></a>

*Application mapping* is the process of assigning each application to a migration pattern, which you identified and validated in [Step 4: Validate the migration patterns](discovery.md#discovery-4). In this step, you define the rules that you will use to evaluate the application. You then define the process that you will use to evaluate each application. Mapping each application to the migration pattern's use case helps you identify the migration tool, any skills necessary to complete the migration, and the complexity of the migration pattern.

You do not always migrate an application to a single pattern. For more information about when you might need multiple patterns for the same application, see *Define the application mapping process*, later in this section.

### Application mapping rules
<a name="application-mapping-rules.230bb014-10bf-5143-87cb-d4d3724c820f"></a>

The application mapping rules help you evaluate the application and identify the appropriate migration pattern. Each rule consists of any information you should use to evaluate the application and match criteria for the pattern.

The attached *Runbook template for application prioritization* includes a section for documenting your application mapping rules. Define your process as follows:

1. Open your application prioritization runbook.

1. In the *Application mapping rules* section, define your application mapping rules.

1. Save the application prioritization runbook.

1. Maintain the rules in the application prioritization runbook.

The following table provides examples of application mapping rules.

**Note**
The pattern IDs and names in this table correspond to the sample patterns in [Step 4: Validate the migration patterns](discovery.md#discovery-4). Use the pattern IDs and names that you defined in your application prioritization runbook.

|
|
| Priority | Mapping rule |
| --- |--- |
| 1 | Using utilization data or monitoring tools, identify whether the application is a zombie or idle application. If the application is a zombie or idle application, choose *Pattern 8: Retire the application*, and then shut down the servers in the application stack. |
| 2 | Identify whether migrating this application to the cloud provides business value. Applications that are used only on premises and are not shared across branch or geographical locations, such as time and attendance applications, typically do not need to be migrated to the cloud. If migrating this application does not provide business value, choose *Pattern 9: Retain on premises*. |
| 3 | Identify whether the operating system (OS) of the application is supported by AWS, AWS migration services, a vendor, or your rehost migration tool, and then do the following:+ If the OS is supported, choose *Pattern 1: Rehost to Amazon EC2 using MGN or Cloud Migration Factory*. <br />+ If the OS is not supported, choose *Pattern 3: Replatform to Amazon EC2 using AWS CloudFormation*. |
| 4 | Identify whether the application has a software as a service (SaaS) version or equivalent, and then evaluate the benefits and costs of moving to this new platform. If these criteria are met, choose *Pattern 10: Repurchase and upgrade to SaaS*. |
| 5 | Identify whether the application's on-premises database(s) can be migrated to a homogeneous service in the cloud, such as migrating an on-premises Oracle database to Amazon RDS for Oracle or migrating an on-premises MySQL database to Amazon Aurora MySQL-Compatible Edition database. If these criteria are met, use *Pattern 2: Replatform to Amazon RDS using AWS DMS and AWS SCT*. |
| 6 | Identify whether the application uses Microsoft .NET Core (.NET 5 or .NET 6), Java, PHP, or another open-source programming language and whether the application is hosted in Microsoft Windows Server. Evaluate whether the cost of replatforming is justifiable. If these criteria are met, choose *Pattern 7: Replatform from Windows to Linux on Amazon EC2*. |
| 7 | Identify the on-premises local and shared file storage that your application is dependent on, and then determine whether it must be included in the migration. If the local and shared file storage must be migrated, choose *Pattern 4: Replatform to Amazon EFS using AWS DataSync or AWS Transfer Family*. |
| 8 | Identify whether the application's servers are mainframe or midrange servers, such as IBM AS/400 or Apache Spark, and confirm that the applications are compatible with emulators. If these criteria are met, use *Pattern 6: Replatform mainframe or midrange servers to Amazon EC2 using an emulator*. |
| 9 | Identify whether this is a legacy, monolithic, or mainframe-based application that can no longer meet the demand of the business due to its limitations. For example, identify whether the application can scale, integrate with related applications, or is expensive and difficult to maintain. If the application meets any of these criteria, choose *Pattern 11: Re-architect the application*. |

### Define the application mapping process
<a name="define-the-application-mapping-process.0d340a86-7096-54dc-a6f2-2f1e233d0a3b"></a>

When you are mapping applications to the migration patterns, it is helpful to request discovery data for the application from the discovery team. This data typically includes information such as a recommended migration pattern (sometimes called the *R pattern* or *R score*), utilization information, application dependencies, and other information that you can use in the assessment. As you explore this application in detail, you might decide to change the migration pattern that was previously identified.

When you have the data, you can compare the application to the business and technical criteria that you identified in [Step 2: Identify the business and technical drivers](discovery.md#discovery-2). You recorded your drivers in your application prioritization runbook. Evaluating the application against the criteria might lead you to select multiple migration patterns for the application, or it might lead you to eliminate patterns based on cost, schedule, or other limitations.

The following is an example of a business driver that requires you to use multiple migration patterns on a single application. You want to migrate an on-premises SQL Server database to Amazon DynamoDB, but because the contract for the data center is expiring, the business would like to migrate it sooner than the proposed schedule to replatform it. To address this business driver, you revise the migration plan for the application into a two-pattern approach. First, you rehost the application to the cloud in order to remove it from the data center. Later, after the application is in the cloud, you can replatform it according to the proposed schedule.

You should also consider whether the application is an n-tier application, which is an application composed of multiple tiers. An *application tier* is a group of physical servers that host horizontal layers of your application. N-tier applications are more complex because each tier might require a different strategy, and you might choose to migrate the application tiers in different waves. For example, if you have an application that is composed of presentation, business service, and database tiers, there is a possibility that you can map a different pattern for each tier.

You then evaluate the application against your application mapping rules, which you defined in your application prioritization runbook. For more information, see *Application mapping rules* earlier in this section.

After you map your application to one or more patterns, review and verify this decision with the application owner. The application owner should confirm the selected pattern, and they should help you plan and perform the migration. At this time, application owners might also provide insights based as their experience or share any issues they anticipate with the migration.

When you have mapped the application to one or more migration patterns and confirmed the patterns with the application owner, you record the application, pattern ID, pattern name, and relevant drivers in an application mapping table in your application prioritization runbook.

The attached *Runbook template for application prioritization* includes a standard step-by-step process for application mapping. Define your process as follows:

1. Open your application prioritization runbook.

1. In the *Application workshop process* section, modify the standard process to meet the needs of your use case.

1. Save the application prioritization runbook.

1. Maintain the process in the application prioritization runbook.

The following table is a sample application mapping table. The provided *Runbook template for application prioritization* includes an empty table in which you can record your results from the application mapping process.

**Note**
The pattern IDs and names in this table correspond to the sample patterns in [Step 4: Validate the migration patterns](discovery.md#discovery-4). Use the pattern IDs and names that you defined in your application prioritization runbook.

|
|
| Application name | Pattern ID | Pattern name | Business and technical drivers addressed |
| --- |--- |--- |--- |
| Corporate website | 1 | Rehost to Amazon EC2 using MGN or Cloud Migration Factory | Data center exit<br />Reduce operational costs |
| HR system | 8 | Retire the application | Reduce operational costs |
| Time and attendance application | 9 | Retain on premises | Reduce operational costs<br />Reduce risk and impact |
| PO system | 3 | Replatform to Amazon EC2 using AWS CloudFormation | Technology integration<br />Storage and compute limitation<br />Hardware and software end-of-life support<br />Improve security and compliance |
| CRM system | 10 | Repurchase and upgrade to SaaS | Reduce operational costs<br />Technology integration<br />Hardware and software end-of-life support<br />Accelerate development, innovation, and growth |
| Fixed asset system | 7 | Replatform from Windows to Linux on Amazon EC2 | Reduce operational costs |
| ERP file storage  | 4 | Replatform to Amazon EFS using AWS DataSync or AWS Transfer Family | Storage and compute limitation |
| Ledger system | 6 | Rehost mainframe or midrange servers to Amazon EC2 using an emulator | Data center exit<br />Technology integration<br />Improve security and compliance<br />Hardware and software end-of-support<br />Storage and compute limitation<br />Modernizing application architecture |
| General ledger | 11 | Re-architect the application | Reduce operational costs<br />Technology integration<br />Improve security and compliance<br />Hardware and software end-of-support<br />Storage and compute limitation<br />Modernizing application architecture<br />Scalability and resiliency<br />Accelerate development, innovation, and growth |

### Step exit criteria
<a name="step-exit-criteria.ff3a7930-85a4-51f0-9569-4800a0a385bd"></a>
+ You have documented the following in your application prioritization runbook:
  + Application mapping rules
  + Application mapping process
+ You have validated the mapping rules and processes by using one or more proof-of-concept (POC) applications.

## Step 3: (Optional) Define the application target state
<a name="deep-dive-3"></a>

In this step, you define the attributes and the process that you use to document the target state, or *to-be* *state*, for the application. The *target state* is how the application operates in the target cloud environment after the migration. The target environment varies based on your target platform or service and business requirements. The target environment could be the AWS Cloud or AWS Managed Services (AMS).

Defining the target state helps project managers, migration consultants, architects, application owners, and stakeholders collaborate effectively. By using this process, the team can identify and resolve issues in advance and more efficiently implement the target state environment.

For some applications, this step is optional. You can skip this step if the application you are migrating is standalone or low-complexity. Migration strategies that don't modify the application, such as rehost, might not require this step. However, for more complex migration strategies, such as replatform and re-architect, you should define the target state before starting the migration.

The workshop provides you with an in-depth understanding of the current state of the application, so it's a good idea to draft the target state after completing the workshop. In addition, mapping the application to its migration pattern provides additional insights and helps you identify whether defining the target state is necessary. For example, if you map the application to the pattern *Rehost to Amazon EC2 using MGN or Cloud Migration Factory*, you've identified that the strategy is rehost, and you likely do not need to define the target state for this application.

### Target state attributes
<a name="target-state-attributes.198bdc5f-89f7-59a2-afd0-92eb2a77cde3"></a>

When defining the target state and making decisions about the application, we recommend that you consider the following target state attributes:
+ **AWS Well-Architected Tool** – Review the application target state against the AWS Well-Architected Framework to help improve the security, performance, and resiliency of the application in the cloud.
+ **Target landing zone** – Typically, by the end of the [mobilize phase](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/mobilize-phase.html), you should have built a complete landing zone that is ready to run pilot applications. The landing zone should already be configured with a multi-account architecture, identity and access management, governance, data security, network design, and logging. You use a pilot application to verify that the landing zone is complete. Verify that you can launch and run your pilot application in the existing target landing zone. If you need to modify the landing zone for the application, inform the landing zone team of your requirements. For example, your application might require access to a service that is hosted in a separate account, or your application might require special routing to a virtual private cloud (VPC).
+ **Dependencies** – Identify any applications that your application relies on in order to function properly. For example, your application might be dependent on databases, storage, or third-party services, such as a payment gateway or external web service, or your application might be dependent on other applications within your environment. In order to access these dependencies, you might need special routing or configuration, such as connecting to a directory service for authentication.
+ **Dependent applications** – Identify any applications that rely on your application in order to function properly. You might need to reconfigure and update these applications in order to prevent downtime during the migration.
+ **Security and compliance** – Review the target environment with the security and compliance team, and identify any gaps. The application might be composed of several components, logical layers, or multiple tiers. Depending on your compliance requirements, you might not be able to migrate some of these components to your target environment, or you might need additional security measures when migrating the workload. Common security and compliance requirements are data residency, encryption in transit, and encryption at rest. These require additional configuration in your target environment. For example, you might need to configure certificates in order to secure communications, or you might need encryption keys to secure the data at rest. You might also need to select multiple migration patterns for the application so that some application tiers remain on premises and other tiers are migrated to the cloud.
+ **Storage dependencies** – Review your application storage dependencies and determine how migrating the application to the target environment would affect these dependencies. For example, if the application is dependent on network storage, such as network-attached storage (NAS) or a storage area network (SAN), you need to plan for a storage service in the cloud, such as Amazon Simple Storage Service (Amazon S3) or Amazon FSx. You also need to plan how you will migrate your data to the target cloud environment in order to keep your application running.
+ **Database** – Review the migration strategy for any databases the application uses. Are you going to replatform to a new database service, such as Amazon Relational Database Service (Amazon RDS), Amazon Aurora, or Amazon DynamoDB? Are you going to rehost your database in the target environment? In some cases, especially for a monolithic database, you need to refactor the database in order to address technical requirements, such as sub-second latency, or to take advantage of the features of a particular type of AWS database. As with data residency compliance requirements, you need to identify which data should be retained on premises and which should be migrated to the cloud. For example, you might need to retain an on-premises database table for customer information, and you could migrate the rest of the database to the cloud.
+ **Application components** – Review the components your application depends on. Determine whether your application depends on a component that isn't supported by the target environment. If the target environment doesn't support all application components, you need to refactor the application to mitigate the issue. For example, if you have a .NET Framework application that is dependent on Windows-only components such as Component Object Model (COM) Interop, COM\+, or the Windows registry, in order to replatform the application on a Linux operating system, you must refactor the application to .NET Core.
+ **Application tiers** – Identify the number of tiers in your application. Is the application n-tier, two-tier, or standalone? Confirm that you understand the migration pattern for each tier. For example, your application might have a presentation (or *web*) tier that hosts the user interface, an application tier that hosts business services, and a database tier that hosts databases, and each tier might require a different migration pattern.
+ **Disaster recovery** – Identify the application's current and future-state disaster recovery (DR) plan, including the recovery point objective (RPO) and recovery time objective (RTO). Decide whether to use the existing on-premises DR plan or to explore a new DR strategy in the cloud. For more information, see the sections [Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html) and [Recovery objectives (RTO and RPO)](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/business-continuity-plan-bcp.html#recovery-objectives-rto-and-rpo) in the *Disaster Recovery of Workloads on AWS: Recovery in the Cloud* whitepaper.

### Define the target state process
<a name="define-the-target-state-process.f5408d89-719c-526f-99aa-62d5e717ec56"></a>

To define the application target state, we recommend you use the provided template, *Application target state worksheet *(Excel format). The template includes standard attributes that you can use or modify. Define the process for documenting the application target state as follows:

1. Open the *Application target state worksheet*.

1. Review the default attributes and make any changes for your use case.

1. Save the worksheet.

1. Open your application prioritization runbook.

1. In the *Target application state*section, do the following:

   1. In the *When to complete this process* section, establish criteria that allow the portfolio team to determine whether they need to define the application's target state.

   1. Update the attribute section as needed.

   1. Update the process section as needed for your use case.

1. Save the application prioritization runbook.

#### Samples of the application target state
<a name="samples-of-the-application-target-state.f1babce3-e89a-5be6-9261-feb64f457587"></a>

The following table shows an example of how you use the *Application target state worksheet* to document the target state of the application.

|
|
| Application | Example  |
| --- |--- |
| **Target platform** | AWS Cloud |
| **Landing zone** | Requires access to an on-premises directory service<br />Requires AWS Control Tower to centralize management of multiple accounts and services across the organization |
| **Dependencies** | Active Directory, payment gateway, inventory system |
| **Dependent applications** | None |
| **Security** | Encryption at rest and in transit |
| **Compliance** | PCI, SOC |
| **Storage dependencies** | Boot drive attached, NAS, network share |
| **Database** | Current: Oracle DB<br />Cloud: Amazon RDS for Oracle |
| **Application component** | .NET Framework 4.5 |
| **Application tiers** | N-tier<br />Front-end, business services, data services and agents, database |
| **Disaster recovery** | RPO: 1 min, RTO: 5 min<br />Current DR strategy is warm standby<br />DR in any US regions |

### Step exit criteria
<a name="step-exit-criteria.91db663c-adfa-5842-8662-1301e07cf58b"></a>
+ In the *Application target state worksheet*, you have defined the attributes that you want to include in the target state process.
+ In your application prioritization runbook, you have done the following:
  + You have established criteria for when the portfolio team is expected to define the target state of the application.
  + You have updated the process for defining the target state based on your use case.

## Step 4: Finalize the application deep dive process
<a name="deep-dive-4"></a>

Now, you define how the portfolio workstream uses the workshop, rules, and processes you established in this task to perform a deep dive into the application. This is the process that the portfolio workstream references in the implementation stage of the migration.

Customize this process in the application prioritization runbook as follows:

1. Open your application prioritization runbook.

1. In the *Stage 2: Perform application deep dive *section, modify the process as appropriate for your use case and environment.

1. Save the application prioritization runbook.

1. Share your application prioritization runbook with the team for review.
