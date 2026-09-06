---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/task-three-cutover-tasks.html
---

# Task 3: Performing cutover tasks
<a name="task-three-cutover-tasks"></a>

At this point, you have completed the migration tasks and tested all of the servers and apps, and you are ready for cutover. Use the RACI matrices you created in the [Foundation playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/) to manage the tasks and ownership of each cutover task, and use your migration runbook for each pattern to perform the cutover activities. The following table is an example of how you might track and manage cutover progress. It is common to have multiple migration patterns in the same wave for different applications.

|
|
| Task name | Wave | Migration runbook | Owner | Status |
| --- |--- |--- |--- |--- |
| Check replication | Wave 1 | Rehost to Amazon EC2 | Jane Doe | Completed |
| Launch cutover EC2 instance | Wave 1 | Rehost to Amazon EC2 | Jane Doe | Completed |
| Validate EC2 instance status | Wave 1 | Rehost to Amazon EC2 | Jane Doe | In progress |
| Launch databases in Amazon RDS | Wave 1 | Replatform to Amazon RDS | John Smith | In progress |
| Complete storage data transfer | Wave 1 | Replatform to Amazon Elastic File System (Amazon EFS) | John Smith | Not started |
| Perform app testing | Wave 1 | All | Jane Doe | Not started |
| App acceptance decision | Wave 1 | All | Jane Doe | Not started |
