---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-list-jobs.html
---

# Listing jobs
<a name="batch-ops-list-jobs"></a>

You can retrieve a list of your S3 Batch Operations jobs. The list provides information about jobs that haven't yet finished, and jobs that finished within the last 90 days. For each job, the list includes details such as job ID, description, priority, current status, and the number of tasks that have succeeded and failed.

You can filter your job list by status. If you retrieve the list by using the console, you can also search your jobs by description or ID and filter them by AWS Region.

## Get a list of `Active` and `Complete` jobs
<a name="batch-ops-example-cli-active-jobs"></a>

The following AWS CLI example gets a list of `Active` and `Complete` jobs. To use this example, replace the {{`user input placeholders`}} with your own information.

```
aws s3control list-jobs \
    --region {{us-west-2}} \
    --account-id {{account-id}} \
    --job-statuses '["Active","Complete"]' \
    --max-results {{20}}
```

For more information and examples, see [list-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-jobs.html) in the *AWS CLI Command Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
