---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/implement-wave-planning.html
---

# Task 3: Performing wave planning and metadata collection
<a name="implement-wave-planning"></a>

This is the final task for portfolio assessment and wave planning. In this task, you use the application information and target migration pattern to build move groups, assign move groups to waves, and collect all the metadata needed to support the migration. Finally, you notify the migration workstream that the wave is ready.

You need the following information to complete this task.

|
|
| Input | Source |
| --- |--- |
| A list of prioritized applications | Created earlier in the implementation stage, in [Task 1: Prioritizing the applications](implement-prioritization.md) |
| Migration pattern mapping | Created earlier in the implementation stage, in [Task 2: Performing the application deep](implement-deep-dive.md) dive |
| Application target state (if applicable) | Also created in [Task 2: Performing the application deep dive](implement-deep-dive.md) |

Do the following:

1. Follow the instructions in your wave planning runbook, in the *Stage 2: Perform wave planning* section. You defined this process in this playbook, in [Step 3: Finalize the wave planning process](wave-planning.md#wave-planning-3).

1. Follow the instructions in your metadata management runbook, in the *Stage 2: Collect metadata* section. You defined this process in this playbook, in [Step 3: Document metadata requirements and collection processes in a runbook](metadata.md#metadata-3).

1. Notify the migration workstream that the wave plan is complete and that the metadata is ready. This communication should adhere to the governance you defined per the [Project governance playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/).

At the end of this task, you have completed the following.

|
|
| Output | Description |
| --- |--- |
| Wave plan | You have planned a wave, identified the servers, applications, and databases in that wave, and defined a start date and cutover date and time. |
| Source infrastructure metadata | You have collected the source infrastructure metadata, such as the server names and operating systems. |
| Target infrastructure metadata | You have collected the target infrastructure metadata, such as the target subnets, security groups, and AWS account. |
| Notification completed | You have notified the migration workstream that the wave plan and metadata are ready. |

The portfolio team repeats all three tasks in this stage for each sprint until the migration project is completed.
