---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/delete-job-queue.html
---

# Delete a job queue in AWS Batch
<a name="delete-job-queue"></a>

When you no longer need your job queue, you can disable and delete the job queue.

------
#### [ Delete a job queue (AWS Batch console) ]

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. In the navigation pane, choose **Job queues** and then choose a job queue.

1. Choose **Actions** and then **Disable**.

1. Once the job queue's state is **Disabled**, choose **Actions** and then **Delete**.

1. In the modal window choose **Delete job queue**.

------
#### [ Delete a job queue (AWS CLI) ]

1. Disable the job queue to prevent new job submissions:

   ```
   aws batch update-job-queue \
     --job-queue {{my-sm-training-fifo-jq}} \
     --state DISABLED
   ```

1. Wait for any running jobs to complete, then delete the job queue:

   ```
   aws batch delete-job-queue \
     --job-queue {{my-sm-training-fifo-jq}}
   ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
