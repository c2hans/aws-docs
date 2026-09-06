---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/introduction.html
---

# Project governance playbook for AWS large migrations
<a name="introduction"></a>

*Bill David, Pratik Chunawala, Wally Lu, Tuhin Mukherjee, Amit Rudraraju, and Senay Swinney, Amazon Web Services*

**Note**
The project teams, roles, and workstreams referenced in this guide are described in the [Foundation playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/). We recommend completing the foundation playbook in advance of starting the project governance tasks in this guide.

Effective project governance is critical to the success of a large migration to the AWS Cloud. *Project governance* defines the rules, boundaries, and plans for completing the migration. Common project governance tools include a communication plan, benefit-tracking office, escalation plan, and quality gates for migration and cutover. By completing this playbook, you create and customize the governance that defines how to run your migration project.

In the third phase of a large migration, *migrate and modernize*, you refine your project governance model and create many of the tools and templates that you use during the migration. You should complete the assess and mobilize phases prior to starting this process. For more information about the phases of a large migration, see [Phases of a large migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/phases.html) in the *Guide for AWS large migrations*.

This playbook provides a step-by-step approach to quickly develop an effective governance model for a large migration project. It describes project governance for a large migration, which spans both stages of the migrate phase, initialization and implementation:
+ In stage 1, *initialize*, you assess team readiness and stand up the governance model. You define the processes and tools that govern your large migration project. At the end of stage 1, you have project governance tools that are customized for your own use case.
+ In stage 2, *implement*, you use the tools you created in the previous stage in order to adhere to your project governance plan.

## Guidance for large migrations
<a name="guidance-large-migrations"></a>

Migrating 300 or more servers is considered a large migration. The people, process, and technology challenges of a large migration project are typically new to most enterprises. This document is part of an AWS Prescriptive Guidance series about large migrations to the AWS Cloud. This series is designed to help you apply the correct strategy and best practices from the outset, to streamline your journey to the cloud.

The following figure shows the other documents in this series. Review the strategy first, then the guides, and then proceed to the playbooks. To access the complete series, see [Large migrations to the AWS Cloud](https://aws.amazon.com/prescriptive-guidance/large-migrations/).

![The structure of the AWS large migration document series](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/images/guide-img/9f06e3cb-7482-4241-b514-429f3118a677/images/1ea127a7-940e-4b5d-b819-67f5ce31c66a.png)

## About the tools and templates
<a name="abouttools"></a>

In this playbook, you create the following tools. You use these tools to communicate with the project stakeholders, including the migration teams, application owners, project sponsors, and executive leadership. The goal of the following tools is to maximize transparency for all project activities, which helps to accelerate the large migration:
+ Kickoff presentation
+ Meeting plan, including types and cadence
+ Escalation plan
+ Weekly project status report
+ Wave workshop
+ Cutover readiness assessment presentation
+ Steering committee status report
+ Benefit-tracking office
+ Project summary dashboard
+ Financial reporting process
+ Resource plan
+ Decision log
+ Risks, actions, issues, and dependencies (RAID) log
+ Communication plan and templates, such as gate communications and reminders

We recommend using the attached templates and then customizing them for your portfolio, processes, and environment. The templates are designed to foster effective communication, set clear expectations, and align executive leadership, application owners, and migration project stakeholders. The instructions in this playbook provide context as to the purpose of each of these templates, which your team can customize. This playbook includes the following templates:
+ **Cutover readiness assessment template** – This template helps you track the progress of each wave through the quality gates and key project management milestones.
+ **Financial glide path template** – This template is used to review financials with your project sponsors on a regular cadence.
+ **Kickoff presentation template** – You use this presentation template at a kickoff meeting early in stage 1.
+ **Meeting plan template** – You use this template to define the types of recurring meetings, establish their cadence, and identify the key participants.
+ **Status report template** – You use this template in order to create a standard presentation format for the project status review meetings.
+ **Steering committee meeting template** – You use this template in order to create a standard presentation format for the steering committee meetings.
+ **Wave workshop template** – You use this template in order to create a standard presentation for the T-14 and T-28 commit meetings.
+ **Gate communication templates **– You use these email communication templates to share the status of the wave with project stakeholders and inform them of recent changes or upcoming activities. This playbook includes the following templates:
  + Communication template for cutover complete
  + Communication template for hypercare complete
  + Communication template for T-0
  + Communication template for T-1
  + Communication template for T-7
  + Communication template for T-14
  + Communication template for T-21
  + Communication template for T-28

## Attachments
<a name="attachments-9f06e3cb-7482-4241-b514-429f3118a677"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
