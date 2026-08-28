---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.Modifying.html
---

# Modifying a task
<a name="CHAP_Tasks.Modifying"></a>

You can modify a task if you need to change the task settings, table mapping, or other settings. You can also enable and run premigration assessments before running the modified task. You can modify a task in the console by selecting the task and choosing **Modify**. You can also use the CLI command or API operation [ModifyReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationTask.html).

There are a few limitations to modifying a task. These include the following:
+ You can't modify the source or target endpoint of a task.
+ You can't change the migration type of a task.
+ Tasks that have run must have a status of **Stopped** or **Failed** to be modified.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
