---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/media-pipeline-service-linked-role-policy.html
---

# AWS managed policy: AmazonChimeSDKMediaPipelinesServiceLinkedRolePolicy
<a name="media-pipeline-service-linked-role-policy"></a>

You can't attach the `AmazonChimeSDKMediaPipelinesServiceLinkedRolePolicy` to your IAM entities.

This policy allows Kinesis Video Streams to stream data to Amazon Chime SDK meetings and publish metrics to CloudWatch. It also allows Amazon Chime SDK media pipelines to access Amazon Chime SDK meetings on your behalf. For more information, see [Using roles with Amazon Chime SDK media pipelines](using-service-linked-roles-media-pipeline.md) in this guide.

**Permissions details**

This policy includes the following permissions.
+ `cloudwatch` – Grants permission to put CloudWatch metrics.
+ `kinesisvideo` – Grants permissions to get data endpoints, put media, update data retention intervals, describe data streams, create data streams, and list data streams.
+ `chime` – Grants permissions to get meetings, create attendees, and delete attendees.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AllowPutMetricsForChimeSDKNamespace",
            "Effect": "Allow",
            "Action": "cloudwatch:PutMetricData",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": "AWS/ChimeSDK"
                }
            }
        },
        {
            "Sid": "AllowKinesisVideoStreamsAccess",
            "Effect": "Allow",
            "Action": [
                "kinesisvideo:GetDataEndpoint",
                "kinesisvideo:PutMedia",
                "kinesisvideo:UpdateDataRetention",
                "kinesisvideo:DescribeStream",
                "kinesisvideo:CreateStream"
            ],
            "Resource": [
                "arn:aws:kinesisvideo:*:*:stream/ChimeMediaPipelines-*"
            ]
        },
        {
            "Sid": "AllowKinesisVideoStreamsListAccess",
            "Effect": "Allow",
            "Action": [
                "kinesisvideo:ListStreams"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "AllowChimeMeetingAccess",
            "Effect": "Allow",
            "Action": [
                "chime:GetMeeting",
                "chime:CreateAttendee",
                "chime:DeleteAttendee"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
