---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/get-readiness-check-resource-status.html
---

# Check the readiness of a resource in a readiness check
<a name="get-readiness-check-resource-status"></a>

The following is an example of a request to check the readiness of an individual resource in a readiness check, and the response.

This request checks the detailed status of an individual resource within a readiness check, to get rule-level visibility.

```
aws route53-recovery-readiness --region us-west-2 get-readiness-check-resource-status \
			--readiness-check-name ebs-volume-readiness \
			--resource-identifier arn:aws:ec2:ap-southeast-1:888888888888:volume/vol-0bc095e048255a901
```

```
{
    "Readiness": "READY",
    "Rules": [
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "EbsVolumeEncryptionDefault"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "EbsVolumeEncryptionEnabled"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "EbsVolumeIops"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "EbsVolumeKmsKeyId"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "EbsVolumeLimits"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "EbsVolumeMultiAttachEnabled"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "EbsVolumeSize"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "EbsVolumeState"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "EbsVolumeType"
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-readiness` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
