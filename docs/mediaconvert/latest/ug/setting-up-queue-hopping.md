---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up-queue-hopping.html
---

# Setting up queue hopping
<a name="setting-up-queue-hopping"></a>

When you set up queue hopping, you specify the *submission queue*, the *wait time*, and the *destination queue*. Typically, the submission queue is a reserved queue and the destination queue is an on-demand queue. The following tabs show different options for setting up queue hopping.

------
#### [ Console ]

To set up queue hopping in the MediaConvert console:

1. On the **Create job** page, choose **Job management**.

1. Enable **Queue hopping**.

1. Enter the amount of time until your job can hop with **Wait minutes**.

1. For **Destination queue**, choose the queue that you want your job to hop to if it stays in the submission queue beyond its wait time.

1. Optionally, specify a new **Job priority** if your job hops to its destination queue. For more information, see [Setting priority for hopped jobs](job-priority-and-queue-hopping.md).

------
#### [ API, SDK, or the AWS CLI ]

To set up queue hopping in the API, SDK, or the AWS CLI, configure the settings for queue hopping under `HopDestinations`. This property is a direct child of `Jobs`, which is in the top level of the JSON job specification.

The following is an excerpt of a job settings JSON that hops to an on-demand queue after 10 minutes.

```
{
    "Settings": {
        "OutputGroups": {{[...]}},
        "Inputs": {{[...]}}
    },
    "HopDestinations": [
        {
        "WaitMinutes": {{10}},
        "Queue": {{"arn:aws:mediaconvert:us-west-2:111122223333:queues/ondemandqueue"}},
        "Priority": {{0}}
        }
    ]
}
```

For more information, see the MediaConvert [API Reference](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobs.html#jobs-model-hopdestination).

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
