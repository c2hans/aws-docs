---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/AmazonSageMakerDomainService.html
---

# AmazonSageMakerDomainService role
<a name="AmazonSageMakerDomainService"></a>

The AmazonSageMakerDomainService role has the [AWS policy: SageMakerStudioDomainServiceRolePolicy](security-iam-awsmanpol-SageMakerStudioDomainServiceRolePolicy.md) attached. This is a service role for domain level actions performed by Amazon SageMaker Unified Studio.

The default `AmazonSageMakerDomainService` role has the following trust policy attached:

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
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "{{domain_account}}"
        }
      }
    }
  ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
