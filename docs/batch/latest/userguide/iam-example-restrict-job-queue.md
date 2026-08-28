---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/iam-example-restrict-job-queue.html
---

# Resource: Restrict to a job queue
<a name="iam-example-restrict-job-queue"></a>

Use the following policy to submit jobs to a specific job queue that's named **queue1** with any job definition name.

**Important**
When scoping resource-level access for job submission, you must provide both job queue and job definition resource types.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "batch:SubmitJob"
            ],
            "Resource": [
                "arn:aws:batch:{{us-east-2}}:{{888888888888}}:job-definition/*",
                "arn:aws:batch:{{us-east-2}}:{{888888888888}}:job-queue/queue1"
            ]
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
