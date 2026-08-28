---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/task-four-migration-runbooks.html
---

# Task 4: Improving your migration runbooks
<a name="task-four-migration-runbooks"></a>

In this task, you improve the runbooks by repeating the POC multiple times. With each wave, the POC test and *retrospective*, a meeting in which the team reviews the completed wave, provide opportunity to improve the runbooks. You also improve your runbooks by automating repetitive tasks, which increases the velocity of the migration and reduces the risk of manual configuration errors.

This task consists of the following steps:
+ [Step 1: Update the migration runbooks and repeat the testing](#step-one-repeat-testing)
+ [Step 2: Automate repetitive tasks](#step-two-automate-tasks)
+ [Step 3: Build a migration task list](#step-three-build-list)

## Step 1: Update the migration runbooks and repeat the testing
<a name="step-one-repeat-testing"></a>

1. For the issues and gaps identified in the previous task, update the runbooks with detailed instructions. For example:
   + If a step is missing, add step-by-step instructions
   + If a step is not clear, consider updating the text, adding a screenshot, or adding reference links

1. Repeat the previous task until you are satisfied that the instructions are complete and clear.

1. Test the final draft of each runbook by asking a new migration team member, one who has not tested this runbook before, to perform a POC and complete the runbook.

## Step 2: Automate repetitive tasks
<a name="step-two-automate-tasks"></a>

1. Review each runbook and identify areas of automation for manual tasks. Consider the following probing questions:
   + Are there any repetitive, manual tasks for each server or app in the runbook?
   + Are there any actions that you perform on every server or application?
   + Do you need to install or uninstall software on the target server?
   + Do you need to change network or infrastructure settings one by one for each server?
   + Do you need to manually copy and paste any data?

1. Build automation scripts and update the runbooks.

1. Repeat task 3 and task 4 until you have documented the runbooks with clear and complete information and automated repetitive migration tasks.

**Note**
For automating migration tasks, we highly recommend that you build new scripts or customize existing scripts in [AWS Cloud Migration Factory Solution](https://aws.amazon.com/solutions/implementations/aws-cloudendure-migration-factory-solution/).

## Step 3: Build a migration task list
<a name="step-three-build-list"></a>

A migration task list can help you manage the status and owners of tasks. You build a task list for each migration runbook, and you include the high-level information from the runbook without including the details. A task list typically contains the following information, and you can add more attributes as needed:
+ Descriptive name, such as:
  + Check server OS version
  + Install an agent
  + Restart a server
  + Update the DNS
+ Dependencies
+ Sequence of tasks
+ Owner
+ Estimation of time required to complete each task
+ Status

There are many tools available for creating and managing task lists. You can use the attached *Rehost migration task list template* (Microsoft Excel format). You can also use project management tools, such as Jira or a Kanban board.

**Note**
We also recommend using the Excel task list template to document small, well-understood, or non-repetitive tasks, such as restarting a server or getting an IP address. These tasks should be captured and tracked but don't require the detailed steps of the Word runbook template.

## Task exit criteria
<a name="task-four-migration-runbooks-exit"></a>

Repeat this task as necessary, and when you have met the following exit criteria, proceed to the next task:
+ You have identified opportunities for automation and have either developed automation scripts or have a plan to do so.
+ Three or more people have peer-reviewed each runbook.
+ Two or more people who were not on the development team for the runbook have tested it end-to-end.
+ Using the most up-to-date runbook, you have migrated 20 or more servers to more than one AWS account.
+ You have developed a task list to help track and manage the progress of the migration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
