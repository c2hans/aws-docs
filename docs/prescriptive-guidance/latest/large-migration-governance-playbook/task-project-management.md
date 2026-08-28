---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/task-project-management.html
---

# Task: Defining project management processes and tools
<a name="task-project-management"></a>

Any large migration project requires well established management processes and tools. With a large migration, there are nuances to sharing information, tracking performance metrics, identifying the correct meeting participants, and assigning tasks to owners. In this task, you document key migration tasks and owners, determine key performance indicators (KPIs) for the migration and decide how to measure them, track the budget, and develop tools for managing risks and tracking decisions.

Many of the steps in this task are performed concurrently, unless otherwise noted. Typically, you complete these steps before or just after the kick-off meeting.

In this task, you do the following:
+ [Step 1: Select a project management tool](#step-pm-tool)
+ [Step 2: Validate roles and responsibilities for all migration activities](#step-validate-roles)
+ [Step 3: Establish a benefit-tracking office](#step-benefit-tracking-office)
+ [Step 4: Create a project summary dashboard](#step-dashboard)
+ [Step 5: Create a financial reporting process](#step-financial-reporting)
+ [Step 6: Determine how to manage and scale resources](#step-resource-plan)
+ [Step 7: Create a decision log](#step-decision-log)
+ [Step 8: Create a RAID log](#step-raid-log)

## Step 1: Select a project management tool
<a name="step-pm-tool"></a>

In this step, you establish the tools you want to use for tracking progress. You might choose to use a software solution such as Jira or Confluence, build your own dashboards in Microsoft Excel, or use a combination of these tools. Consider the following best practices when selecting or building project management tools:
+ For tracking tasks and tracking progress, we recommend a visual management tool such as a Kanban board or Gantt chart, which are commonly available in project management applications. Visual management tools are particularly effective in the daily stand-up meetings for reviewing current tasks and wave progress.
+ If you are selecting a project management application, consider whether you want to enter plans and processes (such as an escalation plan, decision log, or RAID log) in your project management tool, and make sure that it has the features you want.
+ It is important that the project sponsor, executive leaders, project managers, and external stakeholders (if any) are aligned on the selected tool.

For more information about how these tools are used, see [Establishing an agile approach](managing-large-migration.md#establish-agile-approach).

## Step 2: Validate roles and responsibilities for all migration activities
<a name="step-validate-roles"></a>

In the [Foundation playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/), you created a detailed RACI matrix for each migration strategy and high-level task in your large migration project. A *RACI matrix* is a responsibility assignment tool, and the name is derived from the four responsibility types defined in the matrix: responsible (R), accountable (A), consulted (C), and informed (I). This matrix format is recommended to align roles and responsibilities across all of the migration activities. This matrix can align on-site teams with remote teams or external partners. In this step, you validate the matrices are correct and review them with the project teams.

In order to tailor the RACI tasks for your organization, we recommend you consider the following:

Understand the change management processes, the lead times required for those processes, and the roles involved in approving changes. For more information, see [Step 6: Understand the change management process](task-communication-plan.md#step-change-management).

Make sure that you have vetted your back-up and disaster recovery strategy prior to starting the migration, and share this strategy with the migration team. If you identify gaps in the strategy, we recommend you use integrated cloud services, such as AWS Backup or CloudEndure Disaster Recovery.

Do the following:

1. If you haven't done so already, create a RACI matrix for each high-level task according to the instructions in the [Foundation playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/).

1. Review the matrices with the respective teams in each matrix. Confirm that all detailed tasks are represented and that the teams are familiar with their responsibilities.

1. Update and create new matrices throughout the migration as you identify new migration strategies or supporting tasks.

## Step 3: Establish a benefit-tracking office
<a name="step-benefit-tracking-office"></a>

This team is a small group of individuals who are responsible for assessing the migration against key performance indicators (KPIs). This team evaluates whether the migration is progressing according to schedule and can act on any delays or issues impeding progress. This team meets outside of the weekly or bi-weekly project status meetings.

In each meeting, this team usually reviews and answers the following questions:
+ What is the current status of the migration?
+ Are we on track to achieve our target outcomes?
+ Are we measuring performance accurately?
+ Do we need to make any adjustments in order to accelerate the migration?

If the benefit-tracking office determines that the migration isn't achieving the desired velocity, this team should recommend adjustments to process, resourcing, or communications plans.

Do the following to establish a benefit-tracking office for your large migration:

1. Identify the appropriate participants. Typical members of this team include the project sponsor, project manager, migration lead, and an empowered representative from each business unit that has workloads in scope.

1. Establish a regular meeting cadence for the benefit-tracking office. We recommend this team meets once every two weeks.

1. Define qualitative and quantitative KPIs for the large migration with the project sponsor, and collect input from executive leadership. The benefit-tracking office assesses the progress of the migration against your KPIs. Examples of KPIs include:
   + (Quantitative) Actual number of servers migrated compared to plan
   + (Quantitative) The number of servers decommissioned compared to plan
   + (Qualitative) Review of survey feedback and action plan
   + (Qualitative) Corrective steps made in response to survey feedback

## Step 4: Create a project summary dashboard
<a name="step-dashboard"></a>

The project team must work with key project stakeholders collectively to develop a dashboard that clearly conveys how the migration is progressing. Your project summary dashboard should do the following on a single page:
+ Quantifies the overall completed and remaining workloads for the whole project
+ Reflects the performance of the most recently completed wave (planned and actuals)
+ Shows the anticipated workloads in the upcoming wave (planned)

We recommend starting with the attached *Project summary dashboard template* (Microsoft PowerPoint format). Do the following:

1. Modify the template as needed for your project. We recommend representing the allocation of servers to each migration strategy. The provided template includes the rehost and replatform migration strategies.

1. Review your project summary dashboard with the project stakeholders, including executive leadership, and make sure that all stakeholders are aligned and understand how to use and access the dashboard.

1. Save the dashboard in a shared repository. All stakeholders should be able access this information themselves as needed.

## Step 5: Create a financial reporting process
<a name="step-financial-reporting"></a>

Typically, you track financial reporting separately from the project status report because you want to provide it to a more limited audience. The financial report should include the *actual costs*, which are the costs incurred to date, and the *forecasted costs*, which are the expected costs for the remainder of the project. You track internal and external resource costs separately. To assess actual and forecasted internal resource costs, you can use in-house time reporting and your resource plan. For external resources, you should ask your partners or consultants to provide actual and forecasted costs.

We recommend starting with the attached *Financial glide path template* (Microsoft PowerPoint format). Do the following:

1. Determine the stakeholders who should receive this financial report.

1. Determine whether this financial report will be shared in a meeting or through email.

1. Modify the template as needed for your project.

1. Review your financial report with the executive leadership team or project sponsors to confirm alignment on the format and content.

1. With the stakeholders, determine how frequently this report will be updated and reviewed.

1. Determine where you will save this financial report. Because it contains sensitive financial information, we don't recommend saving this template in the shared repository with the rest of the project documentation.

## Step 6: Determine how to manage and scale resources
<a name="step-resource-plan"></a>

Managing resources effectively as the project progresses is critical to a large migration effort. As the project moves from the initialization stage into the implementation stage, the migration team must scale up in order to support the migration waves. At the same time, the discovery team might be able to start scaling down, depending on the remaining discovery activities. In this step, you map out the resource management and scaling plan for efficiency. This step is typically performed by the project manager and workstream leads. After the plan is defined, you audit constantly throughout the project to determine if you need all of the resources in the plan. For example, delays in building the migration pipeline or larger-than-anticipated waves would likely affect the resource plan.

The resource plan is different for each large migration, and it is typically determined by factors unique to your project. Common factors include project budget, how your project team is organized, how quickly discovery activities can be completed, how your portfolio is distributed to each migration strategy (such as refactor, rehost, or replatform), and how much time is needed for change management processes in your organization.

When planning resources, consider the migration strategies for your portfolio and how these affect your migration and portfolio teams. For example, rehost is a common strategy for large migrations because it is low complexity. Almost every large migration project has at least one rehost migration pod of 4­–5 individuals. If you plan to include high-complexity migration strategies, such as replatform or refactor, you should create migration team pods for these strategies and include additional migration and portfolio team resources in your resource plan. For more information about workstreams, team structure, and how many people are needed for each pod, see [Team organization and composition](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/team-org.html) in the *Foundation playbook for AWS large migrations*.

In addition, the presence of specialized workloads, such as SAP, also warrants a separate, specialized team of individuals who have experience with those workloads. For more information about specialized workloads, see *MAP specialized workloads* at [AWS Migration Acceleration Program](https://aws.amazon.com/migration-acceleration-program/).

Do the following:

1. Define the resources you need to support project governance. Typical resources include a program manager for delivery governance and oversight, a project manager, and a supporting project manager.

1. Define the resources you need to support migration tooling. Typical resources include a cloud architect or external consultant.

1. If your project includes migrating a specialized workload, such as an ERP system, define the resources you need to support that workload. Typical resources for a specialized workload include:
   + Project manager
   + Architecture lead
   + Architecture engineer
   + DevOps engineer
   + Specialized migration pod that contains:
     + Functional subject matter expert (SME)
     + Testing specialist

1. Define the resources you need to support each migration strategy, such as rehost. Typical resources include:
   + Project lead
   + Architects and engineers for compute, storage, and networking
   + Testing specialist

1. Allocate the number of resources needed to support these teams at various stages of the project, including discovery, initialization, and implementation. Consider the acceleration of the migration as you refine your processes, and consider how to scale resources down as you approach the end of a stage or project.

## Step 7: Create a decision log
<a name="step-decision-log"></a>

Throughout the large migration, leads make decisions to resolve any issues that arise. Because of the size and scope of a large migration project, the project manager cannot be present when every decision is made. Workstream leads are responsible for recording the decisions that affect their workstream. The project manager is responsible for reviewing the decisions and presenting recent decisions at the project status review meetings.

This step is typically performed by a project manager. In this step, you create a decision log in a shared repository and confirm that the workstream leads understand their responsibilities for logging decisions. When necessary, use the escalation plan to facilitate timely decision making. For more information, see [Step 2: Establish an escalation plan](task-communication-plan.md#step-escalation-plan). Confirm that all team members understand the types of decisions that can be made at each level.

Do the following:

1. Create a decision log. You can use a dedicated project management tool for this, such as Jira or Confluence, or you can create a list in Microsoft Excel. We recommend documenting:
   + Short description of the decision
   + Status
   + How the decision affects the project
   + Alternative options considered
   + Who made the decision
   + Date the decision was made

1. Conduct a meeting with the workstream leads to review the decision log and train them on how to use it. It is important that you establish a culture of recording decisions.

1. Save the decision log in a shared repository, and make sure that all workstream leads can access it.

1. Before each project status review meeting, review the log for any decisions made since the previous meeting, and include these decisions in your *project status report presentation*. This ensures project-level transparency for all decisions made over the course of the project.

## Step 8: Create a RAID log
<a name="step-raid-log"></a>

Similar to the decision log, you should track risks and issues in a project management tool known as a *risks, actions, issues, and dependencies (RAID) log*. No matter how thoroughly you plan your large migration, issues will occur, and you will identify some risks to your project. By identifying and recording risks and issues, you provide transparency to the project, and you establish a process to control and monitor potential issues, minimizing their impact to the project.

Do the following:

1. Create a RAID log. You can use a dedicated project management tool for this, such as Jira or Confluence, or you can create a list in Microsoft Excel. We recommend documenting:
   + Type (risk, action, issue, or dependency)
   + Short description of the item
   + Open date
   + Probability
   + Impact
   + Severity score, which is calculated by multiplying the probability and impact
   + Owner

1. Conduct a meeting with the workstream leads to review the RAID log and train them on how to use it. It important that you establish a culture of recording risks and issues.

1. Save the RAID log in a shared repository and verify that all workstream leads can access it.

1. Before each project status review meeting, review the log for any risks and issues identified since the previous meeting, and include these in your *project status report* presentation. This ensures project-level transparency for all risks and issues.

## Task exit criteria
<a name="task-project-management-exit-criteria"></a>

This task is complete when you have done the following:
+ You have selected one or more project management tools, such as Jira, Confluence, or dashboards and lists in Microsoft Excel.
+ You have created and validated a detailed RACI matrix for each migration strategy (such as rehost) and for each high-level task in your large migration project.
+ You have created a benefit-tracking office, established a regular cadence for their meetings, and created an ownership and reporting template for the meetings.
+ Internal stakeholders are aligned for how financial reporting will be handled. You have established a formal cadence for reviewing the financial report, identified the recipients, and determined who should have access to the financial report.
+ You have created a resource plan for your project.
+ You have established a decision log in a shared repository, and all team leads are empowered to make updates.
+ You have defined a location and template for the RAID log. You have established a process for maintaining the log and prioritizing issues. Week-to-week changes in the RAID log are summarized in the status report.
+ All project stakeholders are aligned on how you will communicate the high-level project status in the project summary dashboard.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
