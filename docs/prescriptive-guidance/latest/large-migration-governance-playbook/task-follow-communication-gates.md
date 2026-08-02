---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/task-follow-communication-gates.html
---

# Task: Completing the communication gates
<a name="task-follow-communication-gates"></a>

In this task, you use the communication gates and the T-minus schedule that you defined in [Task: Defining communication gates and schedules](task-create-communication-gates.md) in order to communicate the status of each wave as it moves through the migration and portfolio workstreams.

You might move waves through these gates individually, or if multiple waves are on the same schedule, you can move them through the gates in a group. Because of the wave overlap in the migration workstream, at any given time in the migration, it is common to have multiple waves or groups of waves at different gates. The following table shows how waves overlap in the migration workstream, and each wave is scheduled 1 week apart. In this example, 6­–7 waves are active in the migration workstream at any given time, and each wave is at a different gate.

|
|
| Gate | Wave 1 | Wave 2 | Wave 3 | Wave 4 | Wave 5 |
| --- |--- |--- |--- |--- |--- |
| Gate 1: T-minus schedule | March 13 | March 20 | March 27 | April 3 | April 10 |
| Gate 2: T-28 meeting | March 20 | March 27 | April 3 | April 10 | April 17 |
| Gate 3: T-21 communication | March 27 | April 3 | April 10 | April 17 | April 24 |
| Gate 4: T-14 meeting | April 3 | April 10 | April 17 | April 24 | May 1 |
| Gate 5: T-7 communication | April 10 | April 17 | April 24 | May 1 | May 8 |
| Gate 6: T-1 go or no-go meeting | April 16 | April 23 | April 30 | May 7 | May 14 |
| Gate 7: Cutover meeting | April 17 | April 24 | May 1 | May 8 | May 15 |
| Gate 8: Hypercare period start | April 18 | April 25 | May 2 | May 9 | May 16 |
| Gate 9: Hypercare period end | April 22 | April 29 | May 6 | May 13 | May 20 |

