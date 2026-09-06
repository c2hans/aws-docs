---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/task-two-drafts-runbooks.html
---

# Task 2: Creating drafts of the migration runbooks
<a name="task-two-drafts-runbooks"></a>

In this task, you draft and review migration runbooks for each migration pattern. For example, you draft a migration runbook for rehost to Amazon EC2 and another runbook for replatform to Amazon RDS. You repeat this task until you have drafted a migration runbook for every migration pattern identified in the previous task.

You can use the attached runbook templates and customize them for your environment. For migration patterns that are repeated frequently, we recommend using the *Rehost migration runbook template* (Microsoft Word format), and for patterns that are one-off or very simple, we recommend the *Rehost migration task list template* (Microsoft Excel format). You can also use a task list to track the status of tasks that are documented in a runbook. For more information, see [About the runbooks, tools, and templates](introduction.md#about-components).

This task consists of the following steps:
+ [Step 1: Create a migration runbook draft for each pattern](#step-one-create-runbooks)
+ [Step 2: Update the migration runbooks with your policies and processes](#step-two-update-runbooks)

## Step 1: Create a migration runbook draft for each pattern
<a name="step-one-create-runbooks"></a>

In this step, you draft runbooks for each of your migration patterns. A complete migration runbook typically contains instructions for how to use the selected migration service or tool, any tasks that are unique to your environment, and cutover instructions.

1. Open the attached *Rehost migration runbook template* (Microsoft Word format).

1. Update the *Premigration tasks* section, *Migration tasks* section, and *Cutover tasks *section with instructions that are specific to your migration pattern. Depending on your use case, you might need to update all three sections. Include the following when customizing your tasks:
   + **Standard migration instructions for the selected service** – You can typically find the information needed to complete your template in [AWS documentation](https://docs.aws.amazon.com/index.html). For example, see the following:
     + [How to use the new AWS Application Migration Service for lift-and-shift migrations](https://aws.amazon.com/blogs/aws/how-to-use-the-new-aws-application-migration-service-for-lift-and-shift-migrations/)
     + [Getting started with AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/getting-started.html)
     + [AWS Database Migration Service step-by-step walkthroughs](https://docs.aws.amazon.com/dms/latest/sbs/dms-sbs-welcome.html)
   + **Tasks that are unique to your IT environment** – Record the tasks that are unique to your IT operations and environment. The goal is that a new person joining your migration teams can follow the runbook with minimal learning curve. For example, what monitoring software do you need to install on the target machine after cutover? Which Domain Name System (DNS) server do you use for that subnet? How do you submit a request for change (RFC)?
   + **Cutover tasks** – Every environment has a slightly different cutover process. It is important to document all the steps for cutover in your environment because you want everyone to follow the same process. Documenting these steps minimizes time spent in the cutover window and helps you plan the amount of time needed to complete the cutover.

## Step 2: Update the migration runbooks with your policies and processes
<a name="step-two-update-runbooks"></a>

Runbook and task list templates cover the majority of the migration tasks, or the portion of the process that is standard. The remaining tasks are unique to your environment, and you must customize the runbook accordingly. For example, consider whether your runbooks should contain custom tasks for the following processes in your environment.

### Connectivity
<a name="connectivity.839ee633-bdae-57ee-81ac-859435bbd95f"></a>
+ How to connect to a VMware environment
+ How to connect to a DNS server and update DNS records
+ How to connect to the migration automation server
+ How to connect to the source environment
+ How to connect to a document repository, such as SharePoint or Confluence

### Permissions and change management
<a name="permissions-and-change-management.74f646d1-27c8-51fd-8bb2-21b27a102975"></a>
+ How to submit an RFC in your environment
+ How to review the status of the RFC for each wave
+ How to grant access for a new migration engineer
+ How to request permissions to the source servers
+ How to request permissions to the target AWS account
+ Who has permission to connect to the target server after the cutover

### Migration implementation and cutover
<a name="migration-implementation-and-cutover.4c7f131d-a74a-5651-b21c-36a25c0710fa"></a>
+ Which software to install or uninstall on the target server
+ How to change infrastructure settings, such as firewall, routing, and load balancer settings
+ Who can change infrastructure settings
+ How to change the application configuration during cutover
+ How to conduct application testing
+ How to complete a cutover and go-live
+ How to complete tasks that occur after cutover, such as configuring monitoring or backups

Some of these tasks might sound trivial, but knowledge and permissions vary in any environment. It is important to document these tasks in the same migration runbook.

**Tip**
We highly recommend using automation to accelerate your large migration. Using a migration factory model simplifies and reduces the number of issues with repetitive tasks, especially for rehost and replatform migration patterns. [AWS Cloud Migration Factory Solution](https://aws.amazon.com/solutions/implementations/aws-cloudendure-migration-factory-solution/) was designed to help customers migrate at scale with automation. You can deploy the solution and use predefined automation scripts in your runbook.

## Task exit criteria
<a name="task-two-drafts-runbooks-exit"></a>

Repeat this task as necessary, and when you have met the following exit criteria, proceed to the next task:
+ You have drafted a runbook for each migration pattern.
+ Each runbook draft contains three main sections: pre-migration tasks, migration tasks, and cutover tasks.
+ Your runbook drafts include tasks that are unique to your environment.
+ Your detailed runbook drafts include step-by-step guidance and screenshots.
