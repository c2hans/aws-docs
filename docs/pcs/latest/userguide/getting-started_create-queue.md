---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_create-queue.html
---

# Create a queue to manage jobs in AWS PCS
<a name="getting-started_create-queue"></a>

 You submit a job to a queue to run it. The job remains in the queue until AWS PCS schedules it to run on a compute node group. Each queue is associated with one or more compute node groups, which provide the necessary EC2 instances to do the processing.

 In this step, you will create a queue that uses the compute node group to process jobs.

**To create a queue**
+ Open the [AWS PCS console](https://console.aws.amazon.com/pcs).
+ Select the cluster named `get-started`.
+ Navigate to **Compute node groups** and make sure the status of the `compute-1` group is **Active**.
**Important**
The status of the `compute-1` group must be **Active** before you proceed to the next step.
+ Navigate to **Queues** and choose **Create queue**.
  + In the **Queue configuration** section, provide the following values:
    + **Queue name** – Enter the following: `demo`
    + **Compute node groups** – Select the compute node group named `compute-1`.
+ Choose **Create queue**.

 The **Status** field shows **Creating** while the queue is being created.

**Important**
 Wait for the **Status** field to show **Active** before proceeding to the next step in this tutorial.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