This task consists of the following communication gates:
+ [Gate 1: Create T-minus schedule for the wave](#gate-tminus-schedule)
+ [Gate 2: T-28 commit meeting](#gate-t28)
+ [Gate 3: T-21 communication](#gate-t21)
+ [Gate 4: T-14 checkpoint meeting](#gate-t14)
+ [Gate 5: T-7 communication](#gate-t7)
+ [Gate 6: T-1 go or no-go meeting](#gate-t1)
+ [Gate 7: T-0 cutover meeting](#gate-t0)
+ [Gate 8: Hypercare period start](#gate-hypercare-start)
+ [Gate 9: Hypercare period end](#gate-hypercare-end)

## Gate 1: Create a T-minus schedule for the wave
<a name="gate-tminus-schedule"></a>

Do the following in this communication gate:

1. Create a single, shared repository where you will store documentation for this wave.

1. Using the *T-minus schedule template* that you created in [Step 2: Create a T-minus schedule template](task-create-communication-gates.md#step-create-tminus-schedule), enter dates specific to this wave, and then save the T-minus schedule in the shared repository.

1. Create a copy of the migration task list that you created in the [Migration playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/), and then save it in the shared repository. You use this task list as a checklist as you progress through the gates.

1. Schedule the T-28 commit meeting with the appropriate participants. For more information about this meeting, see [Step 3: Define meetings and their cadence](task-communication-plan.md#step-define-meetings).

### Gate exit criteria
<a name="gate-exit-criteria.fbbeae57-a604-5f79-972c-9c76799b1d23"></a>

Continue to the next gate when you have completed the following project governance activities:
+ You have established a shared repository for the wave.
+ You have created a T-minus schedule for the wave.
+ You have created a migration task list for the wave.
+ You have scheduled the T-28 commit meeting.

Continue to the next gate when you have completed the following migration activities and any other tasks defined in your migration runbook:
+ The portfolio team has completed the wave plan.
+ The portfolio team has collected the migration metadata for the wave.

## Gate 2: T-28 commit meeting
<a name="gate-t28"></a>

In this gate, the migration team reviews the wave plan with the application owners and asks the applications owners to commit to the wave plan and cutover date. Do the following in this communication gate:

1. Using the *wave workshop presentation* that you created in [Step 4: Prepare meeting presentations](task-communication-plan.md#step-prepare-presentations), customize this presentation for the wave, and then save the presentation in the shared repository. You use this presentation in this gate and [Gate 4: T-14 checkpoint meeting](#gate-t14).

1. Conduct the T-28 commit meeting and, using your presentation, review the following:
   + Provide an overview of the wave plan and migration process.
   + Provide detail about upcoming action items for the application owners.
   + Confirm that the application owners are prepared to migrate each application in this wave.
   + Confirm that application owners understand that they need to provide test plans for their applications. A *test plan* describes how to validate that the cutover was successful. Testing occurs immediately after cutover so that, if there are any issues, the migration team can roll back the application to its original environment with minimal impact to the business and application users.
   + Review how stakeholders are expected to collaborate and communicate throughout the wave. Provide the location of the shared repository where stakeholders can find documents related to this wave.
   + Review the escalation plan that you developed in [Step 2: Establish an escalation plan](task-communication-plan.md#step-escalation-plan).
   + Provide an opportunity for questions and answers.

1. After the T-28 commit meeting, send the *T-28 communication email* that you created in [Step 3: Create standard email templates](task-create-communication-gates.md#step-email-templates) for each gate. Customize the email for the wave information and recipients, and add all applications and servers in this wave.

1. After the T-28 commit meeting, schedule the following meetings with the appropriate participants:
   + T-14 checkpoint meeting
   + T-1 go or no-go meeting
   + T-0 cutover meeting

### Gate exit criteria
<a name="gate-exit-criteria.2348de94-f54e-5661-aa85-ad0f7359b723"></a>

Continue to the next gate when you have completed the following project governance activities:
+ You have conducted the T-28 commit meeting.
+ You have informed all key stakeholders about the shared repository to access wave documentation, and all stakeholders have access.
+ You have started holding migration business hours, per [Task: Schedule recurring meetings for stage 2](task-schedule-meetings-stage2.md).
+ Application owners have confirmed that the applications in the wave plan can be migrated.
+ All stakeholders understand the communication approach and know which meetings they are required to attend.
+ Application owners understand the specific action items for which they are responsible.
+ You have sent the *T-28 communication email* to all stakeholders.
+ You have saved the meeting presentation and meeting notes in the shared repository so that all stakeholders can access it.
+ You have scheduled the T-14 commit meeting.
+ You have scheduled the T-1 go or no-go meeting.
+ You have scheduled the T-0 cutover meeting.

Continue to the next gate when you have completed the following migration activities and any other tasks defined in your migration runbook:
+ You have updated the wave plan with any changes made during the T-28 commit meeting.
+ You have submitted a request for change (RFC) for the applications and servers in the wave, and the change window is scheduled.
+ Understand and identify the change management process.
+ You have submitted RFCs for any new infrastructure requirements, such as forwarding, routing, or proxy services.
+ You have updated the migration task list.

## Gate 3: T-21 communication
<a name="gate-t21"></a>

The communications team continues to maintain contact with the application owners and business unit representatives. These stakeholders are invited to migration business hours to provide an opportunity for questions.

1. Send the *T-21 communication email* that you created in [Step 3: Create standard email templates for each gate](task-create-communication-gates.md#step-email-templates). Customize the email for the wave information and recipients, and add all applications and servers in this wave.

1. Update the scheduled T-14 checkpoint meeting with correct application owners. If any required participants cannot attend, confirm that an alternate representative can attend according to your escalation plan.

### Gate exit criteria
<a name="gate-exit-criteria.fe26a6d6-354c-5741-94fe-16c4673cabc0"></a>

Continue to the next gate when you have completed the following project governance activities:
+ You have sent the *T-21 communication email* to all stakeholders.

Continue to the next gate when you have completed the following migration activities and any other tasks defined in your migration runbook:
+ You have verified that the source servers meet the minimum requirements for replication.
+ You have started replicating applications and servers in the wave.
+ You have updated the migration task list.

## Gate 4: T-14 checkpoint meeting
<a name="gate-t14"></a>

In this gate, you conduct the T-14 checkpoint meeting with the application owners and assess whether the team is on track to cut over as scheduled. Do the following in this communication gate:

1. Using the *wave workshop presentation* that you prepared in [Gate 2: T-28 commit meeting](#gate-t28), update the presentation for the T-14 checkpoint meeting.

1. Conduct the T-14 checkpoint meeting and review the following:
   + Review the applications and servers that are being migrated in this wave.
   + Review the remaining tasks and schedule to make sure that attendees understand the remaining steps in the process.
   + Confirm that all application owners (or their representative) are available for the cutover meeting.
   + Confirm that test plans are ready for when the cutover is complete.

1. After the T-14 checkpoint meeting, send the *T-14 communication email* that you created in [Step 3: Create standard email templates for each gate](task-create-communication-gates.md#step-email-templates). Customize the email for the wave information and recipients, and add all applications and servers in this wave.

1. Update the invitation to the T-1 go or no-go meeting and the T-0 cutover meeting with any changes in participants, such as an alternative representative designated by an application owner.

1. Update the migration task list.

### Gate exit criteria
<a name="gate-exit-criteria.7f524043-583e-523f-90f8-526eaaa67d8f"></a>

Continue to the next gate when you have completed the following project governance activities:
+ You have conducted the T-14 checkpoint meeting. All application owners or their designated representatives attended. If an application owner didn't attend and is non-responsive, escalate the lack of attendance according to the escalation plan.
+ You have conducted migration business hours for the week.
+ You have sent the *T-14 communication email* to all stakeholders.
+ You have saved the meeting presentation and meeting notes in the shared repository so that all stakeholders can access it.
+ You have created a checklist of all pre-migration, migration, and post-migration tasks, closed any completed tasks, and saved the checklist in the shared repository.

Continue to the next gate when you have completed the following migration activities and any other tasks defined in your migration runbook:
+ You have verified the health and status of replicated applications and servers. You are in the process of troubleshooting any issues or have completed troubleshooting.
+ The application owners have provided test plans to the migration team.
+ You have updated the migration task list.

## Gate 5: T-7 communication
<a name="gate-t7"></a>

In this gate, the communications team continues to maintain contact with applications owners and business unit representatives. You also prepare for the cutover activities and meetings.

1. Send the *T-7 communication email* that you created in [Step 3: Create standard email templates for each gate](task-create-communication-gates.md#step-email-templates). Customize the email for the wave information and recipients, and add all applications and servers in this wave.

1. Confirm that required participants can attend the T-1 go or no-go meeting and the T-0 cutover meeting. Update the meeting invitations as needed to include alternate representatives.

### Gate exit criteria
<a name="gate-exit-criteria.2437913a-d67c-5525-8cae-400d4bd867dc"></a>

Continue to the next gate when you have completed the following project governance activities:
+ You have sent the *T-7 communication email* to all stakeholders.
+ You have confirmed attendance for the T-1 go or no-go meeting and T-0 cutover meeting. All participants have accepted the meetings, or alternative representatives have been identified.

Continue to the next gate when you have completed the following pre-migration activities:
+ All requests for change for this wave have been approved.
+ You have validated that the target infrastructure is ready for cutover.
+ You have shut down any test instances that you created in order to validate the infrastructure.
+ You have validated the cutover task list.
+ You have updated the migration task list.

## Gate 6: T-1 go or no-go meeting
<a name="gate-t1"></a>

In this gate, you review a checklist of pre-migration activities with all team members on the RACI matrix in order to validate that the applications and servers in the wave are ready for cutover. This gate occurs 24–48 hours before the scheduled cutover.

1. In the T-1 go or no-go meeting, review the checklist with all team members on the RACI matrix in order to validate that the applications and servers in the wave are ready for cutover.

1. Confirm that all required participants can attend the T-0 cutover meeting.

1. If you decide to proceed with migrating the wave (go), send the *T-1 communication email* that you created in [Step 3: Create standard email templates for each gate](task-create-communication-gates.md#step-email-templates). Customize the email for the wave information and recipients, and add all applications and servers in this wave.

1. If you decide not to proceed with migrating the wave or specific applications and servers (no-go), send an email to all stakeholders informing them of the decision and provide any available information about next steps or schedule changes.

### Gate exit criteria
<a name="gate-exit-criteria.514fd6d1-deee-566c-a82f-483de2c11aab"></a>

Continue to the next gate when you have completed the following project governance activities:
+ You have confirmed that resources are available for the T-0 cutover meeting and that all required participants can attend.
+ You have saved the meeting presentation and meeting notes in the shared repository so that all stakeholders can access it.
+ You have sent the *T-1 communication email* to all stakeholders.

Continue to the next gate when you have completed the following migration activities and any other tasks defined in your migration runbook:
+ In the migration task list, you have confirmed that all migration tasks are complete.

## Gate 7: T-0 cutover meeting
<a name="gate-t0"></a>

In this gate, you migrate all servers and applications in the wave during a cutover meeting, and then you immediately have the application owners test the migrated applications to confirm that they are operating as expected. Application owners might attend the entire meeting or attend only as needed for their applications.

1. Before the cutover meeting, send the *T-0 communication email* that you created in [Step 3: Create standard email templates for each gate](task-create-communication-gates.md#step-email-templates). Customize the email for the wave information and recipients, and add all applications and servers in this wave.

1. In the T-0 cutover meeting, migrate the servers and applications in the wave according to the instructions in your migration runbooks, which you developed according to the instructions in the [Migration playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/).

1. When an application or server has been migrated, use the test plan developed by the application owner to validate that the application is functioning as follows:
   + If the application or server is functioning as expected or has only minor issues, leave it in the AWS environment and remediate any issues.
   + If the application or server isn't functioning or has significant issues, roll it back.

1. As you complete the cutover activities in the migration task list, update the task list.

1. Send the *cutover complete communication email* that you created in [Step 3: Create standard email templates for each gate](task-create-communication-gates.md#step-email-templates). Customize the email for the wave information and recipients, and add all applications and servers in this wave.

### Gate exit criteria
<a name="gate-exit-criteria.5c811116-85fd-58e5-865c-746608466f21"></a>

Continue to the next gate when you have completed the following project governance activities:
+ You have validated that every application or server in the wave has been migrated successfully, or you have rolled it back.
+ You have made note of any applications or servers that rolled back. For these applications or servers, you must update the migration pattern or redefine the target state to address any issues encountered during cutover. You will include these applications or servers in a future wave plan.
+ You have sent the *cutover complete communication email* to all stakeholders.

Continue to the next gate when you have completed the following cutover activities:
+ You have completed all steps in the *Cutover tasks *section of the migration task list.

## Gate 8: Hypercare period start
<a name="gate-hypercare-start"></a>

In this gate, you do the following:

1. Ask project stakeholders to review the migrated applications and servers in the cloud. If any issues are identified, they should be sent to the migration team.

1. Address any issues identified during cutover or during the hypercare period.

1. Confirm that the cloud operations team is prepared to accept the workload.

1. Update all project management tools and repositories to reflect the status of the wave.

### Gate exit criteria
<a name="gate-exit-criteria.d195d1b4-0745-5c99-8340-56e6a4d8a41e"></a>

Continue to the next gate when you have completed the following project governance activities:
+ All stakeholders have reviewed the migrated applications and servers.
+ The migration team has addressed any application or server issues that were identified during cutover or during the hypercare period.
+ The cloud operations team has confirmed that they are ready to accept the migrated applications and servers.
+ You have updated all project management tools and repositories in order to reflect the wave status.

## Gate 9: Hypercare period end
<a name="gate-hypercare-end"></a>

The hypercare period typically lasts 1­–4 days, and it ends when the migration team has resolved any issues with the migrated applications or servers. At the end of the hypercare period, the migration team meets with the cloud operations (Cloud Ops) team to review the migrated applications and servers. In this gate, the migration team transfers ongoing support of the migrated workloads to the Cloud Ops team. The Cloud Ops team notifies application owners that the hypercare period is complete and that they are now the point of contact for any issues. Optionally, you can include a survey in this communication and invite application owners to provide feedback about the migration and cutover process.

1. Incorporate the migrated applications and servers into the configuration management database (CMDB) for the cloud operations team.

1. Incorporate any application information into the Cloud Ops technical management support tool, such as ServiceNow.

1. Send the *hypercare complete communication email* that you created in [Step 3: Create standard email templates for each gate](task-create-communication-gates.md#step-email-templates). Customize the email for the wave information, and include instructions for how to contact the cloud operations team.

1. Notify the infrastructure support team of the transition in order to start the process of decommissioning the source servers and any supporting infrastructure. This step is typically performed by the Cloud Ops team or the project manager.

### Gate exit criteria
<a name="gate-exit-criteria.89068da7-22ba-5709-9b34-efaec6ffa527"></a>

This gate is complete when you have performed the following project governance activities:
+ Cloud Ops has incorporated all workload-related information into their CMDB.
+ Cloud Ops has incorporated all application information into their technical management support tool.
+ You have sent the *hypercare complete communication email* to all stakeholders.
+ The infrastructure team has started to decommission any supporting infrastructure that is no longer needed.
