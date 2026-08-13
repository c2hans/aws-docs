---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/tag-management-for-an-ml-platform.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Tag management for an ML platform
<a name="tag-management-for-an-ml-platform"></a>

The tagging mechanism in AWS enables you to assign metadata information to virtually any AWS resource. Each tag is represented by a key-value pair. Tagging provides a flexible mechanism to categorize and manage cloud resources. Tags become especially crucial as AWS utilization grows.

Tags can serve many purposes. Common use cases of using tags include:
+ **Business tags and cost allocation** — In this scenario, you use tags such as cost center, business unit, team, or project to track resource ownership and AWS spend, and create financial reports.
+ **Tags for automation** — Tags are used to separate resources belonging to different projects and apply different automation policies (for example, shut down all project 1 resources on the weekend, but keep project 2 intact).
+ **Security and risk management** — Apply different tags based on compliance or security policies. For example, use tags to separate sensitive data and apply different policies for it.

In an ML platform, tagging should be considered for the following resources:
+ **Experimentation environment resources** — The SageMaker AI Notebook provision should be automated using CloudFormation script and tags such as owner name, owner id, dept, environment, and project should be automatically populated by the CloudFormation script. For other resources (for example, training job or end point) that are programmatically provisioned by data scientists through SDK / CLI, preventive guardrails should be implemented to ensure that the required tags are populated.
+ **Pipeline automation resources** — Resources automated by the automation pipeline should be properly tagged. Pipeline should be automatically provisioned using CloudFormation scripts and tags such as owner name/id, environment, and project should be automatically populated by the CloudFormation script. These resources include CodePipeline pipeline run, CodeBuild job, Step Functions run, SageMaker AI processing job / training job, SageMaker AI models, SageMaker AI endpoint, Lambda function, and SageMaker AI.
+ **Production resources** — Resources such as SageMaker AI endpoints, model artifacts, and inference images should be tagged.

**Tag example 1** — Enforce tags with a specific pattern when creating new AWS resources.

You may want to enforce specific tagging patterns. For example, the following policy defines that a new SageMaker AI endpoint can be created if tag “team” is present with one of 3 possible values: “`alpha`”, “`bravo`”, and “`charlie`”.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "CreateSageMakerEndPoint",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreateEndpointConfig",
                "sagemaker:CreateEndpoint"
            ],
            "Resource": [
                "arn:aws:sagemaker:*:*:endpoint-config/*",
                "arn:aws:sagemaker:*:*:endpoint/*"
            ],
            "Condition": {
                "StringEqualsIgnoreCase": {
                    "aws:RequestTag/team": [
                        "alpha",
                        "bravo",
                        "charlie"
                    ]
                }
            }
        }
    ]
}
```

------

**Tagging example 2** — Automatically delete any untagged resources.

Users typically mandate tagging of all AWS resources and consider untagged resources as non-compliant. They may want to apply remediation actions, such as deletion of untagged resources or placing it under quarantine. The simplest way to implement this automatic remediation of untagged resources is via AWS Config, using the managed rule “`required-tags`”. This rule automatically applies to customer-defined resource types and checks whether customer resources have the required tags. For example, you can check whether your Amazon EC2 instances have the `CostCenter` tag. For more information, see [required-tags](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html).

**Tagging example 3** — Controlling access to AWS resources.

In many cases, tags provide a powerful and yet flexible way to manage access to various resources. This is an example of identity policy, which blocks access to any S3 objects unless the object has a “`security`” tag with the value “`shared`”.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "S3ObjectAccess",
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "s3:ExistingObjectTag/security": "shared"
                }
            }
        }
    ]
}
```

------

For more information, see the [*Tagging Best Practices*](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/welcome.html) whitepaper.
