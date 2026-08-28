---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/technology-perspective.html
---

# Technology perspective
<a name="technology-perspective"></a>

Technology provides a great foundation for accelerating large migrations. For example, the Cloud Migration Factory solution is focused on how to provide end-to-end automation for migrations. This section explores some of the best practices for using technology to achieve the scale and velocity required, aligned with the scope, strategy, and timelines.

The overarching principle is to look at areas of automation wherever possible. If you have thousands of servers in scope, performing tasks manually can be a costly and time-consuming effort.

To perform a migration, several tools are typically used, such as the following:
+ Discovery
+ Migration implementation
+ Configuration management database (CMDB)
+ Inventory spreadsheet
+ Project management

These tools are used at different stages of migrations, from assessment to mobilize through to implementation. Selection of these tools is driven by the business objectives and timelines.

After migration phases are planned, the next step is to ensure that the migration team has the skills to use the tools they will need. If a team lacks the skills or experience, plan targeted trainings to ramp up the skill set. If possible, create events where teams can get experience with the migration tooling in a safe environment. For example, are there sandpit or lab servers that teams can migrate to experience with the tooling? Alternatively, is it acceptable for initial development workloads to be used for learning purposes?

## Automation, tracking, and tooling integration
<a name="automation-tracking-tooling-integration"></a>

In this section:
+ Automate migration discovery to reduce the time required
+ Automate repetitive tasks
+ Automate tracking and reporting to speed decision making
+ Explore tooling that can facilitate your migration

### Automate migration discovery to reduce the time required
<a name="automate-migration-discovery-to-reduce-the-time-required.891d5c04-a363-5cc9-8754-780339ca784a"></a>

Most large-migration programs commence by understanding the scope of the migration (what must be migrated) and developing a strategy (how it will be migrated). Discovery is an important aspect of this. The required metadata points are captured to form a migration strategy decision tree. To migrate workloads at pace, you must identify and import the required migration metadata into your implementation processes, such as a migration factory. A fully automated mechanism to extract, transform, load (ETL) the migration metadata greatly reduces the time and level of effort involved in the discovery process.

One customer developed a fully automated data intake process for their migration factory. The migration wave plan with all the migration metadata was hosted and maintained in a spreadsheet on Microsoft SharePoint. When changes were made to the source, an AWS Lambda function was triggered to load the data into the migration factory without manual intervention. This automated data intake process helped the customer reduce manual work, minimize human error, and accelerate their velocity. They were able to migrate more than 1,000 servers to AWS.

### Automate repetitive tasks
<a name="automate-repetitive-tasks.e20bab46-8002-5ca9-bab2-2516f713356b"></a>

In the migration implementation phase, many small processes must be repeated frequently. When using AWS Transform MGN (MGN), for example, you must install the agent on each server that is in scope of the migration.

Building a migration factory that works for your specific business and technical requirements is the most effective way to achieve the efficiency and velocity required to deliver a successful large migration. A migration factory provides an integration and orchestration framework that uses a standardized dataset to accelerate the migration. After all the tasks are identified, spend time on automating all the manual tasks that can be automated alongside prescriptive runbooks.

The [Cloud Migration Factory](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/welcome.html) solution is an example of this. Cloud Migration Factory is designed to provide the migration automation foundations on which you can automate aspects that are specific to your organization. For example, you might want to update a flag in your CMDB to highlight that the on-premises servers can now be decommissioned. In this scenario, you could create an automation that which performs this task at the end of the migration wave. Cloud Migration Factory has a centralized metadata store with all the wave, application, and server metadata. The automation script can connect to Cloud Migration Factory to get a list of servers in that wave and perform any actions accordingly. Cloud Migration Factory supports [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html).

### Automate tracking and reporting to speed decision making
<a name="automate-tracking-and-reporting-to-speed-decision-making.803e3acc-2b1d-5673-8f7a-b623b6b9d4a3"></a>

We recommend building an automated migration reporting dashboard to track and report live data, including key performance indicators (KPIs) for the program. Migration projects involve stakeholders from across the organization, including the following:
+ Application teams
+ Testers
+ Decommissioning teams
+ Architects
+ Infrastructure teams
+ Leadership

