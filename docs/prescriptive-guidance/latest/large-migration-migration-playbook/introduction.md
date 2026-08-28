---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/introduction.html
---

# Migration playbook for AWS large migrations
<a name="introduction"></a>

*Wally Lu, Chris Baker, Tuhin Mukherjee, and Senay Swinney, Amazon Web Services*

In a large migration, the migration workstream uses the wave plans and migration metadata supplied by the portfolio workstream in order to migrate workloads to the AWS Cloud. The migration workstream is responsible for submitting any change requests, migrating the application, coordinating application testing with the application owners, performing cutover, and monitoring the application through the hypercare period. In the first stage, initializing a large migration, you create the runbooks that the migration workstream uses to migrate the applications and servers. In the second stage, implementing a large migration, the migration workstream plans sprints and uses the migration runbooks in order to migrate and cutover the applications. For more information about core and supporting workstreams, see [Workstreams in a large migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/workstreams.html) in the *Foundation playbook for AWS large migrations*.

This migration playbook outlines the tasks of the migration workstream, which spans both stages of a large migration, initialization and implementation:
+ In stage 1, *initialize*, you draft, test, and refine the runbooks, and then you automate manual tasks for each migration pattern.
+ In stage 2, *implement*, you perform the migration with the predefined runbooks built in stage 1.

## Guidance for large migrations
<a name="guidance-large-migrations"></a>

Migrating 300 or more servers is considered a large migration. The people, process, and technology challenges of a large migration project are typically new to most enterprises. This document is part of an AWS Prescriptive Guidance series about large migrations to the AWS Cloud. This series is designed to help you apply the correct strategy and best practices from the outset, to streamline your journey to the cloud.

The following figure shows the other documents in this series. Review the strategy first, then the guides, and then proceed to the playbooks. To access the complete series, see [Large migrations to the AWS Cloud](https://aws.amazon.com/prescriptive-guidance/large-migrations/).

![The structure of the AWS large migration document series](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/images/guide-img/0d30bbed-378d-4378-8100-0dcb44a0211f/images/87e66cc2-2cff-4e58-a503-c32149e3e6df.png)

## About the runbooks, tools, and templates
<a name="about-components"></a>

We recommend using the attached templates and then customizing them for your portfolio, processes, and environment. The provided templates include standard processes, typical cutover processes, and placeholders for processes that are unique to your environment. The instructions in this playbook tell you when and how to customize each of these templates. This playbook includes the following templates:
+ Rehost migration runbook template
+ Rehost migration task list template

For migration patterns, from which you can build your own runbooks, see [AWS Prescriptive Guidance migration patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migration-pattern-list.html).

Migration runbooks require varying levels of detail:
+ **Detailed runbooks** – Detailed runbooks are best suited for migration patterns that you will repeat many times. For these patterns, we recommend starting with the *Rehost migration runbook template* (Microsoft Word format). This template captures as many details as possible, including screenshots and step-by-step instructions, and it is designed to help multiple people perform the same task consistently.
+ **Task List** – For migration patterns that are one-off or very simple, a short task list is a better option. For these patterns, we recommend starting with the *Rehost migration task list template* (Microsoft Excel format). This template contains a high-level task list and is typically used for tracking and managing ownership of tasks. You can also use a task list to track the status of tasks that are documented in a runbook.

Whether you are using a detailed runbook or a short task list, verify that your runbook describes the tasks in sequence. For complex tasks, you can provide links to external documentation.

## Attachments
<a name="attachments-0d30bbed-378d-4378-8100-0dcb44a0211f"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
