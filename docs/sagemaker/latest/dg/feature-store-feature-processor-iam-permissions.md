---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-feature-processor-iam-permissions.html
---

# IAM permissions and execution roles
<a name="feature-store-feature-processor-iam-permissions"></a>

To use the The Amazon SageMaker Python SDK requires permissions to interact with AWS services. The following policies are required for full Feature Processor functionality. You can attach the [AmazonSageMakerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.html) and [AmazonEventBridgeSchedulerFullAccess](https://docs.aws.amazon.com/scheduler/latest/UserGuide/security_iam_id-based-policy-examples.html#security_iam_id-based-policies-managed-policies) AWS Managed Policies attached to your IAM role. For information on attaching policies to your IAM role, see [Adding policies to your IAM role](feature-store-adding-policies.md). See the following examples for details.

The trust policy of the role to which this policy is applied must allow the "scheduler.amazonaws.com", "sagemaker.amazonaws.com", and "glue.amazonaws.com" principles.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "scheduler.amazonaws.com",
                    "sagemaker.amazonaws.com",
                    "glue.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
