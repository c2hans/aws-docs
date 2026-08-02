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
