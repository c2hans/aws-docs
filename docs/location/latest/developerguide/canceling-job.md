---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/canceling-job.html
---

# Cancel a job
<a name="canceling-job"></a>

Use the `CancelJob` operation to cancel an existing job currently in Pending or Running status. You might cancel a job if it was submitted with the wrong parameters or input data, or if you no longer need the complete results. It can take time for a job to be fully cancelled. You can use the `GetJob` action to check cancellation status. Cancelled jobs transition from **Cancelling** to **Cancelled** status when cancellation is complete.

## Examples
<a name="canceling-job-examples"></a>

### Cancel an existing address validation job
<a name="cancel-address-validation-job"></a>

------
#### [ Sample request ]

```
{
    "JobId": "{{YOUR_JOB_ID}}"
}
```

------
#### [ Sample response ]

```
{
    "JobArn": "arn:aws:geo:us-west-2:{{YOUR_ACCOUNT_ID}}:job/{{YOUR_JOB_ID}}",
    "JobId": "{{YOUR_JOB_ID}}",
    "Status": "Cancelling"
}
```

------
#### [ AWS CLI ]

```
aws location cancel-job --job-id "{{YOUR_JOB_ID}}" --region us-west-2
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
