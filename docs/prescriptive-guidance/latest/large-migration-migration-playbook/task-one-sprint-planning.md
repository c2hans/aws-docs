---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/task-one-sprint-planning.html
---

# Task 1: Performing sprint planning for scheduled waves
<a name="task-one-sprint-planning"></a>

In this task, you assign waves to *sprints*, which is a fixed period of time in which the migration team works on all waves within that sprint. If each sprint is 2 weeks in duration, each wave spans at least two sprints. *Sprint planning* refers to the process of assigning owners and due dates to all of the tasks within that sprint.

This task consists of the following steps:
+ [Step 1: Review the backlog for the scheduled waves](#step-one-review-backlog)
+ [Step 2: Assign tasks and establish due dates](#step-two-assign-tasks)

## Step 1: Review the backlog for the scheduled waves
<a name="step-one-review-backlog"></a>

In this step, you review existing *backlogs*, or current and pending tasks, for all the concurrent waves, and you use the recommended tools and mechanisms to manage the wave. For example, you might use a Kanban board with a swimlane for each wave, or you might use Jira and track waves with stories and epics. For more information, refer to the [Project governance playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/).

## Step 2: Assign tasks and establish due dates
<a name="step-two-assign-tasks"></a>

In this step, for all waves in this sprint, you assign owners to each task and set a due date accordingly. You can use the migration task list spreadsheet you created in stage 1 to manage your wave progress, task ownership, and due dates, and the tasks are defined in detail in the migration runbook for each pattern. Because waves typically overlap, it is common to manage many concurrent tasks from different waves at the same time. In addition, each wave can range from 3-6 weeks, depending on your internal process. For an example of a wave schedule, see the [Stage 2: Implement a large migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/stage2.html) section of the *Guide for AWS large migrations*.

**Important**
Do not add tasks to the sprint without updating the runbook or task list. These documents that you built in stage 1 should be a source of truth for all your migration activities. If any step is missing or incorrect, update and validate the runbook before adding tasks to the sprint.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
