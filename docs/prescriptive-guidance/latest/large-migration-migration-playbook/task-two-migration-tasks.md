---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/task-two-migration-tasks.html
---

# Task 2: Performing pre-migration and migration tasks
<a name="task-two-migration-tasks"></a>

Now you perform pre-migration and migration tasks and adhere to a schedule based on your sprint planning outcome. A sprint backlog contains a list of all tasks in the migration, for all waves in the current sprint, and organizes the tasks by week. For a list of tasks, see your migration runbooks for each migration pattern, which were created in stage 1 of this playbook. For the wave schedule, see your project management tools, which were established in the [Project governance playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/). Perform the tasks in the scheduled weeks. The following is an example of a rehost migration task schedule in which there are migration tasks for different waves in the same week.

|
|
| Task name | Wave | Category | Owner |
| --- |--- |--- |--- |
| Verify prerequisites | Wave 1 | Build | Jane Doe |
| Install replication agent | Wave 1 | Build | Jane Doe |
| Validate launch template | Wave 2 | Validate | Jane Doe |
| Launch test instances | Wave 3 | Boot-up testing | Jane Doe |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
