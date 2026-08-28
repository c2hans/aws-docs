---
source_url: https://docs.aws.amazon.com/fsx/latest/LustreGuide/recreate-task.html
---

# Duplicating a task
<a name="recreate-task"></a>

You can duplicate an existing data repository task in the Amazon FSx console. When you duplicate a task, an exact copy of the existing task is displayed in the **Create import data repository task** or **Create export data repository task** page. You can make changes to the paths to export or import, as needed, before creating and running the new task.

**Note**
A request to run a duplicate task will fail if an exact copy of that task is already running. An exact copy of a task that is already running contains the same file system path or paths in the case of an export task or the same data repository paths in the case of an import task.

You can duplicate a task from the task details view, the **Data Repository Tasks** pane in the **Data Repository** tab for the file system, or from the **Data repository tasks** page.

**To duplicate an existing task**

1. Choose a task on the **Data Repository Tasks** pane in the **Data Repository** tab for the file system.

1. Choose **Duplicate task**. Depending on which type of task you chose, the **Create import data repository task** or **Create export data repository task** page appears. All settings for the new task are identical to those for the task that you're duplicating.

1. Change or add the paths that you want to import from or export to.

1. Choose **Create**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
