---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/stage1.html
---

# Stage 1: Initializing a large migration
<a name="stage1"></a>

In the initialize stage, it is critical to define the standard operating procedures, or *runbooks*, for most of the migration tasks. Because there are many people, processes, and tools involved in a large migration, you can improve efficiency by defining, connecting, and automating procedures in a runbook. Runbooks provide clear guidance that everyone must follow. Implementing a large migration without runbooks increases the complexity of the migration and might cause the migration effort to lose momentum or fail. To help you get started, this guide reviews the workflow and playbooks, which contain useful templates for building your own runbooks.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/images/guide-img/a7434c46-8e52-4896-84b2-cc91433b5072/images/c673619d-c28c-4e94-8cfc-71fc094d27ac.png)

The playbooks help you complete the first stage, *initialize*, and prepare for the second stage, *implement*:

1. [Foundation playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/) – This playbook helps you prepare your infrastructure and people.

1. [Project governance playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/) – This playbook helps you build project governance processes and tools that effectively manage a large migration project. It includes templates to help you get started.

1. [Portfolio playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/) – This playbook helps you build your own portfolio runbooks for wave planning and portfolio assessment. It includes templates to help you get started.

1. [Migration playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/) – This playbook helps you build a runbook for each migration pattern. It includes several templates for different patterns.

1. **Health-check matrix for AWS large migrations** – The attached *health-check matrix* helps you apply best practices and evaluate the efficiency and progress of your large migration throughout the life cycle of the project.

## Step 1: Use the foundation playbook to get ready
<a name="step1-1"></a>

In this playbook, you get your platform and people ready.

The following are examples of how you might prepare the people in your organization:
+ Make sure your stakeholders are committed to the migration and ready to provide support.
+ Define the workstreams in your large migration.
+ Define your Cloud Enablement Engine, also known as *Cloud Center of Excellence*, team.
+ Create a responsibility assignment model, in the form of a responsible, accountable, consulted, informed (RACI) matrix.
+ Establish a training plan for your migration resources.

The following are examples of how you might prepare your organization's platform:
+ Get the AWS landing zone ready to support a large migration.
+ Evaluate the readiness of your on-premises infrastructure.

For more information, see the [Foundation playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/).

## Step 2: Use the project governance playbook to define the rules
<a name="step1-2"></a>

In this step, you define the rules, boundaries, and plans for running the large migration. This includes defining the following plans and processes:
+ Communication plan
+ Benefit-tracking office
+ Escalation process
+ Migration and cutover communication gates
+ Project management processes and tools

For more information, see [Introduction to governance for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-intro-governance/) and the [Project governance playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/).

## Step 3: Use the portfolio playbook to create portfolio runbooks
<a name="step1-3"></a>

Now, you get a better understanding of the scope and strategy. In this step, you follow the portfolio playbook to build detailed runbooks for portfolio assessment and wave planning. The goal is to make sure the migration factory doesn't run out of raw materials (servers) and has all the information needed to support the migration. Tasks include the following:
+ Review the migration strategy from the mobilize phase (if you defined it in that phase). For more information, see [About the migration strategies](migration-strategies.md).
+ Define metadata requirements for each migration pattern.
+ Define the metadata collection process and a metadata storage location that serves as a single source of truth.
+ Define application prioritization rules.
+ Define application deep dive rules.
+ Define the wave planning process.

For more information, see the [Portfolio playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/).

## Step 4: Use the migration playbook to build a migration runbook for each pattern
<a name="step1-4"></a>

This step can run in parallel with the previous step. Using the migration playbook, you build your runbook for each of the migration patterns, such as rehosting to Amazon Elastic Compute Cloud (Amazon EC2) with AWS Cloud Migration Factory, or replatforming storage to Amazon Elastic File System (Amazon EFS) with AWS DataSync. You repeatedly test the runbooks until there are minimal to no errors. Tasks include the following:
+ Understand the migration patterns.
+ Get the runbook templates and add your on-premises process and tools.
+ Test and improve the runbooks.
+ Automate the runbooks as much as possible.

For more information, see the [Migration playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/).

## Step 5: Use the health-check matrix to evaluate your current state
<a name="step1-5"></a>

In this final step, you verify that your project team has completed the previous steps and identify any remaining gaps. Evaluating the health of the migration and improving the process are critical to the migration's success and helps maintain alignment with best practices.

Use the attached health-check matrix to evaluate the current state of your migration from a people, process, and technology perspective. This is not a one-off process. You should perform this evaluation on a regular basis.
