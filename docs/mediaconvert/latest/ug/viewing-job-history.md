---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/viewing-job-history.html
---

# Viewing your job history
<a name="viewing-job-history"></a>

You can view the recent history of MediaConvert jobs that you created with your AWS account in a given AWS Region. After three months, the service automatically deletes the record of a job.

The **Jobs** page shows jobs that are successfully completed, are canceled, are being processed, are waiting in the queue, and that ended in error. You can filter the job history list by the status and by the queue that the jobs were sent to. You can also choose a specific job from the list to view the job's settings.

------
#### [ Console  ]

To view your jobs using the MediaConvert console

1. Open the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list) page in the MediaConvert console.

1. Optionally, filter the list by status and queue by choosing from the dropdown lists.

1. To see details for a job, choose a **Job ID** to view its **Job summary** page.

------
#### [ CLI  ]

The following `list-jobs` example lists up to twenty of your most recently created jobs.

```
aws mediaconvert list-jobs
```

For more information about how to cancel a job using the AWS CLI, see the [AWS CLI command reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-jobs.html).

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
