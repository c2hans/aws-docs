---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/call-analytics-resource-access-role.html
---

# Using the call analytics resource access role for the Amazon Chime SDK
<a name="call-analytics-resource-access-role"></a>

The calling account must create the resource access role used by a media insights pipeline configuration. You can't use cross-account roles.

Depending on the features that you enable when you create a call analytics configuration, you must use additional resource policies. Expand the following sections to learn more.

## Minimum required policy
<a name="minimum-policy"></a>

The role requires the following policy, at a minimum:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [{
            "Effect": "Allow",
            "Action": [
                "transcribe:StartCallAnalyticsStreamTranscription",
                "transcribe:StartStreamTranscription"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "kinesisvideo:GetDataEndpoint",
                "kinesisvideo:GetMedia"
            ],
            "Resource": "arn:aws:kinesisvideo:{{us-east-1}}:{{111122223333}}:stream/Chime*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "kinesisvideo:GetDataEndpoint",
                "kinesisvideo:GetMedia"
            ],
            "Resource": "arn:aws:kinesisvideo:{{us-east-1}}:{{111122223333}}:stream/*",
            "Condition": {
                "StringLike": {
                    "aws:ResourceTag/AWSServiceName": "ChimeSDK"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": ["kms:Decrypt"],
            "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/*",
            "Condition": {
                "StringLike": {
                    "aws:ResourceTag/AWSServiceName": "ChimeSDK"
                }
            }
        }
    ]
}
```

------

You must also use the following trust policy:

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "mediapipelines.chime.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "{{111122223333}}"
        },
        "ArnLike": {
            "aws:SourceARN": "arn:aws:chime:*:{{111122223333}}:*"
        }
        }
    }
  ]
}
```

------

## KinesisDataStreamSink policy
<a name="kds-stream-sink-policy"></a>

If you use the `KinesisDataStreamSink`, add the following policy:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [{
            "Effect": "Allow",
            "Action": [
                "kinesis:PutRecord"
            ],
            "Resource": [
                "arn:aws:kinesis:{{us-east-1}}:{{111122223333}}:stream/{{output_stream_name}}"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:GenerateDataKey"
            ],
            "Resource": [
            "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/*"
            ],
            "Condition": {
                "StringLike": {
                    "aws:ResourceTag/AWSServiceName": "ChimeSDK"
                }
            }
        }
    ]
}
```

------

## S3RecordingSink policy
<a name="s3-recording-sink-policy"></a>

If you use the `S3RecordingSink`, add the following policy:

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
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:PutObjectTagging"
            ],
            "Resource": [
                "arn:aws:s3:::{{input_bucket_path}}/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kinesisvideo:GetDataEndpoint",
                "kinesisvideo:ListFragments",
                "kinesisvideo:GetMediaForFragmentList"
            ],
            "Resource": [
                "arn:aws:kinesisvideo:{{us-east-1}}:{{111122223333}}:stream/*"
            ],
            "Condition": {
                "StringLike": {
                    "aws:ResourceTag/AWSServiceName": "ChimeSDK"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "kinesisvideo:ListFragments",
                "kinesisvideo:GetMediaForFragmentList"
            ],
            "Resource": [
            "arn:aws:kinesisvideo:{{us-east-1}}:{{111122223333}}:stream/Chime*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:GenerateDataKey"
            ],
            "Resource": [
            "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/*"
            ],
            "Condition": {
                "StringLike": {
                    "aws:ResourceTag/AWSServiceName": "ChimeSDK"
                }
            }
        }
    ]
}
```

------

## Post Call Analytics policy
<a name="post-call-analytics-policy"></a>

If you use the Post Call Analytics feature of the `AmazonTranscribeCallAnalyticsProcessor`, add the following policy:

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
                "iam:PassRole"
            ],
            "Resource": [
                "arn:aws:iam::{{111122223333}}:role/{{transcribe_role_name}}"
            ],
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "transcribe.streaming.amazonaws.com"
                }
            }
        }
    ]
}
```

------

## VoiceEnhancementSinkConfiguration policy
<a name="enhancement-sink-config-policy"></a>

If you use the `VoiceEnhancementSinkConfiguration` element, add the following policy:

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "s3:GetObject",
            "s3:PutObject",
            "s3:PutObjectAcl",
            "s3:PutObjectTagging"
         ],
         "Resource":[
            "arn:aws:s3:::{{input_bucket_path}}/*"
         ]
      },
      {
         "Effect":"Allow",
         "Action":[
            "kinesisvideo:GetDataEndpoint",
            "kinesisvideo:ListFragments",
            "kinesisvideo:GetMediaForFragmentList"
         ],
         "Resource":[
            "arn:aws:kinesisvideo:{{us-east-1}}:{{111122223333}}:stream/*"
         ],
         "Condition":{
            "StringLike":{
               "aws:ResourceTag/AWSServiceName":"ChimeSDK"
            }
         }
      },
      {
         "Effect":"Allow",
         "Action":[
            "kinesisvideo:ListFragments",
            "kinesisvideo:GetMediaForFragmentList"
         ],
         "Resource":[
         "arn:aws:kinesisvideo:{{us-east-1}}:{{111122223333}}:stream/Chime*"
         ]
      },
      {
         "Effect":"Allow",
         "Action":[
            "kms:GenerateDataKey"
         ],
         "Resource":[
         "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/*"
         ],
         "Condition":{
            "StringLike":{
               "aws:ResourceTag/AWSServiceName":"ChimeSDK"
            }
         }
      }
   ]
}
```

------

## VoiceAnalyticsProcessor policy
<a name="voice-analytics-processor-policy"></a>

If you use the `VoiceAnalyticsProcessor`, add the policies for `LambdaFunctionSink`, `SqsQueueSink`, and `SnsTopicSink` depending on which sinks you have defined.

`LambdaFunctionSink` policy:
****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Action": [
        "lambda:InvokeFunction",
        "lambda:GetPolicy"
       ],
      "Resource": [
          "arn:aws:lambda:{{us-east-1}}:{{111122223333}}:{{function}}:{{function_name}}"
       ],
      "Effect": "Allow"
    }
  ]
}
```

`SqsQueueSink` policy
****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Action": [
        "sqs:SendMessage",
        "sqs:GetQueueAttributes"
       ],
      "Resource": [
      "arn:aws:sqs:{{us-east-1}}:{{111122223333}}:{{queue_name}}"
        ],
      "Effect": "Allow"
    },
    {
      "Effect": "Allow",
      "Action": ["kms:GenerateDataKey", "kms:Decrypt"],
      "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/*",
      "Condition": {
        "StringLike": {
            "aws:ResourceTag/AWSServiceName": "ChimeSDK"
        }
      }
    }
  ]
}
```

`SnsTopicSink` policy:
****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Action": [
        "sns:Publish",
        "sns:GetTopicAttributes"
      ],
      "Resource": [
      "arn:aws:sns:{{us-east-1}}:{{111122223333}}:{{topic_name}}"
      ],
      "Effect": "Allow"
    },
    {
      "Effect": "Allow",
      "Action": ["kms:GenerateDataKey", "kms:Decrypt"],
      "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/*",
      "Condition": {
        "StringLike": {
            "aws:ResourceTag/AWSServiceName": "ChimeSDK"
        }
      }
    }
  ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
