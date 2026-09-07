---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/phases.html
---

# Phases of a large migration
<a name="phases"></a>

AWS segments the large migration process into three sequential phases:

1. [Assess phase](#aboutassess) – You build the business case for the migration.

1. [Mobilize phase](#aboutmobilize) – You prepare the organization and mobilize the resources needed for the migration.

1. [Migrate and modernize phase](#aboutmigrate) – You use your strategy, plan, and the best practices to migrate and modernize. In this phase, migration is divided into two stages, initialize and implement.

The assess and mobilize phases are the foundation of any large migration and prepare the organization for the migration. This guide includes a brief summary of the first two phases and provides references for additional support. The primary purpose of this guide is to describe the migrate part of the third phase, migrate and modernize, and its two stages, initialize and implement. We recommend that you first migrate to the AWS Cloud and then modernize the workload. Modernization is not included in this documentation set for large migrations. For more information about modernization, see [Phased approach to modernizing applications in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-phased-approach/) on the AWS Prescriptive Guidance website.

The following figure shows the three phases of a large migration: assess, mobilize, and migrate and modernize. Migration is divided into two stages, initialize and implement.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/images/guide-img/a7434c46-8e52-4896-84b2-cc91433b5072/images/7105cf2e-2968-4996-a504-5dc697f07ce6.png)

Even though this document set for large migration is focused on the migrate phase, we highly recommend you go through all three phases of a large migration in sequence. Completing the assess and mobilize phases builds a solid foundation to support the migration.

## Assess phase
<a name="aboutassess"></a>

This is the start of your large-migration journey. In this phase, you build your business case for the large migration. You assess your organization's readiness for cloud transformation, take an initial look at your portfolio, and confirm that the key stakeholders in your organization are aligned.

For more information about the assess phase, see [Evaluating migration readiness](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-readiness/) on the AWS Prescriptive Guidance website.

## Mobilize phase
<a name="aboutmobilize"></a>

Now that you have built your business case for a cloud transformation, you use the readiness assessment from the previous phase and begin to fill in the gaps. You mobilize your organization and set up workstreams that prepare your organization for the large migration in the next phase. In this phase, you typically build your AWS landing zone, conduct a more thorough portfolio assessment, build your security and operating model, and prepare teams for change.

For more information about the mobilize phase, see [Mobilize your organization to accelerate large-scale migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/) on the AWS Prescriptive Guidance website.

## Migrate and modernize phase
<a name="aboutmigrate"></a>

After the mobilize phase, your organization should have a solid foundation and be ready to start migration and modernization. Before proceeding, you evaluate the foundations, including the people and the platform, and make sure they are ready to support a large migration. The key for this step is to build standard operating procedures and automations that simplify and accelerate a repeatable pattern. This approach is known as a *migration factory*.

Just like a manufacturing factory, when you build a migration factory, you must initialize and calibrate it, define the standard operating procedures, measure the factory's performance, and continually improve the process and tools. In a large migration, initialization is a critical first stage. Running and improving the factory is the second stage, implementation, which migrates your servers at scale in batches known as *waves*. You organize your resources into workstreams, which are focused on accomplishing one aspect of the large migration.

### About workstreams
<a name="about-workstreams.3906ef72-8d89-5480-88a7-5e9001e717ec"></a>

Each workstream in your large migration project is dedicated to completing certain tasks, and those tasks change as you progress from stage 1, initialization, into stage 2, implementation. Although each workstream is independent, they work together to accomplish the same goal—migrate servers at scale.

The following are the four core workstreams, and you can create additional, supporting workstreams as needed to support your use case:
+ **Foundation workstream** – This workstream is focused on preparing the people and platform for the large migration.
+ **Project governance workstream** – This workstream manages the overall migration project, facilitates communication, and focuses on completing the project within budget and on time.
+ **Portfolio workstream** – The teams in this workstream collect metadata to support the migration, prioritize applications, and perform wave planning.
+ **Migration workstream** – Using the wave plan and collected metadata from the portfolio workstream, the teams in this workstream migrate and cutover the applications and servers.

For more information and instructions about how to establish and resource the workstreams in your large migration project, see the [Foundation playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/).

### About the initialize and implement stages
<a name="about-the-initialize-and-implement-stages.03819874-13f7-56d3-ab21-366408b67e21"></a>

Migrate and modernize is the third and final phase of your migration journey. Generally, you migrate first and then modernize. Migrate consists of two stages:
+ **Stage 1: Initialize a large migration** – You prepare your platform and people for a large migration. For example, you review the landing zone design and verify that it has enough bandwidth to support the scale, and you design and implement a training plan. In this stage, based on your organization's policies and processes, you also define the standard operating procedures (or *runbooks*) for the large migration. The runbooks and automations simplify and accelerate implementation of the large migration in stage 2.
+ **Stage 2: Implement a large migration** – In this stage, you migrate servers at scale by using the runbooks defined in stage 1. You manage the migration factory with project governance tools, monitor the migration with a health-check matrix, and continuously improve the runbooks in order to increase the velocity of the migration.

|  |  |  |
| --- |--- |--- |
| Stage | Duration | Purpose |
| Stage 1: Initialize | 1–3 months | + Prepare your platform and people for a large migration.<br />+ Build your standard operating procedures (runbooks). |
| Stage 2: Implement | Varies by project scope and strategy | + Use runbooks to implement the large migration.<br />+ Manage, monitor, and improve the migration. |
