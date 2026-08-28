---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/view-jobs.html
---

# View AWS Batch jobs in a job queue
<a name="view-jobs"></a>

You can view and filter your jobs in AWS Batch. This feature provides an option to view an existing job queue and filter its jobs by one of three options.

Search and filter are able to retrieve jobs that are not in a terminal state (`SUCCEEDED` or `FAILED`). Once a job's state is `SUCCEEDED` or `FAILED` you should be able to retrieve the job for up to seven days. You are still able to view a job's CloudWatch or Amazon EventBridge logs.

Use this procedure to list all the jobs in a job queue in the AWS Batch console. Optionally, use the **Filter results** field to narrow the results based on the criteria you specify.

1. Navigate to the [AWS Batch console](https://console.aws.amazon.com/batch/home).

1. In the Navigation pane, choose **Jobs**.

1. Expand the **Job queue** dropdown list and choose the job queue that you want to search within.
**Note**
You can search for jobs within only one job queue at a time.

1. In the **Filter results** field, enter keywords to include in the results. You can use this field to filter by **Job name**, **Status**, or **Job ID**. Depending on the property, there may be additional operators, such as equals (=) or contains (:) that you must define.
**Note**
SageMaker Training job queues only support filtering by **Job name** and **Job ID**

1. Choose **Search**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
