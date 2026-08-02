---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-intro-governance/communication-delivery-layers.html
---

# Communication plan for the delivery layers
<a name="communication-delivery-layers"></a>

The communications and meetings for the delivery governance layers are typically designed to facilitate the migration activities and coordinate across the portfolio and migration workstreams. There are communications that are intended to facilitate project management and communications that are intended to inform or help application owners and other owners of migration tasks, as defined in a responsible, accountable, consulted, informed (RACI) matrix.

## Project management team communications
<a name="pm-team-communications"></a>

The following communications and meetings are intended to support the project management aspects of the migration:
+ **Workstream daily stand-ups** – Using the roles and responsibilities defined within your RACI matrix, ensure the migration team participates in a daily stand-up meeting. As part of the working agreement within each workstream, establish a KPI that immediately starts the escalation process if one or more defined application owners are not participating.
+ **PMO daily stand-ups** – Schedule a daily stand-up meeting with the workstream leads and oversight leadership. Use this meeting to make sure the team is aligned and communicate any activities or delays that impact other workstreams.
+ **Communication gates** – The project management team must participate in all communication gate meetings and notifications, which are described in detail in the next section, [Application owner communications](#app-owner-communications).

## Application owner communications
<a name="app-owner-communications"></a>

When planning and cutting over waves, you must establish mechanisms with application owners to ensure their commitment and easily initiate escalations. We recommend that you adopt a communication gate framework. The communication gates are repeatable touchpoint events for each wave or group of waves, and they clearly establish the criteria that must be met to proceed to the next gate. For more information, see [Define the communication gates](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/task-create-communication-gates.html#step-communication-gates) in the *Project governance playbook for AWS large migrations*.

To align all parties on the communication gates and migration activities, the project management team should define a T-minus schedule. A *T-minus schedule* is a visual way to represent all of the high-level migration activities that need to be completed for each wave. It covers the period of time between the end of wave planning and the end of the hypercare period. For tracking tasks and progress, we recommend a visual management tool such as a Kanban board or Gantt chart. For more information, see [Create a T-minus schedule template](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/task-create-communication-gates.html#step-create-tminus-schedule) in the *Project governance playbook for AWS large migrations*. The following image shows an example of a T-minus schedule.

![Sample T-minus schedule](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-intro-governance/images/guide-img/0ce37e8e-2c4b-4da7-ad35-503caa83d254/images/4c1fe2bf-383a-48d5-91c8-20126e22318a.png)

As defined in your communication gates, you have the following regular meetings and communications with the application owners and migration team for each wave or group of waves:
+ **T-28 commit meetings** – About four weeks before the scheduled cutover, you conduct this formal wave kickoff. In this meeting, you share the T-minus schedule, make sure application owners understand the migration process and their tasks, and review key milestones. The purpose of this meeting is to make sure that the application owners are ready and committed to the cutover date the hypercare period. For more information, see [Hypercare period](preparing-organization.md#hypercare).
+ **T-14 checkpoint meetings** – About two weeks before the scheduled cutover, you conduct this formal checkpoint with the application owners, the communication lead, and the migration lead. The purpose of this meeting is to confirm the application owners are ready for cutover and address any questions or concerns. This meeting identifies key issues that need to be escalated to leadership, such as an application owner communicating that they want to remove their application from the wave. The project management office (PMO) prepares the agenda for this meeting and customizes the presentation to include the servers and applications in the wave.
+ **Weekly communications** – In your T-minus schedule, you define regular communications with the application owners and other stakeholders. These communications are intended to remind stakeholders about upcoming activities or notify them of meeting key milestones. Standard communication points include T-28, T-21, T-14, T-7, T-1, T-0, cutover compete, and hypercare period end. We recommend you create standard templates for these communications.

For presentation and communication templates, see [Create standard email templates for each gate](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/task-create-communication-gates.html#step-email-templates) and [Prepare meeting presentations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/task-communication-plan.html#step-prepare-presentations) in the *Project governance playbook for AWS large migrations*.
