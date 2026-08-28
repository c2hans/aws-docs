---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/batch-load-using-error-reports.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Using batch load error reports
<a name="batch-load-using-error-reports"></a>

Batch load tasks have one of the following status values:
+ `CREATED` (**Created**) – Task is created.
+ `IN_PROGRESS` (**In progress**) – Task is in progress.
+ `FAILED` (**Failed**) – Task has completed. But one or more errors was detected.
+ `SUCCEEDED` (**Completed**) – Task has completed with no errors.
+ `PROGRESS_STOPPED` (**Progress stopped**) – Task has stopped but not completed. You can attempt to resume the task.
+ `PENDING_RESUME` (**Pending resume**) – The task is pending to resume.

When there are errors, an error log report is created in the S3 bucket defined for that. Errors are categorized as taskErrors or fileErrors in separate arrays. Following is an example error report.

```
{
    "taskId": "9367BE28418C5EF902676482220B631C",
    "taskErrors": [],
    "fileErrors": [
        {
            "fileName": "example.csv",
            "errors": [
                {
                    "reason": "The record timestamp is outside the time range of the data ingestion window.",
                    "lineRanges": [
                        [
                            2,
                            3
                        ]
                    ]
                }
            ]
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
