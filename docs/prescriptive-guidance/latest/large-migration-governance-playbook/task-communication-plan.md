---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/task-communication-plan.html
---

# Task: Creating a communications plan
<a name="task-communication-plan"></a>

A critical element of the governance model is identifying who is responsible for communicating with application owners and how to escalate if an application owner doesn't respond. In this task, you define who is responsible for communications, determine what the regular communications and meetings will be, create your standard communication templates, and determine what happens if you need to escalate an issue.

In this task, you do the following:
+ [Step 1: Create a communications team](#step-communications-team)
+ [Step 2: Define meetings and their cadence](#step-escalation-plan)
+ [Step 3: Establish an escalation plan](#step-define-meetings)
+ [Step 4: Prepare meeting presentations and communication tools](#step-prepare-presentations)
+ [Step 5: Schedule recurring meetings for stage 1](#step-schedule-meetings-stage1)
+ [Step 6: Understand the change management process](#step-change-management)

## Step 1: Create a communications team
<a name="step-communications-team"></a>

The communications team is part of the project governance workstream. This team is responsible for communicating with project stakeholders at key migration milestones, scheduling meetings, coordinating feedback, and confirming attendance for required meeting participants. The activities of the communications team are typically governed by communication gates, which you define in [Task: Defining communication gates and schedules](task-create-communication-gates.md).

Do the following:

1. Identify the appropriate members of this team.

1. Designate a *communications lead*. This individual acts as a single point of contact throughout the migration for scheduling gate meetings, coordinating questions and feedback from the other workstreams, and confirming meeting attendance with required participants.

## Step 2: Establish an escalation plan
<a name="step-escalation-plan"></a>

When an issue arises in the migration, you must be able to quickly resolve it. By defining an escalation plan before the migration starts, you can provide a clear action plan to the team in advance, which helps prevent delay, frustration, or surprises. We recommend specifying a single-threaded leader for each business unit. If an application owner isn't engaging or responding, you can escalate to that individual.

This step is typically completed by the project manager and project sponsor. When establishing the escalation plan, you need to define the type of issue, the circumstances in which you should escalate the issue (known as the *trigger*), and define the tiers of escalation. We recommend no more than three tiers. For each tier, you should identify the *audience*, or *response owner*, and the amount of time that the audience has to respond. For example, if the first escalation audience doesn't resolve the issue within 24 hours, escalate the issue to the second tier, which is a different audience. With each escalation, CC the audiences of any prior tiers.

Do the following:

1. Create an escalation plan. You can use a dedicated project management tool for this, such as Jira or Confluence, or you can create a list in Microsoft Excel. We recommend documenting:
   + Short description of the anticipated or experienced issue
   + The trigger
   + Tiers of escalation and audience
   + The amount of time each tier has to respond to the issue

1. Conduct a meeting with the workstream leads and project sponsor to review the escalation plan.

1. Share the escalation plan with the entire project team to make sure that all members are familiar with the escalation process.

1. Save the escalation plan in a shared repository, and make sure that all project team members can access it.

The following is an example of how you might record an issue in the escalation plan.

|
|
| \# | Issue | Trigger | Tier 1 | Tier 2 | Tier 3 |
| --- |--- |--- |--- |--- |--- |
| **Audience** | **Escalate after** | **Audience** | **Escalate after** | **Audience** |
| 1 | Firewall ports need to be open to migrate workloads to AWS | Firewall isn't open by T-28 commit meeting | Network team, migration lead | 24 hours | Network team manager | 24 hours | Executive team, lead of impacted business unit |

## Step 3: Define meetings and their cadence
<a name="step-define-meetings"></a>

In this step, you identify the regular, recurring meetings for the migration project and establish the meeting frequency, or *cadence*. Documenting the meetings and their cadence improves project transparency. When an issue arises, team members can quickly identify the appropriate meeting to address it. You should identify the name of the meeting, the frequency, the core objectives, and the owners and participants. You might need to update this document as the migration progresses and you identify new meeting participants.

The following recurring meetings are common in a large migration project:
+ **Steering committee meetings** – These meetings are typically held twice a month, and the objective is to share the project status and resolve any issues that require involvement from executive leadership. Participants of this meeting typically include the project sponsor, executive leadership, and a representative from the project management office.
+ **Project status review meetings** – These meetings are typically held once per week. The objective is to review the project status at the workstream level and evaluate the need for resources or subject matter experts. Participants of this meeting include the project manager, project stakeholders, workstream owners, and the migration lead.
+ **Daily stand-ups** – These are very short meetings held once per day. It is called a *stand-up* because the meeting should be short enough that the participants don't require a chair. The purpose is to review planned and recently completed tasks and surface any issues. In daily stand-ups, you typically use a visual task management tool, such as a Kanban board or Gantt chart, which you determine in [Step 1: Select a project management tool](task-project-management.md#step-pm-tool).
+ **Infrastructure and operations checkpoint meetings** – These meetings are usually held twice a week. The objective is to review the progress of the migration, review active issues and decide whether escalation is required, collaborate across workstreams, and plan resources for the next sprint. Participants of this meeting include the technical team members who own RACI-defined migration activities.
+ **Migration business hours** – This time is reserved as an open meeting for application owners to seek support or guidance. We recommend that you hold business hours three times per week.

We recommend starting with the attached *Meeting plan template* (Microsoft Excel format). This template contains a default example, and you can customize it for your project.

## Step 4: Prepare meeting presentations
<a name="step-prepare-presentations"></a>

As defined in [Step 3: Define meetings and their cadence](#step-define-meetings), large migrations require frequent meetings to align workstreams, address issues, and confirm that the migration is on schedule. Defining standard formats and presentations for these meetings helps participants by establishing consistent expectations for the meeting. It also helps reduce the amount of time needed to prepare for each meeting. In this step, you create the presentation templates for your regularly scheduled meetings.

We recommend starting with the following attached templates:
+ *Status report template* (Microsoft PowerPoint format)
+ *Steering committee meeting template* (Microsoft PowerPoint format)
+ *Wave workshop template* (Microsoft PowerPoint format)
+ *Cutover readiness assessment template* (Microsoft Excel format)

Do the following:

1. Customize the *Steering committee meeting template* for your project.

1. Customize the *Status report template* for your project. This presentation is used in project status review meetings, which are typically held on a weekly cadence. This template is a more robust version of the executive-level summary you created in the previous step.

1. Customize the *Wave workshop template* for your project. This presentation is used in the T-28 and T-14 commit meetings. In T-28 commit meetings, application owners commit to the wave, and in the T-14 commit meeting, they recommit to the cutover date.

1. Customize the *Cutover readiness assessment template* for your project. This presentation is used in the infrastructure and operations checkpoint meetings to review current progress of migration activities. The purpose of the presentation is to help the team confirm that the progress gates have been met and that the application is ready for cutover.

1. Store these presentation templates in a shared repository, where the meeting owners can access them.

1. For each type of meeting, define a shared repository where the meeting owners can save their presentations. After each meeting, the meeting owner should save a version of their presentation and any other meeting artifacts in this repository so that meeting attendees and the project team can reference this information. For example, the repository for the project status review meeting would contain a copy of the status report presented at each meeting.

## Step 5: Schedule recurring meetings for stage 1
<a name="step-schedule-meetings-stage1"></a>

If you completed the mobilize phase, you might have already established some of the meetings in this step. Complete this step for any meetings that you haven't already scheduled. According to the meeting plan you developed in [Step 3: Define meetings and their cadence](#step-define-meetings), the meeting owner should schedule the following recurring meetings:
+ Daily stand-ups for each workstream
+ Financial reporting meetings
+ Steering committee meetings
+ Project status reviews
+ Infrastructure and operations checkpoint meetings

These meetings continue until the migration is complete.

## Step 6: Understand the change management process
<a name="step-change-management"></a>

Understanding the change management process for your organization is critical to the success of a large migration project. The change management process affects the schedules and deadlines in your migration. You must understand the information and approvals required for each workload. Make sure that you understand:
+ The deadlines for submitting the list of applications and servers in the wave plan
+ The criteria and information required for gaining approval to move workloads on the planned date
+ Any formal process documents that must be completed
+ The process for submitting firewall or domain changes

All migration leads should understand the change management process prior to discovery activities. Some migration-related tasks require approval, and team members need to understand their responsibilities in the change management process. For more information about training, see [Training and skills required for large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/training-skills.html) in the *Foundation playbook for AWS large migrations*.

## Task exit criteria
<a name="task-communication-plan-exit-criteria"></a>

This task is complete when you have done the following:
+ You have created a communications team.
+ You have defined participants for all meetings.
+ You have established and approved an escalation plan.
+ You have scheduled recurring meetings that start in stage 1, as defined in your meeting plan.
+ You have defined the standard presentations that should be used in each meeting.
+ For each meeting, you have defined a shared repository for capturing all presentations, activities, and artifacts.
+ All change management processes are understood and documented.
