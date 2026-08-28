---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/AmazonDataZoneBedrockModelManagementRole.html
---

# AmazonDataZoneBedrockModelManagementRole
<a name="AmazonDataZoneBedrockModelManagementRole"></a>

Amazon SageMaker Unified Studio uses this role to create an inference profile for an Amazon Bedrock model in a project. The inference profile is required for the project to interact with the model. You can either let Amazon SageMaker Unified Studio automatically create a unique provisioning role, or you can provide a custom provisioning role.

The AmazonDataZoneBedrockModelManagementRole has the [AWS policy: AmazonDataZoneBedrockModelManagementPolicy](security-iam-awsmanpol-AmazonDataZoneBedrockModelManagementPolicy.md) attached.

The default `AmazonDataZoneBedrockModelManagementRole` has the following trust policy attached:

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
           "sts:SetContext"
      ],
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{accountId}}"
        }
      }
    }
  ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
