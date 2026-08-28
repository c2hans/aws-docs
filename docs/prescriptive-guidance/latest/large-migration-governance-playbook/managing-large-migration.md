---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/managing-large-migration.html
---

# About managing a large migration
<a name="managing-large-migration"></a>

To manage and effectively govern a large migration project, the project manager needs to have a high-level understanding of the portfolio, the phases of a large migration, and the responsibilities of each workstream.

**This section contains the following topics:**
+ Workstreams in a large migration
+ Feeding the migration pipeline
+ Hypercare period
+ Establishing an agile approach

## Workstreams in a large migration
<a name="large-migration-workstreams"></a>

In the migrate phase, at any given time, a minimum of four workstreams are operating simultaneously: the foundation, project governance, portfolio, and migration workstreams. These are the core workstreams of any large migration project, and your project might have additional, supporting workstreams. For more information, see [Workstreams in a large migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/workstreams.html) in the *Foundation playbook for AWS large migrations*.

## Feeding the migration pipeline
<a name="migration-pipeline"></a>

In the migration factory, wave planning and migration occur at the same time and operate continuously. The portfolio team feeds the migration pipeline by planning waves, and the migration team completes the pipeline by performing the migration and cutting over workloads. The portfolio team prepares five waves at the end of the initialization stage, and the implementation stage begins when the migration team begins migrating one or more of the prepared waves.

For each wave, the portfolio workstream runs 1–2 weeks, and the migration workstream typically runs 3–4 weeks. The portfolio workstream is five waves ahead of the migration workstream, so there is always a five-wave buffer between the portfolio and migration workstreams. Throughout the implementation stage, both the portfolio team and the migration team continue to process waves, and the buffer prevents the migration workstream from running out of servers to migrate. For an example of a wave schedule, see [Stage 2: Implementing a large migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/stage2.html) in the *Guide for AWS large migrations*.

The portfolio team prioritizes applications and then assigns them to waves in logical move groups. When planning waves, the portfolio team considers migration complexity, application similarities, and application and infrastructure dependencies. This helps make sure that the applications and their dependencies are migrated in their entirety. For more information about wave planning, see the [Portfolio playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/). For project governance, you manage and track information about the waves and sprints, including the applications, servers, and application owners. You might use a dashboard on a Confluence site, a list in Microsoft Excel, or a combination of tools.

## Hypercare period
<a name="hypercare-period"></a>

After you have completed the cutover, the migrated applications and servers enter the *hypercare period*. In the hypercare period, the migration team manages and monitors the migrated applications in the cloud in order to address any issues. Typically, this period is 1–4 days in length. At the end of the hypercare period, the migration team transfers responsibility for the applications to the cloud operations (Cloud Ops) team. At this time, the wave is considered complete.

## Establishing an agile approach
<a name="establish-agile-approach"></a>

By establishing an agile approach, the project team can remain flexible and quickly adapt to change during the migration. We recommend adopting a Scrum framework for a large migration. In the [Migration playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/), you assign waves to *sprints*, which is a fixed period of time in which the migration team works on all waves within that sprint. If each sprint is 2 weeks in duration, each wave spans at least two sprints. A sprint consists of standard events, such as planning the sprint and conducting daily stand-up meetings, a review, and a retrospective.

You use a *sprint backlog*, which consists of the current and pending tasks in the sprint, to manage the activities. In this playbook, you select a project management tool for tracking progress. You might select a project or issue-tracking application, such as Jira or Confluence, and you might also select a visual approach of representing tasks, such as a Kanban board or a Gantt chart. By tracking the sprint backlog in one or more of these tools, you provide project transparency, assign owners to each task, and establish clear deadlines.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
