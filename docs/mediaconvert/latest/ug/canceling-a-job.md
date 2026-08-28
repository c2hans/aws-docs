---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/canceling-a-job.html
---

# Canceling a job
<a name="canceling-a-job"></a>

The following procedure explains how to cancel a job using the AWS Elemental MediaConvert console.

------
#### [ Console  ]

To cancel a job using the MediaConvert console

1. Open the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list) page in the MediaConvert console.

1. Select the **Job ID** of the job that you want to cancel by choosing the option (![Empty circle outline representing a placeholder or selection option.](http://docs.aws.amazon.com/mediaconvert/latest/ug/images/circle-icon.png)) next to it.

1. Choose **Cancel job**.

------
#### [ CLI  ]

The following `cancel-job` example cancels a job.

```
aws mediaconvert cancel-job \
	--id {{1234567890123-efg456}}
```

For more information about how to cancel a job using the AWS CLI, see the [AWS CLI command reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/cancel-job.html).

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
