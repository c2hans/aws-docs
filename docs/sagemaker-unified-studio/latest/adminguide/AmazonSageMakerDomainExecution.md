---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/AmazonSageMakerDomainExecution.html
---

# AmazonSageMakerDomainExecution role
<a name="AmazonSageMakerDomainExecution"></a>

The AmazonSageMakerDomainExecution role has the [AWS policy: SageMakerStudioDomainExecutionRolePolicy](security-iam-awsmanpol-SageMakerStudioDomainExecutionRolePolicy.md) attached. This is an IAM role that Amazon SageMaker Unified Studio requires to call APIs on behalf of authorized users, including those logged in to Amazon SageMaker Unified Studio.

The default `AmazonSageMakerDomainExecution` role has the following trust policy attached:

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
              "Service": "datazone.amazonaws.com"
          },
          "Action": [
              "sts:AssumeRole",
              "sts:TagSession",
              "sts:SetContext"
          ],
          "Condition": {
              "StringEquals": {
                  "aws:SourceAccount": "{{source_account_id}}"
              },
              "ForAllValues:StringLike": {
                  "aws:TagKeys": "datazone*"
              }
          }
      }
  ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
