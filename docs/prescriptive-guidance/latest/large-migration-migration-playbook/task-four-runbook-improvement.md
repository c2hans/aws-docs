---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/task-four-runbook-improvement.html
---

# Task 4: Reviewing and improving the migration runbooks
<a name="task-four-runbook-improvement"></a>

This task consists of the following steps:
+ [Step 1: Review the completed waves and identify gaps in the current migration runbook](#step-one-review-waves)
+ [Step 2: Update the migration runbooks and complete testing](#step-two-update-runbooks-testing)

## Step 1: Review the completed waves and identify gaps in the current migration runbook
<a name="step-one-review-waves"></a>

*Fail fast* is a philosophy that uses frequent and incremental testing to reduce the development lifecycle, and it is a critical part of an agile approach to a large migration. After each cutover, schedule a retrospective meeting to review each task with the migration teams. Ask the following probing sample questions. You can also add your own questions:
+ Was the cutover successful? If not, what was the issue?
+ Does the migration runbook cover all of the tasks to perform the migration and cutover?
+ Do any of the tasks take longer than expected?
+ Are you aware of any technical issues with any tasks in the runbook?
+ Are there any manual tasks that can be automated?
+ Are there any process-related issues with the runbook or cutover?

## Step 2: Update the migration runbooks and complete testing
<a name="step-two-update-runbooks-testing"></a>

After collecting data from the retrospective meeting, update the migration runbooks as follows:
+ Add detailed instructions for any missing steps.
+ Fix or update any steps as needed.
+ Perform an end-to-end migration test with at least one Windows and one Linux server.
+ Send the updated runbook to the migration teams for use in the next wave.
