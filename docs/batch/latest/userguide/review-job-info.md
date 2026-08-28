---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/review-job-info.html
---

# Review AWS Batch job information
<a name="review-job-info"></a>

You can review AWS Batch job information such as status, job definition and container information.

1. Open the [AWS Batch console](https://console.aws.amazon.com/batch/home).

1. Choose **Jobs**.

1. For **Job queue**, choose the job queue that you want.
**Tip**
If there are several jobs in the job queue, you can turn on **Search and filter** to find a job faster. For more information, see [Search AWS Batch for jobs in a job queue](searching-filtering-jobs.md).

1. Choose the job that you want.

**Note**
You can also use the AWS Command Line Interface (AWS CLI) to view details about an AWS Batch job. For more information, see [describe-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-jobs.html) in the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
