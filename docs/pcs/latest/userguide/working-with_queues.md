---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_queues.html
---

# AWS PCS queues
<a name="working-with_queues"></a>

An AWS PCS queue is a lightweight abstraction over the scheduler’s native implementation of a work queue. In the case of Slurm, an AWS PCS queue is equivalent to a Slurm partition.

 Users submit jobs to a queue where they reside until they can be scheduled to run on nodes provided by one or more compute node groups. An AWS PCS cluster can have multiple job queues. For example, you can create a queue that uses Amazon EC2 On-demand Instances for high priority jobs and another queue that uses Amazon EC2 Spot Instances for low-priority jobs.

**Topics**
+ [Creating a queue in AWS PCS](working-with_queues_create.md)
+ [Updating an AWS PCS queue](working-with_queues_update.md)
+ [Deleting a queue in AWS PCS](working-with_queues_delete.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
