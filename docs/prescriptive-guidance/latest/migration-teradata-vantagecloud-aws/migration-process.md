---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-teradata-vantagecloud-aws/migration-process.html
---

# Migration process
<a name="migration-process"></a>

Not every enterprise that implements a migration strategy does so by transferring all of its data to the cloud at the same time. In fact, many organizations take an iterative approach to cloud migration that's driven by both business and technical demands. You can find more about the deployment options in [On-premises to Cloud Migration](https://www.teradata.com/insights/data-platform/on-premises-to-cloud-migration) on the Teradata website.

When you're ready to migrate your data from Teradata Vantage in an on-premises environment to Teradata VantageCloud Enterprise on AWS, you can use the Teradata migration framework as a guide for each step of the process. The framework covers the entire span of a cloud migration—from design through go live, from the Teradata platform to the ecosystem connecting to it. The framework provides guidance for internal and external teams, and gives you a reliable, fast, and effective roadmap for migrating to and taking advantage of Teradata's cloud offerings.

The following diagram shows the framework phases that you can use to plan your migration.

## Design
<a name="design-stage"></a>

The goals of the Design phase are to determine your migration readiness and secure an agreement with your stakeholders on a common migration approach. This phase consists of the following stages:
+ Initiate – Set stakeholder expectations.
+ Assess – Complete a high-level assessment.
+ Design solution – Complete a detailed assessment, design, and approach.

These are some of the roles we recommend that you engage during the Design phase to provide input to the requirements:
+ Your project sponsor and business users
+ Your Data Analytics Architect and Ecosystem Architect
+ Your Information Security Architect
+ Your Data Warehouse Lead
+ Your Test Lead

These are some of the Teradata roles which are involved in the Design phase and will lead the requirement discussions:
+ Teradata account team
+ Teradata Solution Engineer
+ Teradata Cloud Architect

At the end of the Design phase, you will have detailed architecture diagrams, a high-level timeline, and an initial list of critical dependencies and risks. You will also have an agreement on the overall migration approach.

## Connect
<a name="connect"></a>

The goals of the Connect phase are to confirm your migration readiness, deploy your cloud instance or instances, and complete a detailed plan. The Connect phase consists of the following stages:
+ Test strategy and success criteria – Define what success looks like.
+ Onboarding – Provision and deploy your cloud instance or instances.
+ Implementation plans – Define a detailed implementation plan.

These are some of the roles that we recommend you engage during the Connect phase to provide input to the detailed planning:
+ Your project sponsor and business users
+ Your Data Analytics Architect and Ecosystem Architect
+ Your Information Security Architect
+ Your Data Warehouse Lead
+ Your IT Leads for areas such as firewalls and network connectivity
+ Your Test Lead
+ Your Project Manager

These are some of the Teradata roles which are involved in the Connect phase and will lead the requirement discussions:
+ Teradata Solution Engineer
+ Teradata Cloud Architect
+ Teradata Service Experience Manager
+ Teradata Cloud provisioning team
+ Teradata Cloud support teams
+ Teradata Project Manager
+ Teradata Migration Consultant
+ Teradata Cloud Implementation Manager

At the end of the Connect phase, you will have a test strategy, a deployed cloud instance, a detailed implementation plan, and an agreement that you're ready to begin the implementation of your migration plan.

## Execute
<a name="execute-stage"></a>

The goals of the Execute phase are to prepare an environment to support your testing, complete all pre-migration testing, and execute the migration plan. This phase consists of the following stages:
+ Convert – Migrate test data to the cloud systems and convert extract, transform, and load (ETL) and/or business intelligence (BI) workloads if required.
+ Validate the platform and ecosystem – Regression test any converted ETL and/or BI workloads, test Teradata and third-party applications, and complete performance testing.
+ Migrate, validate, and catch up data – Execute a detailed migration plan.

These are some of the roles that we recommend you engage during the Execute phase to complete the migration:
+ Your project sponsor and business users
+ Your Data Warehouse Lead
+ Your ETL and BI Leads
+ Your Test Lead and testing teams
+ Your IT Leads for areas such as firewalls and network connectivity
+ Your Project Manager

These are some of the Teradata roles which are involved in the Execute phase:
+ Teradata Migration Consultant
+ Teradata Service Experience Manager
+ Teradata Cloud support teams
+ Teradata Project Manager
+ Teradata Migration Consultant
+ Teradata Cloud Implementation Manager

At the end of the Execute phase, your on-premises Teradata environment will be live in Teradata VantageCloud Enterprise on AWS.

## Go Live
<a name="golive-stage"></a>

The goals of the Go Live phase are to optimize the cloud system and transition to operational support. The Go Live phase consists of the following stages:
+ Optimize – Complete workload management and other post-migration work.
+ Transition – Complete transition to operational support teams.

These are some of the roles that we recommend you engage during the Go Live phase:
+ Your Data Warehouse Lead
+ Your IT Leads for areas such as firewalls and network connectivity
+ Your Test Lead
+ Your Project Manager

These are some of the Teradata roles which are involved in the Go Live phase:
+ Teradata Service Experience Manager
+ Teradata Cloud support teams
+ Teradata Project Manager
+ Teradata Cloud Implementation Manager

At the end of the Go Live phase, your Teradata VantageCloud Enterprise system will be live on AWS, ongoing operational support will be initiated, and post-migration activities will be completed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