To perform their roles, these stakeholders require live data. For example, network teams must know the upcoming migration waves to understand the impact on the shared connection between on-premises resources and AWS. Leadership teams want to understand how much of the migration is complete. Having a dependable, automated live feed of data prevents miscommunications and provides a basis on which decisions can be made.

A large healthcare customer was working toward a data center exit with an upcoming deadline. Given the scale and complexity, a significant amount of time was initially spent on tracking and communicating the migration status between stakeholders. The migration team later used [Amazon Quick Sight](https://docs.aws.amazon.com/quicksuite/latest/userguide/quick-bi.html) to build automated dashboards that visualized the data, significantly simplifying tracking and communications while increasing the migration velocity.

### Explore tooling that can facilitate your migration
<a name="explore-tooling-that-can-facilitate-your-migration.3e678658-a181-5bb6-b7f1-e86049c76eb5"></a>

Choosing the right tools for your migration is not easy, especially if no one in your organization has managed a large migration before.

We recommend spending time to choose suitable tooling to support the migration. This exploration might involve a license cost, but it can provide a cost benefit when you consider the wider initiative. Alternatively, you might find that tooling embedded in your organization can provide a similar outcome. For example, you might already have application performance monitoring tooling deployed across your estate, which can provide rich discovery information.

A technology customer was initially reluctant to run automated discovery tooling during their migration due to a lack of familiarity. As a result, an SI AWS Partner had to run 5-10 hours of meetings per application to discovery the estate manually, including server names, operating system versions, and dependencies. It was estimated that if discovery tooling had been used, the discovery effort could have been reduced by more than 1,000 hours.

## Prerequisites and post migration validation
<a name="prereqs-post-migration-validation"></a>

In this section:
+ Build the landing zone during the pre-migration phase
+ Outline prerequisite activities
+ Implement post-migration checks for continuing improvement

### Build the landing zone during the pre-migration phase
<a name="build-the-landing-zone-during-the-pre-migration-phase.422d1735-1a2c-5fc9-93ee-fdb530032816"></a>

We recommend building the AWS target environment, or landing zone, ahead of time, instead of building the target virtual private clouds (VPCs) and subnets during the migration wave. Building a well-architected landing zone is a prerequisite for the migration. The landing zone should include monitoring, governance, operational, and security controls.

Building and validating the landing zone ahead of the migration minimizes the uncertainty that comes with running your workloads in a new environment. With the landing zone in place, the stakeholders can focus on migrating the workloads without worrying about aspects managed at an account or VPC level.

### Outline prerequisite activities
<a name="outline-prerequisite-activities.dc5409c0-36fa-5584-b4a4-36d47fadfbd2"></a>

Alongside the landing zone, it's important to align other technical prerequisites before the migration, especially processes with lengthy lead time. For example, make the necessary firewall changes to allow the data to be replicated from on premises to AWS. Communicating technical prerequisites early helps to prepare and allocate the resources required. It's common for migrations to stall because prerequisites haven't been met. Not only does this impact the in-progress migration wave, it might push back the dates of all future migrations while the issue is being remediated.

A financial services company intended to perform a mass-migration to AWS, with the goal of vacating several data centers. However, their bandwidth available between on-premises and AWS was not sufficient for the velocity they intended. Unfortunately, increasing the bandwidth required a new connection and had a lead time of three months. This meant that the migration velocity was constrained for the first three months.

### Implement post-migration checks for continuing improvement
<a name="implement-post-migration-checks-for-continuing-improvement.e2f2bf55-5c06-5e23-84a7-03d313955dd0"></a>

Finally, remember to implement post-migration validations such as operations integration, cost optimization, and governance and compliance checks. Post-migration validation includes assessing previously migrated workloads to uncover technical lessons learned that should be applied to future waves.

Further, this is a great opportunity to implement cost-control operations. For example, during the migration you might decide to size match the AWS instances to your on-premises estate to reduce the need for performance testing. Now that testing is no longer on the data center closure critical path, you can use Amazon CloudWatch to assess the instance utilization and determine whether a smaller-sized instance would be suitable.

To illustrate the importance of this phase, a large technology customer was performing a large migration but initially did not include post-migration validations. After migrating more than 100 servers, they identified that the AWS Systems Manager Agent (SSM Agent) was not configured correctly. All previously migrated servers had to be remediated, and the migration stalled. The customer also identified that the instances were as large as five times the initial estimates, so they implemented a cost checkpoint at the end of each migration wave.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
