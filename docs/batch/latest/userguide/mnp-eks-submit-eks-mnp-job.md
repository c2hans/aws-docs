---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/mnp-eks-submit-eks-mnp-job.html
---

# Submit an Amazon EKS MNP job
<a name="mnp-eks-submit-eks-mnp-job"></a>

To submit a job using the registered job definition, enter the following command. Replace the value of <EKS\_JOB\_QUEUE\_NAME> with the name or ARN of a pre-existing job queue associated with an Amazon EKS compute environment.

```
aws batch submit-job --job-queue {{<EKS_JOB_QUEUE_NAME>}} \
    --job-definition MyEksMnpJobDefinition \
    --job-name myFirstEksMnpJob
```

You will receive the following JSON response.

```
{
    "jobArn": "arn:aws:batch:{{region}}:{{account}}:job/9b979cce-9da0-446d-90e2-ffa16d52af68",
    "jobName": "myFirstEksMnpJob",
    "jobId": "{{<JOB_ID>}}"
}
```

You can check the status of the job using the returned jobId with the following command.

```
aws batch describe-jobs --jobs {{<JOB_ID>}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
