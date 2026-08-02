---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/task-three-analyze-runbooks.html
---

# Task 3: Analyzing and testing your migration runbooks
<a name="task-three-analyze-runbooks"></a>

In this task, you walk through each runbook that you built in the previous task, analyze any identified gaps, conduct a migration proof of concept (POC), and review the notes and feedback.

This task consists of the following steps:
+ [Step 1: Conduct a walkthrough of each runbook](#step-one-walkthrough-runbook)
+ [Step 2: Conduct a POC that tests each migration pattern](#step-two-poc-tests)
+ [Step 3: Review and identify the gaps in the current migration runbook drafts](#step-three-review-gaps)

## Step 1: Conduct a walkthrough of each runbook
<a name="step-one-walkthrough-runbook"></a>

In this step, the migration teams assess the runbook and task sequence as though they were performing it for real. The migration teams meet and review each step, and the team members ask questions and share their feedback. This walkthrough process helps the teams identify missing steps and sequence issues. Complete the walkthrough as follows:

1. Gather the migration teams that are responsible for completing the tasks in the runbook.

1. Walk through the steps in the runbook one by one, as if this was a live migration. As you go, identify and make note of any gaps or issues. Do not perform the migration or tasks as part of the walkthrough.

1. Update the runbook draft to address any gaps or issues identified in the walkthrough.

## Step 2: Conduct a POC that tests each migration pattern
<a name="step-two-poc-tests"></a>

1. Select a POC candidate from the already prepared waves.

1. Open the migration runbook draft.

1. Complete the runbook step by step in order to migrate the POC candidate as follows:
   + Follow every step in the runbook. Do not make assumptions or make your own decisions.
   + Assume the person using the runbook has no prior knowledge about migration or your environment.
   + If a step is not clear but you can continue, make note of the step and continue.
   + If a step is missing and you can't continue, stop, and highlight the section from which you could not proceed. Work with the runbook owner to clarify the missing step so that you can continue and complete the POC.

## Step 3: Review and identify the gaps in the current migration runbook drafts
<a name="step-three-review-gaps"></a>

1. Review any issues or gaps identified in the previous steps.

1. Analyze the gaps and consider the following questions:
   + Does the runbook have the steps needed to complete a migration and cutover, from end to end?
   + Does the runbook contain reference links for the tasks that are predefined in your environment?
   + Does the runbook clearly defined who, what, when, and how to complete a task?

## Task exit criteria
<a name="task-three-analyze-runbooks-exit"></a>

When you have met the following exit criteria, proceed to the next task:
+ You have reviewed and tested each migration runbook.
+ For each runbook, you have completed a migration POC for at least one application and for more than two operating system (OS) variants.
+ You have identified and documented the identified gaps and issues in each runbook.
