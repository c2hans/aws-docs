---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/AmazonDataZoneBedrockFMConsumptionRole.html
---

# AmazonDataZoneBedrockFMConsumptionRole
<a name="AmazonDataZoneBedrockFMConsumptionRole"></a>

A consumption role is required for each Amazon Bedrock model that you want to enable in the playground for non-builders. Amazon SageMaker Unified Studio can create a consumption role per model by default or you have the option to configure a single existing consumption role for all models.

The AmazonDataZoneBedrockFMConsumptionRole has the [AWS policy: AmazonDataZoneBedrockModelConsumptionPolicy](security-iam-awsmanpol-AmazonDataZoneBedrockModelConsumptionPolicy.md) attached.

The default `AmazonDataZoneBedrockFMConsumptionRole` has the following inline policy attached:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AllowInferenceProfileToInvokeFoundationModels",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": [
                "arn:aws:bedrock:us-east-1::foundation-model/{{modelId}}"
            ],
            "Condition": {
                "ArnLike": {
                    "bedrock:InferenceProfileArn": "arn:aws:bedrock:*:{{111122223333}}:application-inference-profile/*"
                }
            }
        }
    ]
}
```

------

The default `AmazonDataZoneBedrockFMConsumptionRole` has the following trust policy attached:

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
