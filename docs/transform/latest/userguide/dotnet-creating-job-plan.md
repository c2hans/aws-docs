---
source_url: https://docs.aws.amazon.com/transform/latest/userguide/dotnet-creating-job-plan.html
---

# Creating the AWS Transform .NET job plan
<a name="dotnet-creating-job-plan"></a>

After you create your workspace, on the **Jobs** tab, select **Create job**. Then follow the prompts from AWS Transform in the chat pane using natural language. These are the typical steps for creating a .NET modernization job.

1. AWS Transform will ask you which type of transformation job you would like to create. In the chat, enter *.NET modernization*.

1. AWS Transform will suggest a job name and ask you if you want to change the job name. If you would like to change the job name, tell AWS Transform in natural language, for example, *change the job name to ExampleCorpDotNet1*. Otherwise, in the chat, you can accept the suggested job name. After you accept the job name, AWS Transform notifies you in the chat window that it is creating the job.

1. AWS Transform creates the transformation job.

## Components of the AWS Transform .NET job plan
<a name="dotnet-job-plan-components"></a>

The AWS Transform .NET job display has 5 tabs which you select from the vertical icons on the far left: **Tasks**, **Dashboard**, **Approvals**, **Artifacts**, and **Worklog**. Each tab has a left pane and a center chat pane. A right collaboration pane may appear at times to show additional details and to request human input.

### Tasks (Job Plan)
<a name="tasks-job-plan"></a>

This tab displays your job plan in the left pane. A .NET job has 5 steps:

1. *Get resources to be transformed*: In this phase, you create a connector to your code repository using AWS CodeConnections. Depending on your repository permissions, an admin of the code repository may need to approve the connector and give AWS Transform access to the repository.

1. *Discover resources for transformation*: In this phase, AWS Transform discovers repositories in source control, and you select some or all of them for assessment.

1. *Assess code for transformation*: Selected repositories are assessed, and you can view assessment reports.

1. *Prepare for transformation*: In this phase, AWS Transform notifies you if any dependencies are missing from your repositories. You can upload the missing dependencies or ignore them. If you are not an admin for the repo, an admin may need to approve the final transformation plan.

1. *Transform*: In this phase, AWS Transform transforms your repo and provides you the ongoing status during the transformation until it's completed. You can review transformation reports to understand what was changed and why.

You can see the status for each step:
+ Not started
+ Await user input
+ In Progress
+ Completed

### Dashboard
<a name="dashboard-tab"></a>

The **Dashboard** tab provides a high level summary of the transformation. It displays metrics for the number of jobs transformed, transformation applied, and estimated time to complete the transformation. Below the dashboard is a table of repositories and their status - In-progress, Failed, or Success.

### Approvals
<a name="approvals-tab"></a>

Approval requests for the job are displayed and completed on this tab.

### Artifacts
<a name="artifacts-tab"></a>

Jjob-related artifacts are uploaded or downloaded from this tab.

### Worklog
<a name="worklog-tab"></a>

AWS Transform logs its actions in the **Worklog** tab. The **Worklog** provides a detailed log of the actions AWS Transform takes, along with human input requests, and your responses to those requests.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transform` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
