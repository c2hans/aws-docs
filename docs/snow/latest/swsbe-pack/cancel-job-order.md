---
source_url: https://docs.aws.amazon.com/snow/latest/swsbe-pack/cancel-job-order.html
---

# Cancelling a job to order a Snow Family device
<a name="cancel-job-order"></a>

After creating a job to order a Snow Family device, you can cancel the job through the AWS Snow Family Management Console. If you cancel the job, you won't receive the device you ordered. You can only cancel the job while the job status is *Job created*. After the job progresses past this status, you cannot cancel the job.

1. Log in to the [AWS Snow Family Management Console](https://console.aws.amazon.com/snowfamily/home).

1. Choose the job to cancel.

1. Choose **Actions**. From the menu that appears, choose **Cancel job**.
![AWS Snow Family Management Console with job selected and Actions menu showing Cancel job.](http://docs.aws.amazon.com/snow/latest/swsbe-pack/images/cancel-job-console.png)

1. The **Cancel job** window appears. To confirm cancelling the job, enter the **job name** and choose **Cancel job**. In the list of jobs, **Cancelled** appears in the **Status** column.
![Cancel job window.](http://docs.aws.amazon.com/snow/latest/swsbe-pack/images/cancel-job-window-console.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Snow Family Device Guides. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
