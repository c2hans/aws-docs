---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/logging-and-monitoring.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Logging and monitoring
<a name="logging-and-monitoring"></a>

 To help you debug your compilation jobs, processing jobs, training jobs, endpoints, transform jobs, notebook instances, and notebook instance lifecycle configurations, anything that an algorithm container, a model container, or a notebook instance lifecycle configuration sends to stdout or stderr is also sent to [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html). You can monitor SageMaker AI Studio using Amazon CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 15 months, so you can access historical information and gain a better perspective on how your web application or service is performing.

## Logging with CloudWatch
<a name="logging-with-cloudwatch"></a>

 As the data science process is inherently experimental and iterative, it is essential to log activity such as notebook usage, training/processing job run time, training metrics, and endpoint serving metrics such as invocation latency. By default, SageMaker AI publishes metrics to CloudWatch Logs, and these logs can be encrypted with customer-managed keys using AWS KMS.

 You can also use VPC endpoints to send logs to CloudWatch without using the public internet. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, refer to the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

 SageMaker AI creates a single log group for Studio, under `/aws/sagemaker/studio`. Each user profile and app has their own log stream under this log group, and lifecycle configuration scripts have their own log stream as well. For example, a user profile named ‘studio-user’ with a Jupyter Server app and with an attached lifecycle script, and a Data Science Kernel Gateway app has the following log streams:

 `/aws/sagemaker/studio/<domain-id>/studio-user/JupyterServer/default`

 `/aws/sagemaker/studio/<domain-id>/studio-user/JupyterServer/default/LifecycleConfigOnStart`

 `/aws/sagemaker/studio/<domain-id>/studio-user/KernelGateway/datascience-app`

 For SageMaker AI to send logs to CloudWatch on your behalf, the caller of the Training/Processing/Transform job APIs will need the following permissions:

------
#### [ JSON ]

****

```
{
     "Version":"2012-10-17",
     "Statement": [
         {
             "Action": [
                 "logs:CreateLogDelivery",
                 "logs:CreateLogGroup",
                 "logs:CreateLogStream",
                 "logs:DeleteLogDelivery",
                 "logs:Describe*",
                 "logs:GetLogEvents",
                 "logs:GetLogDelivery",
                 "logs:ListLogDeliveries",
                 "logs:PutLogEvents",
                 "logs:PutResourcePolicy",
                 "logs:UpdateLogDelivery"
             ],
             "Resource": "*",
             "Effect": "Allow"
         }
     ]
 }
```

------

To encrypt those logs with a custom AWS KMS key, you will first need to modify the key policy to allow the CloudWatch service to encrypt and decrypt the key. Once you create a log encryption AWS KMS key, modify the key policy to include the following:

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
                "Service": "logs.region.amazonaws.com"
            },
            "Action": [
                "kms:Encrypt*",
                "kms:Decrypt*",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*",
                "kms:Describe*"
            ],
            "Resource": "*",
            "Condition": {
                "ArnLike": {
                    "kms:EncryptionContext:aws:logs:arn": "arn:aws:logs:us-east-1:111122223333:*"
                }
            }
        }
    ]
}
```

------

 Note that you can always use `ArnEquals` and provide a specific [Amazon Resource Name](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) (ARN) for the CloudWatch log you want to encrypt. Here we are showing that you can use this key to encrypt all logs in an account for simplicity. Additionally, training, processing, and model endpoints publish metrics about the instance CPU and memory utilization, hosting invocation latency, and so on. You can further configure Amazon SNS to notify administrators of events when certain thresholds are crossed. The consumer of the training and processing APIs needs to have the following permissions:

------
#### [ JSON ]

****

```
{
     "Version":"2012-10-17",
     "Statement": [
         {
             "Action": [
                 "cloudwatch:DeleteAlarms",
                 "cloudwatch:DescribeAlarms",
                 "cloudwatch:GetMetricData",
                 "cloudwatch:GetMetricStatistics",
                 "cloudwatch:ListMetrics",
                 "cloudwatch:PutMetricAlarm",
                 "cloudwatch:PutMetricData",
                 "sns:ListTopics"
             ],
             "Resource": "*",
             "Effect": "Allow",
             "Condition": {
                 "StringLike": {
                     "cloudwatch:namespace": "aws/sagemaker/*"
                 }
             }

         },
         {
             "Action": [
                 "sns:Subscribe",
                 "sns:CreateTopic"
             ],
             "Resource": [
                 "arn:aws:sns:*:*:*SageMaker*",
                 "arn:aws:sns:*:*:*Sagemaker*",
                 "arn:aws:sns:*:*:*sagemaker*"
             ],
             "Effect": "Allow"
         }
     ]
 }
```

------

### Audit with AWS CloudTrail
<a name="audit-with-cloudtrail"></a>

 To improve your compliance posture, audit all your APIs with AWS CloudTrail. By default, all SageMaker AI APIs are logged with [AWS CloudTrail](https://aws.amazon.com/cloudtrail/). You do not need any additional IAM permissions to enable CloudTrail.

 All SageMaker AI actions, with the exception of `InvokeEndpoint` and `InvokeEndpointAsync`, are logged by CloudTrail and are documented in the operations. For example, calls to the `CreateTrainingJob`, `CreateEndpoint`, and `CreateNotebookInstance` actions generate entries in the CloudTrail log files.

 Every CloudTrail event entry contains information about who generated the request. The identity information helps you determine the following:
+  Whether the request was made with root or AWS IAM user credentials.
+  Whether the request was made with temporary security credentials for a role or federated user.
+  Whether the request was made by another AWS service. For an example event, refer to the [Log SageMaker AI API Calls with CloudTrail](https://docs.aws.amazon.com/sagemaker/latest/dg/logging-using-cloudtrail.html) documentation.

By default, CloudTrail logs the Studio execution role name of the user profile as the identifier for each event. This works if each user has their own execution role. If multiple users share the same execution role, you can use the `sourceIdentity` configuration to propagate the Studio user profile name to CloudTrail. Refer to [Monitoring user resource access from Amazon SageMaker AI Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/monitor-user-access.html) to enable the `sourceIdentity` feature. In a shared space, all actions refer to the space ARN as the source, and you cannot audit through `sourceIdentity`.
