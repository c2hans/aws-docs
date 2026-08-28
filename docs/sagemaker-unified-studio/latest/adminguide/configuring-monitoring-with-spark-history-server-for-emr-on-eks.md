---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/configuring-monitoring-with-spark-history-server-for-emr-on-eks.html
---

# Configuring monitoring with Spark History Server for Amazon EMR on EKS
<a name="configuring-monitoring-with-spark-history-server-for-emr-on-eks"></a>

 Amazon EMR on EKS requires additional IAM permissions to enable monitoring with Spark History Server. You must attach the following inline IAM role policy to the IAM role created as the project user role.

**Note**
 The project user role for an Amazon SageMaker Unified Studio project is named `datazone_usr_role_{{{project_id}}}`.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SparkHistoryServer",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreatePresignedDomainUrl"
            ],
            "Resource": "arn:aws:sagemaker:*:*:user-profile/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/AmazonDataZoneProject": "${aws:PrincipalTag/AmazonDataZoneProject}"
                }
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
