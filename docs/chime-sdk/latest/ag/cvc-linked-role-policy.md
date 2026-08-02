---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/cvc-linked-role-policy.html
---

# AWS managed policy: AmazonChimeVoiceConnectorServiceLinkedRolePolicy
<a name="cvc-linked-role-policy"></a>

The `AmazonChimeVoiceConnectorServiceLinkedRolePolicy` enables Amazon Chime SDK Voice Connectors to stream media to Amazon Kinesis Video Streams, provide streaming notifications, and synthesize speech using Amazon Polly. This policy grants the Amazon Chime SDK Voice Connector service permissions to access customer’s Amazon Kinesis Video Streams, send notification events to the Amazon Simple Notification Service (SNS) and Amazon Simple Queue Service (SQS), and use Amazon Polly to synthesize speech when using the Amazon Chime SDK Voice Applications `Speak` and `SpeakAndGetDigits` actions.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["chime:GetVoiceConnector*"],
            "Resource": ["*"]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kinesisvideo:GetDataEndpoint",
                "kinesisvideo:PutMedia",
                "kinesisvideo:UpdateDataRetention",
                "kinesisvideo:DescribeStream",
                "kinesisvideo:CreateStream"
            ],
            "Resource": ["arn:aws:kinesisvideo:*:*:stream/ChimeVoiceConnector-*"]
        },
        {
            "Effect": "Allow",
            "Action": ["kinesisvideo:ListStreams"],
            "Resource": ["*"]
        },
        {
            "Effect": "Allow",
            "Action": ["SNS:Publish"],
            "Resource": ["arn:aws:sns:*:*:ChimeVoiceConnector-Streaming*"]
        },
        {
            "Effect": "Allow",
            "Action": ["sqs:SendMessage"],
            "Resource": ["arn:aws:sqs:*:*:ChimeVoiceConnector-Streaming*"]
        },
        {
            "Effect": "Allow",
            "Action": ["polly:SynthesizeSpeech"],
            "Resource": ["*"]
        },
        {
            "Effect": "Allow",
            "Action": [
                "chime:CreateMediaInsightsPipeline",
                "chime:GetMediaInsightsPipelineConfiguration"
            ],
            "Resource": ["*"]
        }
    ]
}
```

------

 For more information, see [Using the Amazon Chime SDK Voice Connector service linked role policy](using-service-linked-roles-stream.md).
